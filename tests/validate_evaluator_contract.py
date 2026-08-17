from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "00_workflow" / "llm_evaluator_protocol.md"
SCHEMA = ROOT / "00_workflow" / "qc" / "llm_evaluator_evidence_schema.json"

REQUIRED_PROTOCOL_TERMS = {
    "CONTENT_FAILURE",
    "GENERATOR_FAILURE",
    "EVALUATOR_FAILURE",
    "RUBRIC_FAILURE",
    "DATASET_FAILURE",
    "INPUT_FAILURE",
    "INFRASTRUCTURE_FAILURE",
    "DISAGREEMENT",
    "QC_EVIDENCE",
    "calibration",
    "provenance",
}


def main() -> int:
    errors: list[str] = []
    try:
        protocol = PROTOCOL.read_text(encoding="utf-8")
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load evaluator contract: {exc}")
        return 1

    missing_terms = sorted(term for term in REQUIRED_PROTOCOL_TERMS if term not in protocol)
    if missing_terms:
        errors.append(f"Evaluator protocol missing terms: {missing_terms}")

    required_fields = set(schema.get("required", []))
    expected_fields = {
        "evidence_id",
        "candidate",
        "evaluator",
        "rubric",
        "judge",
        "calibration",
        "results",
        "failure_classification",
        "gate_recommendation",
        "human_decision_state",
        "provenance",
    }
    if missing := expected_fields - required_fields:
        errors.append(f"Evaluator evidence schema missing fields: {sorted(missing)}")

    expected_failures = {term for term in REQUIRED_PROTOCOL_TERMS if term.endswith("FAILURE")} | {"DISAGREEMENT"}
    if set(schema.get("failure_classifications", [])) != expected_failures:
        errors.append("Evaluator failure classifications do not match the controlled vocabulary")

    if "EXPERIMENTAL" not in schema.get("calibration_states", []):
        errors.append("Evaluator schema must represent experimental calibration")
    if "AWAITING_HUMAN_DECISION" not in schema.get("human_decision_states", []):
        errors.append("Evaluator evidence must preserve human decision authority")

    print(f"Evaluator contract errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
