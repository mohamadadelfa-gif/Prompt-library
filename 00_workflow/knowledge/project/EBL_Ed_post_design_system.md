# English Beyond Language — `Ed.post` Template Design System

## Status

- **System ID:** `EBL-DS-EDPOST-001`
- **Template:** `Ed.post`
- **Reference artifact:** `EBL-POST-001 — Post 01: English Independence`
- **Medium:** Instagram feed carousel
- **Default slide count:** 6
- **Status:** APPROVED / CANONICAL DESIGN SYSTEM
- **Human approval basis:** finalized six-slide Post 01 set, 2026-08-17

## Source-of-Truth Hierarchy

```text
CURRENT HUMAN INSTRUCTION
> APPROVED CANONICAL SLIDE IMAGE
> EBL-POST-001 ARTIFACT RECORD
> THIS DESIGN SYSTEM
> Ed.post TEMPLATE DESCRIPTION
> MODEL MEMORY / INFERENCE
```

Never reconstruct `Ed.post` from memory alone when the approved visual source can be retrieved.

---

# 1. System Purpose

`Ed.post` is a reusable editorial carousel system for English Beyond Language.

It is designed to turn a structured idea into a six-slide visual essay that feels:

- editorial rather than infographic-like;
- intellectually clear but visually alive;
- painterly without becoming decorative noise;
- structured underneath, alive on the surface;
- consistent as a family while allowing slide-specific variation.

Core rule:

> **Preserve the visual system; let meaning determine hierarchy, emphasis, rhythm, and slide function.**

---

# 2. Design Tokens

## 2.1 Color Roles

Use roles, not random swatches.

### Ground
- warm ivory / cream paper texture
- low-contrast, tactile, editorial

### Primary ink
- black / charcoal
- used for main readable text, rules, linework and structural marks

### Semantic accent
- rust / burnt orange
- used for conceptual contrast, key phrase emphasis, directional emphasis and CTA
- must not be applied decoratively without semantic purpose

### Structural field 1
- ochre / mustard
- used for large painterly concept fields, thought containers and warm emphasis

### Structural field 2
- deep navy / desaturated blue
- used for strong contrast fields, conceptual containers, anchors and visual counterweight

### Secondary field
- muted olive / neutral green-gray
- used sparingly for lower-weight balancing fields or symbolic grounding

## 2.2 Texture

- warm paper grain is part of the visual identity;
- painted shapes keep visibly imperfect / brush-based edges;
- avoid glossy vector-clean surfaces unless explicitly requested;
- texture must support material character, not reduce text legibility.

## 2.3 Line Language

Allowed line behavior:

- hand-drawn continuous lines;
- loose curves;
- thin structural rules;
- short underlines;
- occasional grid fragments;
- dots / dot clusters;
- spirals / arches / simple sign-like forms.

Linework should create movement, linkage, tension or structure. Avoid meaningless decoration.

---

# 3. Typography System

## 3.1 Semantic Roles

### Editorial serif
Best suited to:
- conceptual title;
- thesis/question;
- reflective contrast;
- concluding statement;
- culturally weighted text.

### Clean sans-serif
Best suited to:
- direct explanation;
- practical statements;
- examples;
- operational or learner-facing language.

Typography is selected by content role, not by fixed font-per-slide rules.

## 3.2 Hierarchy Levels

### T1 — Primary concept
Dominant title/question.

### T2 — Semantic contrast
Key phrase with selective rust/red, weight shift, line break or field contrast.

### T3 — Supporting explanation
Secondary text that clarifies the concept.

### T4 — Examples / evidence / list
Readable, flexible and rhythmically arranged; may use controlled scatter.

### T5 — CTA / closing action
Strong final signal; may use rust/red + bold treatment.

## 3.3 Semantic Emphasis Rules

Use emphasis only where meaning requires it.

Examples learned from Post 01:

- `things that matter` → rust semantic emphasis;
- `still gets in the way` → rust conceptual friction;
- `the English you have.` → rust key-definition emphasis;
- `perfect` → rust contrast while `English.` remains black;
- `Become independent in English.` → rust + bold CTA.

## 3.4 Size Adjustment Rule

Prefer micro-adjustments:

- slightly bigger;
- slightly smaller;
- selective bold;
- word-level color;
- line-break refinement;
- spacing refinement.

Avoid dramatic scale changes unless the human explicitly requests a new hierarchy.

## 3.5 Line Break Rule

Line breaks are semantic and compositional.

A correct line break should:

- preserve natural reading;
- create a deliberate phrase unit;
- support visual balance;
- avoid orphaned words unless intentional;
- keep approved phrases together when specified.

Example:

```text
The goal is not
perfect English.
```

with `perfect` rust/red and `English.` black.

---

# 4. Composition System

## 4.1 Global Layout Principle

Each slide should feel related but not mechanically duplicated.

Shared family traits:

- asymmetry;
- strong negative space;
- painterly masses near edges or corners;
- text blocks positioned for clear reading order;
- small recurring logo signature bottom-left;
- numbering top-left;
- visual movement through lines, fields and signs.

## 4.2 Fixed Repeated Components

### Slide number
Format:

`01 / 06` → `06 / 06`

Preserve:
- top-left anchor logic;
- slash spacing;
- scale relationship;
- visual weight.

