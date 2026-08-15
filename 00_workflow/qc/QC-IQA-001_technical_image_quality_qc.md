# QC-IQA-001 — Technical Image Quality QC

## Purpose
Provide reproducible technical evidence about raster quality and visual damage. This protocol detects defects and compares source, revision, and export assets; it does not decide whether a design is aesthetically successful, on-brand, meaningful, or approved.

## Required inputs
- Candidate ID and candidate raster/export
- Asset role and intended platform
- Expected output dimensions and file format
- Approved source or prior approved image when fidelity comparison is required
- Comparison type: `STANDALONE`, `SOURCE_TO_REVISED`, or `REVISED_TO_EXPORT`
- Known intentional changes and allowed crop/resize/format transformations

## Preconditions
- Inputs must be identified by stable path or artifact ID.
- Reference and candidate must be normalized for orientation, color mode, dimensions, and alpha handling before pixel or perceptual comparison.
- A comparison must not treat an approved intentional change as damage.
- Missing source assets or missing intended transformations produce `BLOCKED`, not an invented score.

## Checks

### IQA-01 File and raster integrity — mandatory
Confirm that the asset decodes successfully and record format, dimensions, color mode, alpha, file size, and metadata warnings. Reject corrupt, empty, truncated, or unintended-resolution output.

### IQA-02 Blur and sharpness
Measure and localize unexpected loss of edge definition or detail. Use metrics only relative to asset type, scale, and an approved reference; painterly softness and intentional depth-of-field are not defects by themselves.

### IQA-03 Compression and encoding artifacts
Detect blocking, ringing, banding, mosquito noise, posterization, severe chroma degradation, and repeated lossy re-encoding.

### IQA-04 Noise and contamination
Detect unintended sensor-like noise, speckling, dirty alpha edges, isolated pixels, halos, and export contamination. Do not penalize approved grain, paper texture, brush texture, or material variation.

### IQA-05 Structural and reference fidelity
For normalized image pairs, calculate perceptual/structural similarity and difference localization. Report where the candidate diverges; do not infer whether the divergence is acceptable without consulting approved change instructions.

### IQA-06 Logo and typography damage
Inspect protected regions for clipped marks, distorted proportions, changed spacing, rasterized text degradation, glyph corruption, edge halos, or accidental movement. OCR or feature matching may support evidence but cannot authorize copy or identity changes.

### IQA-07 Export fitness
Check target dimensions, aspect ratio, crop safety, scaling artifacts, transparency behavior, color consistency, and platform delivery constraints.

### IQA-08 Comparison chain
When original, revised, and approved/export images exist, compare adjacent controlled states:

`original → revised → approved/export`

Record each intended transformation separately so that defect attribution remains traceable.

## Measurement rules
- Record the tool, version, parameters, thresholds, normalization, and region used for every metric.
- Prefer reference-aware measurements when a valid approved source exists.
- Report raw measurements and threshold outcomes; never present a synthetic score without its components.
- Thresholds are asset-class and project specific. Calibrate them from approved examples; do not invent universal quality thresholds.
- Separate whole-image findings from localized logo, typography, and focal-region findings.
- A metric anomaly is evidence for inspection, not proof of creative failure.

## Output contract

```yaml
candidate_id: POST-XXX-GEN-vN
protocol: QC-IQA-001
comparison_type: STANDALONE|SOURCE_TO_REVISED|REVISED_TO_EXPORT
inputs:
  reference_id: ""
  candidate_id: ""
  intentional_changes: []
normalization:
  orientation: ""
  dimensions: ""
  color_mode: ""
  alpha_handling: ""
measurements:
  - check: IQA-01
    metric: ""
    value: ""
    threshold_or_baseline: ""
    tool_and_version: ""
    parameters: ""
    region: whole_image
    status: PASS|CONDITIONAL|BLOCKED
findings:
  - severity: CRITICAL|MAJOR|MINOR|INFORMATIONAL
    location: ""
    observation: ""
    evidence: ""
    likely_cause: ""
    revision_action: ""
technical_result: PASS|CONDITIONAL|BLOCKED
human_visual_review_required: true
```

## Decision rules
- `PASS` — required checks ran and no unintended material defect was found.
- `CONDITIONAL` — a measurable anomaly or low-severity defect requires review or correction.
- `BLOCKED` — an input, reference, normalization rule, tool result, or required comparison is missing or invalid.
- Any corrupt/unusable output or material damage to protected logo, typography, or content regions blocks approval until corrected.

## Boundaries
This protocol does not determine:
- aesthetics or artistic merit;
- brand direction or visual identity compliance;
- content meaning or truth;
- composition quality, creative effectiveness, or creative decisions;
- human preference or emotional resonance;
- final approval status.

Those decisions remain with `QC-IG-001`, `QC-AUD-001`, `QC-001`, applicable project rules, and the authorized human approver.

## Handoff
Pass the technical evidence package to `QC-SOC-001` and `QC-001`. Findings may trigger export correction, localized reconstruction, revision, or regeneration. Technical measurements must remain attached to the candidate/version they evaluated.

When an authorized human explicitly requests `heavy QC`, also run `HEAVY-QC-001_human_triggered_ensemble.md`. Never trigger the learned ensemble automatically.

## Version
1.0

## Status
Production Candidate
