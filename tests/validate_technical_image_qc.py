from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IQA_PATH = ROOT / "00_workflow" / "qc" / "QC-IQA-001_technical_image_quality_qc.md"
SOC_PATH = ROOT / "00_workflow" / "qc" / "QC-SOC-001_social_visual_audience_gate.md"
HEAVY_PATH = ROOT / "00_workflow" / "qc" / "HEAVY-QC-001_human_triggered_ensemble.md"
RUNTIME_PATH = ROOT / "runtime" / "heavy_qc.py"
AES_PATH = ROOT / "00_workflow" / "qc" / "QC-AES-001_aesthetic_evidence_qc.md"
AES_KNOWLEDGE_PATH = ROOT / "00_workflow" / "knowledge" / "external" / "image_aesthetics_assessment_sources.md"

REQUIRED_CHECKS = {f"IQA-{number:02d}" for number in range(1, 9)}
PROTECTED_HUMAN_JUDGMENTS = {
    "aesthetics",
    "brand direction",
    "content meaning",
    "composition quality",
    "creative decisions",
    "human preference",
    "approval status",
}


def main() -> int:
    errors: list[str] = []
    try:
        iqa = IQA_PATH.read_text(encoding="utf-8")
        social = SOC_PATH.read_text(encoding="utf-8")
        heavy = HEAVY_PATH.read_text(encoding="utf-8")
        runtime = RUNTIME_PATH.read_text(encoding="utf-8")
        aesthetic = AES_PATH.read_text(encoding="utf-8")
        aesthetic_knowledge = AES_KNOWLEDGE_PATH.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: cannot load technical image QC controls: {exc}")
        return 1

    for check in sorted(REQUIRED_CHECKS):
        if check not in iqa:
            errors.append(f"Technical image QC is missing {check}")

    for judgment in sorted(PROTECTED_HUMAN_JUDGMENTS):
        if judgment not in iqa:
            errors.append(f"Technical image QC does not protect human judgment: {judgment}")

    for concept in (
        "blur",
        "compression",
        "noise",
        "artifacts",
        "reference fidelity",
        "logo and typography damage",
        "original → revised → approved/export",
    ):
        if concept not in iqa.lower():
            errors.append(f"Technical image QC is missing required concept: {concept}")

    if "QC-IQA-001_technical_image_quality_qc.md" not in social:
        errors.append("Combined social QC does not invoke QC-IQA-001")
    if "without combining the three scores" not in social:
        errors.append("Combined social QC must prohibit a synthetic aggregate score")
    if "Human approval remains mandatory." not in social:
        errors.append("Combined social QC must preserve human approval authority")

    for metric in ("nima", "musiq-ava", "topiq_iaa", "clipiqa", "brisque", "niqe", "ssim", "lpips", "psnr"):
        if metric not in heavy or metric not in runtime:
            errors.append(f"Heavy QC is missing controlled metric: {metric}")
    for control in ("HEAVY_QC_APPROVED", "AWAITING_HUMAN_DECISION"):
        if control not in heavy or control not in runtime:
            errors.append(f"Heavy QC is missing human authority control: {control}")
    if "Do not invoke this protocol" not in heavy:
        errors.append("Heavy QC must prohibit automatic invocation")

    for gate in (f"AES-{number:02d}" for number in range(1, 11)):
        if gate not in aesthetic:
            errors.append(f"Aesthetic evidence QC is missing {gate}")
    for source in ("AES-SRC-001", "AES-SRC-002", "AES-SRC-003", "AES-SRC-004"):
        if source not in aesthetic_knowledge:
            errors.append(f"Aesthetic knowledge package is missing {source}")
    for boundary in ("MODEL_INFERENCE", "AWAITING_HUMAN_DECISION"):
        if boundary not in aesthetic:
            errors.append(f"Aesthetic evidence QC is missing authority boundary: {boundary}")
    if "QC-AES-001" not in heavy or "image_aesthetics_assessment_sources.md" not in heavy:
        errors.append("Heavy QC is not connected to aesthetic knowledge and QC")
    for control in (
        "UNCLASSIFIED_CONTINUOUS_EVIDENCE",
        "CONTINUOUS_RAW_VALUES",
        "NOT_COMPUTED_WITHOUT_PROJECT_CALIBRATION",
    ):
        if control not in runtime:
            errors.append(f"Heavy QC runtime is missing continuous evidence control: {control}")
    if "do not quantize" not in aesthetic.lower() or "same-model" not in aesthetic.lower():
        errors.append("Aesthetic QC must preserve precision and require same-model calibration")

    print(f"Technical checks: {len(REQUIRED_CHECKS)}")
    print(f"Protected human judgments: {len(PROTECTED_HUMAN_JUDGMENTS)}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
