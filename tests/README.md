# Semantic Test Framework

## Purpose

Structural CI checks whether the repository is internally valid. Semantic tests check whether prompts perform their intended creative-production task on realistic inputs.

## Test Levels

### Level 1 — Structural

Checks IDs, stages, versions, required sections, deprecated files, and workflow references.

`validate_presentation_layout_guard.py` also verifies that the presentation source guard accepts a minimally safe deck and rejects a known P0 layout failure.

`validate_evaluator_contract.py` verifies the versioned LLM-evaluator evidence contract, failure taxonomy, calibration state and preserved human-decision authority.

`validate_carousel_exporter.py` verifies Instagram format dimensions, aspect-ratio safety and a side-effect-free exporter preflight without installing Playwright or downloading Chromium.

`validate_design_system_references.py` verifies unique reference IDs, official HTTPS sources, and the mandatory freshness and no-automatic-adoption safeguards.

`validate_design_token_system.py` verifies the Learn–Structure–Refine token template, tiered names, reference resolution, theme parity, component states, and raw-value safeguards.

### Level 2 — Contract

Checks that each task declares required inputs, boundaries, outputs, provenance, confidence, unknown handling, gate, and handoff.

### Level 3 — Semantic

Runs selected prompts against controlled synthetic fixtures and evaluates:

- task adherence
- factual/source fidelity
- unsupported invention
- completeness
- classification accuracy
- traceability
- output-schema compliance
- downstream usability

### Level 4 — End-to-End

Runs the complete pipeline against a synthetic project and verifies that every handoff can satisfy the next stage without hidden assumptions.

## Evaluation Principles

A test must distinguish:

- prompt failure
- input insufficiency
- model failure
- evaluator failure

A semantic test must never mark an invented answer correct merely because it sounds plausible.

LLM-as-judge evidence must additionally identify evaluator, rubric, judge model/settings, calibration state, candidate excerpts, uncertainty, failure class and revision route. Evaluator evidence supports—but never replaces—the final human decision.

## Required Test Artifacts

Each test should contain:

- fixture
- prompt/version under test
- expected invariants
- actual output
- evaluator result
- failure category
- severity
- regression status

## Current Fixture

`tests/fixtures/noura_coffee/project_input.md` is a synthetic project used only for controlled testing. It deliberately contains explicit facts and explicit unknowns so the pipeline can be tested for provenance and hallucination control.
