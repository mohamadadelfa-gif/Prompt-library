# QC-EBL-EDPOST-001 — `Ed.post` Template Design System QC

## Purpose

Quality-control gate for all English Beyond Language `Ed.post` carousel work.

This QC checks whether a new or revised `Ed.post` output:

- belongs to the approved template family;
- preserves the canonical design-system logic;
- uses typography semantically;
- maintains controlled asymmetry;
- respects slide function;
- preserves locked components;
- changes only authorized areas during revision;
- remains readable and coherent as an Instagram carousel.

This module supplements, not replaces:

- `QC-EBL-MEM-001_memory_compliance_qc.md`
- `QC-EBL-TYPE-001_semantic_typography_edit_qc.md`
- `QC-EBL-001_project_master_qc.md`
- `QC-LOGO-001_logo_application_qc.md`

---

# Required Retrieval — Mandatory

Before running this QC retrieve:

1. `EBL_memory_registry.json`
2. `EBL_Ed_post_design_system.md`
3. `EBL_template_Ed_post.md`
4. `EBL_post_01_approved_artifact.md`
5. `EBL_visual_examples.md`
6. `EBL_decision_log.md`
7. `EBL_failure_memory.md`
8. current approved source slide/set when revising
9. current Writing/Design handoff when meaningful copy is involved
10. exact canonical slide references when available

If canonical references required for the task are not available, record:

`CANONICAL_REFERENCE_UNRESOLVED`

Do not pretend a prose description is equivalent to the image.

---

# Gate 0 — Memory / Authority Lock — Mandatory

Verify:

- current human instruction is understood;
- newest approved `Ed.post` system is loaded;
- Post 01 canonical artifact is not confused with an earlier alternate set;
- superseded visual versions are not used as source-of-truth;
- no model-memory reconstruction overrides an approved image.

Pass state:

`PASS_AUTHORITY_LOCK`

Any unresolved conflict => `BLOCKED_CONFLICT`.

---

# Gate 1 — Template Family Fidelity — Mandatory

The output must visibly belong to `Ed.post`.

Check:

- warm cream / ivory paper ground;
- tactile painterly texture;
- ochre / mustard, rust, navy, muted olive/green, black family;
- editorial rather than corporate or dashboard-like composition;
- asymmetry and meaningful negative space;
- hand-drawn line/sign language;
- painterly shapes with imperfect edges;
- no generic language-school visual clichés;
- no random icon-grid or infographic drift.

Fail if technically clean but visually outside the family.

---

# Gate 2 — Slide Function Integrity — Mandatory

For each slide, identify its narrative function.

Expected six-slide architecture by default:

```text
01 QUESTION / COVER
02 BLOCKAGE / PROBLEM
03 OBSTACLES / EXAMPLES
04 PERSPECTIVE SHIFT
05 AGENCY / DEFINITION
06 EXPANSION / CTA
```

For each slide ask:

- does the layout support this function?
- is the reading order appropriate to the function?
- does the dominant form reinforce the meaning?
- has the slide become visually repetitive with adjacent slides?
- has the slide drifted into a different function accidentally?

A different slide count or function map requires explicit human approval.

---

# Gate 3 — Typography Hierarchy — Mandatory

Map all text to T1–T5:

```text
T1 PRIMARY CONCEPT
T2 SEMANTIC CONTRAST
T3 SUPPORTING EXPLANATION
T4 EXAMPLES / EVIDENCE
T5 CTA / CLOSING ACTION
```

Check:

- T1 is clearly dominant;
- T2 emphasis follows meaning;
- T3 does not compete with title;
- T4 remains readable even when loosely arranged;
- T5 has enough ending emphasis;
- line breaks preserve phrase meaning;
- no accidental hierarchy inversions.

Then run `QC-EBL-TYPE-001`.

---

# Gate 4 — Semantic Color Use — Mandatory

For every accent-colored word/phrase ask:

**Why is this colored?**

Acceptable answers:

- conceptual contrast;
- semantic friction;
- key definition;
- CTA / action;
- intentional field contrast required for reading.

Reject:

- random decoration;
- coloring whole sentences when only one phrase is meant to carry emphasis;
- inconsistent use of rust/red across similar semantic roles;
- color that reduces readability.

Post 01 calibration examples:

- `things that matter`
- `still gets in the way`
- `the English you have.`
- `perfect`
- `Become independent in English.`

These examples teach the rule; they are not mandatory phrases for future posts.

---

# Gate 5 — Controlled Looseness — Mandatory for Multi-Item Slides

When a slide contains several supporting statements, verify:

- reading order remains obvious;
- staggered placement feels intentional;
- spacing is unequal but balanced;
- left/right alternation or scatter has rhythm;
- text does not collide with painterly forms;
- composition does not become a rigid table;
- composition does not become random chaos.

For Slide-3-like structures, prefer **controlled scatter** over a generic two-column list when content and space allow.

Pass condition:

`ALIVE + READABLE + ORDERED`

---

# Gate 6 — Repeated Components — Mandatory

Check slide number:

- correct `XX / 06` format;
- top-left anchor logic;
- consistent scale relationship;
- consistent slash spacing and weight.

Check EBL production signature:

- bottom-left role preserved;
- visually secondary;
- no regeneration of a merely similar logo;
- clear space preserved;
- not distorted or retyped.

Any logo change also runs `QC-LOGO-001`.

---

# Gate 7 — Painterly Geometry & Linework — Mandatory

For every major painted field / line / sign ask:

```text
WHAT JOB DOES THIS ELEMENT DO?
```

