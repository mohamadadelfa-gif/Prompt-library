from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "00_workflow" / "knowledge" / "knowledge_registry.json"
DESIGN_CONTRACT_PATH = ROOT / "00_workflow" / "task_contracts.json"
WRITING_CONTRACT_PATH = ROOT / "00_workflow" / "writing_task_contracts.json"

# Workflow protocols that are valid knowledge consumers but are not executable
# prompt contracts in the Design/Writing task registries.
NON_TASK_CONSUMERS = {"FINAL-AI-001", "FINAL-AI-002"}

REQUIRED_FIELDS = {
    "kb_id",
    "source_id",
    "title",
    "knowledge_type",
    "path",
    "project_id",
    "scope",
    "approval_state",
    "promotion_state",
    "allowed_consumers",
    "unknowns_required",
    "provenance_required",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        registry = load_json(REGISTRY_PATH)
        design_contracts = load_json(DESIGN_CONTRACT_PATH)
        writing_contracts = load_json(WRITING_CONTRACT_PATH)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load knowledge registry/contracts: {exc}")
        return 1

    records = registry.get("records", [])
    approval_states = set(registry.get("approval_states", []))
    promotion_states = set(registry.get("promotion_states", []))
    design_tasks = set(design_contracts.get("tasks", {}))
    writing_tasks = set(writing_contracts.get("tasks", {}))
    known_consumers = design_tasks | writing_tasks | NON_TASK_CONSUMERS
    seen_kb_ids: set[str] = set()
    seen_source_ids: set[str] = set()

    for index, record in enumerate(records, start=1):
        label = record.get("kb_id", f"record-{index}")
        missing = REQUIRED_FIELDS - set(record)
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
            continue

        kb_id = record["kb_id"]
        source_id = record["source_id"]
        if kb_id in seen_kb_ids:
            errors.append(f"Duplicate kb_id: {kb_id}")
        seen_kb_ids.add(kb_id)

        if source_id in seen_source_ids and source_id != kb_id:
            errors.append(f"Duplicate source_id: {source_id}")
        seen_source_ids.add(source_id)

        if record["approval_state"] not in approval_states:
            errors.append(f"{kb_id}: invalid approval_state {record['approval_state']}")
        if record["promotion_state"] not in promotion_states:
            errors.append(f"{kb_id}: invalid promotion_state {record['promotion_state']}")
        if record["promotion_state"] == "SYSTEM_RULE" and record["approval_state"] != "APPROVED":
            errors.append(f"{kb_id}: SYSTEM_RULE requires APPROVED state")
        if not record["project_id"] or not record["scope"]:
            errors.append(f"{kb_id}: project_id and scope are required")
        if not isinstance(record["allowed_consumers"], list):
            errors.append(f"{kb_id}: allowed_consumers must be a list")
            continue

        # Pending records should normally preserve unknowns explicitly. Existing
        # legacy records are reported as debt rather than making the entire
        # repository structurally invalid.
        if record["approval_state"] == "PENDING_CONFIRMATION" and not record["unknowns_required"]:
            warnings.append(f"{kb_id}: pending knowledge should set unknowns_required=true")

        knowledge_path = ROOT / record["path"]
        if not knowledge_path.exists() or not knowledge_path.is_file():
            errors.append(f"{kb_id}: missing knowledge file {record['path']}")
            continue

        # The registry is the canonical home of kb_id/source_id. Older source
        # documents do not always repeat the registry identifier or use literal
        # headings named 'Provenance'/'Unknown'. Flag this as migration debt,
        # not structural corruption.
        body = knowledge_path.read_text(encoding="utf-8")
        if kb_id not in body:
            warnings.append(f"{kb_id}: registry identifier is not repeated inside {record['path']}")
        if record["provenance_required"] and "provenance" not in body.lower():
            warnings.append(f"{kb_id}: provenance_required but no literal provenance label found")
        if record["unknowns_required"] and "unknown" not in body.lower():
            warnings.append(f"{kb_id}: unknowns_required but no literal unknown label found")

        for task_id in record["allowed_consumers"]:
            if task_id not in known_consumers:
                errors.append(f"{kb_id}: unknown allowed consumer {task_id}")

    print(f"Knowledge records: {len(records)}")
    print(f"Unique knowledge IDs: {len(seen_kb_ids)}")
    print(f"Known Design consumers: {len(design_tasks)}")
    print(f"Known Writing consumers: {len(writing_tasks)}")
    print(f"Known protocol consumers: {len(NON_TASK_CONSUMERS)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Errors: {len(errors)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
