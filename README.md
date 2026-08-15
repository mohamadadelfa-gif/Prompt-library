# Prompt Library v3 — Controlled Creative Production System

A version-controlled creative-production system in which prompts are executable tasks with defined inputs, boundaries, outputs, provenance, confidence, handoffs, and decision gates.

## Workflow

Customer Information
→ Strategy
→ Research
→ Visual Analysis
→ Conditional Style Study and Motif Extraction
→ Reference Style Synthesis
→ Visual DNA
→ Platform / Template Synthesis
→ Art Direction
→ Generation
→ Content Package
→ Human Revision / Style Learning
→ Conditional Editable Reconstruction
→ Figma Implementation
→ Quality Control / Final Approval

## Control Layer

The orchestration rules live in `00_workflow/`:

- `workflow.md` — execution pipeline and revision routing
- `task_contract.md` — universal executable-task standard
- `task_contracts.json` — canonical task-level dependencies, gates, approvals, and revision policy
- `stage_registry.md` — stage responsibilities and active tasks
- `handoff_contract.md` — controlled transfer between stages
- `decision_gates.md` — canonical gate vocabulary and approval rules
- `information_model.md` — SOURCE / DERIVED / DECISION / OUTPUT states
- `task_registry.json` — machine-readable stage/task index
- `process_registry.json` — canonical 15-stage production process, including goals, conditions, artifacts, gates, protocols, and memory effects

## Canonical Gate Vocabulary

All active prompts and task contracts use only:

`PASS` · `CONDITIONAL` · `BLOCKED` · `APPROVE` · `REVISE` · `REJECT` · `READY` · `REGENERATE`

Natural-language explanations may accompany a gate, but the final status must use the canonical value.

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

The optional `runtime/` package turns a prompt file into an auditable model execution. It is not required for structural consistency validation.

## Testing

### Structural CI

`tests/validate_library.py` validates:

- active prompt IDs and stage prefixes
- exact match between active prompts and task contracts
- task-level dependencies and next-task references
- canonical gate vocabulary
- lifecycle status
- deprecated/retired references
- domain-specific leakage
- required task-contract metadata
- canonical 15-stage process order, task coverage, protocol paths, stage dependencies, gates, artifacts, and memory effects

### Semantic validation

The semantic framework in `tests/` evaluates task adherence, source fidelity, unknown handling, completeness, classification, traceability, contract compliance, and handoff quality against controlled fixtures.

Semantic execution remains a separate release gate because it depends on a selected model/runtime.

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

## Revision Control

Maximum automatic revision cycles: **3**. After the third unsuccessful cycle, route to **HUMAN_REVIEW** rather than continuing automatically.

## Production Release Rule

A production release requires:

1. Structural CI PASS.
2. No duplicate or invalid IDs.
3. Exact task-contract alignment.
4. No unresolved critical workflow dependency.
5. Production-eligible prompt version/status.
6. Relevant semantic tests PASS with the selected model/runtime.
7. Required human approvals recorded.
8. Release artifact records prompt versions, model/runtime, and test results.

## Status

Production Candidate — consistency controls hardened; semantic release gate remains separate.

## Version

3.1-production-candidate

## Core Principle

**Analyze → Structure → Research → Synthesize → Direct → Generate → Evaluate → Revise**
