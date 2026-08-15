# QC-AES-001 — Aesthetic Evidence QC

## Purpose
Evaluate aesthetic quality through traceable graphic-design principles, project-calibrated judgment, and optional learned-model evidence. The protocol produces an evidence package for human decision; it cannot grant approval.

## Required inputs
- Candidate ID and asset(s)
- Asset class, platform, and viewing size
- Approved project strategy, Visual DNA, and Art Direction
- Content role and locked copy
- Applicable human preferences and approved/rejected examples
- Model evidence package when Heavy QC was explicitly authorized

## Preconditions
- Project direction and candidate identity must be known.
- If project rules or viewing context are absent, return `BLOCKED` rather than substituting generic taste.
- Learned metrics are optional evidence. Missing models must be recorded as unavailable, never treated as a pass.

## Gates

### AES-01 Context and intention — mandatory
Identify what the design must communicate, for whom, where, and under which approved direction. Judge deliberate choices within that context.

### AES-02 Composition and hierarchy
Assess focal priority, reading path, balance, tension, alignment, grouping, scale relationships, rhythm, visual weight, and use of negative space.

### AES-03 Typography and layout
Assess type hierarchy, font-role consistency, line length, line breaks, spacing, contrast, text-image integration, density, and platform-size readability. Distinguish stylistic irregularity from accidental typesetting damage.

### AES-04 Color aesthetics
Assess palette coherence, contrast, emphasis, spatial color distribution, temperature, saturation relationships, accessibility, and consistency with approved direction. Do not reduce color quality to histogram statistics.

### AES-05 Material, texture, and craft
Assess whether texture, grain, brushwork, edges, layering, and irregularity have compositional or semantic purpose. Separate intended material character from noise, compression, or careless export.

### AES-06 Theme, meaning, and emotional fit
Assess whether form supports the content territory, intended emotional tone, audience experience, and project character. Generic learned scores cannot pass this gate.

### AES-07 Distinctiveness and coherence
Assess recognizability, originality within constraints, cross-asset family resemblance, meaningful variation, motif discipline, and avoidance of generic template behavior.

### AES-08 Learned evidence interpretation
When Heavy QC is authorized, preserve each model result separately with model/version, training-domain caveat, direction, raw continuous value, asset class, and availability status. Do not quantize continuous scores into rating classes. Record agreement and disagreement only after model-specific calibration; do not create an aggregate approval score.

### AES-09 Human preference calibration
Compare against identified approved/rejected project examples when available. Record whether an observation is a project rule, repeated preference, single-example signal, or model inference.

### AES-10 Human decision — mandatory
An authorized human decides `APPROVE`, `REVISE`, `REGENERATE`, or `BLOCKED`. Model values and heuristic findings remain advisory evidence.

## Severity
- `CRITICAL` — contradicts content truth, approved direction, identity integrity, or usable communication.
- `MAJOR` — materially weakens hierarchy, readability, composition, coherence, or intended experience.
- `MINOR` — localized refinement opportunity.
- `INFORMATIONAL` — observation or uncertain model signal requiring no immediate correction.

## Output contract

```yaml
candidate_id: ""
protocol: QC-AES-001
asset_class: ""
viewing_context: ""
project_evidence:
  rules: []
  approved_examples: []
  rejected_examples: []
gate_results:
  - gate: AES-01
    status: PASS|CONDITIONAL|BLOCKED
    evidence: ""
    severity: INFORMATIONAL|MINOR|MAJOR|CRITICAL
    revision: ""
learned_evidence:
  - model: ""
    version: ""
    training_domain: ""
    status: MEASURED|UNAVAILABLE|ERROR
    value: null
    interpretation_status: UNCLASSIFIED_CONTINUOUS_EVIDENCE
    calibration_baseline: null
    lower_better: null
    caveat: ""
model_disagreement: []
preserve: []
revise: []
unknowns: []
provisional_result: PASS|CONDITIONAL|BLOCKED
final_human_decision: AWAITING_HUMAN_DECISION
```

## Scoring boundary
Do not calculate a universal aesthetic score. Preserve model precision and do not turn regression evidence into coarse aesthetic classes. Project-specific interpretation may be defined only from approved criteria and same-model, same-asset-class calibrated examples. A model ensemble cannot compensate for a critical content, brand, typography, or usability failure.

## Knowledge handoff
Pass evidence to `QC-003` only with candidate/version identity, model provenance, human decision, and scope. A model result is `MODEL_INFERENCE`; one human correction is not automatically a reusable rule. Repeated approved evidence may become a project QC candidate through the normal promotion policy.

## Handoff
- `PASS` or `CONDITIONAL` → authorized human review.
- `BLOCKED` → obtain missing direction, context, asset, or evidence.
- Human `REVISE` or `REGENERATE` → route through the applicable revision protocol and rerun this QC.

## Version
1.1

## Status
Production Candidate
