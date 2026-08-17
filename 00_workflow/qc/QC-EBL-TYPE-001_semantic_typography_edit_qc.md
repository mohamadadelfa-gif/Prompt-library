# QC-EBL-TYPE-001 — Semantic Typography & Scoped Edit QC

## Purpose

Provide the canonical quality-control gate for typography refinement and text-layout editing in **English Beyond Language (EBL)** visual assets, especially approved or near-approved Instagram posts/carousels such as `Ed.post-text`.

This QC exists to prevent a typography correction from becoming an unintended redesign.

The governing principle is:

> **Preserve the design system. Improve clarity, hierarchy, rhythm, and emphasis.**

Typography is treated as a carrier of meaning, not as decoration.

---

## Scope

Use this QC when the requested change involves one or more of the following:

- text color;
- word- or phrase-level emphasis;
- font weight / boldness;
- slight font-size adjustment;
- line breaks;
- text alignment;
- spacing between text blocks;
- editorial rhythm;
- list or multi-item arrangement;
- controlled asymmetry / controlled looseness;
- CTA emphasis;
- local typography repair;
- preserving a fixed template while changing text behavior.

Do **not** use this QC as permission to redesign the entire asset.

---

# Core Principle

```text
APPROVED / FIXED TEMPLATE
        ↓
AUTHORIZED TEXT ZONE
        ↓
SEMANTIC TYPOGRAPHY EDIT
        ↓
LOCAL BALANCE CHECK
        ↓
PRESERVE EVERYTHING ELSE
```

For an approved slide:

```text
APPROVED SLIDE = LOCKED ARTWORK
REQUESTED EDIT = AUTHORIZED CHANGE AREA
EVERYTHING ELSE = PRESERVE
```

---

# Gate 0 — Scope Lock — MANDATORY

Before editing, identify exactly what the human authorized.

Record:

- slide / asset;
- exact text block;
- requested change;
- elements explicitly required to remain unchanged.

Typical fixed elements include:

- background texture;
- painterly shapes;
- palette;
- logo;
- slide numbering;
- decorative lines;
- dot-grid motifs;
- established geometry;
- overall composition;
- unrelated typography.

### Pass condition

The editable region is explicitly bounded.

### Fail conditions

- unrelated artwork changes;
- logo moved or regenerated without request;
- color fields altered without request;
- new decorative objects introduced merely to support a text edit;
- slide composition redesigned when only typography was requested.

Failure state:

`FAIL_SCOPE_DRIFT`

---

# Gate 1 — Meaning Before Styling — MANDATORY

For every text block, identify its semantic role before changing its appearance.

Use the hierarchy:

```text
L1 — MAIN CONCEPT / TITLE
L2 — KEY CONTRAST / KEY PHRASE
L3 — SUPPORTING EXPLANATION
L4 — EXAMPLES / EVIDENCE / LIST
L5 — CTA / FINAL ACTION
```

Typography must reflect the role of the text.

### Rule

> **Meaning determines typography.**

Do not add emphasis because an area feels visually empty.

### Pass condition

The visual emphasis corresponds to semantic importance.

### Fail condition

Decorative emphasis changes the meaning hierarchy or highlights an arbitrary phrase.

Failure state:

`FAIL_SEMANTIC_HIERARCHY`

---

# Gate 2 — Semantic Color — MANDATORY

EBL accent color is used intentionally, not randomly.

Typical semantic functions for rust / red include:

- conceptual contrast;
- key phrase;
- point of tension;
- meaningful emphasis;
- CTA;
- selected phrase inside an explanatory sentence.

Black / charcoal generally carries:

- neutral statement;
- body explanation;
- structural text;
- readable supporting information.

Other EBL colors may operate as fields or conceptual containers according to the approved artwork.

### Word-level precision

When a human specifies a phrase for color emphasis, apply color **only to that phrase**.

Do not expand the color to neighboring words.

Example from approved EBL editing logic:

```text
means being able to use       = neutral
THE ENGLISH YOU HAVE          = accent color
```

### Pass condition

Accent color identifies the intended semantic phrase precisely.

### Fail conditions

- color bleed into adjacent words;
- entire sentence colored when only a phrase was authorized;
- arbitrary multi-color treatment;
- accent color weakens rather than clarifies the hierarchy.

Failure state:

`FAIL_COLOR_SEMANTICS`

---

# Gate 3 — Micro-Scale Hierarchy — MANDATORY

EBL typography refinement normally favors **small, controlled size changes** rather than dramatic scaling.

Human instructions such as:

- `slightly bigger`;
- `slightly smaller`;
- `a little stronger`;
- `make this more visible`;

