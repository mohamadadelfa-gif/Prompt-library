# QC-SOC-001 — Social Visual + Audience Gate

## Purpose
Run Instagram visual QC, audience-catcher QC, and technical image-quality QC as one controlled pre-Figma gate while preserving their separate evidence, scores, and authority boundaries.

## Required inputs
- Candidate ID and asset
- Locked copy
- Platform and format
- Slide narrative map
- EBL audience record
- EBL visual grammar
- Motif curation rules
- Relevant approved human revisions
- Expected export specification
- Approved comparison source and intended transformations when reference fidelity applies

## Execution order
1. Run `QC-IG-001_instagram_visual_qc.md`.
2. If a critical visual/content failure exists, stop and return FAIL.
3. Run `QC-AUD-001_audience_catcher_qc.md`.
4. Run `QC-IQA-001_technical_image_quality_qc.md`.
5. If technical QC is BLOCKED, stop; do not substitute an aesthetic judgment for missing measurements.
6. Merge findings into one revision brief without combining the three scores into a single synthetic score.
7. Require human decision before Figma.

`HEAVY-QC-001` is optional and runs only after an authorized human explicitly requests `heavy QC`. Its measurements are appended as evidence and do not change the authority of this gate.

## Final states
- `PASS` — both QCs pass and no unresolved critical/high finding remains.
- `PASS_WITH_REVISION` — no critical failure, but revision is recommended before human approval.
- `FAIL` — any mandatory gate fails or a critical issue remains.

## Output contract

```yaml
candidate_id: POST-XXX-GEN-vN
platform: instagram
format: carousel|single|reel_cover|story

instagram_visual_qc:
  result: PASS|PASS_WITH_REVISION|FAIL
  score: 0-100
  critical_failures: []
  gate_results:
    - gate: IG-01
      status: PASS|PARTIAL|FAIL
      evidence: ""
      revision: ""

audience_catcher_qc:
  result: PASS|PASS_WITH_REVISION|FAIL
  score: 0-100
  critical_failures: []
  gate_results:
    - gate: AUD-01
      status: PASS|PARTIAL|FAIL
      evidence: ""
      revision: ""

technical_image_quality_qc:
  result: PASS|CONDITIONAL|BLOCKED
  comparison_type: STANDALONE|SOURCE_TO_REVISED|REVISED_TO_EXPORT
  critical_failures: []
  measurements:
    - check: IQA-01
      metric: ""
      value: ""
      threshold_or_baseline: ""
      status: PASS|CONDITIONAL|BLOCKED
  findings: []

combined_findings:
  preserve: []
  revise_now: []
  learning_candidates: []

final_gate:
  result: PASS|PASS_WITH_REVISION|FAIL
  human_approval_required: true
  figma_handoff_allowed: false
```

## Revision priority
1. Critical content/truth failure
2. Instagram readability/usability failure
3. Audience relevance/hook failure
4. Visual identity/grammar failure
5. Narrative/retention failure
6. Unintended raster/reference damage
7. Painterly/artistic refinement
8. Low-severity polish

## Rule
A high audience score cannot compensate for visual/brand failure, and a beautiful visual cannot compensate for weak audience relevance or content fidelity.

Technical measurements provide evidence about blur, compression, noise, artifacts, export fitness, and unintended reference divergence. They cannot score aesthetics, brand direction, meaning, composition quality, creative decisions, human preference, or approval status. Human approval remains mandatory.
