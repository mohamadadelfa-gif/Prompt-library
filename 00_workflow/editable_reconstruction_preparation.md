# Editable Reconstruction Preparation

## ID

`PROD-EDIT-001`

## Purpose

Prepare an approved raster visual for exact manual reconstruction in Figma without redesigning the approved output.

This protocol separates the approved visual into controlled production assets while preserving the approved PNG as the visual source of truth.

## Position in the Workflow

```text
APPROVED VISUAL
      ↓
SOURCE LOCK
      ↓
EDITABLE RECONSTRUCTION PREPARATION
      ↓
LIVE EDITABLE TEXT LAYERS
      ↓
FIGMA IMPLEMENTATION
      ↓
FIGMA QC / FINAL APPROVAL
```

Use this protocol when the approved visual is rasterized, generated, flattened, or otherwise not directly editable.

Do not use it to reinterpret, improve, restyle, or redesign the approved visual.

## Governing Principle

> The approved PNG defines what the design must look like. The textless artwork provides the visual base. Figma provides the editable production structure.

The approved PNG, textless reconstruction, live editable text package, and Figma master are separate artifacts and must not be collapsed into one.

## Required Inputs

- approved final visual artifact(s)
- approval/version identifier
- exact frame dimensions
- approved on-canvas copy
- approved typography reference or typography master when available
- approved logo/brand assets when available
- target production application: Figma

If the approved visual or copy is not locked, STOP.

## Artifact Classification

```text
APPROVED PNG                = OUTPUT / APPROVED VISUAL SOURCE OF TRUTH
TEXTLESS ARTWORK PNG        = DERIVED PRODUCTION ASSET
EDITABLE TEXT SPECIFICATION = DERIVED FROM APPROVED COPY + TYPOGRAPHY
LIVE EDITABLE TEXT PACKAGE  = PRODUCTION ASSET
FIGMA MASTER                = PRODUCTION OUTPUT
```

A textless reconstruction must never replace the approved PNG as provenance evidence.

## Process

### 1. Source Lock

Preserve the approved visual exactly and create a protected source artifact.

Record:

- content/output ID
- version
- dimensions
- file format
- approval status
- checksum or other integrity reference when available

Never overwrite the approved source file.

### 2. Text / Artwork Inventory

Classify every visible element as one of:

- TEXT — must become editable live text where practical
- SIMPLE VECTOR / SIGN — may become editable vector/component
- RASTER ARTWORK — preserve as raster when reconstruction would change appearance
- LOCKED BRAND ASSET — use approved source asset
- BACKGROUND / TEXTURE — preserve visually

The inventory must distinguish editable need from visual appearance.

### 3. Textless Artwork Derivation

Create one textless artwork file per approved frame.

Remove only typography-related content, including when applicable:

- headline
- supporting copy
- emphasis text
- CTA
- slide number
- textual labels
- brand-name text when it will be rebuilt as live text

Preserve:

- paper/material texture
- painterly fields
- brush marks
- lines
- grids
- circles
- dots
- signs and motifs
- organic/geometric shapes
- color relationships
- composition
- internal negative space

### 4. Hidden-Background Reconstruction Rule

Raster text removal does not reveal original pixels underneath the text.

Any repaired area is therefore a reconstruction and must be treated as DERIVED.

Requirements:

- reconstruct only the minimum area necessary;
- match surrounding texture/material behavior;
- do not rebalance composition;
- do not introduce new motifs;
- do not alter approved shapes merely to simplify cleanup;
- flag visible uncertainty for human review.

### 5. Textless Artwork QC

Compare each textless file against the approved PNG.

Check:

- non-text artwork preserved;
- colors preserved;
- shape proportions preserved;
- lines/signs/motifs preserved;
- no ghost letters;
- no obvious patching or smearing;
- reconstructed texture appears continuous;
- frame dimensions match the approved source;
- no external gutter or accidental crop was introduced.

Gate state:

```text
PASS
PASS_WITH_REVISION
FAIL
```

FAIL blocks Figma reconstruction.

### 6. Editable Layer Map

Create a reconstruction map for each frame.

Recommended structure:

