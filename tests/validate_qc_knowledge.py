from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "00_workflow" / "qc" / "qc_knowledge_schema.json"
CONTRACT_PATH = ROOT / "00_workflow" / "task_contracts.json"
PROMPT_PATH = ROOT / "07_quality_control" / "qc_knowledge_synthesis.md"

REQUIRED_EVIDENCE_TYPES = {
    "CHAT_STATEMENT",
    "RESEARCH_SOURCE",
    "RESEARCH_DERIVATION",
    "PROJECT_REQUIREMENT",
    "HUMAN_PREFERENCE",
    "QC_FINDING",
    "REVISION_DECISION",
    "APPROVED_OUTPUT_EVIDENCE",
    "MODEL_INFERENCE",
    "UNKNOWN",
}
REQUIRED_APPROVAL_STATES = {"UNCONFIRMED", "ACTIVE_SOURCE", "APPROVED", "REJECTED", "SUPERSEDED"}
REQUIRED_PROMOTION_TYPES = {"PROJECT_QC_REFERENCE", "PROJECT_QC_RULE", "SYSTEM_QC_RULE_CANDIDATE"}
REQUIRED_GATES = {"PASS", "CONDITIONAL", "BLOCKED"}


def main() -> int:
    errors: list[str] = []
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        contracts = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        prompt = PROMPT_PATH.read_text(encoding="utf-8")
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load QC knowledge controls: {exc}")
        return 1

    evidence_types = set(schema.get("evidence_types", []))
    approval_states = set(schema.get("approval_states", []))
    promotion_types = set(schema.get("candidate_memory_types", []))
    gates = set(schema.get("gate", []))
    qc_contract = contracts.get("tasks", {}).get("QC-003")

    if evidence_types != REQUIRED_EVIDENCE_TYPES:
        errors.append("QC evidence vocabulary has drifted from the controlled set")
    if approval_states != REQUIRED_APPROVAL_STATES:
        errors.append("QC approval vocabulary has drifted from the controlled set")
    if promotion_types != REQUIRED_PROMOTION_TYPES:
        errors.append("QC memory promotion vocabulary has drifted from the controlled set")
    if gates != REQUIRED_GATES:
        errors.append("QC knowledge gates must be PASS / CONDITIONAL / BLOCKED")
    if not qc_contract:
        errors.append("QC-003 task contract is missing")
    elif set(qc_contract.get("gate", [])) != gates:
        errors.append("QC-003 contract gates do not match the QC knowledge schema")

    for value in sorted(evidence_types | approval_states | promotion_types | gates):
        if value not in prompt:
            errors.append(f"QC-003 prompt does not expose controlled value {value}")

    promotion_policy = schema.get("promotion_policy", {})
    if set(promotion_policy) != REQUIRED_PROMOTION_TYPES:
        errors.append("Every candidate QC memory type requires an explicit promotion policy")
    if "No candidate becomes an approved rule within QC-003 itself." not in prompt:
        errors.append("QC-003 must retain its non-promotion boundary")

    print(f"QC evidence types: {len(evidence_types)}")
    print(f"QC approval states: {len(approval_states)}")
    print(f"QC candidate memory types: {len(promotion_types)}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