### EBL production signature
- approved small Geometric Reader application;
- bottom-left;
- secondary to content;
- never regenerated from memory when exact asset is available.

## 4.3 Painterly Geometry

Painterly forms must:

- act as content containers, anchors or counterweights;
- preserve rough material edges;
- avoid looking like generic infographic boxes;
- keep enough breathing room around text.

---

# 5. Slide Function Architecture

A standard `Ed.post` six-slide narrative uses functions rather than identical layouts.

## Slide 1 — QUESTION / COVER

Purpose:
- introduce central idea;
- create the strongest hook;
- establish visual world.

Design behavior:
- dominant title;
- large painterly field;
- one supporting statement;
- selective semantic highlight;
- strong counter-shape / architectural form;
- restrained decorative marks.

## Slide 2 — BLOCKAGE / PROBLEM

Purpose:
- show the gap, friction or failure state.

Design behavior:
- direct practical language;
- clear contrast phrase;
- bold problem statement;
- sparse, expressive marks;
- strong negative space.

## Slide 3 — OBSTACLES / EXAMPLES

Purpose:
- expand the problem into multiple real situations.

Design behavior:
- title with semantic accent;
- 4–6 support statements;
- controlled scatter / staggered left-right rhythm allowed;
- no rigid table appearance;
- reading order must remain obvious.

## Slide 4 — PERSPECTIVE SHIFT

Purpose:
- contrast an old question with a better one.

Design behavior:
- two conceptual fields;
- clear `not this → but this` logic;
- contrasting painterly colors;
- strong negative space between the two ideas.

## Slide 5 — AGENCY / DEFINITION

Purpose:
- define the positive capability or principle.

Design behavior:
- dominant title;
- short definition;
- semantic phrase highlight;
- 2–3 supporting points maximum unless human-approved otherwise;
- symbolic markers or simple visual anchors.

## Slide 6 — EXPANSION / CTA

Purpose:
- reframe the goal;
- connect to wider participation;
- end with action.

Design behavior:
- thesis/contrast title;
- concept cluster / field;
- reflective conclusion;
- bold CTA;
- strong final visual anchor.

---

# 6. Controlled Looseness System

`Ed.post` should never become mechanically gridded.

Allowed controlled looseness:

- alternating left/right placement;
- staggered vertical rhythm;
- unequal but intentional spacing;
- partial alignment rather than perfect columns;
- line paths that guide the eye;
- painterly shapes that slightly interrupt strict geometry.

Not allowed:

- random placement without reading order;
- collisions;
- decorative chaos;
- inconsistent margins that feel accidental;
- unnecessary icon systems that turn the slide into an infographic.

---

# 7. Editable vs Locked Layers

## Locked by default

- overall palette roles;
- paper texture;
- visual family;
- numbering logic;
- logo application role;
- painterly / hand-drawn character;
- asymmetry / negative-space logic;
- slide-function architecture;
- semantic typography principle.

## Editable when authorized

- text content;
- phrase-level emphasis;
- line breaks;
- local text size;
- local boldness;
- local alignment;
- controlled support-text placement;
- slide-specific painterly balance when creating a new post inside the system.

## Requires explicit human approval

- changing color-role logic;
- moving/removing logo system;
- replacing serif/sans semantic roles;
- changing slide count;
- switching to infographic/grid-first composition;
- changing the template family away from painterly editorial language.

---

# 8. New `Ed.post` Production Workflow

```text
1. RETRIEVE CANONICAL Ed.post SYSTEM
2. RETRIEVE APPROVED CONTENT / WRITING
3. MAP CONTENT TO SLIDE FUNCTIONS
4. DEFINE T1–T5 TYPOGRAPHY ROLES
5. DEFINE SEMANTIC COLOR EMPHASIS
6. BUILD COMPOSITION WITH CONTROLLED ASYMMETRY
7. APPLY LOCKED REPEATED COMPONENTS
8. RUN QC-EBL-EDPOST-001
9. RUN QC-EBL-TYPE-001
10. RUN PROJECT MASTER QC
11. HUMAN REVIEW
12. FINAL MASTER
13. PLATFORM DERIVATIVE
```

---

# 9. Adaptation Rule

A new post should reuse the **system**, not copy Post 01 literally.

Correct reuse:

- same visual grammar;
- same semantic typography logic;
- same material palette family;
- same slide-function discipline;
- new compositions derived from new meaning.

Incorrect reuse:

- copying every shape position mechanically;
- forcing every new topic into the exact Post 01 text geometry;
- inventing a new style because the topic changes;
- converting the system into a generic template grid.

---

# 10. Required QC

Mandatory for all `Ed.post` work:

- `QC-EBL-MEM-001_memory_compliance_qc.md`
- `QC-EBL-EDPOST-001_template_design_system_qc.md`
- `QC-EBL-TYPE-001_semantic_typography_edit_qc.md`
- `QC-EBL-001_project_master_qc.md`
- `QC-LOGO-001_logo_application_qc.md` when logo placement is touched

---

# 11. Canonical Rule

> **`Ed.post` is a meaning-driven editorial design system, not a fixed picture and not a generic social-media template.**

The canonical artifact teaches the system; the design system governs future adaptations; human-approved visuals remain the final authority.
