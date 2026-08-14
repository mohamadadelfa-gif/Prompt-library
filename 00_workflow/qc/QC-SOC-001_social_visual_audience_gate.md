# QC-SOC-001 — Social Visual + Audience Gate

## Purpose
Run Instagram visual QC and audience-catcher QC as one controlled pre-Figma gate while preserving their separate scores and findings.

## Required inputs
- Candidate ID and asset
- Locked copy
- Platform and format
- Slide narrative map
- EBL audience record
- EBL visual grammar
- Motif curation rules
- Relevant approved human revisions

## Execution order
1. Run `QC-IG-001_instagram_visual_qc.md`.
2. If a critical visual/content failure exists, stop and return FAIL.
3. Run `QC-AUD-001_audience_catcher_qc.md`.
4. Merge findings into one revision brief.
5. Require human decision before Figma.

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
6. Painterly/artistic refinement
7. Low-severity polish

## Rule
A high audience score cannot compensate for visual/brand failure, and a beautiful visual cannot compensate for weak audience relevance or content fidelity.