Valid jobs include:

- frame a concept;
- create contrast;
- move the eye;
- connect sections;
- anchor a corner;
- balance visual weight;
- symbolize a path / tension / opening / growth.

Reject:

- added shapes with no function;
- generic decoration;
- over-clean vector geometry that breaks the material language;
- too many marks competing with typography;
- painterly fields that obscure copy.

---

# Gate 8 — Revision Scope Lock — Mandatory for Edits

Before editing record:

```text
AUTHORIZED_CHANGE_AREA
LOCKED_ELEMENTS
```

After editing compare against the approved source.

Fail if an unrequested change occurs in:

- background;
- painterly shapes;
- logo;
- numbering;
- unrelated typography;
- linework;
- dot/grid motifs;
- composition;
- color outside the authorized text/element.

Rule:

> **A successful local edit with collateral redesign is still a failure.**

---

# Gate 9 — Content-to-Form Fit — Mandatory

For every slide complete:

```text
MESSAGE
→ FUNCTION
→ PRIMARY FOCAL POINT
→ TYPOGRAPHY ROLE
→ COLOR EMPHASIS
→ PAINTERLY FIELD ROLE
→ READING PATH
```

The design must emerge from meaning rather than from mechanical template filling.

Fail if:

- the content has been forced into an old composition that no longer fits;
- every slide copies the same layout;
- visual choices are attractive but semantically arbitrary.

---

# Gate 10 — Carousel Coherence — Mandatory

Inspect the six slides as one sequence.

Check:

- visual family consistency;
- enough variation slide-to-slide;
- narrative progression;
- recurring palette logic;
- recurring logo/numbering discipline;
- balanced distribution of heavy painterly masses;
- no two adjacent slides feel accidentally identical;
- final slide feels like a conclusion.

Pass condition:

`COHERENT FAMILY + MEANINGFUL VARIATION`

---

# Gate 11 — Instagram Readability — Mandatory

Check at realistic feed/mobile viewing scale:

- title readable immediately;
- body copy not too small;
- key accents visible without zoom;
- adequate contrast;
- no important content too close to edge;
- CTA legible;
- texture does not interfere with glyph clarity.

Then run relevant Instagram visual QC.

---

# Gate 12 — Canonical Comparison — Mandatory for Revisions / Template Calibration

Compare candidate against canonical references.

Inspect:

- typography density;
- paper tone;
- brush texture;
- shape-edge character;
- line weight;
- logo scale/anchor;
- numbering;
- asymmetry;
- semantic color behavior;
- negative space.

Do **not** require pixel-identical copying for a new post.

Require **system fidelity**, unless the task is an exact repair/reproduction.

---

# Scoring

Score each non-blocked category 0–2:

- 0 = fail
- 1 = acceptable but weak / needs refinement
- 2 = strong pass

Categories:

1. Template family fidelity
2. Slide function integrity
3. Typography hierarchy
4. Semantic color
5. Controlled looseness / spacing
6. Repeated component fidelity
7. Meaning-to-form fit
8. Carousel coherence
9. Instagram readability
10. Revision isolation, when applicable

Maximum: 20.

## Result States

### `PASS_EDPOST`
- no mandatory gate fails;
- score >= 17/20;
- no unresolved asset/memory conflict.

### `PASS_WITH_MINOR_REFINEMENT`
- no mandatory gate fails;
- score 14–16;
- only local, non-conceptual refinements remain.

### `FAIL_EDPOST`
Any of:
- mandatory gate fails;
- score <= 13;
- unrequested redesign;
- logo substitute;
- semantic typography failure;
- generic infographic drift;
- canonical source conflict.

### `BLOCKED`
Use when:
- canonical source needed but unresolved;
- approved text/handoff missing;
- memory conflict cannot be resolved.

---

# QC Output Schema

```text
QC_ID: QC-EBL-EDPOST-001
ASSET / POST:
TEMPLATE: Ed.post
SOURCE ARTIFACT:
MEMORY FILES RETRIEVED:
DECISION IDS APPLIED:
AUTHORIZED CHANGE AREA:
LOCKED ELEMENTS:

GATE 0 — AUTHORITY LOCK: PASS / FAIL / BLOCKED
GATE 1 — TEMPLATE FAMILY: 0 / 1 / 2
GATE 2 — SLIDE FUNCTION: 0 / 1 / 2
GATE 3 — TYPOGRAPHY: 0 / 1 / 2
GATE 4 — SEMANTIC COLOR: 0 / 1 / 2
GATE 5 — CONTROLLED LOOSENESS: 0 / 1 / 2 / N-A
GATE 6 — REPEATED COMPONENTS: 0 / 1 / 2
GATE 7 — PAINTERLY FORM / LINE: 0 / 1 / 2
GATE 8 — REVISION SCOPE: 0 / 1 / 2 / N-A
GATE 9 — CONTENT-TO-FORM: 0 / 1 / 2
GATE 10 — CAROUSEL COHERENCE: 0 / 1 / 2
GATE 11 — INSTAGRAM READABILITY: 0 / 1 / 2
GATE 12 — CANONICAL COMPARISON: PASS / FAIL / N-A

TOTAL SCORE:
KNOWN FAILURES CHECKED:
UNRESOLVED RISKS:
RESULT:
SMALLEST SAFE CORRECTION:
HUMAN REVIEW REQUIRED: YES
```

---

# Core QC Principle

> **`Ed.post` passes when it feels unmistakably like the same design system, communicates the new meaning clearly, and introduces no unauthorized change.**
