# English Beyond Language — Decision Log

## Purpose

Record durable human-approved EBL decisions with their rationale, scope, status, and supersession relationship.

A decision log remembers **what was decided and why**. It is not a chronological transcript.

## Decision Record Schema

```text
DECISION_ID
DATE
TITLE
DECISION
RATIONALE
SCOPE
STATUS
SUPERSEDES
SOURCE / PROVENANCE
AFFECTED MEMORY / QC
```

---

## EBL-DEC-001 — Public Brand Name

**Date:** 2026-08-15  
**Decision:** Use **English Beyond Language** as the default public-facing name. Do not use `EBL` as the default shorthand unless explicitly requested.  
**Rationale:** The full name communicates the project idea; acronym-first branding weakens clarity and can drift from the approved identity.  
**Scope:** Project-wide public visual communication.  
**Status:** APPROVED.  
**Supersedes:** Earlier exploratory public acronym use.  
**Provenance:** Explicit human preference during EBL visual-system development.  
**Affected:** `EBL_project_memory.md`, `EBL_approved_project_rules.md`, `QC-EBL-001`.

---

## EBL-DEC-002 — Chosen Primary Logo

**Date:** 2026-08-15  
**Decision:** The **Geometric Reader Integrated Logo** is the chosen primary EBL logo.  
**Rationale:** It integrates the reader, book, architectural geometry, painterly material language, and full English Beyond Language name into one recognizable identity asset.  
**Scope:** Project identity.  
**Status:** LOCKED APPROVED IDENTITY.  
**Supersedes:** Earlier overlapping-circle logo direction and exploratory substitutes.  
**Provenance:** Explicit human selection of the supplied logo image.  
**Affected:** `EBL_asset_registry.json`, `EBL_logo_application_rules.md`, `QC-LOGO-001`, `QC-EBL-001`.

### Verified source fingerprint

The chosen source binary was verified in the active production runtime on 2026-08-16:

```text
filename: Codex Image Aug 15, 2026, 02_47_23 PM.png
sha256: 4cb1c9796cf358338ef6d0c49486cd2e04292775b838c603ffdf658aede283f7
dimensions: 1536 × 1024
mode: RGBA
```

The repository binary path is still unresolved. This is intentional and explicit: the verified fingerprint identifies the chosen source binary, but no repository path may be invented until the binary is actually ingested and verified there.

---

## EBL-DEC-003 — Visual Direction

**Date:** 2026-08-15  
**Decision:** Use a contemporary editorial/cultural visual system with restrained painterly character, warm paper grounds, rust/ochre/navy/green/charcoal palette, asymmetry, negative space, hand-drawn signs, and meaningful geometric/organic fields.  
**Rationale:** The brand should feel intelligent, curious, human and culturally aware rather than like a generic language school or infographic account.  
**Scope:** Project visual grammar.  
**Status:** APPROVED.  
**Supersedes:** Generic infographic/default education aesthetics.  
**Affected:** Visual DNA, Story, carousel, `QC-EBL-001`.

---

## EBL-DEC-004 — Semantic Typography

**Date:** 2026-08-15  
**Decision:** Typography should follow meaning and content function. Editorial serif generally supports conceptual/reflective/thesis language; clean sans generally supports direct/practical/operational language.  
**Rationale:** Font, alignment, hierarchy, line break and emphasis should communicate the role of the content rather than act as decoration.  
**Scope:** Project typography system.  
**Status:** APPROVED RULE.  
**Affected:** `QC-TYPE-001`, `QC-EBL-001`, final-AI stages.

---

## EBL-DEC-005 — Native Typography Reconstruction

**Date:** 2026-08-15  
**Decision:** When raster typography becomes faded, haloed, ghosted, weak or partially erased, do not repeatedly recolor/darken it. Reconstruct the local background and redraw the exact approved copy once at native resolution with full-opacity type.  
**Rationale:** Dark RGB values can still look optically faded because repeated raster manipulation damages edge/stroke density.  
**Scope:** EBL production and repair.  
**Status:** APPROVED RULE.  
**Affected:** `QC-TYPE-001`, `typography_native_reconstruction.md`, `EBL_failure_memory.md`.

