from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_DIRS = [
    ROOT / "01_strategy",
    ROOT / "02_research",
    ROOT / "03_visual_analysis",
    ROOT / "04_visual_dna",
    ROOT / "05_art_direction",
    ROOT / "06_generation",
    ROOT / "07_quality_control",
]
DEPRECATED_FILES = {"02_research/reference_selection.md"}
REGISTRY_PATH = ROOT / "00_workflow" / "task_registry.json"
CONTRACT_PATH = ROOT / "00_workflow" / "task_contracts.json"

ID_RE = re.compile(r"^##\s+ID\s*$", re.M)
VERSION_RE = re.compile(r"^##\s+Version\s*$", re.M)
STATUS_RE = re.compile(r"^##\s+Status\s*$", re.M)
ID_VALUE_RE = re.compile(r"^([A-Z]+-\d{3})$", re.M)

CANONICAL_GATES = {"PASS", "CONDITIONAL", "BLOCKED", "APPROVE", "REVISE", "REJECT", "READY", "REGENERATE"}
FORBIDDEN_GATE_PHRASES = {
    "DO NOT PROCEED",
    "PROCEED WITH CONDITIONS",
    "READY FOR GEN-002",
    "READY FOR GENERATION",
    "APPROVE WITH MINOR REVISION",
    "FULL REGENERATION",
    "SIMPLIFY REVISION",
}
FORBIDDEN_LEGACY_REFERENCES = {
    "RES-002 — Reference Selection",
    "RES-002 - Reference Selection",
    "Reference Selection & Evaluation",
}
FORBIDDEN_DOMAIN_LEAKS = {
    "English-learning organization",
    "English-learning organizations",
    "educational model",
}

errors: list[str] = []
warnings: list[str] = []
ids: dict[str, Path] = {}
files_checked = 0


def has_any(text: str, terms: list[str]) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def prompt_id_from_text(text: str) -> str | None:
    if not ID_RE.search(text):
        return None
    match = re.search(r"^##\s+ID\s*\n+\s*([^\n]+)", text, re.M)
    return match.group(1).strip() if match else None


try:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    contracts = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    print(f"ERROR: cannot load workflow registry/contracts: {exc}")
    sys.exit(1)

contract_tasks = contracts.get("tasks", {})
canonical_from_contract = set()
for task_id, spec in contract_tasks.items():
    canonical_from_contract.update(spec.get("gate", []))

if canonical_from_contract - CANONICAL_GATES:
    errors.append(f"Contract contains non-canonical gates: {sorted(canonical_from_contract - CANONICAL_GATES)}")

registry_tasks = [task for stage in registry.get("stages", []) for task in stage.get("tasks", [])]
if set(registry_tasks) != set(contract_tasks):
    missing = sorted(set(registry_tasks) - set(contract_tasks))
    extra = sorted(set(contract_tasks) - set(registry_tasks))
    if missing:
        errors.append(f"Tasks missing from task_contracts.json: {missing}")
    if extra:
        errors.append(f"Tasks present only in task_contracts.json: {extra}")

expected_prefixes = {
    "01_strategy": "STR-",
    "02_research": "RES-",
    "03_visual_analysis": "VIS-",
    "04_visual_dna": "VDNA-",
    "05_art_direction": "ART-",
    "06_generation": "GEN-",
    "07_quality_control": "QC-",
}

