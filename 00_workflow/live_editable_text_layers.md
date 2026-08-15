# Live Editable Text Layers Contract

## ID

`PROD-TEXT-001`

## Purpose

Define how approved rasterized typography must be rebuilt as **real, selectable, editable Figma text layers** while preserving the approved visual appearance.

This contract is used after `editable_reconstruction_preparation.md` and before final Figma approval.

## Governing Rule

> Text that must remain editable in production must not remain baked into the raster artwork.

The approved PNG remains the visual source of truth. Live text layers must reproduce it rather than reinterpret it.

## Required Layer Types

Create separate live text layers where applicable:

```text
02_EDITABLE_TEXT
├── Slide Number
├── Headline
├── Subheadline
├── Supporting Copy
├── Emphasis Text
├── Quote / Question
├── CTA
├── Brand Text
└── Labels / Captions
```

Do not merge unrelated text roles into one text object merely for convenience.

## Live Text Requirement

A valid live editable text layer must:

- be a native Figma `TEXT` layer;
- remain selectable and editable by a human;
- contain the exact approved copy;
- preserve approved line breaks;
- preserve hierarchy and emphasis;
- preserve alignment and text direction;
- preserve approximate visual position and bounding box;
- use the approved or human-confirmed font family/style;
- remain independent from the raster artwork layer.

Flattened, outlined, rasterized, or image-based text does not satisfy this requirement unless explicitly classified as a locked brand asset.

## Typography Fields

Record for every live text layer:

```text
LAYER_NAME
TEXT_ROLE
EXACT_COPY
FONT_FAMILY
FONT_STYLE
FONT_WEIGHT
FONT_SIZE
LINE_HEIGHT
LETTER_SPACING
TEXT_ALIGN
TEXT_COLOR
LINE_BREAKS
PARAGRAPH_SPACING
BOUNDING_BOX
POSITION
ROTATION
OPACITY
SOURCE_REFERENCE
CONFIDENCE
APPROVAL_STATUS
```

## Copy Fidelity

The editable text must match the approved source exactly.

Do not:

- rewrite wording;
- fix grammar silently;
- change punctuation;
- remove ellipses;
- alter capitalization;
- change slide numbering;
- change emphasis wording;
- change line breaks solely because another layout looks cleaner.

Any copy change requires an explicit upstream revision decision.

## Font Matching

Use the approved typography master or confirmed font specification when available.

If the exact font cannot be identified confidently:

1. keep the approved PNG visible as the comparison reference;
2. test candidate fonts only for reconstruction;
3. record the uncertainty;
4. mark `TYPOGRAPHY_REVIEW_REQUIRED`;
5. do not silently approve a substitute.

A visually similar font is not automatically an approved font.

## Position and Formatting Match

Match the approved PNG for:

- left/right/center alignment;
- line arrangement;
- line formatting;
- line length;
- line spacing;
- paragraph spacing;
- text block width;
- baseline relationships;
- visual weight;
- emphasis color;
- proximity to artwork and margins.

The objective is visual registration, not automatic typographic normalization.

## Layer Naming

Recommended convention:

```text
TXT/01/SlideNumber
TXT/01/Headline
TXT/01/Supporting/01
TXT/01/Supporting/02
TXT/01/Emphasis
TXT/01/CTA
TXT/01/Brand
```

Use deterministic names so future automation or human editing can locate each layer reliably.

## Editable vs Controlled

Text layers are normally classified as:

- `EDITABLE_CONTENT` — wording may change in future content instances;
- `CONTROLLED_STYLE` — font, size, color, spacing, and hierarchy should follow the approved template/system;
- `LOCKED_REFERENCE` — approved PNG only, never edited as production text.

Human editors may change editable content, but style changes should follow the template or an explicit revision decision.

## Figma Frame Structure

Recommended slide structure:

```text
SLIDE XX
│
├── 00_REFERENCE
│   └── Approved Final PNG [LOCKED]
│
├── 01_ARTWORK
│   └── Textless Artwork PNG [CONTROLLED]
│
└── 02_EDITABLE_TEXT
    ├── Slide Number [LIVE TEXT]
    ├── Headline [LIVE TEXT]
    ├── Supporting Copy [LIVE TEXT]
    ├── Emphasis Text [LIVE TEXT]
    ├── CTA [LIVE TEXT]
    └── Brand Text [LIVE TEXT]
```

Simple vector signs/components may live in a separate `03_EDITABLE_GRAPHICS` group.

## Overlay QC

Validate every live text layer against the approved PNG using overlay, opacity, or visibility comparison.

Check:

- exact copy;
- line breaks;
- text position;
- font metrics;
- font size;
- line height;
- spacing;
- emphasis color;
- visual hierarchy;
- edge/margin relationships.

Gate states:

```text
PASS
PASS_WITH_REVISION
FAIL
```

A noticeable mismatch blocks final Figma approval.

## Output

`LIVE_EDITABLE_TEXT_PACKAGE`

Required contents:

- live editable text layers for every approved text element;
- typography specification;
- layer naming map;
- copy-fidelity record;
- font-confidence record;
- overlay-QC result;
- approval status.

## Non-Task

This stage must not:

- redesign typography;
- invent copy;
- change approved hierarchy;
- alter artwork to make text easier to fit;
- convert approved irregularity into a generic grid;
- flatten live text after reconstruction unless an export requires it;
- treat a font substitution as approved without human review.
