from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "00_workflow"
PROCESS_PATH = WORKFLOW / "process_registry.json"
TASK_REGISTRY_PATH = WORKFLOW / "task_registry.json"
CONTRACT_PATH = WORKFLOW / "task_contracts.json"
STAGE_REGISTRY_PATH = WORKFLOW / "stage_registry.md"
WORKFLOW_DOC_PATH = WORKFLOW / "workflow.md"

MARKER_RE = re.compile(r"<!--\s*ARCHITECTURE_STAGE:\s*(\d{2})\|([a-z0-9_]+)\s*-->")

EXPECTED_VERSION = "4.0-production-candidate"
EXPECTED_STATES = [
    "EXECUTE",
    "SATISFIED_BY_REUSE",
    "SKIPPED_NOT_APPLICABLE",
    "BLOCKED",
    "REVISE",
    "COMPLETE",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def markers(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    return MARKER_RE.findall(text)


def main() -> int:
    errors: list[str] = []
    try:
        process = json.loads(PROCESS_PATH.read_text(encoding="utf-8"))
        task_registry = json.loads(TASK_REGISTRY_PATH.read_text(encoding="utf-8"))
        contracts = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        stage_markers = markers(STAGE_REGISTRY_PATH)
        workflow_markers = markers(WORKFLOW_DOC_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load architecture sources: {exc}")
        return 1

    canonical = [(stage["id"], stage["name"]) for stage in process.get("stages", [])]
    task_view = [(stage.get("id"), stage.get("name")) for stage in task_registry.get("stages", [])]

    if process.get("process_version") != EXPECTED_VERSION:
        fail(errors, f"Process version must be {EXPECTED_VERSION}")
    if task_registry.get("pipeline_version") != EXPECTED_VERSION:
        fail(errors, f"Task-registry pipeline version must be {EXPECTED_VERSION}")
    if process.get("process_version") != task_registry.get("pipeline_version"):
        fail(errors, "Process and task-registry architecture versions differ")

    if len(canonical) != 20:
        fail(errors, f"Canonical lifecycle must contain 20 stages; found {len(canonical)}")
    expected_ids = [f"{i:02d}" for i in range(1, len(canonical) + 1)]
    if [stage_id for stage_id, _ in canonical] != expected_ids:
        fail(errors, "Canonical stage IDs are not sequential")
    if task_view != canonical:
        fail(errors, "task_registry stage IDs/names do not exactly match process_registry")
    if stage_markers != canonical:
        fail(errors, "stage_registry.md architecture markers do not exactly match process_registry")
    if workflow_markers != canonical:
        fail(errors, "workflow.md architecture markers do not exactly match process_registry")

    if process.get("stage_state_vocabulary") != EXPECTED_STATES:
        fail(errors, "process_registry stage-state vocabulary/order is inconsistent")
    if task_registry.get("stage_state_vocabulary") != EXPECTED_STATES:
        fail(errors, "task_registry stage-state vocabulary/order is inconsistent")

    source_of_truth = task_registry.get("source_of_truth", {})
    if source_of_truth.get("stage_structure") != "process_registry.json":
        fail(errors, "task_registry must delegate stage structure to process_registry.json")
    if source_of_truth.get("task_behavior") != "task_contracts.json":
        fail(errors, "task_registry must delegate task behavior to task_contracts.json")

    process_by_id = {stage["id"]: stage for stage in process["stages"]}
    task_by_id = {stage["id"]: stage for stage in task_registry["stages"]}

    for stage_id, stage in process_by_id.items():
        if task_by_id[stage_id].get("tasks", []) != stage.get("tasks", []):
            fail(errors, f"Stage {stage_id} task placement differs between registries")

    contract_tasks = set(contracts.get("tasks", {}))
    process_tasks = [task for stage in process["stages"] for task in stage.get("tasks", [])]
    task_registry_tasks = [task for stage in task_registry["stages"] for task in stage.get("tasks", [])]

    if len(process_tasks) != len(set(process_tasks)):
        fail(errors, "process_registry assigns at least one task to multiple stages")
    if len(task_registry_tasks) != len(set(task_registry_tasks)):
        fail(errors, "task_registry assigns at least one task to multiple stages")
    if set(process_tasks) != contract_tasks:
        fail(errors, "process_registry task set differs from task_contracts")
    if set(task_registry_tasks) != contract_tasks:
        fail(errors, "task_registry task set differs from task_contracts")

    if process_by_id["13"].get("tasks") != ["QC-001", "QC-002"]:
        fail(errors, "Stage 13 must own QC-001 and QC-002")
    if process_by_id["20"].get("tasks") != ["QC-003"]:
        fail(errors, "Stage 20 must own QC-003")
    if process_by_id["14"].get("tasks"):
        fail(errors, "Stage 14 FINAL-AI remains protocol-based until explicit task contracts are added")

    required_final_ai = {
        "00_workflow/creative_ai_final_edit.md",
        "00_workflow/final_ai_creative_synthesis_heavy_qc.md",
        "00_workflow/final_ai_closed_loop_production.md",
    }
    if not required_final_ai.issubset(set(process_by_id["14"].get("protocols", []))):
        fail(errors, "Stage 14 is missing one or more required Final-AI protocols")

    if process_by_id["18"].get("name") != "human_final_approval":
        fail(errors, "Stage 18 must preserve explicit human final authority")
    if process_by_id["19"].get("depends_on") != ["18"]:
        fail(errors, "Stage 19 must run only after human final approval")
    if process_by_id["20"].get("depends_on") != ["18", "19"]:
        fail(errors, "Stage 20 learning must occur after approval and final output packaging")

    print(f"Architecture version: {process.get('process_version')}")
    print(f"Canonical stages: {len(canonical)}")
    print(f"Mapped executable tasks: {len(contract_tasks)}")
    print(f"Stage-registry markers: {len(stage_markers)}")
    print(f"Workflow markers: {len(workflow_markers)}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
