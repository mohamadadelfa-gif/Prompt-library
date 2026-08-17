# Controlled Creative Production Workflow

## Purpose

This repository is a controlled creative-production system, not a loose collection of prompts.

The lifecycle separates reusable foundation-building from content-instance production and makes reuse, conditional skipping, blocking, revision, and human approval explicit.

## Canonical Authority

`00_workflow/process_registry.json` is the single canonical machine-readable source of truth for stage identity, order, dependencies, conditions, tasks, protocols, outputs, gates, and memory effects.

- `task_registry.json` mirrors stage identity and task placement.
- `task_contracts.json` remains authoritative for executable task dependencies and gates.
- `stage_registry.md` is the human-readable stage map.
- This file explains execution behavior.

No secondary representation may redefine the lifecycle independently.

## Core Information Rule

Information states remain:

- `SOURCE`
- `DERIVED`
- `DECISION`
- `OUTPUT`

No stage may silently rewrite approved upstream facts, requirements, decisions, source identity, or scope.

## Stage-Satisfaction Rule

Before executing any stage, resolve its routing state:

```text
CURRENT APPROVED ARTIFACT SATISFIES THIS STAGE?
        |
       YES
        ↓
SATISFIED_BY_REUSE
        |
       NO
        ↓
IS THE STAGE APPLICABLE?
   |             |
  NO            YES
   ↓             ↓
SKIPPED       REQUIRED INPUTS AVAILABLE?
NOT_APPLICABLE    |             |
                 NO            YES
                  ↓             ↓
               BLOCKED       EXECUTE
                                ↓
                         PASS / REVISION GATE
                                ↓
                         COMPLETE or REVISE
```

Allowed routing states:

`EXECUTE`, `SATISFIED_BY_REUSE`, `SKIPPED_NOT_APPLICABLE`, `BLOCKED`, `REVISE`, `COMPLETE`.

Reuse is valid only when the artifact is current, approved, non-superseded, correctly scoped, traceable, and satisfies the required gate.

## Lifecycle Zones

### Zone A — Foundation / System Creation (01–08)

Build or validate the reusable project/design foundation.

### Zone B — Content Production / Finalization (09–20)

Use that foundation for a content instance, finalization, human approval, publishing outputs, and controlled learning.

## Canonical Stage Markers

<!-- ARCHITECTURE_STAGE: 01|strategy -->
<!-- ARCHITECTURE_STAGE: 02|research -->
<!-- ARCHITECTURE_STAGE: 03|visual_analysis -->
<!-- ARCHITECTURE_STAGE: 04|named_style_study -->
<!-- ARCHITECTURE_STAGE: 05|motif_sign_extraction -->
<!-- ARCHITECTURE_STAGE: 06|reference_style_synthesis -->
<!-- ARCHITECTURE_STAGE: 07|visual_dna -->
<!-- ARCHITECTURE_STAGE: 08|platform_template_synthesis -->
<!-- ARCHITECTURE_STAGE: 09|approved_content_handoff -->
<!-- ARCHITECTURE_STAGE: 10|art_direction -->
<!-- ARCHITECTURE_STAGE: 11|generation -->
<!-- ARCHITECTURE_STAGE: 12|human_directed_revision -->
<!-- ARCHITECTURE_STAGE: 13|pre_final_quality_control -->
<!-- ARCHITECTURE_STAGE: 14|final_ai_creative_refinement -->
<!-- ARCHITECTURE_STAGE: 15|editable_reconstruction_preparation -->
<!-- ARCHITECTURE_STAGE: 16|editable_implementation -->
<!-- ARCHITECTURE_STAGE: 17|final_production_quality_control -->
<!-- ARCHITECTURE_STAGE: 18|human_final_approval -->
<!-- ARCHITECTURE_STAGE: 19|master_platform_derivatives -->
<!-- ARCHITECTURE_STAGE: 20|learning_memory_promotion -->

## Production Lifecycle

```text
01 Strategy
↓
02 Research
↓
03 Visual Analysis
↓
04 Named Style Study [conditional]
↓
05 Motif & Sign Extraction [conditional]
↓
06 Reference Style Synthesis
↓
07 Visual DNA
↓
08 Platform / Template System [conditional]
══════════════════════════════════
APPROVED CREATIVE FOUNDATION
══════════════════════════════════
↓
09 Approved Content / Writing Handoff
↓
10 Content Function + Art Direction
↓
11 Generation / Build Candidate
↓
12 Human-Directed Revision [conditional]
↓
13 Pre-Final Quality Control
↓
14 Final AI Creative Refinement [conditional]
↓
15 Editable Reconstruction Preparation [conditional]
↓
16 Editable Implementation [conditional]
↓
17 Final Production Quality Control
↓
18 Human Final Approval
↓
19 Master + Platform Derivatives
↓
20 Learning / Memory Promotion [conditional]
```

## Stage Responsibilities

### 01–08 Foundation / System Creation

Strategy, research, visual analysis, named-style study, motif extraction, reference synthesis, Visual DNA, and platform/template synthesis create an `APPROVED_CREATIVE_FOUNDATION`.

For established projects, these stages should usually be satisfied by validated reuse rather than recomputed.

### 09 Approved Content / Writing Handoff

Resolve the approved copy/content and its provenance before visualizing it. This is the input-side content handoff, not the final publishing package.

### 10 Content Function + Art Direction

Determine message function, hierarchy, concept, and content-specific visual decisions while preserving the approved foundation.

### 11 Generation / Build Candidate

Create the generation specification/prompt and output candidate. A generated output remains `OUTPUT`, not an approved rule or final master.

### 12 Human-Directed Revision

