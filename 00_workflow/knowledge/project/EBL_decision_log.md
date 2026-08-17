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

### Source fingerprint history

The originally registered source binary was:

```text
filename: Codex Image Aug 15, 2026, 02_47_23 PM.png
sha256: 4cb1c9796cf358338ef6d0c49486cd2e04292775b838c603ffdf658aede283f7
dimensions: 1536 × 1024
mode: RGBA
status: SUPERSEDED_SOURCE_BINARY
```

On 2026-08-16 the human explicitly supplied and identified a new file as **the fixed English Beyond Language logo**. The current canonical source binary is therefore:

```text
filename: Codex Image Aug 15, 2026, 02_47_23 PM(2).png
sha256: 20facdbc7917edada59fc0beafba2b963ba6eb3a4effcf033eb956f9355d6d02
dimensions: 1536 × 1024
mode: RGBA
format: PNG
bytes: 1409989
status: CURRENT_CANONICAL_SOURCE_BINARY
```

This supersedes only the prior source-binary fingerprint. It does **not** change the approved Geometric Reader Integrated Logo design decision. The repository binary path remains unresolved until the actual binary is ingested and verified there.

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

## EBL-DEC-011 — Series Rename: A World from the World

**Date:** 2026-08-17  
**Decision:** Rename the recurring series formerly called **A Line for Today** to **A World from the World**. The new name is the active public series identifier.  
**Rationale:** The series is intended to open a larger cultural, linguistic, or interpretive world from a small fragment rather than operate as a generic daily quote format.  
**Scope:** Series naming, Story/Feed headers, content workflow, launch calendar, future references.  
**Status:** APPROVED.  
**Supersedes:** `A Line for Today` as the active series name.  
**Provenance:** Explicit human instruction on 2026-08-17.  
**Affected:** `EBL_a_world_from_the_world_system.md`, superseded `EBL_a_line_for_today_template.md`, `EBL_memory_registry.json`, launch calendar and future content briefs.

---

## EBL-DEC-012 — A World from the World Becomes a Full Content System

**Date:** 2026-08-17  
**Decision:** The renamed series is not only a visual quote template. Its workflow is structured as source selection → source/attribution verification → copyright/rights context → interpretation/teaching layer → writing lock → Story/Feed design → QC → human final review.  
**Rationale:** The EBL value comes from transforming a cultural/language fragment into context, interpretation and independent participation; presentation alone is insufficient.  
**Scope:** All `A World from the World` production.  
**Status:** APPROVED CURRENT WORKFLOW.  
**Supersedes:** The narrower visual-only operational use of the former `A Line for Today` template.  
**Affected:** `EBL_a_world_from_the_world_system.md`, `EBL_copyright_rules.md`, content handoffs and QC.

---

## EBL-DEC-013 — First Launch Calendar

**Date:** 2026-08-17  
**Decision:** Use the approved launch schedule beginning **Saturday, 22 August 2026**, with `A World from the World` as the recurring morning Story and `Vocabulary` as the recurring evening Story through the recorded first-two-weeks launch period. Feed posts progress through English Independence → Tell → Explain → Argue → Participate → Keyvan introductory video.  
**Rationale:** This established the first version of the daily Story rhythm around a paced feed narrative.  
**Scope:** Launch operations, 22 Aug–1 Sep 2026.  
**Status:** SUPERSEDED IN PART by `EBL-DEC-014`.  
**Affected:** `EBL_launch_calendar_weeks_01_02.md`, daily content planning and series retrieval.

---

## EBL-DEC-014 — Remove Vocabulary Story from Current Launch Calendar

**Date:** 2026-08-17  
**Decision:** Remove the recurring evening `Vocabulary` Story from the current first-two-weeks launch calendar. Keep the feed-post schedule and daily morning `A World from the World` Story unchanged.  
**Rationale:** The human revised the launch plan and does not want a Vocabulary evening Story scheduled for now.  
**Scope:** Launch operations, 22 Aug–1 Sep 2026.  
**Status:** APPROVED CURRENT CALENDAR.  
**Supersedes:** The evening-Story portion of `EBL-DEC-013`.  
**Provenance:** Explicit human revision on 2026-08-17.  
**Affected:** `EBL_launch_calendar_weeks_01_02.md`, daily content planning.

