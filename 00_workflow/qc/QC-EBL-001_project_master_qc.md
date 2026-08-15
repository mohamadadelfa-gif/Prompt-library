# QC-EBL-001 — English Beyond Language Project Master QC

## Purpose

Provide one project-specific QC gate for English Beyond Language visual production.

This QC does not replace asset-specific modules. It orchestrates them and adds EBL-specific brand, semantic, memory, and learning checks.

Use for:

- Instagram feed posts;
- carousels;
- Stories;
- promotional graphics;
- profile/identity applications;
- final AI creative synthesis;
- master/publishing export.

## Governing Principle

```text
EBL QUALITY =
MEMORY COMPLIANCE
+ CONTENT FIDELITY
+ BRAND MEMORY
+ SEMANTIC TYPOGRAPHY
+ VISUAL IDENTITY
+ LOGO FIDELITY
+ ARTIFACT INTEGRITY
+ PLATFORM READABILITY
+ HUMAN APPROVAL
```

A high aesthetic score cannot compensate for a mandatory memory, brand, asset, or content failure.

---

# Gate 0 — Memory Compliance — mandatory

Run first:

`00_workflow/qc/QC-EBL-MEM-001_memory_compliance_qc.md`

Required result before continuing:

`PASS_MEMORY_COMPLIANCE`

or an explicitly documented non-blocking unknown.

Blocking states include:

- `BLOCKED_MEMORY_EVIDENCE_MISSING`;
- `BLOCKED_CONFLICT`;
- `CANONICAL_ASSET_UNRESOLVED` when the task requires exact canonical asset placement;
- `FAIL`.

If memory compliance fails, do not continue to aesthetic scoring as if the task were valid.

---

# Required Retrieval — mandatory

Before QC, retrieve:

1. `00_workflow/knowledge/project/EBL_memory_registry.json`;
2. `00_workflow/knowledge/project/EBL_project_memory.md`;
3. `00_workflow/knowledge/project/EBL_approved_project_rules.md`;
4. `00_workflow/knowledge/project/EBL_decision_log.md`;
5. `00_workflow/knowledge/project/EBL_failure_memory.md`;
6. `00_workflow/knowledge/project/EBL_retrieval_map.md`;
7. content-specific approved decision record, if one exists;
8. `00_workflow/knowledge/project/EBL_asset_registry.json` when assets/branding are involved;
9. `00_workflow/knowledge/project/EBL_logo_application_rules.md` when branding is present;
10. current approved artifact / clean master / textless master;
11. applicable asset-specific QC modules.

For visual calibration also retrieve:

`00_workflow/knowledge/project/EBL_visual_examples.md`

For final-stage work additionally retrieve:

- `00_workflow/final_ai_closed_loop_production.md`;
- `00_workflow/knowledge/system/final_ai_production_learnings.md`.

If required project memory was not retrieved, QC state = `BLOCKED_CONTEXT_MISSING`.

---

# Gate 1 — Content / Meaning Fidelity — mandatory

Verify:

- exact approved wording;
- no unauthorized claims;
- no omitted required point;
- correct CTA meaning;
- correct semantic role of the asset;
- correct sequence for multi-slide content;
- no silent simplification into generic language-school messaging.

For EBL, communication should support English as independent participation rather than grammar/vocabulary-only framing unless the specific content says otherwise.

Any unauthorized meaning change => `FAIL`.

---

# Gate 2 — Public Brand Name — mandatory

Default public-facing name:

**English Beyond Language**

Reject unauthorized public `EBL` acronym use unless:

- it is already embedded inside an explicitly approved asset/variant; or
- the human explicitly requests acronym use.

Do not invent alternative names.

---

# Gate 3 — Chosen Logo Fidelity — mandatory when logo is present

Chosen logo asset ID:

`EBL-ASSET-LOGO-001 — Geometric Reader Integrated Logo`

Run `QC-LOGO-001` plus these project checks.

Verify:

- approved master or approved production variant used;
- exact asset state resolved through `EBL_asset_registry.json`;
- no regeneration of a merely similar mark;
- figure/book/arch/semicircle/structural-line geometry preserved;
- integrated brand-name typography preserved;
- logo visually secondary unless the asset is specifically about identity;
- optical clear-space passes;
- replacement/cleanup area has no artifacts;
- repeated-set placement follows the approved anchor/scale logic.

Reject:

- newly generated substitute logo;
- changed logo typography;
- changed colors/geometry;
- invented canonical asset metadata;
- extra decorative supports around logo;
- collision with text/artwork;
- visible cleanup residue.

## Master vs production signature check

Do not confuse:

- `EBL-ASSET-LOGO-001` — primary supplied master identity;
- `EBL-ASSET-LOGO-001-APP-SMALL` — approved application pattern, not a replacement master.

A production signature does not supersede the primary master.

New variants require explicit review before reuse.

---

# Gate 4 — Visual Identity — mandatory