The human defines what changes; references inform how; execution changes only authorized areas. Preserve the original and record the delta.

Human revision does not automatically create reusable style memory.

### 13 Pre-Final Quality Control

Run `QC-001`, then `QC-002` when correction is required. Use applicable project/asset QC modules and route failures to the earliest responsible stage.

A critical failure overrides numerical scores.

### 14 Final AI Creative Refinement

Run the controlled closed loop using:

- `creative_ai_final_edit.md`;
- `final_ai_creative_synthesis_heavy_qc.md`;
- `final_ai_closed_loop_production.md`.

Preservation is a valid final-edit decision. `FINAL-AI-001` and `FINAL-AI-002` are protocol identities in architecture 4.0 and are not executable task contracts yet.

AI may produce `PASS_FOR_HUMAN_FINAL_REVIEW`, not `FINAL_PUBLISHING_MASTER`.

### 15 Editable Reconstruction Preparation

Conditional production reconstruction for flattened/raster approved visuals when an editable master is required. Preserve the approved source lock and classify reconstructed content as derived where appropriate.

### 16 Editable Implementation

Conditional structured production-master implementation, such as Figma. Implementation must not redesign or reinterpret approved creative decisions.

### 17 Final Production Quality Control

Re-check the actual production representation after Final AI and any reconstruction/implementation. Do not inherit a prior pass across a material production transformation.

### 18 Human Final Approval

Final creative authority remains human. Only explicit approval authorizes the publishing master.

### 19 Master + Platform Derivatives

Preserve the archival/project master separately from platform derivatives and final publishing package. Create derivatives once from the approved master.

### 20 Learning / Memory Promotion

Run `QC-003` and the controlled learning protocols only after finalization when learning/structuralization is requested or required.

Separate one-off corrections, content decisions, reusable project rules, and system-level learnings. Promotion always requires traceability and the appropriate human authority.

## Conditionality and Reuse

A lifecycle dependency may be resolved by `COMPLETE`, `SATISFIED_BY_REUSE`, or `SKIPPED_NOT_APPLICABLE` where the dependency itself is conditional.

`BLOCKED` stops downstream execution.

`REVISE` routes to the earliest responsible stage and invalidates downstream approvals only to the extent affected by the change.

## Stepwise Review Checkpoints

The main checkpoints are:

1. Foundation approval.
2. Approved content handoff.
3. Art direction.
4. Generation output.
5. Human revision when used.
6. Pre-final QC.
7. Final AI refinement when used.
8. Editable reconstruction/implementation when used.
9. Final production QC.
10. Human final approval.
11. Final content package/master derivatives.
12. Learning promotion when used.

Use `stepwise_creative_review.md` for checkpoint behavior.

## Specialized Production Protocols

Platform-specific systems remain subordinate to this lifecycle. Examples include:

- Instagram/template synthesis;
- presentation Design DNA and layout guard;
- HTML visual production;
- DESIGN.md/token-system generation;
- editable reconstruction and live editable text;
- Figma structure/output contract;
- project-specific memory and QC systems such as EBL.

These protocols may add checks inside a stage but may not silently create a conflicting global stage map.

## Content Handoff vs Final Content Package

The lifecycle intentionally separates:

```text
APPROVED CONTENT / WRITING HANDOFF  (Stage 09)
!=
FINAL CONTENT PACKAGE               (Stage 19)
```

The first authorizes what Design may visualize. The second assembles the human-approved publishing result, metadata, accessibility/publishing material, and master/derivative relationships.

## Human Revision vs Learning

The lifecycle intentionally separates:

```text
HUMAN-DIRECTED REVISION  (Stage 12)
!=
LEARNING / PROMOTION     (Stage 20)
```

A correction is evidence. It becomes reusable knowledge only after classification, scope, provenance, and required approval.

## Finalization Order

```text
GENERATION / REVISION
→ PRE-FINAL QC
→ FINAL AI CLOSED LOOP (when applicable)
→ EDITABLE RECONSTRUCTION (when applicable)
→ EDITABLE IMPLEMENTATION (when applicable)
→ FINAL PRODUCTION QC
→ HUMAN FINAL APPROVAL
→ MASTER + PLATFORM DERIVATIVES
→ LEARNING / MEMORY PROMOTION
```

This prevents a later production transformation from invalidating an earlier final pass and prevents Final AI from making the editable master stale after it was locked.

## Failure Routing

Route to the earliest responsible stage:

- requirement/source definition → Strategy;
- evidence → Research;
- visual observation/style interpretation → Visual Analysis / Style Study / Motif / Reference Synthesis;
- reusable visual rule → Visual DNA;
- platform/template structure → Platform / Template System;
- content/copy handoff → Approved Content Handoff;
- creative decision → Art Direction;
- specification/prompt/model output → Generation;
- authorized local human change → Human Revision;
- candidate quality/root cause → Pre-Final QC;
- late-stage refinement → Final AI;
- source-lock/reconstruction → Editable Reconstruction;
- implementation mismatch → Editable Implementation;
- production representation quality → Final Production QC;
- human acceptance → Human Final Approval;
- publishing package/derivative → Master + Platform Derivatives;
- reusable learning scope/provenance → Learning / Memory Promotion.

Do not regenerate unaffected work.

## Approval Rule

A stage is complete only when:

- its routing state is recorded;
- its gate is satisfied or its conditional skip/reuse is valid;
- required provenance is present;
- the handoff is complete;
- no unresolved blocking conflict remains.

A high numerical score never overrides a critical failure.

AI approval does not override human final authority.

## Version

`4.0-production-candidate`

## Status

Active architecture.
