# LLM Evaluator Protocol

## Purpose

Evaluate model-generated text with a versioned rubric and a controlled LLM-as-judge process while separating content failure, generating-model failure, judge failure, rubric failure and infrastructure failure.

This protocol extends the existing semantic test framework. It does not allow an evaluator score to override source fidelity, mandatory gates or human approval.

## Activation

Use when a generated text artifact requires semantic, audience, literacy, pedagogical, purpose, vocabulary, sentence-structure, subject-matter or model-comparison evaluation.

Educational dimensions are conditional. Do not apply grade-level or pedagogy rubrics to non-educational content unless the task explicitly requires them.

## Required Inputs

- immutable candidate text and candidate ID;
- generation task/prompt version;
- approved requirements and source evidence;
- evaluator ID, version and rubric version;
- target population, audience or grade band when relevant;
- calibration status and benchmark provenance;
- judge model/provider configuration when execution is authorized;
- explicit unknowns and exclusions.

## Evaluator Contract

Every evaluator must declare:

- dimension and operational definition;
- intended use and prohibited use;
- input/output schema;
- scoring scale and anchors;
- pass/fail thresholds and critical failures;
- evidence required for every judgment;
- handling for missing, ambiguous and out-of-domain input;
- calibration dataset/version and licensing;
- known limitations, bias risks and expected disagreement;
- judge model/provider/version/settings;
- evaluator prompt/version;
- retry and adjudication policy.

## Evidence-First Judgment

The judge must cite candidate excerpts or source-linked evidence for every material score. Unsupported evaluator explanations are invalid even if the score appears plausible.

The evaluator must not reward fluent writing that contradicts approved facts, invents evidence, ignores task constraints or changes the intended audience.

## Failure Classification

Classify the primary failure as one or more of:

- `CONTENT_FAILURE` — the candidate itself violates the rubric;
- `GENERATOR_FAILURE` — the generating model failed the prompt or task contract;
- `EVALUATOR_FAILURE` — the judge misread evidence, contradicted anchors or produced invalid output;
- `RUBRIC_FAILURE` — criteria, anchors or thresholds are ambiguous or unsuitable;
- `DATASET_FAILURE` — calibration labels, coverage or licensing are inadequate;
- `INPUT_FAILURE` — required source, audience or task context is missing;
- `INFRASTRUCTURE_FAILURE` — provider, credential, quota, schema, network or runtime failure;
- `DISAGREEMENT` — valid judges or experts reach materially different supported conclusions.

Do not route every low score to regeneration. Route correction to the earliest responsible layer.

## Calibration

An evaluator is not production-ready merely because it produces valid JSON.

Record, when available:

- expert-annotated benchmark identity and license;
- sample count and domain coverage;
- train/development/test separation;
- agreement against experts;
- confusion or error analysis;
- threshold selection rationale;
- subgroup, language, script and difficulty coverage;
- evaluator version/model/settings used for calibration;
- drift date and recalibration trigger.

If no approved calibration exists, the evidence status is `EXPERIMENTAL` and cannot act as an automatic release gate.

## Judge Independence and Leakage

- Do not expose expected labels to the judge.
- Do not evaluate on examples used to tune the same evaluator without marking leakage.
- Prefer blinded candidate ordering for comparisons.
- Randomize or counterbalance order where position bias matters.
- Preserve raw judge outputs for audit.
- Treat self-evaluation by the same generating model as weaker evidence unless independently calibrated.

## Repetition and Adjudication

Use repeated judgments only when variance materially affects the decision. Record all runs rather than only the preferred result.

When judgments conflict:

1. verify input and rubric version;
2. inspect cited evidence and schema validity;
3. classify judge/rubric/domain mismatch;
4. run an independent judge or human adjudication when required;
5. preserve disagreement rather than averaging away a critical conflict.

## Output

Produce `LLM_EVALUATOR_EVIDENCE` following `qc/llm_evaluator_evidence_schema.json`.

The evidence package must contain:

- candidate and evaluator identities;
- rubric, judge and calibration provenance;
- dimension scores and evidence excerpts;
- critical failures;
- uncertainty and disagreement;
- failure classification and revision route;
- reproducibility metadata;
- final gate recommendation;
- human-decision state.

## Knowledge-Graph Handoff

Register material evaluator results as `QC_EVIDENCE` nodes. Link them using:

```text
QC_EVIDENCE EVALUATES OUTPUT
QC_TASK PRODUCES QC_EVIDENCE
QC_EVIDENCE SUPPORTS DECISION
```

An evaluator result is evidence, not a decision. Human approval remains separate.

## Security and Credentials

- Never commit API keys, provider tokens, raw browser credentials or confidential evaluation inputs.
- Use project-ignored environment files and existing secure credential handling.
- Structural CI must not require paid provider calls.
- Store only the minimum raw evaluation material permitted by project privacy rules.

## Gate

- `PASS` — evaluator is applicable, valid, sufficiently calibrated and the candidate meets all critical requirements.
- `CONDITIONAL` — useful evidence exists with declared limitations or experimental calibration.
- `BLOCKED` — required input, evaluator validity, calibration, provider execution or evidence is insufficient.
- `REVISE` — the candidate has a correctable, well-supported content failure.

A numeric aggregate never overrides a critical source-fidelity, safety, licensing, privacy or approval failure.

## Provenance

Adapted conceptually from Learning Commons Evaluators. General evaluator architecture and terminology were reimplemented for Prompt Library. Upstream evaluator code is MIT-licensed; evaluator prompts/settings are CC BY 4.0; the annotated CLEAR dataset is CC BY-NC-SA 4.0 and is not incorporated here.

## Version

1.0-production-candidate

## Status

Active conditional protocol