for directory in ACTIVE_DIRS:
    if not directory.exists():
        errors.append(f"Missing active stage directory: {directory.relative_to(ROOT)}")
        continue

    for path in sorted(directory.glob("*.md")):
        rel = path.relative_to(ROOT)
        rel_string = str(rel).replace("\\", "/")
        if path.name.startswith("README") or rel_string in DEPRECATED_FILES:
            continue

        files_checked += 1
        text = path.read_text(encoding="utf-8")
        prompt_id = prompt_id_from_text(text)

        if not prompt_id:
            errors.append(f"{rel}: missing or empty ## ID")
            continue
        if not ID_VALUE_RE.fullmatch(prompt_id):
            errors.append(f"{rel}: invalid ID '{prompt_id}'")
        elif prompt_id in ids:
            errors.append(f"Duplicate ID {prompt_id}: {ids[prompt_id]} and {rel}")
        else:
            ids[prompt_id] = rel

        if prompt_id not in contract_tasks:
            errors.append(f"{rel}: ID {prompt_id} has no task contract")
            continue

        spec = contract_tasks[prompt_id]
        expected_prefix = expected_prefixes[rel.parts[0]]
        if not prompt_id.startswith(expected_prefix):
            errors.append(f"{rel}: ID {prompt_id} does not match stage prefix {expected_prefix}")

        if not VERSION_RE.search(text):
            errors.append(f"{rel}: missing ## Version")
        if not STATUS_RE.search(text):
            errors.append(f"{rel}: missing ## Status")

        status_match = re.search(r"^##\s+Status\s*\n+\s*([^\n]+)", text, re.M)
        if status_match and status_match.group(1).strip().lower() in {"draft", "deprecated", "archived"}:
            errors.append(f"{rel}: lifecycle status '{status_match.group(1).strip()}' is not production-eligible")

        if has_any(text, list(FORBIDDEN_LEGACY_REFERENCES)):
            errors.append(f"{rel}: contains retired reference-selection terminology")
        if has_any(text, list(FORBIDDEN_DOMAIN_LEAKS)):
            errors.append(f"{rel}: contains non-domain-agnostic educational-domain language")
        if has_any(text, list(FORBIDDEN_GATE_PHRASES)):
            errors.append(f"{rel}: contains non-canonical gate vocabulary")

        allowed_gates = set(spec.get("gate", []))
        if not any(re.search(rf"\b{re.escape(gate)}\b", text) for gate in allowed_gates):
            warnings.append(f"{rel}: prompt does not explicitly expose contract gate {sorted(allowed_gates)}; registry contract remains authoritative")

        for field_name in ("depends_on", "next", "gate"):
            if field_name not in spec:
                errors.append(f"{prompt_id}: contract missing '{field_name}'")

        if spec.get("approval_required") and not spec.get("approval_role"):
            errors.append(f"{prompt_id}: approval_required=true but approval_role is missing")

        if not has_any(text, ["Input", "Required Inputs", "Input Contract"]):
            warnings.append(f"{rel}: prompt does not explicitly label its input section")
        if not has_any(text, ["Output", "Output Format", "Output Contract"]):
            warnings.append(f"{rel}: prompt does not explicitly label its output section")
        if not has_any(text, ["Provenance", "Source / Confidence", "Evidence"]):
            warnings.append(f"{rel}: prompt does not explicitly label provenance/evidence")
        if not has_any(text, ["Handoff", "Handoff to"]):
            warnings.append(f"{rel}: prompt does not explicitly label a handoff")

for task_id, spec in contract_tasks.items():
    for dep in spec.get("depends_on", []):
        if dep not in contract_tasks:
            errors.append(f"{task_id}: unknown dependency {dep}")
    for nxt in spec.get("next", []):
        if nxt != "HUMAN_REVIEW" and nxt not in contract_tasks:
            errors.append(f"{task_id}: unknown next task {nxt}")

if set(ids) != set(contract_tasks):
    errors.append(f"Active prompt IDs do not exactly match contracts: active={sorted(ids)}, contracts={sorted(contract_tasks)}")

print(f"Checked {files_checked} active prompt files")
print(f"Unique IDs: {len(ids)}")
print(f"Task contracts: {len(contract_tasks)}")
print(f"Warnings: {len(warnings)}")
print(f"Errors: {len(errors)}")
for item in warnings:
    print(f"WARNING: {item}")
for item in errors:
    print(f"ERROR: {item}")

sys.exit(1 if errors else 0)