Check against EBL project memory.

Expected family characteristics:

- warm ivory/paper ground;
- rust/burnt orange;
- ochre/mustard;
- deep navy / muted green / olive;
- charcoal/black;
- editorial/cultural tone;
- painterly/material texture;
- asymmetry;
- negative space;
- meaningful signs/lines/forms;
- restraint.

Reject generic default drift into:

- stock corporate graphics;
- generic language-school visuals;
- flag/classroom clichés;
- dashboard/infographic composition;
- random icons/shapes;
- neon/gradient-heavy style;
- literal Paul Klee copying.

---

# Gate 5 — Meaning-to-Form / Creative Synthesis — mandatory

For each asset or slide, identify:

```text
MESSAGE
→ FUNCTION
→ PRIMARY FOCAL POINT
→ READING ORDER
→ TYPOGRAPHY ROLE
→ ALIGNMENT / SPACE
→ LINE / SHAPE / COLOR JOB
```

Ask:

- does the formal treatment support what the content is doing?
- is the focal point obvious?
- does any decoration compete with meaning?
- is the visual solution authored rather than mechanically templated?
- is there enough variation without losing family resemblance?

A final-stage decision of `P0 PRESERVE` is valid when the form already performs correctly.

---

# Gate 6 — Typography Integrity — mandatory when text is present

Run `QC-TYPE-001`.

Additionally verify EBL semantic typography:

- serif used when conceptual/editorial/reflection benefits from it;
- sans used when direct/practical/operational language benefits from it;
- role-specific variation remains coherent;
- emphasis follows meaning rather than decoration.

Reject:

- faded or washed black;
- gray halos;
- ghost edges;
- weak optical stroke density;
- arbitrary font switching;
- decorative emphasis on the wrong words;
- poor line breaks;
- poor mobile readability;
- inconsistent repeated numbering/system typography.

## Damaged raster type rule

If text is damaged:

```text
DO NOT KEEP DARKENING THE EXISTING RASTER
```

Use:

```text
CLEANEST APPROVED SOURCE
→ BACKGROUND RECONSTRUCTION
→ EXACT COPY REDRAWN ONCE AT NATIVE RESOLUTION
→ FULL-OPACITY TYPE
→ NO POST-RENDER RESIZE
```

---

# Gate 7 — Painterly / Material Integrity

Check:

- texture feels intentional;
- painterly edge variation is controlled;
- line character has a communicative role;
- geometric and organic forms are balanced;
- texture does not weaken typography;
- no visible rectangular patching from repair;
- no generic AI texture contamination.

Intentional imperfection is allowed.
Accidental repair evidence is not.

---

# Gate 8 — Artifact / Repair Integrity — mandatory

Inspect at 100% native scale.

Reject:

- gray blobs;
- ghost marks;
- clone seams;
- halos;
- accidental dots/lines;
- color mismatch;
- broken paper texture;
- hard rectangular repair patches;
- inpainting smear;
- compression/blur introduced during revision;
- AI anatomy/object artifacts if people/objects are present;
- hidden remnants of old branding.

Use the clean-source hierarchy before local repair:

```text
LIVE SOURCE
→ CLEAN APPROVED MASTER
→ TEXTLESS MASTER
→ SAME-ARTWORK CLEAN REGION
→ TARGETED LOCAL REPAIR
→ GENERATIVE RECONSTRUCTION LAST
```

---

# Gate 9 — Known Failure Memory — mandatory for revisions/finalization

Retrieve `EBL_failure_memory.md` and record relevant failure IDs checked.

Ask explicitly:

```text
DOES THIS OUTPUT REPRODUCE ANY ACTIVE EBL FAILURE PATTERN?
```

A reproduced known failure => `FAIL` even if other aesthetic checks pass.

---

# Gate 10 — Multi-Asset / Carousel System — mandatory for sets

Check:

- sequence makes semantic progress;
- neighboring slides differ meaningfully;
- shared grammar exists without identical layouts;
- logo behavior is coherent;
- numbering system is coherent;
- typography grammar is coherent;
- palette relationships are coherent;
- pacing and density vary according to meaning;
- entry/development/shift/payoff structure works where relevant.

Mechanical sameness is not the goal.
Semantic consistency is.

---

# Gate 11 — Instagram Story QC — mandatory for Stories

Canvas target:

`1080 × 1920 px` (`9:16`)

Check:

- essential content remains inside practical UI-safe zones;
- headline remains readable at phone size;
- Story is not merely a stretched feed post;
- central content/sticker area is usable;
- poll/question/link sticker space is not blocked by essential branding;
- logo remains secondary and clear;
- painterly elements weight the edges without crowding the content;
- negative space is sufficient;
- no fake Instagram UI is baked into reusable clean templates unless explicitly requested.

## Story-template status rule

Current Story asset record:

`EBL-ASSET-STORY-TPL-001 = REVIEW_CANDIDATE`

A newly generated Story template remains:

