# HEAVY-QC-001 — Human-Triggered Heavy QC Ensemble

## Purpose
Run a deeper computational assessment only when an authorized human explicitly asks for **Heavy QC**. The ensemble adds multiple independent technical and learned aesthetic signals to the existing project-calibrated review; it never grants creative approval.

## Trigger and authorization
- Trigger phrase: an authorized human asks for `heavy QC` or explicitly invokes `HEAVY-QC-001`.
- Runtime authorization: `--approval HEAVY_QC_APPROVED` is mandatory.
- Do not invoke this protocol during ordinary generation, CI, lightweight review, or automatic revision loops.
- Model downloads, external network access, and significant local computation occur only after this authorization.

## Assessment panel

Interpret the panel through `QC-AES-001_aesthetic_evidence_qc.md` and the model-scope knowledge in `00_workflow/knowledge/external/image_aesthetics_assessment_sources.md`.

### Aesthetic evidence
- `nima` — learned aesthetic-rating distribution signal.
- `musiq-ava` — multi-scale aesthetic signal trained/evaluated for AVA-style assessment.
- `topiq_iaa` — semantic-to-local aesthetic-quality signal.
- `clipiqa` — CLIP-based look-and-feel quality signal.

These are population/dataset-trained priors, not EBL taste, brand truth, or human preference. Disagreement between models is useful uncertainty evidence and must not be averaged away.

All learned results remain raw continuous evidence. Preserve their available precision; do not quantize them into `good/bad`, star bands, or approval classes. Compare a model only against that same model on approved examples from the same asset class. Until project baselines exist, disagreement is recorded as uncalibrated rather than converted into a synthetic number.

### No-reference technical evidence
- `brisque` — natural-scene-statistics distortion signal.
- `niqe` — opinion-unaware naturalness/distortion signal.
- Classical raw diagnostics — Laplacian variance, high-frequency residual spread, and JPEG 8-pixel boundary ratio.

Painterly texture, grain, soft focus, flat color, typography, and graphic compositions may violate photographic assumptions. Interpret these measurements relative to approved same-class examples.

### Full-reference evidence when an approved source exists
- `ssim` — structural similarity.
- `lpips` — learned perceptual distance.
- `psnr` — pixel-error signal.

Reference and candidate must have identical normalized dimensions. Intended changes must be declared before interpretation.

## Execution

```powershell
.\.venv\Scripts\python.exe runtime\heavy_qc.py <candidate-image> `
  --reference <approved-source-image> `
  --approval HEAVY_QC_APPROVED
```

Omit `--reference` for standalone assessment. Evidence is written under ignored `runs/heavy-qc/` unless `--output` is supplied.

## Interpretation and human gate
1. Verify that every metric ran and record failures as missing evidence.
2. Inspect raw values, metric direction, source/candidate hashes, and classical diagnostics.
3. Compare each model against the same model on approved examples of the same asset class; do not use universal pass thresholds or cross-model score arithmetic.
4. Reconcile model evidence with `QC-IQA-001`, `QC-IG-001`, `QC-AUD-001`, `QC-001`, and project rules.
5. Run `QC-AES-001` to assess graphic-design principles, model disagreement, project fit, and preference evidence.
6. An authorized human records the final `APPROVE`, `REVISE`, `REGENERATE`, or `BLOCKED` decision.

The runtime always returns `AWAITING_HUMAN_DECISION`; it cannot write final approval.

## Installation and storage
- Reproducible dependency: `requirements-heavy-qc.txt`.
- Local environment: `.venv/` (ignored by Git).
- Pretrained weights: downloaded by PyIQA on first authorized use to the user cache; never commit them.
- Training datasets are not required and must not be downloaded for routine Heavy QC.
- Review third-party model and code licenses before commercial use. IQA-PyTorch currently declares PolyForm Noncommercial and component-specific licensing.

## Output
Machine-readable JSON containing input identity, hashes, runtime/device, raw diagnostics, per-metric values/errors/direction/domain/range, continuous-evidence and calibration policy, and `AWAITING_HUMAN_DECISION` authority state.

## Version
1.1

## Status
Production Candidate
