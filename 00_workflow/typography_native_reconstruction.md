# PROD-TYPE-REPAIR-001 — Native Typography Reconstruction

## Purpose

Repair damaged raster typography in approved visual assets without redesigning the slide.

Use this protocol when text is visibly faded, haloed, ghosted, soft, partially transparent, or repeatedly damaged by raster edits.

## Core Rule

```text
DAMAGED RASTER TYPE
≠
KEEP DARKENING / RECOLORING
```

Preferred repair model:

```text
LOCK APPROVED COPY + TYPOGRAPHIC GEOMETRY
→ ISOLATE DAMAGED TEXT AREA
→ RECONSTRUCT LOCAL BACKGROUND
→ REDRAW EXACT APPROVED COPY ONCE
→ FINAL NATIVE RESOLUTION
→ FULL-OPACITY TYPE
→ NO POST-RENDER RESIZE
→ NATIVE-SIZE QC
```

## Inputs

- approved slide/reference;
- approved copy;
- approved font family or verified production equivalent;
- approved weight, size, tracking, leading, line breaks, alignment and emphasis;
- final output resolution;
- authorized text-repair region.

## Step 1 — Lock the Slide

Everything outside the authorized text region remains unchanged.

Do not alter:

- painterly artwork;
- logo;
- numbering unless explicitly part of the correction;
- unrelated text;
- shapes;
- colors outside approved emphasis;
- composition;
- texture outside the repair area.

## Step 2 — Diagnose the Failure

Do not rely only on RGB values.

Inspect at 100% native scale for:

- gray fringe around black glyphs;
- washed interiors;
- inconsistent stroke density;
- duplicate/ghost edges;
- blur from resizing;
- partial transparency;
- color bleed between emphasis segments;
- inpainting residue.

If the text is optically weak even when numerically dark, treat it as a reconstruction problem.

## Step 3 — Reconstruct the Background

Remove only the damaged typography footprint and restore the local underlying field/texture.

Requirements:

- use same-slide texture/background evidence when possible;
- preserve local tone and material character;
- avoid visible clone seams;
- do not cover nearby artwork or design elements;
- inspect the cleaned field before redrawing type.

## Step 4 — Redraw Once

Render the approved copy once at final native resolution.

Preserve:

- exact wording;
- punctuation;
- capitalization;
- approved line breaks;
- approved font family / verified equivalent;
- weight;
- size;
- alignment;
- leading;
- tracking;
- color segmentation;
- hierarchy.

Use full-opacity approved colors.

Do not use glow, shadow, stroke, transparency, or decorative effects unless explicitly approved.

## Step 5 — Emphasis Segmentation

For mixed-color copy, treat color as semantic structure.

Example:

```text
BASE COPY = charcoal/black
APPROVED EMPHASIS PHRASE = rust/red
ALL OTHER WORDS = base color
```

Never recolor a whole line when only a phrase is approved for emphasis.

## Step 6 — Freeze Resolution

After the final typography render:

- do not resize the slide;
- do not scale the text raster;
- do not apply another destructive retouch pass;
- do not recompress through unnecessary intermediate exports.

If the platform requires a different delivery size, render from the editable/native master rather than scaling an already-final raster repeatedly.

## Step 7 — QC

Run `QC-TYPE-001`.

Mandatory views:

1. 100% native text crop;
2. full slide at final resolution;
3. reduced Instagram-size preview.

Pass only if:

- glyph interiors are solid;
- antialiasing is natural and crisp;
- optical weight is uniform;
- approved emphasis is exact;
- no background-repair artifacts remain;
- no unrelated slide pixels/elements were changed.

## EBL Post 01 Learned Example

Slide 1 supporting question:

```text
But can you use it to do     = black / charcoal
the                          = black / charcoal
things that matter           = rust / red ONLY
to you?                      = black / charcoal
```

The repair succeeded only after switching from repeated raster recoloring to one native-resolution reconstruction.

## Result States

```text
PASS_FOR_HUMAN_REVIEW
PASS
REVISION_REQUIRED
FAIL
```

Human approval remains mandatory before final production.
