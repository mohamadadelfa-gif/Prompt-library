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

### TYPE-09 Single Native Render / Reconstruction Integrity — mandatory when raster text is damaged

Repeated raster edits are not an acceptable repair method when typography has already become soft, faded, outlined, or partially transparent.

If approved text is visibly degraded:

```text
REMOVE ONLY THE DAMAGED TEXT AREA
→ RECONSTRUCT LOCAL BACKGROUND
→ REDRAW THE EXACT APPROVED COPY ONCE
→ AT FINAL NATIVE OUTPUT RESOLUTION
→ WITH FULL-OPACITY TYPOGRAPHY
→ DO NOT RESIZE AFTER THE FINAL TEXT RENDER
```

Requirements:

- use the approved font family / closest verified production equivalent;
- preserve approved weight, size, line breaks, alignment, and hierarchy;
- render at the final slide resolution, not on a smaller intermediate canvas;
- use solid/full-opacity approved colors;
- do not recolor anti-aliased raster glyphs as the main repair method;
- do not repeatedly inpaint/recolor the same glyphs across revision passes;
- do not enlarge or shrink the slide after the final type render;
- inspect glyph interiors and edges at 100% native scale.

Failure indicators:

- dark centers with gray rims;
- inconsistent stroke density;
- pale antialiasing that visually reads as fading;
- double-edge / shadow-like artifacts;
- color contamination between emphasized and non-emphasized words;
- typography that is technically black by RGB but optically gray.

### TYPE-10 Optical Stroke Density — mandatory

Text color values alone do not prove typography integrity.

Check whether the letterforms have uniform optical density:

- solid interiors;
- consistent weight across letters and words;
- natural but crisp antialiasing;
- no accidental translucency;
- no gray fringe that weakens the perceived weight;
- no word or line appearing lighter than another without an approved hierarchy reason.

The test is visual and structural, not only numerical.

## Typography Integrity Assessment — 100 Points

| Area | Weight |
|---|---:|
| Copy Fidelity | 15 |
| Font / Size / Shape Preservation | 15 |
| Raster Clarity / No Fading | 20 |
| Native Reconstruction Integrity | 15 |
| Emphasis Integrity | 10 |
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

### Failure A — Slide 5 faded typography + numbering inconsistency

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

### Failure B — Slide 1 repeated raster repair still looked faded

Observed:

- Slide 1 supporting question remained visually faded after recoloring/darkening passes;
- the RGB values could be dark while the antialiased edge structure still made the words look gray or weak;
- repeated raster editing degraded stroke density.

Root cause:

```text
RASTER TEXT → RECOLOR / INPAINT → RESIZE / RE-EDIT
```

created soft gray edge pixels, inconsistent optical opacity, and visible fading.

Approved correction model:

```text
RECONSTRUCT BACKGROUND
→ REDRAW EXACT APPROVED COPY ONCE AT 1254×1254
→ FULL-OPACITY TYPE
→ EXACT EMPHASIS SEGMENTATION
→ NO POST-RENDER RESIZE
```

For EBL Post 01 Slide 1:

```text
But can you use it to do     = black / charcoal
the                          = black / charcoal
things that matter           = rust / red ONLY
to you?                      = black / charcoal
```

Promoted learning:

```text
DARK RGB ≠ OPTICALLY SOLID TYPE
REPEATED RASTER REPAIR ≠ TYPOGRAPHIC RECONSTRUCTION
```

Future final QC must include native-size stroke-density inspection and must prefer one clean native-resolution reconstruction over repeated glyph-level raster correction.