must be interpreted as local hierarchy refinement, not a new layout system.

### Check

A size change must:

- preserve the established type family;
- remain subordinate to higher hierarchy levels;
- not create new collisions;
- not force unnecessary reflow;
- maintain visual balance with nearby artwork.

### Pass condition

The text becomes clearer or more appropriately weighted without looking newly redesigned.

### Fail conditions

- support text grows into title scale;
- text shrinks below comfortable platform readability;
- new line breaks degrade rhythm;
- a small request causes large layout displacement.

Failure state:

`FAIL_SCALE_HIERARCHY`

---

# Gate 4 — Weight / Boldness — MANDATORY

Use boldness as a semantic signal.

Typical EBL function:

```text
BOLD = stronger statement / action / conclusion
```

For CTA text, bold may be used to strengthen closure and action when explicitly requested.

Example:

```text
Become independent in English.
→ accent color + bold
```

Do not make surrounding supporting copy equally bold unless required by meaning.

### Fail condition

Too many bold elements flatten the hierarchy.

Failure state:

`FAIL_WEIGHT_HIERARCHY`

---

# Gate 5 — Editorial Rhythm & Controlled Looseness — MANDATORY WHEN MULTIPLE ITEMS EXIST

EBL should not default to rigid spreadsheet-like alignment when the content can support a more authored editorial rhythm.

For multi-item text groups, acceptable strategies include:

- alternating left / right placement;
- staggered vertical rhythm;
- soft zigzag composition;
- different but controlled indent levels;
- asymmetric clusters;
- varied line lengths;
- deliberate negative space.

The goal is **controlled looseness**, not disorder.

### EBL rule

> **Structured underneath. Alive on the surface.**

### Example — six-item arrangement

A six-item support block may follow:

```text
01 → LEFT
02 → RIGHT
03 → LEFT
04 → RIGHT
05 → LEFT
06 → RIGHT
```

But the rows do not need identical baselines or equal spacing. Slight vertical staggering may create a more natural visual rhythm.

### Required preservation

- reading order must remain understandable;
- no item may appear detached from the title;
- items must remain inside safe/readable zones;
- negative space must feel intentional;
- surrounding painterly elements remain unchanged unless explicitly authorized.

### Reject

- rigid table appearance when not semantically required;
- perfect mechanical symmetry;
- random scatter;
- text collisions;
- confusing reading order;
- decorative icons added merely to make the list look creative.

Failure states:

`FAIL_RHYTHM_TOO_RIGID`

or

`FAIL_RHYTHM_CHAOTIC`

---

# Gate 6 — Line Break Integrity — MANDATORY

Line breaks should support:

- meaning;
- natural phrase grouping;
- visual balance;
- readability;
- the approved composition.

Avoid breaking a phrase in a way that weakens comprehension merely to fill space.

When the human has approved a line-break structure, preserve it unless the requested size/alignment edit makes a small adjustment unavoidable.

Any adjustment must remain local.

Failure state:

`FAIL_LINE_BREAK_LOGIC`

---

# Gate 7 — CTA Hierarchy — MANDATORY WHEN CTA EXISTS

A CTA should read as the closing action, not as ordinary body copy.

Check:

- wording is exact;
- CTA remains visually distinct;
- emphasis is stronger than supporting copy;
- CTA does not overpower the main conceptual title;
- color and weight follow the approved EBL system.

Preferred logic when approved:

```text
CTA = ACCENT COLOR + STRONGER WEIGHT
```

Failure state:

`FAIL_CTA_HIERARCHY`

---

# Gate 8 — Readability & Platform Check — MANDATORY

Evaluate at intended publishing size, not only zoomed in.

Check:

- text is readable on Instagram feed/mobile scale;
- serif strokes remain clear;
- black/charcoal text is optically solid;
- accent text retains enough contrast;
- no faded halos or ghosting;
- no text sits too close to edges or shapes;
- line spacing remains comfortable;
- creative looseness does not reduce legibility.

If raster editing damages typography, reconstruct the local text cleanly instead of repeatedly inpainting damaged glyphs.

Failure state:

`FAIL_PLATFORM_READABILITY`

---

# Gate 9 — Preservation Comparison — MANDATORY

Compare the edited slide against the approved source.

Ask:

```text
WHAT CHANGED?
WAS EACH CHANGE AUTHORIZED?
WHAT DID NOT NEED TO CHANGE?
WAS IT PRESERVED?
```

Every visible change must be explainable by the edit brief.

### Blocking failure

If a human requested only a typography edit but the system also changed painterly artwork, logo, palette, geometry, or unrelated copy:

`FAIL_UNAUTHORIZED_VISUAL_CHANGE`

