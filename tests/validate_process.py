from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROCESS_PATH = ROOT / "00_workflow" / "process_registry.json"
CONTRACT_PATH = ROOT / "00_workflow" / "task_contracts.json"

REQUIRED_STAGE_FIELDS = {
    "id",
    "name",
    "goal",
    "depends_on",
    "condition",
    "tasks",
    "protocols",
    "output_artifacts",
    "gates",
    "memory_effect",
}

REQUIRED_STAGE_STATES = {
    "EXECUTE",
    "SATISFIED_BY_REUSE",
    "SKIPPED_NOT_APPLICABLE",
    "BLOCKED",
    "REVISE",
    "COMPLETE",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    try:
        process = json.loads(PROCESS_PATH.read_text(encoding="utf-8"))
        contracts = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load process registry/contracts: {exc}")
        return 1

    stages = process.get("stages", [])
    canonical_gates = set(process.get("canonical_gates", []))
    contract_tasks = set(contracts.get("tasks", {}))
    expected_ids = [f"{index:02d}" for index in range(1, len(stages) + 1)]
    actual_ids = [stage.get("id") for stage in stages]

    if not stages:
        fail(errors, "Process registry must contain at least one stage.")
    if actual_ids != expected_ids:
        fail(errors, f"Process stages must be sequential from 01; found {actual_ids}")
    if process.get("max_revision_cycles") != 3:
        fail(errors, "Process max_revision_cycles must remain 3")
    if process.get("terminal_escalation") != "HUMAN_REVIEW":
        fail(errors, "Process terminal_escalation must be HUMAN_REVIEW")
    if set(process.get("information_states", [])) != {"SOURCE", "DERIVED", "DECISION", "OUTPUT"}:
        fail(errors, "Process information states must exactly match the controlled information model")
    if set(process.get("stage_state_vocabulary", [])) != REQUIRED_STAGE_STATES:
        fail(errors, "Stage-state vocabulary does not match the controlled routing model")
    if not str(process.get("stage_satisfaction_rule", "")).strip():
        fail(errors, "Process must define a stage_satisfaction_rule")

    zones = process.get("lifecycle_zones", {})
    foundation = zones.get("foundation_system_creation", [])
    production = zones.get("content_production_finalization", [])
    if foundation != [f"{i:02d}" for i in range(1, 9)]:
        fail(errors, f"Foundation lifecycle zone must be 01-08; found {foundation}")
    if production != [f"{i:02d}" for i in range(9, 21)]:
        fail(errors, f"Production/finalization lifecycle zone must be 09-20; found {production}")

    seen_names: set[str] = set()
    process_tasks: set[str] = set()
    known_stage_ids = set(actual_ids)

    for stage in stages:
        stage_id = stage.get("id", "UNKNOWN")
        missing_fields = REQUIRED_STAGE_FIELDS - set(stage)
        if missing_fields:
            fail(errors, f"Stage {stage_id} missing fields: {sorted(missing_fields)}")

        name = stage.get("name")
        if name in seen_names:
            fail(errors, f"Duplicate process stage name: {name}")
        seen_names.add(name)

        if not str(stage.get("goal", "")).strip():
            fail(errors, f"Stage {stage_id} has an empty goal")
        if not str(stage.get("condition", "")).strip():
            fail(errors, f"Stage {stage_id} has an empty condition")
        if not str(stage.get("memory_effect", "")).strip():
            fail(errors, f"Stage {stage_id} has an empty memory effect")
        if not stage.get("output_artifacts"):
            fail(errors, f"Stage {stage_id} has no output artifacts")
        if not stage.get("gates"):
            fail(errors, f"Stage {stage_id} has no gates")

        unknown_gates = set(stage.get("gates", [])) - canonical_gates
        if unknown_gates:
            fail(errors, f"Stage {stage_id} uses non-canonical gates: {sorted(unknown_gates)}")

        for dependency in stage.get("depends_on", []):
            if dependency not in known_stage_ids:
                fail(errors, f"Stage {stage_id} has unknown stage dependency {dependency}")
            elif dependency >= stage_id:
                fail(errors, f"Stage {stage_id} dependency {dependency} must be upstream")

        for task_id in stage.get("tasks", []):
            if task_id not in contract_tasks:
                fail(errors, f"Stage {stage_id} references unknown task {task_id}")
            if task_id in process_tasks:
                fail(errors, f"Task {task_id} is assigned to more than one process stage")
            process_tasks.add(task_id)

        for protocol in stage.get("protocols", []):
            protocol_path = ROOT / protocol
            if not protocol_path.exists() or not protocol_path.is_file():
                fail(errors, f"Stage {stage_id} references missing protocol {protocol}")

    if process_tasks != contract_tasks:
        missing = sorted(contract_tasks - process_tasks)
        extra = sorted(process_tasks - contract_tasks)
        if missing:
            fail(errors, f"Contract tasks absent from process registry: {missing}")
        if extra:
            fail(errors, f"Process tasks absent from contracts: {extra}")

    print(f"Process version: {process.get('process_version')}")
    print(f"Process stages: {len(stages)}")
    print(f"Mapped task contracts: {len(process_tasks)}")
    print(f"Referenced protocols: {sum(len(stage.get('protocols', [])) for stage in stages)}")
    print(f"Stage routing states: {len(process.get('stage_state_vocabulary', []))}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