---

## EBL-DEC-006 — Human Revision Isolation

**Date:** 2026-08-15  
**Decision:** Human decides **what** changes; reference informs **how**; AI changes only the authorized area and preserves unrelated approved design.  
**Rationale:** Unrequested redesign is treated as a failure, even if visually attractive.  
**Scope:** All EBL revisions.  
**Status:** APPROVED RULE.  
**Affected:** `human_feedback_style_learning.md`, `QC-EBL-001`, `EBL_failure_memory.md`.

---

## EBL-DEC-007 — Final AI Closed Loop

**Date:** 2026-08-16  
**Decision:** Final AI work uses a preserve/intervene classification and closed loop: source lock → whole-work read → function map → Creative Final Edit → Heavy QC → smallest-safe correction → global recheck → human approval.  
**Rationale:** Final quality requires maximum coherence with minimum necessary change. A correct final-stage decision may be `P0 PRESERVE`.  
**Scope:** Finalization workflow.  
**Status:** APPROVED project process + cross-project system learning where separately promoted.  
**Affected:** `final_ai_closed_loop_production.md`, `final_ai_production_learnings.md`, `QC-EBL-001`.

---

## EBL-DEC-008 — Master and Platform Derivative Are Separate

**Date:** 2026-08-16  
**Decision:** Preserve the archival/project master at native production resolution and create the platform derivative only after master approval.  
**Rationale:** Repeated resizing during revision degrades type, texture and edge quality.  
**Scope:** Final output.  
**Status:** APPROVED RULE.  
**Affected:** final-AI workflow, `QC-EBL-001`.

---

## EBL-DEC-009 — Story Template Status

**Date:** 2026-08-16  
**Decision:** EBL Story production uses 1080×1920 / 9:16 and inherits EBL identity through negative space, edge-weighted painterly fields, restrained signs, interaction space and secondary branding. The current generated Story composition remains a **REVIEW_CANDIDATE**, not a locked reusable master.  
**Rationale:** A Story should not be a feed post stretched vertically, and one generated candidate must not silently become a permanent project template.  
**Scope:** Instagram Story.  
**Status:** PLATFORM RULE APPROVED; exact candidate composition PENDING HUMAN APPROVAL.  
**Affected:** `EBL_story_template_rules.md`, `EBL_asset_registry.json`, `QC-EBL-001`.

---

## EBL-DEC-010 — Disciplined Operational Memory

**Date:** 2026-08-16  
**Decision:** EBL memory must operate as a structured system, not as one prose document. The project uses separate memory registry, asset registry, decision log, failure memory, visual-example index, task retrieval map, memory-compliance QC and project master QC.  
**Rationale:** Memory becomes reliable only when it is retrievable, scoped, versioned/superseded, testable, and able to reject known failures.  
**Scope:** EBL project knowledge/workflow architecture.  
**Status:** APPROVED RULE.  
**Affected:** `EBL_memory_registry.json`, `EBL_asset_registry.json`, `EBL_failure_memory.md`, `EBL_visual_examples.md`, `EBL_retrieval_map.md`, `QC-EBL-MEM-001`, `QC-EBL-001`, `EBL_visual_production_workflow.md`.

### Operational rule

```text
MEMORY EXISTS
→ MEMORY RETRIEVED
→ MEMORY APPLIED
→ MEMORY COMPLIANCE TESTED
→ CREATIVE / TECHNICAL QC
→ HUMAN APPROVAL
→ LEARNING UPDATE
```

A prose-only memory update is incomplete when future retrieval/QC cannot consume it.

---

## Discipline Rule

When a decision changes:

```text
ADD NEW DECISION
→ MARK OLD DECISION SUPERSEDED
→ NAME WHAT IT SUPERSEDES
→ UPDATE MEMORY REGISTRY / QC / ASSET STATE
```

Do not silently rewrite history in a way that makes old and new rules indistinguishable.
