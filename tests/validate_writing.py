from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "00_workflow" / "writing_task_registry.json"
CONTRACT_PATH = ROOT / "00_workflow" / "writing_task_contracts.json"
PROCESS_PATH = ROOT / "00_workflow" / "writing_process_registry.json"
HANDOFF_PATH = ROOT / "00_workflow" / "workflows" / "cross_workflow_handoff_contract.md"
RUBRIC_PATH = ROOT / "tests" / "writing_evaluation_rubric.md"
WRITING_ROOT = ROOT / "writing"

CANONICAL_GATES = {"PASS", "CONDITIONAL", "BLOCKED", "APPROVE", "REVISE", "REJECT", "READY", "REGENERATE"}
ID_RE = re.compile(r"^##\s+ID\s*\n+\s*([^\n]+)", re.M)
VERSION_RE = re.compile(r"^##\s+Version\s*$", re.M)
STATUS_RE = re.compile(r"^##\s+Status\s*$", re.M)
ID_VALUE_RE = re.compile(r"^[A-Z]+-\d{3}$")


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Cannot load {path.relative_to(ROOT)}: {exc}")
        return {}


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    registry = load_json(REGISTRY_PATH, errors)
    contracts = load_json(CONTRACT_PATH, errors)
    process = load_json(PROCESS_PATH, errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    stages = registry.get("stages", [])
    process_stages = process.get("stages", [])
    tasks = contracts.get("tasks", {})

    registry_ids = [stage.get("id") for stage in stages]
    process_ids = [stage.get("id") for stage in process_stages]
    expected_ids = [f"{i:02d}" for i in range(1, 11)]
    if registry_ids != expected_ids:
        errors.append(f"Writing registry stage IDs must be 01-10; found {registry_ids}")
    if process_ids != expected_ids:
        errors.append(f"Writing process stage IDs must be 01-10; found {process_ids}")

    registry_names = [stage.get("name") for stage in stages]
    process_names = [stage.get("name") for stage in process_stages]
    if registry_names != process_names:
        errors.append("Writing task registry and process registry stage names do not match")

    prefixes: dict[str, str] = {}
    directories: dict[str, str] = {}
    registry_tasks: list[str] = []
    for stage in stages:
        stage_id = stage.get("id")
        prefix = stage.get("prefix")
        directory = stage.get("directory")
        if not prefix or not directory:
            errors.append(f"Writing stage {stage_id} requires prefix and directory")
            continue
        if prefix in prefixes.values():
            errors.append(f"Duplicate Writing prefix: {prefix}")
        if directory in directories.values():
            errors.append(f"Duplicate Writing directory: {directory}")
        prefixes[stage_id] = prefix
        directories[stage_id] = directory
        registry_tasks.extend(stage.get("tasks", []))

    if set(registry_tasks) != set(tasks):
        errors.append(
            f"Writing registry tasks and contracts differ: registry={sorted(registry_tasks)}, contracts={sorted(tasks)}"
        )

    process_tasks: list[str] = []
    known_stage_ids = set(process_ids)
    for stage in process_stages:
        stage_id = stage.get("id", "UNKNOWN")
        required = {"id", "name", "goal", "depends_on", "condition", "tasks", "protocols", "output_artifacts", "gates", "memory_effect"}
        missing = required - set(stage)
        if missing:
            errors.append(f"Writing process stage {stage_id} missing fields: {sorted(missing)}")
        for dependency in stage.get("depends_on", []):
            if dependency not in known_stage_ids:
                errors.append(f"Writing stage {stage_id} has unknown dependency {dependency}")
            elif dependency >= stage_id:
                errors.append(f"Writing stage {stage_id} dependency {dependency} must be upstream")
        unknown_gates = set(stage.get("gates", [])) - CANONICAL_GATES
        if unknown_gates:
            errors.append(f"Writing stage {stage_id} has non-canonical gates: {sorted(unknown_gates)}")
        if not stage.get("output_artifacts"):
            errors.append(f"Writing stage {stage_id} has no output artifacts")
        for protocol in stage.get("protocols", []):
            protocol_path = ROOT / protocol
            if not protocol_path.exists() or not protocol_path.is_file():
                errors.append(f"Writing stage {stage_id} references missing protocol {protocol}")
        process_tasks.extend(stage.get("tasks", []))

    if set(process_tasks) != set(tasks):
        errors.append(
            f"Writing process tasks and contracts differ: process={sorted(process_tasks)}, contracts={sorted(tasks)}"
        )

    for task_id, spec in tasks.items():
        for field in ("depends_on", "next", "gate"):
            if field not in spec:
                errors.append(f"{task_id}: Writing contract missing {field}")
        unknown_gates = set(spec.get("gate", [])) - CANONICAL_GATES
        if unknown_gates:
            errors.append(f"{task_id}: non-canonical gates {sorted(unknown_gates)}")
        if spec.get("approval_required") and not spec.get("approval_role"):
            errors.append(f"{task_id}: approval_required=true but approval_role missing")
        for dep in spec.get("depends_on", []):
            if dep not in tasks:
                errors.append(f"{task_id}: unknown Writing dependency {dep}")
        for nxt in spec.get("next", []):
            if nxt != "HUMAN_REVIEW" and nxt not in tasks:
                errors.append(f"{task_id}: unknown Writing next task {nxt}")

    active_prompt_ids: dict[str, Path] = {}
    if WRITING_ROOT.exists():
        for path in sorted(WRITING_ROOT.rglob("*.md")):
            if path.name.lower().startswith("readme"):
                continue
            text = path.read_text(encoding="utf-8")
            match = ID_RE.search(text)
            if not match:
                errors.append(f"{path.relative_to(ROOT)}: missing ## ID")
                continue
            task_id = match.group(1).strip()
            if not ID_VALUE_RE.fullmatch(task_id):
                errors.append(f"{path.relative_to(ROOT)}: invalid Writing task ID {task_id}")
                continue
            if task_id in active_prompt_ids:
                errors.append(f"Duplicate Writing task ID {task_id}")
            active_prompt_ids[task_id] = path
            if task_id not in tasks:
                errors.append(f"{path.relative_to(ROOT)}: {task_id} has no Writing task contract")
                continue
            matching_stage = next((s for s in stages if str(path.relative_to(ROOT)).replace('\\', '/').startswith(s['directory'] + '/')), None)
            if matching_stage and not task_id.startswith(matching_stage["prefix"]):
                errors.append(f"{path.relative_to(ROOT)}: {task_id} does not match prefix {matching_stage['prefix']}")
            if not VERSION_RE.search(text):
                errors.append(f"{path.relative_to(ROOT)}: missing ## Version")
            if not STATUS_RE.search(text):
                errors.append(f"{path.relative_to(ROOT)}: missing ## Status")
            for label in ("Input", "Output"):
                if label.lower() not in text.lower():
                    warnings.append(f"{path.relative_to(ROOT)}: no explicit {label} section")
            if "provenance" not in text.lower() and "evidence" not in text.lower():
                warnings.append(f"{path.relative_to(ROOT)}: no explicit provenance/evidence section")
            if "handoff" not in text.lower():
                warnings.append(f"{path.relative_to(ROOT)}: no explicit handoff section")

    if set(active_prompt_ids) != set(tasks):
        errors.append(
            f"Active Writing prompt IDs do not exactly match contracts: active={sorted(active_prompt_ids)}, contracts={sorted(tasks)}"
        )

    if not HANDOFF_PATH.exists():
        errors.append("Cross-workflow handoff contract is missing")
    if not RUBRIC_PATH.exists():
        errors.append("Writing evaluation rubric is missing")

    print(f"Writing stages: {len(stages)}")
    print(f"Writing task contracts: {len(tasks)}")
    print(f"Active Writing prompts: {len(active_prompt_ids)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Errors: {len(errors)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
