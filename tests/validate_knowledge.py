from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "00_workflow" / "knowledge" / "knowledge_registry.json"
DESIGN_CONTRACT_PATH = ROOT / "00_workflow" / "task_contracts.json"
WRITING_CONTRACT_PATH = ROOT / "00_workflow" / "writing_task_contracts.json"

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
    known_consumers = design_tasks | writing_tasks
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
        if record["approval_state"] == "PENDING_CONFIRMATION" and not record["unknowns_required"]:
            errors.append(f"{kb_id}: pending knowledge must preserve explicit unknowns")
        if not record["project_id"] or not record["scope"]:
            errors.append(f"{kb_id}: project_id and scope are required")

        knowledge_path = ROOT / record["path"]
        if not knowledge_path.exists() or not knowledge_path.is_file():
            errors.append(f"{kb_id}: missing knowledge file {record['path']}")
            continue
        body = knowledge_path.read_text(encoding="utf-8")
        if kb_id not in body:
            errors.append(f"{kb_id}: identifier not found in {record['path']}")
        if record["provenance_required"] and "provenance" not in body.lower():
            errors.append(f"{kb_id}: required provenance section/field is absent")
        if record["unknowns_required"] and "unknown" not in body.lower():
            errors.append(f"{kb_id}: required unknown handling is absent")

        for task_id in record["allowed_consumers"]:
            if task_id not in known_consumers:
                errors.append(f"{kb_id}: unknown allowed consumer {task_id}")

    print(f"Knowledge records: {len(records)}")
    print(f"Unique knowledge IDs: {len(seen_kb_ids)}")
    print(f"Known Design consumers: {len(design_tasks)}")
    print(f"Known Writing consumers: {len(writing_tasks)}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
