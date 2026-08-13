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

## Automated Validation

`tests/validate_library.py` validates active prompt IDs, versions, statuses, stage prefixes, duplicates, and required operational sections.

GitHub Actions runs the validator on changes to the v3 branch and pull requests.

## Status

Active — validation and end-to-end testing

## Version

3.0

## Core Principle

**Analyze → Structure → Research → Synthesize → Direct → Generate → Evaluate → Revise**