`PROJECT_REFERENCE / REVIEW_CANDIDATE`

until the human explicitly approves it as the reusable Story master.

Do not silently promote exact candidate coordinates/composition to a project rule.

---

# Gate 12 — Profile / Portrait QC — when applicable

Run `QC-IG-PROFILE-001`.

Priority:

```text
RECOGNITION > DECORATION
NATURALNESS > STYLIZATION
FACE > BRANDING
SMALL-SIZE CLARITY > DETAIL
```

Do not apply the full feed-post design language to the avatar unless a branded avatar is explicitly requested.

---

# Gate 13 — Platform / Export Integrity — mandatory for final output

Distinguish:

```text
PROJECT / ARCHIVAL MASTER
≠
PLATFORM DERIVATIVE
```

Check:

- master stays at approved native production resolution;
- platform derivative is created only after master approval;
- master is not repeatedly resized during revision;
- export is sharp;
- correct aspect ratio;
- edge/crop safety;
- no new compression or color drift.

---

# Gate 14 — Final AI Closed Loop — mandatory for finalization

For FINAL-AI stages classify every asset:

```text
P0 PRESERVE
P1 CLEANUP
P2 MICRO-REFINE
P3 SOURCE-BASED RECONSTRUCTION
P4 CONCEPTUAL CHANGE — HUMAN AUTHORIZATION REQUIRED
```

On failure:

```text
LOCAL FAILURE
→ ROOT-CAUSE DIAGNOSIS
→ SMALLEST SAFE CORRECTION
→ RERUN FAILED GATE
→ RERUN WHOLE-SET COHERENCE
```

Do not redesign unaffected assets merely because one asset failed.

---

# Gate 15 — QC Evidence Package — mandatory for final review

A verbal `PASS` is insufficient.

Produce evidence appropriate to the asset:

- memory-compliance trace;
- full-set contact sheet;
- native-resolution critical-area crop(s);
- realistic Instagram-size preview;
- logo close-up(s) if branding was touched;
- typography close-up(s) if type was touched;
- repair-region close-up(s) if cleanup was performed;
- before/after for meaningful final refinements;
- Heavy QC report;
- unresolved-risk list.

Memory trace must include:

```text
MEMORY_FILES_RETRIEVED
DECISION_IDS_APPLIED
ASSET_IDS_APPLIED
FAILURE_IDS_CHECKED
EXAMPLE_IDS_USED
UNRESOLVED_UNKNOWNS
CONFLICTS
MEMORY_COMPLIANCE_RESULT
```

---

# Gate 16 — Human Final Approval — mandatory

AI may return:

`PASS_FOR_HUMAN_FINAL_REVIEW`

AI may **not** independently promote an EBL visual to:

`FINAL_PUBLISHING_MASTER`

Final creative acceptance remains human.

---

# EBL Master QC Result States

```text
BLOCKED_CONTEXT_MISSING
BLOCKED_MEMORY_EVIDENCE_MISSING
BLOCKED_CONFLICT
CANONICAL_ASSET_UNRESOLVED
FAIL
REVISION_REQUIRED
PASS_FOR_HUMAN_REVIEW
PASS_FOR_HUMAN_FINAL_REVIEW
FINAL_PUBLISHING_MASTER — human approval required
```

---

# Compact EBL QC Checklist

Before presenting a final EBL visual, verify:

```text
[ ] memory compliance QC passed
[ ] project memory registry retrieved
[ ] task-specific retrieval map followed
[ ] current human instruction obeyed
[ ] newest non-superseded decisions used
[ ] copy/meaning exact
[ ] correct public name
[ ] chosen logo asset/variant exact and resolved
[ ] no canonical metadata invented
[ ] logo optical clearance safe
[ ] EBL visual grammar intact
[ ] no infographic/generic-school drift
[ ] typography semantically appropriate
[ ] typography optically solid
[ ] active failure memory checked
[ ] no repair artifacts
[ ] painterly texture intentional
[ ] sequence/system coherent if multi-asset
[ ] Story safe/useful if Story
[ ] candidate/approved states not confused
[ ] native-size inspection complete
[ ] realistic platform-size inspection complete
[ ] master and derivative separated
[ ] QC evidence produced
[ ] unresolved risks disclosed
[ ] human final approval pending/recorded correctly
```

---

## Relationship to Other QC Modules

This protocol orchestrates rather than replaces:

- `QC-EBL-MEM-001_memory_compliance_qc.md`
- `QC-IG-001_instagram_visual_qc.md`
- `QC-AUD-001_audience_catcher_qc.md`
- `QC-SOC-001_social_visual_audience_gate.md`
- `QC-IG-PROFILE-001_instagram_profile_picture_qc.md`
- `QC-LOGO-001_logo_application_qc.md`
- `QC-TYPE-001_typography_integrity_qc.md`

Use the relevant specialized module, then evaluate the result through this EBL project gate.

Updated: 2026-08-16
