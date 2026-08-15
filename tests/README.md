# Semantic Test Framework

## Purpose

Structural CI checks whether the repository is internally valid. Semantic tests check whether prompts perform their intended creative-production task on realistic inputs.

## Test Levels

### Level 1 — Structural

Checks IDs, stages, versions, required sections, deprecated files, and workflow references.

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
