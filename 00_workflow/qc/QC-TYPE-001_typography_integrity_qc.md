# QC-TYPE-001 — Typography Integrity & Carousel Consistency QC

## Purpose

Validate that typography remains clear, high-contrast, structurally consistent, and faithful to the approved design after generation, retouching, logo replacement, cleanup, or raster editing.

This QC does not authorize redesign. It protects approved typography from fading, ghosting, halo artifacts, unintended softening, inconsistent numbering, or silent changes in size/shape.

## Core Principle

```text
APPROVED TYPOGRAPHY = LOCKED
CLARITY = REQUIRED
CONSISTENCY = REQUIRED
```

A text layer can remain geometrically present and still fail if its raster appearance becomes faded or visually degraded.

## Required Inputs

- approved slide/reference;
- revised slide;
- approved copy;
- carousel/page-number convention;
- target output dimensions;
- human revision instruction.

## Mandatory Gates

### TYPE-01 Copy Fidelity — mandatory

Check exact wording, punctuation, capitalization, emphasis, line breaks, and approved color treatment.

Unauthorized wording or emphasis change => FAIL.

### TYPE-02 Font / Size / Shape Preservation — mandatory

Unless explicitly requested, preserve:

- font family;
- weight;
- size;
- tracking;
- leading;
- line breaks;
- alignment;
- text-box proportion;
- letterform shape;
- typographic hierarchy.

Do not redraw text in a different typeface merely to make it cleaner.

### TYPE-03 Raster Clarity / No Fading — mandatory

Inspect text at native resolution and realistic Instagram viewing size.

Reject:

- faded black text;
- washed-out dark text;
- pale halos around dark glyphs;
- ghosted duplicate edges;
- blur introduced by resizing;
- anti-aliasing artifacts that make letters look outlined when no outline is approved;
- inpainting residue around text;
- partially erased strokes;
- uneven opacity across a word or line;
- accidental transparency.

Black/charcoal typography should read as intentional dark typography, not gray or translucent text, unless the approved design explicitly uses gray.

### TYPE-04 Emphasis Integrity — mandatory

Approved emphasis must remain exact.

For mixed-color lines, verify the precise approved words rather than recoloring the whole sentence.

Example:

```text
ONLY APPROVED PHRASE = ACCENT COLOR
ALL OTHER WORDS = APPROVED BASE COLOR
```

### TYPE-05 Carousel Numbering Consistency — mandatory for multi-slide sets

Page/slide numbering must use one consistent system across the carousel:

- same format;
- same font family;
- same weight relationship;
- same size relationship;
- same baseline logic;
- same spacing around slash;
- same top/left anchor;
- same color;
- same visual hierarchy.

If the system is:

```text
01 / 06
02 / 06
03 / 06
04 / 06
05 / 06
06 / 06
```

then a slide showing only `05` is inconsistent and must be corrected.

### TYPE-06 Revision Isolation — mandatory

When correcting faded text or numbering, change only the authorized typography area.

Do not move or alter:

- painterly shapes;
- illustrations;
- logo;
- colors outside the text edit;
- background composition;
- unrelated text.

### TYPE-07 Native-Size Review — mandatory

Do not approve typography from a contact sheet alone.

Review:

1. native-resolution crop;
2. full slide at target size;
3. reduced Instagram-size preview.

A contact-sheet preview can hide fading, ghosting, or halo artifacts.

### TYPE-08 Human Approval — mandatory

Typography correction is not final until the human approves the revised slide or set.

## Typography Integrity Assessment — 100 Points

| Area | Weight |
|---|---:|
| Copy Fidelity | 20 |
| Font / Size / Shape Preservation | 20 |
| Raster Clarity / No Fading | 20 |
| Emphasis Integrity | 15 |
| Carousel Numbering Consistency | 10 |
| Alignment / Hierarchy Consistency | 10 |
| Native-size / Instagram-size Readability | 5 |
| **TOTAL** | **100** |

Mandatory-gate failure overrides the score.

## Result States

```text
PASS_FOR_HUMAN_REVIEW
PASS
REVISION_REQUIRED
FAIL
```

## Learned Failure Pattern — EBL Post 01, 2026-08-15

Observed:

- Slide 5 typography appeared visually faded/haloed even though the words and approximate layout were present.
- Slide 5 displayed `05` while the rest of the carousel used the `NN / 06` numbering system.

Root causes:

- raster edits were checked for content/layout preservation but not strongly enough for glyph opacity and edge integrity;
- carousel numbering was treated as local slide decoration instead of a system component.

Promoted learning:

```text
TEXT PRESENT ≠ TEXT INTEGRITY
LOCAL NUMBER ≠ CAROUSEL CONSISTENCY
```

Future final QC must include native-size typography inspection and cross-slide numbering comparison before publishing.