```text
SLIDE XX
│
├── 00_REFERENCE
│   └── Approved Final PNG [LOCKED]
│
├── 01_ARTWORK
│   └── Textless Artwork PNG
│
├── 02_EDITABLE_TEXT
│   ├── Slide Number
│   ├── Headline
│   ├── Subheadline
│   ├── Supporting Copy
│   ├── Emphasis Text
│   ├── CTA
│   └── Brand Text
│
└── 03_EDITABLE_GRAPHICS
    ├── Simple Signs / Shapes
    └── Approved Logo Asset
```

Not every frame needs every layer type.

### 7. Typography Reconstruction Specification

Rebuild rasterized text as live editable text.

Record:

- font family
- style/weight
- size
- line height
- letter spacing
- alignment
- line breaks
- paragraph spacing
- color
- bounding box / position
- hierarchy role

When an approved typography master exists, use it as the system reference.

If the exact font cannot be identified with sufficient confidence, do not silently substitute it. Mark `TYPOGRAPHY_REVIEW_REQUIRED`.

### 8. Live Editable Text Layer Contract

Run:

`live_editable_text_layers.md`

for all text that must remain editable in the Figma production master.

The required output is `LIVE_EDITABLE_TEXT_PACKAGE`.

Every approved text element that is not intentionally a locked brand asset must become a native, selectable Figma text layer rather than remaining baked into the raster artwork.

Required behaviors:

- exact approved copy;
- approved line breaks;
- approved emphasis;
- approved alignment;
- approved hierarchy;
- deterministic layer naming;
- font confidence recorded;
- overlay QC against the approved PNG.

### 9. Figma Handoff Package

Required handoff:

- approved PNG(s), locked reference
- textless artwork PNG(s)
- approved exact copy
- editable layer map
- typography reconstruction specification
- live editable text package
- frame dimensions
- color/style references
- known uncertainties
- provenance/version identifiers

## Figma Overlay Validation

During Figma reconstruction, the approved PNG must remain available as a locked comparison layer.

Use overlay / visibility comparison to validate:

- text position
- line breaks
- font metrics
- line height
- spacing
- alignment
- visual weight
- artwork registration
- frame dimensions

The approved reference may be hidden after validation but should remain in the production file unless the project explicitly requires removal.

## File Naming

Recommended generic convention:

```text
{CONTENT_ID}_SLIDE_01_APPROVED.png
{CONTENT_ID}_SLIDE_01_TEXTLESS.png
{CONTENT_ID}_SLIDE_01_EDITABLE_SPEC.md
```

For multi-slide content, preserve deterministic slide order.

## Decision Gate

The protocol passes only when:

- the approved raster source is preserved and versioned;
- all textless artwork files exist at the correct dimensions;
- non-text artwork is visually preserved;
- reconstructed regions pass human/visual QC;
- editable content is mapped;
- required text is represented in the live editable text package;
- typography uncertainty is explicitly recorded;
- the Figma handoff package is complete.

## Failure Routing

- wrong approved source → Human Revision / Approval
- incorrect crop or frame extraction → Editable Reconstruction Preparation
- visible text-removal artifact → Editable Reconstruction Preparation
- missing/uncertain font → Typography Review / Human Decision
- missing/non-editable text layer → Live Editable Text Layers
- artwork drift → restore from approved source and redo reconstruction
- Figma mismatch after correct preparation → Figma Implementation
- approved visual itself needs redesign → route upstream; do not fix here

## Non-Task

This protocol must not:

- rewrite copy;
- change typography hierarchy;
- change colors;
- redesign composition;
- add/remove motifs for aesthetic reasons;
- normalize painterly irregularity;
- turn a raster reconstruction into a new visual direction;
- promote reconstruction decisions into style rules.

## Example — Multi-Slide Instagram Carousel

```text
APPROVED 6-SLIDE CAROUSEL
        ↓
6 LOCKED APPROVED PNGs
        ↓
6 TEXTLESS ARTWORK PNGs
        ↓
TEXTLESS QC
        ↓
LIVE EDITABLE TEXT PACKAGE
        ↓
FIGMA RECONSTRUCTION
        ↓
OVERLAY MATCH
        ↓
APPROVED EDITABLE MASTER
```

The number of slides and dimensions come from the approved content requirement; they are not hard-coded by this protocol.

## Output

`EDITABLE_RECONSTRUCTION_PACKAGE`

Status must be one of:

- `READY_FOR_FIGMA`
- `REVISION_REQUIRED`
- `BLOCKED`
