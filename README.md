# Prompt Library v3 — Controlled Dual-Workflow Production System

A version-controlled production system in which Writing and Design operate as separate workflows with explicit inputs, outputs, provenance, handoffs, approvals, quality gates, and revision routing.

## Architecture

```text
                     SHARED KNOWLEDGE
                    /                \
           WRITING WORKFLOW      DESIGN WORKFLOW
                    \                /
                 EXPLICIT VERSIONED HANDOFF
                           ↓
                 COMBINED CONTENT PACKAGE
                           ↓
                    HUMAN FINAL APPROVAL
```

Core governance:

```text
SHARE EVIDENCE.
SHARE KNOWLEDGE.
SHARE TOOLS.
DO NOT SHARE AUTHORITY SILENTLY.
```

Writing owns meaning, claims, language, textual structure, captions, CTAs, and source-grounded content decisions.

Design owns visual communication, visual systems, art direction, generation, layout, typography implementation, production implementation, and visual QC.

## Writing Workflow

Canonical architecture:

- `00_workflow/workflows/writing_workflow.md`
- `00_workflow/writing_task_registry.json`
- `00_workflow/writing_task_contracts.json`
- `00_workflow/writing_process_registry.json`
- `tests/validate_writing.py`
- `tests/writing_evaluation_rubric.md`

Canonical stages:

```text
01 WST    Writing Strategy
02 WRES   Textual Research
03 WAN    Source Analysis
04 WSYN   Content Synthesis
05 WSTR   Content Structure
06 WDR    Drafting
07 WLANG  Language Adaptation
08 WQC    Writing Quality Control
09 WAPP   Human Content Approval
10 WHOFF  Design Handoff
```

The Writing architecture is active and validated. Its prompt library is intentionally still empty; new Writing prompts must be registered in the Writing task registry and contracts before CI will accept them.

## Design Workflow

Canonical architecture:

- `00_workflow/workflows/design_workflow.md`
- `00_workflow/task_registry.json`
- `00_workflow/task_contracts.json`
- `00_workflow/process_registry.json`
- `tests/validate_library.py`
- `tests/validate_process.py`

The established Design production pipeline remains active:

```text
Strategy
→ Research
→ Visual Analysis
→ Conditional Style / Motif Study
→ Reference Style Synthesis
→ Visual DNA
→ Platform / Template Synthesis
→ Art Direction
→ Generation
→ Content Package Assembly
→ Human Revision / Style Learning
→ Conditional Editable Reconstruction
→ Figma / Production Implementation
→ Visual QC / Final Approval
```

Design must not silently re-author approved Writing content.

## Cross-Workflow Handoff

Canonical contract:

`00_workflow/workflows/cross_workflow_handoff_contract.md`

### Writing → Design

Transfers the exact approved Writing version, content purpose, audience, language level, locked/flexible wording, semantic hierarchy, caption/CTA state, source/fact status, and unresolved unknowns.

### Design → Writing

Transfers visual/platform constraints that require a new Writing decision, such as text-area limits, reading-order constraints, density problems, maximum recommended length, or semantic emphasis needs.

A rewrite creates a **new Writing version**. Design never overwrites the earlier approved version.

## Shared Knowledge Layer

Canonical architecture:

`00_workflow/workflows/shared_knowledge_layer.md`

Both workflows may share:

- project briefs;
- audience/cultural research;
- brand memory;
- approved project rules;
- terminology;
- factual sources;
- external references;
- platform constraints;
- typography/readability knowledge;
- tools and technical methods;
- provenance records.

Shared knowledge should identify workflow usefulness and authority scope where helpful. Evidence may cross workflows; approval does not.

## Content Package

Canonical contract:

`00_workflow/content_package_contract.md`

The Content Package is an assembly and final-QC layer, not a second authoring workflow.

Writing owns authored text. Design owns visual implementation. The combined package links exact approved versions and creates final publishing/accessibility metadata from both.

## Information Model

Every important item remains identifiable as:

- `SOURCE` — supplied or observed evidence;
- `DERIVED` — analysis/inference based on source;
- `DECISION` — explicit approved project/creative choice;
- `OUTPUT` — execution result.

Forbidden silent transitions include:

- DERIVED → SOURCE;
- ASSUMPTION → FACT;
- OUTPUT → REQUIREMENT;
- SOURCE → DECISION without an explicit decision step.

These rules apply independently inside Writing and Design.

## Canonical Gate Vocabulary

`PASS` · `CONDITIONAL` · `BLOCKED` · `APPROVE` · `REVISE` · `REJECT` · `READY` · `REGENERATE`

Maximum automatic revision cycles: **3**. After the third unsuccessful cycle, route to `HUMAN_REVIEW`.

## Testing and CI

The real `Prompt Library Validation` workflow runs on pushes and pull requests to `main` and `production-candidate-v1`.

It validates:

- Design prompt structure and contracts;
- Design process integrity;
- Writing workflow architecture and future Writing prompts;
- controlled knowledge registry consumers across both workflows;
- QC knowledge controls;
- Python compilation;
- required semantic-test rubrics and fixtures.

The old placeholder Hello World CI workflow has been removed so a green repository check represents meaningful validation.

Semantic model execution remains a separate release gate. Structural CI verifies the system, not whether a selected model produces a high-quality semantic result.

## Writing Quality Standard

Writing QC covers at minimum:

- source quality;
- factual accuracy;
- claim-evidence relationship;
- unknown handling;
- purpose/relevance;
- audience fit;
- language-level fit;
- meaning preservation;
- clarity/structure;
- tone/voice;
- grammar/style;
- project-specific rules;
- downstream handoff quality.

Critical failures override numerical averages.

## English Beyond Language

EBL now routes content tasks through Writing rules and visual tasks through Design rules. The retrieval map explicitly includes the approved content/communication rules for Writing and for Design whenever meaningful text is present.

Current EBL content constraints include non-elitist positioning, realistic learner motivation, purposeful/non-random content, and approximately B1 public-facing language by default while preserving intellectual substance.

Regression fixtures:

`tests/fixtures/english_beyond_language/writing_regression_cases.md`

## Versioning

Top-level architecture version:

**3.3-controlled-dual-workflow**

Design and Writing subworkflow registries maintain their own internal workflow/process versions. These subworkflow versions are intentionally independent from the top-level architecture version.

## Status

**Controlled dual-workflow architecture active.**

- Design workflow: established production branch.
- Writing workflow: machine-controlled architecture ready for prompt development.
- Shared knowledge: active with explicit authority boundaries.
- Cross-workflow handoff: explicit and versioned.
- CI: validates both workflow control layers on `main`.

## Core Principle

**Research → Structure → Create → Evaluate → Revise — with evidence shared and authority preserved.**
