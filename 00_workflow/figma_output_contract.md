# Figma Implementation Output Contract

## Purpose

Every approved content output that is intended for visual production must produce a corresponding Figma-ready implementation package.

The Figma package is the editable production specification for the approved visual artifact. It is not merely a screenshot, reference image, or design description.

## Content-to-Figma Relationship

```text
CONTENT OUTPUT
   |
   +-- Visual Artifact
   +-- Copy / Caption Package
   +-- Reusable Template
   +-- Style Reference / Style Rules
   `-- FIGMA IMPLEMENTATION PACKAGE
```

The Figma package must remain traceable to the exact content output and approved version from which it was created.

## Pre-Figma Reconstruction Requirement

When the approved visual is rasterized, flattened, generated, or otherwise not natively editable, run:

`editable_reconstruction_preparation.md`

before building the Figma master.

The required pre-Figma package must include:

- locked approved PNG/reference artifact;
- textless artwork reconstruction where editable typography is required;
- approved exact copy;
- editable layer map;
- typography reconstruction specification;
- frame dimensions;
- visual/style references;
- known reconstruction uncertainties;
- provenance and version identifiers.

The approved PNG remains the visual source of truth. The textless artwork is a DERIVED production asset and must not replace the approved PNG as provenance evidence.

For reconstruction-sensitive work, keep the approved PNG in Figma as a locked reference layer and validate the editable reconstruction by overlay/visibility comparison.

## Structured Production File Requirement

The internal organization of the Figma production file must follow:

`figma_file_structure.md`

The file must separate:

- approved reference evidence;
- editable production masters;
- reusable style-system assets;
- publish/export outputs.

For reconstructed raster visuals, the working file should expose clear `LOCKED`, `CONTROLLED`, `EDITABLE`, and `REFERENCE` states so a manual edit cannot silently replace or corrupt the approved visual source.

If a Figma MCP operation is blocked by a plan, permission, rate, or tool-call limit, treat the failed operation as **NO CHANGE APPLIED** unless the tool explicitly reports mutated or created node IDs. Do not claim the file was restructured after a blocked call.

## Required Fields

```text
FIGMA_PACKAGE_ID
CONTENT_ID
OUTPUT_ID
CONTENT_VERSION
APPROVED_ARTIFACT
RECONSTRUCTION_PACKAGE_ID
PLATFORM
FORMAT
FRAME_SIZE
PAGE_STRUCTURE
FRAME_STRUCTURE
COMPONENTS
VARIANTS
LOCAL_STYLES
VARIABLES
GRID
AUTO_LAYOUT
SPACING_TOKENS
SAFE_AREAS
TYPOGRAPHY
COLOR_STYLES
EFFECTS
ASSET_PLACEMENT
LAYER_NAMING
EXPORT_SETTINGS
TEMPLATE_BEHAVIOR
EDITABLE_FIELDS
LOCKED_ELEMENTS
PROVENANCE
APPROVAL_STATUS
VERSION
```

`RECONSTRUCTION_PACKAGE_ID` is required when `editable_reconstruction_preparation.md` applies; otherwise record `NOT_APPLICABLE`.

## Platform Specification

Each Figma package must identify the destination platform and output format, for example:

- Instagram Feed Post — 1080×1080
- Instagram Portrait Post — 1080×1350
- Instagram Story — 1080×1920
- Instagram Reel Cover — 1080×1920
- YouTube Thumbnail — 1280×720

The format must be derived from the actual content requirement, not assumed from a previous project.

## Frame Architecture

The package must specify:

1. Page name
2. Frame name
3. Frame dimensions
4. Number of frames/slides
5. Frame order
6. Safe margins
7. Content zones
8. Background treatment
9. Brand area

For multi-slide content, every slide must have a defined role and structure.

For reconstructed raster visuals, the recommended internal frame architecture is:

```text
SLIDE XX
│
├── 00_REFERENCE
│   └── Approved Final PNG [LOCKED]
│
├── 01_ARTWORK
│   └── Textless Artwork / Approved Raster Artwork [CONTROLLED]
│
├── 02_EDITABLE_TEXT
│   ├── Slide Number [EDITABLE]
│   ├── Headline [EDITABLE]
│   ├── Supporting Copy [EDITABLE]
│   ├── Emphasis Text [EDITABLE]
│   ├── CTA [EDITABLE]
│   └── Brand Text [EDITABLE]
│
├── 03_EDITABLE_GRAPHICS
│   ├── Simple Signs / Shapes [CONTROLLED]
│   └── Approved Logo Asset [CONTROLLED or LOCKED]
│
└── 04_QC
    └── Overlay Reference / Comparison Controls
