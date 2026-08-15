from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


APPROVAL_PHRASE = "HEAVY_QC_APPROVED"
AESTHETIC_METRICS = ("nima", "musiq-ava", "topiq_iaa", "clipiqa")
NO_REFERENCE_METRICS = ("brisque", "niqe")
FULL_REFERENCE_METRICS = ("ssim", "lpips", "psnr")
METRIC_METADATA: dict[str, dict[str, Any]] = {
    "nima": {"evidence_type": "aesthetic", "training_domain": "AVA", "nominal_range": [0, 10]},
    "musiq-ava": {"evidence_type": "aesthetic", "training_domain": "AVA", "nominal_range": [1, 10]},
    "topiq_iaa": {"evidence_type": "aesthetic", "training_domain": "AVA", "nominal_range": [1, 10]},
    "clipiqa": {"evidence_type": "look_and_feel", "training_domain": "prompt-conditioned broad imagery", "nominal_range": [0, 1]},
    "brisque": {"evidence_type": "technical_no_reference", "training_domain": "natural-scene statistics"},
    "niqe": {"evidence_type": "technical_no_reference", "training_domain": "natural-scene statistics"},
    "ssim": {"evidence_type": "technical_full_reference", "training_domain": "structural similarity"},
    "lpips": {"evidence_type": "perceptual_full_reference", "training_domain": "learned perceptual similarity"},
    "psnr": {"evidence_type": "technical_full_reference", "training_domain": "pixel error"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the human-triggered Heavy QC evidence ensemble."
    )
    parser.add_argument("candidate", type=Path, help="Candidate image to assess")
    parser.add_argument("--reference", type=Path, help="Approved source image")
    parser.add_argument(
        "--approval",
        required=True,
        help=f"Explicit human authorization phrase: {APPROVAL_PHRASE}",
    )
    parser.add_argument("--output", type=Path, help="JSON evidence output path")
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    parser.add_argument(
        "--metrics",
        nargs="+",
        help="Override the default metric panel; intended for controlled diagnostics",
    )
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect_image(path: Path) -> dict[str, Any]:
    from PIL import Image, ImageOps

    with Image.open(path) as source:
        normalized = ImageOps.exif_transpose(source)
        return {
            "path": str(path.resolve()),
            "sha256": sha256(path),
            "format": source.format,
            "width": normalized.width,
            "height": normalized.height,
            "mode": normalized.mode,
            "has_alpha": "A" in normalized.getbands(),
            "file_bytes": path.stat().st_size,
        }


def classical_diagnostics(path: Path) -> dict[str, Any]:
    import cv2
    import numpy as np
    from PIL import Image, ImageOps

    with Image.open(path) as source:
        rgb = np.asarray(ImageOps.exif_transpose(source).convert("RGB"), dtype=np.uint8)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    residual = gray.astype(np.float32) - cv2.GaussianBlur(gray, (3, 3), 0).astype(np.float32)

    # JPEG-style 8 px boundary discontinuity. Raw evidence only; no universal threshold.
    vertical = np.abs(np.diff(gray.astype(np.float32), axis=1))
    horizontal = np.abs(np.diff(gray.astype(np.float32), axis=0))
    v_boundaries = vertical[:, 7::8]
    h_boundaries = horizontal[7::8, :]
    v_nonboundaries = np.delete(vertical, np.arange(7, vertical.shape[1], 8), axis=1)
    h_nonboundaries = np.delete(horizontal, np.arange(7, horizontal.shape[0], 8), axis=0)
    boundary_mean = float(np.mean([v_boundaries.mean(), h_boundaries.mean()]))
    background_mean = float(np.mean([v_nonboundaries.mean(), h_nonboundaries.mean()]))

    return {
        "laplacian_variance": float(laplacian.var()),
        "high_frequency_residual_std": float(residual.std()),
        "jpeg_block_boundary_ratio": boundary_mean / max(background_mean, 1e-8),
        "interpretation": "Raw diagnostics require comparison to approved same-class examples.",
    }


def resolve_device(requested: str) -> str:
    import torch

    if requested == "auto":
        return "cuda" if torch.cuda.is_available() else "cpu"
    if requested == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but not available")
    return requested


def run_metric(name: str, candidate: Path, reference: Path | None, device: str) -> dict[str, Any]:
    import pyiqa

    result: dict[str, Any] = {
        "name": name,
        **METRIC_METADATA.get(name, {"evidence_type": "unknown", "training_domain": "unknown"}),
        "interpretation_status": "UNCLASSIFIED_CONTINUOUS_EVIDENCE",
        "calibration_baseline_required": True,
    }
    try:
        metric = pyiqa.create_metric(name, device=device)
        result["lower_better"] = bool(metric.lower_better)
        if name in FULL_REFERENCE_METRICS:
            if reference is None:
                raise ValueError("reference image required")
            value = metric(str(candidate), str(reference))
        else:
            value = metric(str(candidate))
        numeric = float(value.detach().cpu().reshape(-1)[0].item())
        if not math.isfinite(numeric):
            raise ValueError(f"metric returned non-finite value {numeric}")
        result.update(status="MEASURED", value=numeric)
    except Exception as exc:  # Preserve partial evidence when one optional model fails.
        result.update(status="ERROR", error=f"{type(exc).__name__}: {exc}")
    return result


def main() -> int:
    args = parse_args()
    if args.approval != APPROVAL_PHRASE:
        print("BLOCKED: Heavy QC requires explicit human approval.", file=sys.stderr)
        return 2

    candidate = args.candidate.resolve()
    reference = args.reference.resolve() if args.reference else None
    if not candidate.is_file():
        print(f"BLOCKED: candidate does not exist: {candidate}", file=sys.stderr)
        return 2
    if reference is not None and not reference.is_file():
        print(f"BLOCKED: reference does not exist: {reference}", file=sys.stderr)
        return 2

    candidate_info = inspect_image(candidate)
    reference_info = inspect_image(reference) if reference else None
    if reference_info and (
        candidate_info["width"], candidate_info["height"]
    ) != (reference_info["width"], reference_info["height"]):
        print("BLOCKED: full-reference inputs must have identical normalized dimensions.", file=sys.stderr)
        return 2

    device = resolve_device(args.device)
    metrics = tuple(args.metrics or (AESTHETIC_METRICS + NO_REFERENCE_METRICS))
    if reference:
        metrics += tuple(name for name in FULL_REFERENCE_METRICS if name not in metrics)

    evidence = {
        "schema_version": "1.0",
        "protocol": "HEAVY-QC-001",
        "trigger": "EXPLICIT_HUMAN_REQUEST",
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "candidate": candidate_info,
        "reference": reference_info,
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "device": device,
        },
        "classical_diagnostics": classical_diagnostics(candidate),
        "metric_results": [run_metric(name, candidate, reference, device) for name in metrics],
        "evidence_policy": {
            "score_representation": "CONTINUOUS_RAW_VALUES",
            "precision_rule": "Preserve model output precision; do not quantize into aesthetic classes.",
            "aggregation": None,
            "comparison_rule": "Compare each model only with the same model on approved same-class examples.",
            "model_disagreement": "NOT_COMPUTED_WITHOUT_PROJECT_CALIBRATION",
        },
        "authority": {
            "automated_decision": None,
            "approval_status": "AWAITING_HUMAN_DECISION",
            "rule": "Scores are evidence only and cannot approve, reject, or redefine direction.",
        },
    }

    output = args.output
    if output is None:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output = Path("runs") / "heavy-qc" / f"{candidate.stem}-{stamp}.json"
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(evidence, indent=2), encoding="utf-8")

    errors = sum(item["status"] == "ERROR" for item in evidence["metric_results"])
    print(f"Heavy QC evidence: {output}")
    print(f"Metrics measured: {len(evidence['metric_results']) - errors}")
    print(f"Metric errors: {errors}")
    print("Approval status: AWAITING_HUMAN_DECISION")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
