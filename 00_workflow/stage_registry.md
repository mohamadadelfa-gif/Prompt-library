# Stage Registry

## Authority

`00_workflow/process_registry.json` is the canonical machine-readable lifecycle source of truth.

This file is a human-readable view of that registry. `task_registry.json` mirrors stage identity/task placement, while `task_contracts.json` remains authoritative for executable task behavior.

## Stage-Satisfaction States

Before re-running a stage, resolve it to exactly one controlled routing state:

- `EXECUTE` — applicable and required inputs are available.
- `SATISFIED_BY_REUSE` — a current approved, non-superseded artifact already satisfies the stage for the required scope.
- `SKIPPED_NOT_APPLICABLE` — the stage is conditional and does not apply.
- `BLOCKED` — required evidence, approval, or provenance is missing/conflicting.
- `REVISE` — an upstream or current-stage correction is required.
- `COMPLETE` — execution/reuse/skip resolution is recorded and the stage handoff is valid.

A stage must never be re-executed merely because it appears earlier in the lifecycle when an approved reusable artifact already satisfies it.

## Lifecycle Zones

### Zone A — Foundation / System Creation

Stages 01–08 build or validate the reusable creative foundation.

### Zone B — Content Production / Finalization

Stages 09–20 use an approved foundation to produce, refine, approve, package, and learn from a content instance.

## Canonical Stage Map

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

| ID | Stage | Active Tasks | Primary Output |
|---|---|---|---|
| 01 | Strategy | STR-001–STR-005 | Approved Strategy Package |
| 02 | Research | RES-001–RES-006 | Research Synthesis |
| 03 | Visual Analysis | VIS-001–VIS-006 | Visual Evidence Package |
| 04 | Named Style Study | STYLE-001 | Approved Style Study Package |
| 05 | Motif & Sign Extraction | Protocol stage | Controlled Motif Library |
| 06 | Reference Style Synthesis | Protocol stage | Approved Reference Style Synthesis |
| 07 | Visual DNA | VDNA-001 | Visual DNA Package |
| 08 | Platform / Template System | Protocol stage | Approved Creative Foundation |
| 09 | Approved Content / Writing Handoff | Protocol/gate stage | Approved Content Handoff |
| 10 | Content Function + Art Direction | ART-001–ART-003 | Approved Art Direction |
| 11 | Generation / Build Candidate | GEN-001–GEN-002 | Generated Candidate |
| 12 | Human-Directed Revision | Protocol stage | Revision Record / Revised Candidate |
| 13 | Pre-Final Quality Control | QC-001–QC-002 | Pre-Final QC Evidence / Revision Route |
| 14 | Final AI Creative Refinement | FINAL-AI protocols | Creative Final Candidate / Heavy QC Evidence |
| 15 | Editable Reconstruction Preparation | Protocol stage | Editable Reconstruction Package |
| 16 | Editable Implementation | Protocol stage | Structured Editable Master |
| 17 | Final Production Quality Control | Protocol/gate stage | PASS_FOR_HUMAN_FINAL_REVIEW |
| 18 | Human Final Approval | Human gate | Final Publishing Master Authorization |
| 19 | Master + Platform Derivatives | Production protocols | Final Master / Derivatives / Content Package |
| 20 | Learning / Memory Promotion | QC-003 + learning protocols | QC Knowledge / Promotion Decision |

## Key Boundaries

### Foundation reuse

For an existing approved system, Stages 01–08 may resolve to `SATISFIED_BY_REUSE` after scope, provenance, current approval state, and supersession status are checked. Reuse is a validated lifecycle action, not skipped work.

### Approved content handoff vs final package

Stage 09 resolves the content/writing input that Design is allowed to visualize. Stage 19 assembles the final human-approved publishing result. These are intentionally separate.

### Human revision vs learning

Stage 12 captures authorized human-directed revision and preserves everything outside the authorized change area. It does not automatically promote a correction into reusable knowledge. Promotion belongs to Stage 20.

### Pre-Final QC

Stage 13 owns the existing executable QC tasks:

- `QC-001` — evaluate the generated/revised candidate.
- `QC-002` — diagnose failure and define the smallest controlled revision.

A passing pre-final gate clears the candidate for final creative refinement; it does not grant final publishing approval.

### Final AI Creative Refinement

Stage 14 governs the closed loop defined by:

- `creative_ai_final_edit.md` (`FINAL-AI-001` protocol identity);
- `final_ai_creative_synthesis_heavy_qc.md` (`FINAL-AI-002` protocol identity);
- `final_ai_closed_loop_production.md`.

`FINAL-AI-001` and `FINAL-AI-002` remain controlled protocols in architecture version 4.0; they are not added to `task_contracts.json` in this repair.

The allowed AI result is a candidate or `PASS_FOR_HUMAN_FINAL_REVIEW`, never self-issued final approval.

### Reconstruction vs local repair

Stage 15 is production-level editable reconstruction of an approved flattened/raster source. It is distinct from a local `P3 SOURCE-BASED RECONSTRUCTION` repair inside Stage 14.

### Editable implementation

Stage 16 is conditional. If an editable production master is not required, it may resolve to `SKIPPED_NOT_APPLICABLE`.

### Final production QC

Stage 17 validates the final production representation after Final AI and any reconstruction/implementation. A production transformation cannot inherit a prior QC pass automatically.

### Human final authority

Stage 18 is the only lifecycle stage that may authorize the `FINAL_PUBLISHING_MASTER`. AI gates can recommend or clear for review, but cannot replace explicit human approval.

### Master and derivative separation

Stage 19 preserves `ARCHIVAL / PROJECT MASTER != PLATFORM DERIVATIVE`. Platform derivatives are created once from the approved master and never replace it as provenance evidence.

### Learning / memory promotion

Stage 20 contains `QC-003` because QC knowledge synthesis is a learning/memory activity, not ordinary output evaluation. Promotion must distinguish one-off correction, content-specific decision, reusable project rule, and cross-project/system rule.

## EBL Routing Example

For an existing approved `Ed.post` system, a new post should normally route:

```text
01–08 SATISFIED_BY_REUSE
→ 09 APPROVED CONTENT HANDOFF
→ 10 ART DIRECTION
→ 11 GENERATION
→ 12 HUMAN REVISION (if needed)
→ 13 PRE-FINAL QC
→ 14 FINAL AI CLOSED LOOP (if applicable)
→ 15–16 EDITABLE PRODUCTION (if required)
→ 17 FINAL PRODUCTION QC
→ 18 HUMAN FINAL APPROVAL
→ 19 MASTER + DERIVATIVES
→ 20 LEARNING / MEMORY PROMOTION (when requested/required)
```

Project-specific memory and QC protocols remain authoritative inside the applicable stages.

## Revision Routing Principle

Route a failure to the earliest responsible stage. Do not regenerate by default. A local failure should receive a local correction plus downstream/global re-check where affected.

## Version

`4.0-production-candidate`

## Status

Active architecture — derived from `process_registry.json`.
