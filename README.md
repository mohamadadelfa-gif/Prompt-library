# Prompt Library v3 — Controlled Creative Production System

A version-controlled creative-production system in which prompts are executable tasks with defined inputs, boundaries, outputs, provenance, confidence, handoffs, and decision gates.

## Dual Workflow Architecture

The repository now has two sibling execution workflows:

```text
WRITING WORKFLOW
DESIGN WORKFLOW
```

They function separately but may use a controlled Shared Knowledge Layer for research, project knowledge, external references, structures, and tools.

They do **not** silently share approvals, execution state, QC results, or domain decisions.

### Writing Workflow

Used for:

- textual research
- source search and evaluation
- article/document analysis
- key-term and idea extraction
- content strategy
- outlining
- drafting
- rewriting
- summarization
- explanation
- language-level adaptation
- tone adaptation
- grammar/style revision
- fact/claim review
- captions, hooks, CTAs, alt text, scripts, and other text deliverables
- writing QC

Canonical architecture:

`00_workflow/workflows/writing_workflow.md`

### Design Workflow

Used for:

- visual strategy
- visual research
- reference analysis
- named-style study
- motif extraction
- reference-style synthesis
- Visual DNA
- platform/template synthesis
- art direction
- generation
- editable reconstruction
- Figma implementation
- visual QC

Canonical architecture:

`00_workflow/workflows/design_workflow.md`

### Shared Knowledge Layer

Both workflows may consult shared:

- project briefs
- audience research
- cultural/context research
- brand memory
- approved terminology
- external references
- platform constraints
- tools and technical methods
- factual source material
- provenance records

Canonical architecture:

`00_workflow/workflows/shared_knowledge_layer.md`

Core governance rule:

```text
SHARE EVIDENCE.
SHARE KNOWLEDGE.
SHARE TOOLS.
DO NOT SHARE AUTHORITY SILENTLY.
```

## Combined Production Pattern

When one deliverable requires both writing and design:

```text
CONTENT NEED
→ WRITING WORKFLOW
→ APPROVED WRITING HANDOFF
→ DESIGN WORKFLOW
→ APPROVED VISUAL OUTPUT
→ COMBINED PACKAGE QC
→ HUMAN FINAL APPROVAL
```

Writing owns meaning, claims, language, and textual structure.
Design owns visual communication of approved content.

If visual constraints require a meaningful rewrite, the request returns to Writing instead of being silently rewritten inside Design.

## Existing Design Production Pipeline

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

This remains the active Design branch and should not be expanded with unrelated writing responsibilities.

## Control Layer

The orchestration rules live in `00_workflow/`:

- `workflow.md` — execution pipeline and revision routing
- `workflows/design_workflow.md` — Design branch architecture
- `workflows/writing_workflow.md` — Writing branch architecture
- `workflows/shared_knowledge_layer.md` — cross-workflow knowledge and handoff rules
- `task_contract.md` — universal executable-task standard
- `task_contracts.json` — canonical task-level dependencies, gates, approvals, and revision policy
- `stage_registry.md` — stage responsibilities and active tasks
- `handoff_contract.md` — controlled transfer between stages
- `decision_gates.md` — canonical gate vocabulary and approval rules
- `information_model.md` — SOURCE / DERIVED / DECISION / OUTPUT states
- `task_registry.json` — machine-readable stage/task index
- `process_registry.json` — canonical design production process, including goals, conditions, artifacts, gates, protocols, and memory effects

## Canonical Gate Vocabulary

All active prompts and task contracts use only:

`PASS` · `CONDITIONAL` · `BLOCKED` · `APPROVE` · `REVISE` · `REJECT` · `READY` · `REGENERATE`

Natural-language explanations may accompany a gate, but the final status must use the canonical value.

## Active Design Prompt Sequence

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
- QC-003 — QC Knowledge Synthesis

The Writing Workflow will have its own task sequence and contracts as it is developed. It should reuse the same governance concepts without being forced into visual-stage IDs.

## Runtime

The optional `runtime/` package turns a prompt file into an auditable model execution. It is not required for structural consistency validation.

### Human-triggered Heavy QC

Heavy QC is an optional local PyIQA ensemble for aesthetic, no-reference technical, and full-reference evidence. It runs only after an authorized human explicitly asks for `heavy QC`; its output always remains `AWAITING_HUMAN_DECISION`.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-heavy-qc.txt
.\.venv\Scripts\python.exe runtime\heavy_qc.py <candidate-image> --approval HEAVY_QC_APPROVED
```

Add `--reference <approved-source-image>` for SSIM, LPIPS, and PSNR comparisons. Runtime evidence is stored under ignored `runs/`; pretrained weights remain in the local user cache and must not be committed. Review the upstream PyIQA and model licenses before commercial use.

## Testing

### Structural CI

`tests/validate_library.py` currently validates the established Design workflow, including:

- active prompt IDs and stage prefixes
- exact match between active prompts and task contracts
- task-level dependencies and next-task references
- canonical gate vocabulary
- lifecycle status
- deprecated/retired references
- domain-specific leakage
- required task-contract metadata
- canonical production-process order, task coverage, protocol paths, stage dependencies, gates, artifacts, and memory effects

Writing-workflow structural validation should be added separately rather than overloading Design validation rules.

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

These rules apply independently inside both Writing and Design.

## Revision Control

Maximum automatic revision cycles: **3**. After the third unsuccessful cycle, route to **HUMAN_REVIEW** rather than continuing automatically.

Cross-workflow revisions must route to the responsible domain:

- meaning/language/fact problem → Writing
- visual hierarchy/composition/style problem → Design
- shared source problem → shared research/evidence layer, then re-run affected workflows

## Production Release Rule

A production release requires:

1. Structural CI PASS for the relevant workflow.
2. No duplicate or invalid IDs.
3. Exact task-contract alignment for the relevant workflow.
4. No unresolved critical workflow dependency.
5. Production-eligible prompt version/status.
6. Relevant semantic tests PASS with the selected model/runtime.
7. Required human approvals recorded.
8. Release artifact records prompt versions, model/runtime, and test results.
9. When both workflows are used, the Writing Handoff and Design output remain mutually traceable.

## Status

Production Candidate — dual-workflow architecture established; Writing task library still to be built.

## Version

3.2-dual-workflow-architecture

## Core Principle

**Research → Structure → Create → Evaluate → Revise — with domain ownership preserved.**
