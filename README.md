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

The knowledge layer also includes a validated relationship graph connecting registered sources and rules to authorized tasks, protocols, artifacts, decisions, outputs, and QC evidence without collapsing their information states.

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
- QC-003 — QC Knowledge Synthesis

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

### Presentation Design DNA

Presentation, PPT/PPTX, and HTML-deck work can use the conditional protocol in `00_workflow/presentation_design_dna_protocol.md`. It extends approved Visual DNA into a scenario-specific Design Contract, Blueprint, per-slide Page Specs, optional reusable Design Profiles, and mechanical layout safety checks without bypassing the existing production pipeline.

Reference images remain style evidence unless explicitly approved as slide content. HTML decks require the presentation layout QC module and a passing source-level layout-guard report when Node is available.

The presentation protocol and layout guard include Apache-2.0-licensed adaptations from PPT-Design-DNA; see `THIRD_PARTY_NOTICES.md`.

### Instagram HTML Carousel Export

The optional controlled exporter in `scripts/export_instagram_carousel.py` renders approved HTML slides to exact square, portrait or story PNG dimensions. It never installs dependencies automatically, supports side-effect-free preflight, creates non-destructive run directories, verifies dimensions, hashes sources and outputs, and leaves every export awaiting mandatory Instagram, image, typography, logo and audience QC as applicable.

External design-system precedents are governed by `00_workflow/design_system_reference_protocol.md` and its curated registry. References must be verified at use time and can support derived principles, but they never become target tokens or brand assets automatically.

Approved design decisions can be operationalized through the Learn–Structure–Refine token system. It separates Global primitives, Alias semantics, and Component states; validates theme parity and references; and requires versioned human approval before release.

### HTML Visual Production

The conditional protocol in `00_workflow/html_visual_production_protocol.md` converts an approved Producer Handoff, Visual DNA package or standalone approved brief into an original browser-rendered artifact. It provides medium routing, optional brand integration, real-context priority, originality controls and anti-slop QC for pages, interfaces, dashboards, prototypes, posters and cards.

### DESIGN.md Generation

`00_workflow/design_md_generation_protocol.md` converts inspected website or interface evidence into an agent-readable design system. It records exact source observations separately from transferable principles and approved target tokens, documents responsive behavior and component states, and uses `assets/templates/DESIGN_MD_TEMPLATE.md` as the canonical handoff format.

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

The optional LLM-evaluator protocol adds versioned rubrics, calibration status, evidence-citing judgments, judge disagreement, failure classification and graph-compatible QC evidence. Structural CI validates the contract without making paid provider calls.

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