```

## Components

Identify reusable components separately from instance content.

Examples:

- `IG/Carousel/Headline`
- `IG/Carousel/Question`
- `IG/Carousel/Body`
- `IG/Carousel/GraphicField`
- `IG/Carousel/BrandMark`
- `IG/Carousel/Footer`

Components should define which properties can vary without breaking the system.

## Editable vs Locked

Every important layer or component must be classified as:

- EDITABLE — content can change for future posts.
- CONTROLLED — can change only through defined style variables or component properties.
- LOCKED — should not be changed without design-system approval.
- REFERENCE — source-of-truth evidence used for comparison, not the working production object.

For reconstructed approved visuals, the reference PNG is LOCKED/REFERENCE. Derived textless artwork is normally CONTROLLED or LOCKED depending on whether manual retouching is allowed.

## Typography

The package must define:

- Typeface
- Weight
- Size
- Line height
- Letter spacing
- Alignment
- Text hierarchy
- Maximum text length where layout depends on it

Typography preferences extracted from approved human revisions must reference the Style Memory system rather than becoming unexplained hard-coded rules.

When rasterized text is being rebuilt as live Figma text, preserve the approved line breaks, hierarchy, alignment, spacing, emphasis, and position. If the exact typeface cannot be identified with sufficient confidence, mark the reconstruction for human typography review rather than silently substituting a font.

## Color

Define reusable Figma color styles or variables where appropriate.

Each color should identify:

- Name
- Value
- Role
- Scope
- Source / approval

## Layout System

Define:

- Grid type
- Columns / rows
- Margins
- Gutters
- Spacing tokens
- Alignment rules
- Auto-layout behavior
- Responsive behavior where relevant

## Content Zones

Each content zone must have a purpose, for example:

```text
HEADLINE_ZONE
SUPPORTING_COPY_ZONE
GRAPHIC_ZONE
BRAND_ZONE
CTA_ZONE
FOOTER_ZONE
```

A future content item can therefore reuse the template without copying the original post's text.

## Overlay Validation

For raster-to-editable reconstruction, validate the Figma master against the approved PNG using overlay, opacity, or visibility comparison.

Check:

- frame dimensions;
- text position;
- font metrics;
- line breaks;
- line height;
- paragraph spacing;
- alignment;
- artwork registration;
- visual weight;
- color appearance.

A visually noticeable reconstruction drift must be routed back to either Editable Reconstruction Preparation or Figma Implementation depending on the cause.

## Export Specification

The Figma package must define:

- Export frame(s)
- File format
- Resolution / scale
- Naming convention
- Transparency requirement where applicable
- Color-space expectations where applicable

## Template Extraction

When an approved output establishes a repeatable visual structure, create a reusable template artifact separate from the specific content artifact.

For example:

```text
CONTENT-EBL-001
  |
  `-- TPL-IG-001
        |
        +-- frame specification
        +-- components
        +-- variables
        +-- editable zones
        `-- locked style structure
```

The template must not inherit post-specific copy or campaign-specific content unless explicitly designated as part of the template.

## Approval Gate

A Figma implementation package is complete only when:

- the approved visual and Figma structure correspond;
- required reconstruction preparation has passed when applicable;
- the Figma production file follows `figma_file_structure.md`;
- the approved PNG remains traceable as the visual reference;
- all critical content is represented;
- editable, controlled, locked, and reference elements are identified;
- platform dimensions are correct;
- typography and color specifications are traceable;
- reusable components are identified;
- overlay validation passes for reconstructed raster visuals;
- export settings are defined;
- any MCP/access blocker is resolved or explicitly recorded;
- the package has an approval status.

## Versioning

Every Figma package must be versioned independently from the prompt and content artifact.

Changes to content do not automatically change the visual template.
Changes to the template do not automatically change the approved content artifact.
Changes to a textless reconstruction do not automatically change the approved visual reference.

## Provenance

The Figma package must identify:

- originating content task;
- originating generation output;
- approved human revision;
- approved raster/reference artifact where applicable;
- reconstruction package where applicable;
- style references used;
- template/version used;
- approval record.

## Non-Task

The Figma implementation layer must not:

- invent customer requirements;
- change approved content strategy;
- silently change approved art direction;
- turn one-off content into a global style rule;
- replace the approved visual without an explicit revision decision;
- treat a reconstructed textless image as more authoritative than the approved source;
- use manual reconstruction as permission to redesign the approved output;
- claim a Figma change was applied when the connector operation failed or was blocked.