---

# EBL Typography Role Map

## Level 1 — Main Concept / Title

- strongest hierarchy;
- establishes slide meaning;
- usually dominant serif/display treatment in `Ed.post-text`;
- must remain the primary focal point unless a specific slide intentionally behaves differently.

## Level 2 — Key Contrast / Key Phrase

- may use rust/red;
- may receive controlled size/weight emphasis;
- communicates conceptual tension or the central shift.

## Level 3 — Supporting Explanation

- calm and highly readable;
- secondary to title;
- size can be refined slightly to improve comprehension.

## Level 4 — Examples / Evidence / List

- may be arranged more freely;
- can use controlled asymmetry;
- reading order remains clear;
- avoid generic infographic behavior.

## Level 5 — CTA

- clear closing signal;
- may use accent color;
- may be bold;
- should be decisive without competing with the main title.

---

# Learned EBL Examples

## Slide 3 — Controlled Looseness

Learned editing principle:

The six support items under the title should not need to behave like a rigid two-column list. They may use a staggered left/right rhythm to create editorial movement while preserving readability and all surrounding artwork.

Derived QC rule:

```text
MULTI-ITEM SUPPORT TEXT
→ PRESERVE READING ORDER
→ BREAK MECHANICAL ALIGNMENT
→ USE CONTROLLED ASYMMETRY
→ KEEP DESIGN LOCKED
```

## Slide 5 — Phrase-Level Color

Learned editing principle:

Within:

`means being able to use the English you have.`

only the conceptually important phrase:

`the English you have.`

receives accent color.

Derived QC rule:

```text
SEMANTIC PHRASE
→ LOCAL COLOR EMPHASIS
→ SURROUNDING COPY REMAINS NEUTRAL
```

## Slide 6 — Multi-Level Hierarchy

Learned editing principles:

- `Not perfect English.` functions as the contrast phrase and may be rust/red;
- the supporting statement below may be made slightly bigger when more readability/weight is needed;
- the wider-world explanatory sentence may also be slightly enlarged while remaining secondary;
- `Become independent in English.` functions as CTA and should be bold when stronger action emphasis is requested.

Derived QC rule:

```text
CONTRAST = COLOR
SUPPORT = MICRO-SCALE ADJUSTMENT
EXPLANATION = READABILITY BALANCE
CTA = COLOR + BOLD
```

---

# QC Checklist

Before approving an EBL typography edit, answer all items:

- [ ] Was the authorized edit zone identified?
- [ ] Was all unrelated artwork preserved?
- [ ] Is the exact approved copy preserved?
- [ ] Does emphasis follow meaning?
- [ ] Is color applied only to the intended phrase?
- [ ] Are size changes subtle and hierarchy-safe?
- [ ] Is boldness used intentionally?
- [ ] Are line breaks semantically natural?
- [ ] If multiple items exist, is the arrangement alive without becoming chaotic?
- [ ] Is reading order clear?
- [ ] Does negative space remain balanced?
- [ ] Is the logo untouched unless explicitly authorized?
- [ ] Is slide numbering untouched unless explicitly authorized?
- [ ] Does the output remain recognizably the same approved slide/template?
- [ ] Does typography remain clear at native/mobile viewing size?
- [ ] Can every visible change be traced to the human edit brief?

---

# Decision States

Use one final state:

- `PASS_EBL_TYPE_QC`
- `PASS_WITH_MINOR_REFINEMENT`
- `FAIL_SCOPE_DRIFT`
- `FAIL_SEMANTIC_HIERARCHY`
- `FAIL_COLOR_SEMANTICS`
- `FAIL_SCALE_HIERARCHY`
- `FAIL_WEIGHT_HIERARCHY`
- `FAIL_RHYTHM_TOO_RIGID`
- `FAIL_RHYTHM_CHAOTIC`
- `FAIL_LINE_BREAK_LOGIC`
- `FAIL_CTA_HIERARCHY`
- `FAIL_PLATFORM_READABILITY`
- `FAIL_UNAUTHORIZED_VISUAL_CHANGE`

Any `FAIL_*` state blocks final approval until corrected.

---

# Compact Operational Rule

```text
LOCK TEMPLATE
→ IDENTIFY TEXT ROLE
→ EDIT ONLY AUTHORIZED AREA
→ EMPHASIZE MEANING
→ REFINE SIZE / COLOR / WEIGHT / RHYTHM
→ CHECK READABILITY
→ COMPARE AGAINST SOURCE
→ HUMAN APPROVAL
```

## One-Line EBL Typography Rule

> **Edit meaning through typography; never redesign the approved artwork by accident.**