---

## EBL-DEC-015 — `Ed.post` Becomes the Canonical EBL Feed-Post Template

**Date:** 2026-08-17  
**Decision:** The human-approved six-slide Post 01 visual system is designated as the canonical EBL feed-post template named **`Ed.post`**.  
**Rationale:** The template was refined through direct human typography, hierarchy, placement and semantic-emphasis decisions and should now be reused as a stable visual system rather than reconstructed from generic EBL style memory.  
**Scope:** EBL Instagram feed carousels using the `Ed.post` system.  
**Status:** LOCKED APPROVED TEMPLATE.  
**Supersedes:** Earlier unresolved Post-template reconstructions and alternate Post 01 grids as template authority.  
**Provenance:** Explicit human instruction after final six-slide confirmation on 2026-08-17.  
**Affected:** `EBL_template_Ed_post.md`, `EBL_post_01_approved_artifact.md`, `EBL_memory_registry.json`, `EBL_asset_registry.json`, `EBL_visual_examples.md`, `EBL_retrieval_map.md`, `QC-EBL-TYPE-001_semantic_typography_edit_qc.md`.

---

## EBL-DEC-016 — Post 01 English Independence Is the Canonical `Ed.post` Calibration Artifact

**Date:** 2026-08-17  
**Decision:** The six human-confirmed slides of **Post 01 — English Independence** are the approved fixed first post and primary canonical visual calibration artifact for `Ed.post`.  
**Rationale:** Earlier saved/generated versions conflicted with later human edits. The exact approved source binaries now have verified fingerprints, preventing future confusion between alternate generations and the final set.  
**Scope:** Post 01, `Ed.post` calibration, revisions, QC and future template reuse.  
**Status:** LOCKED APPROVED ARTIFACT.  
**Supersedes:** Earlier Post 01 grid alternatives, generated reconstructions and unverified remembered versions.  
**Provenance:** Human supplied the final six slides in the active conversation on 2026-08-17; SHA-256 and dimensions verified in the production runtime.  
**Affected:** `EBL_post_01_approved_artifact.md`, `EBL_asset_registry.json`, `EBL_visual_examples.md`, `EBL_memory_registry.json`, `EBL_retrieval_map.md`.

### Canonical artifact rule

```text
ACTUAL APPROVED POST 01 SLIDE BINARY
> VERIFIED ARTIFACT RECORD
> Ed.post TEMPLATE DESCRIPTION
> GENERAL EBL STYLE MEMORY
> MODEL INFERENCE
```

Repository image paths remain unresolved until the binaries are actually ingested. Do not invent paths.

---

## EBL-DEC-017 — `Ed.post` Scoped Typography Editing Becomes Reusable QC Knowledge

**Date:** 2026-08-17  
**Decision:** Human revision patterns learned from Post 01 are promoted into reusable EBL QC for `Ed.post`: preserve approved artwork, modify only the authorized text zone, use semantic color rather than decorative color, use micro-size/weight adjustments, allow controlled looseness for list-like text, and make CTA hierarchy explicit.  
**Rationale:** These corrections recur across slides and represent a stable art-direction method rather than isolated one-off changes.  
**Scope:** `Ed.post` typography refinement and related EBL scoped visual revisions.  
**Status:** APPROVED REUSABLE EBL PROJECT QC.  
**Provenance:** Human-approved edits to Post 01 Slides 3, 5 and 6 on 2026-08-17.  
**Affected:** `QC-EBL-TYPE-001_semantic_typography_edit_qc.md`, `EBL_template_Ed_post.md`, `EBL_retrieval_map.md`, `EBL_visual_examples.md`.

### Learned examples

- Slide 3: six examples use controlled alternating/scattered left-right rhythm instead of a rigid list.
- Slide 5: `the English you have.` receives rust/red semantic emphasis.
- Slide 6: `The goal is not` stays black on one line; `perfect` is rust/red while `English.` stays black; supporting copy receives the approved size hierarchy; final CTA is bold rust/red.

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
