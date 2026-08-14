# Prompt Library v3 — Controlled Creative Production System

A version-controlled creative-production system in which prompts are executable tasks with defined inputs, boundaries, outputs, provenance, confidence, handoffs, and decision gates.

## Workflow

Customer Information
→ Strategy
→ Research
→ Visual Analysis
→ Visual DNA
→ Art Direction
→ Generation
→ Quality Control
→ Approval / Root-Cause Revision

## Control Layer

The orchestration rules live in `00_workflow/`:

- `workflow.md` — execution pipeline and revision routing
- `task_contract.md` — executable task standard
- `stage_registry.md` — stage responsibilities and active tasks
- `handoff_contract.md` — controlled transfer between stages
- `decision_gates.md` — pass/block/revise rules
- `information_model.md` — SOURCE / DERIVED / DECISION / OUTPUT states
- `task_registry.json` — machine-readable stages, tasks, dependencies, and gate vocabulary

## Active Prompt Sequence

### 01 — Strategy
- STR-001 — Customer Analysis
- STR-002 — Brief Analysis
- STR-003 — Requirement Extraction
- STR-004 — Clarification Questions
- STR-005 — Project Reconciliation

### 02 — Research
- RES-001 — Research Strategy
- RES-002 — Audience Research
- RES-003 — Competitor & Market Research
- RES-004 — Cultural & Context Research
- RES-005 — Visual Reference Research
- RES-006 — Research Synthesis

### 03 — Visual Analysis
- VIS-001 — Composition Analysis
- VIS-002 — Color Analysis
- VIS-003 — Shape & Form Analysis
- VIS-004 — Texture & Material Analysis
- VIS-005 — Typography & Graphic Language
- VIS-006 — Lighting, Mood & Atmosphere Analysis

### 04 — Visual DNA
- VDNA-001 — Visual DNA Extraction & Synthesis

### 05 — Art Direction
- ART-001 — Creative Concept Generation
- ART-002 — Concept Evaluation & Selection
- ART-003 — Art Direction Development

### 06 — Generation
- GEN-001 — Generation Specification
- GEN-002 — Prompt Construction

### 07 — Quality Control
- QC-001 — Generated Image Evaluation
- QC-002 — Revision Strategy

## Runtime

The `runtime/` package turns a prompt file into an auditable model execution.

- `runtime/runner.py` — provider abstraction for OpenAI and Gemini
- `runtime/run_task.py` — execute one task and persist a run artifact
- `runtime/evaluate_task.py` — LLM-based semantic evaluation using the project rubric
- `runtime/README.md` — setup and execution instructions

Provider credentials are supplied through environment variables. No credentials are stored in the repository.

## Testing

### Structural CI

`tests/validate_library.py` validates active prompt IDs, versions, statuses, stage prefixes, duplicates, deprecated files, and operational contract sections.

GitHub Actions also compiles runtime/test modules and validates the synthetic semantic-test assets.

### Semantic validation

The semantic framework uses the controlled Noura Coffee fixture and rubric in `tests/`. A production prompt change requires a semantic run with the selected model/runtime in addition to passing structural CI.

Semantic tests evaluate task adherence, source fidelity, unknown handling, completeness, classification, traceability, contract compliance, and handoff quality.

## Deprecated

`02_research/reference_selection.md` is retained only as a migration note. It is not an active task and is excluded from validation.

## Information Rules

Every important item must remain identifiable as one of:

- SOURCE — supplied or observed evidence
- DERIVED — analysis or inference supported by source
- DECISION — explicit approved project or creative choice
- OUTPUT — generated execution result

Forbidden silent transitions include:

- DERIVED → SOURCE
- ASSUMPTION → FACT
- OUTPUT → REQUIREMENT
- SOURCE → DECISION without an explicit decision step

## Quality Gates

A task cannot pass when a required input is missing, contradictory, or unsupported. Unknown information remains UNKNOWN.

A numerical score never overrides a critical failure.

QC routes failures to the earliest responsible stage rather than automatically regenerating.

## Production Release Rule

A production release requires:

1. Structural CI PASS.
2. No duplicate or invalid IDs.
3. No unresolved critical workflow dependency.
4. Prompt version/status present.
5. Relevant semantic tests PASS with the selected model/runtime.
6. Human approval for strategic/creative decision gates.
7. Release artifact records the model, prompt versions, and test results.

## Status

Production Candidate — structural runtime validation enabled; semantic release gate required.

## Version

3.0-production-candidate.1

## Core Principle

**Analyze → Structure → Research → Synthesize → Direct → Generate → Evaluate → Revise**
