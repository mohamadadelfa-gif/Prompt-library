# Instagram Template Synthesis Protocol

## Purpose

Convert approved visual language from the Reference Style Synthesis step into an original, reusable Instagram template system.

This is a translation task, not a reproduction task.

## Inputs

Required:

- approved reference style analysis
- customer / brand requirements
- existing Visual DNA
- content objective
- Instagram content type
- platform dimensions

Optional:

- approved style references
- prior approved templates
- approved human revision records

## Step 1 — Define Platform Role

Identify:

- platform: Instagram
- content type: carousel, single post, story, reel cover, etc.
- dimensions
- number of slides / frames
- mobile readability requirement
- safe areas
- expected viewing distance

## Step 2 — Define Communication Hierarchy

Establish:

- primary message
- secondary message
- supporting information
- CTA
- brand signature

Typography must remain the dominant communication layer unless the content explicitly requires another hierarchy.

## Step 3 — Translate Emotional Effect

The template must preserve the intended emotional experience from the reference analysis.

For English Beyond Language, preserve the intended qualities:

- curious
- human
- thoughtful
- warm
- artistic
- culturally aware
- intelligent
- exploratory

Do not achieve these qualities through random decoration. Achieve them through composition, mark-making, texture, shape, pacing, and whitespace.

## Step 4 — Define Graphic Vocabulary

Create a controlled library of:

- organic shapes
- geometric fields
- hand-drawn lines
- symbols
- grids
- texture treatments
- accent marks

Each element should have a functional role.

## Step 5 — Define Template Zones

Every reusable Instagram template should have explicit zones such as:

```text
HEADLINE_ZONE
SUPPORTING_COPY_ZONE
GRAPHIC_ZONE
BRAND_ZONE
CTA_ZONE
FOOTER_ZONE
```

Zones should be flexible enough for new content but constrained enough to preserve the visual identity.

## Step 6 — Define Repeatable Components

Examples:

- headline block
- question headline
- quote block
- vocabulary block
- pillar label
- decorative field
- hand-drawn line
- symbol
- footer
- slide number
- brand signature

## Step 7 — Define Slide Roles

For a carousel, explicitly define each slide role.

Example:

```text
SLIDE 01 — HOOK
SLIDE 02 — QUESTION / TENSION
SLIDE 03 — EXPLANATION
SLIDE 04 — EXAMPLE / CONTRAST
SLIDE 05 — SUMMARY / CTA
```

The role should derive from content strategy, not from the reference artwork.

## Step 8 — Define Editable vs Controlled Elements

Each template element must be classified:

- EDITABLE — content changes freely.
- CONTROLLED — visual value changes through approved variables or component properties.
- LOCKED — structural brand element requiring design approval.

## Step 9 — Define Figma Implementation

The template must be implementable as editable Figma layers.

Required implementation details:

- page
- frame dimensions
- frame naming
- components
- variables / styles
- text styles
- color styles
- layout grid
- spacing tokens
- auto-layout relationships
- safe zones
- editable fields
- locked fields
- export settings

## Step 10 — Separate Template from Content

Never embed post-specific copy into the reusable template unless the text is explicitly defined as a structural label.

```text
CONTENT INSTANCE
      ↓
TPL-IG-XXX
      ↓
new content can reuse structure
```

## Step 11 — Human Review Checkpoint

The first generated implementation is a **candidate**, not a final template.

Human review must assess:

- typography
- hierarchy
- readability
- emotional effect
- style fidelity
- originality
- consistency across slides
- template reusability

Human revisions must be captured as revision records.

## Step 12 — Template Approval

A template becomes APPROVED only when:

- the content instance is approved;
- the template structure is judged reusable;
- style references are identified;
- editable / controlled / locked elements are documented;
- Figma implementation is complete;
- provenance is recorded;
- the template version is assigned.

## Output

```text
TEMPLATE_ID
PLATFORM
CONTENT_TYPE
FRAME_SPEC
SLIDE_ROLES
CONTENT_ZONES
TYPOGRAPHY_SYSTEM
COLOR_SYSTEM
SHAPE_SYSTEM
LINE_SYSTEM
TEXTURE_SYSTEM
GRID_SYSTEM
COMPONENT_SYSTEM
EDITABLE_FIELDS
CONTROLLED_FIELDS
LOCKED_FIELDS
FIGMA_IMPLEMENTATION
STYLE_REFERENCES
STYLE_RULES
HUMAN_REVISIONS
PROVENANCE
VERSION
DECISION_GATE
```

## Core Principle

The final Instagram template should feel like it belongs to the reference's visual world while remaining an original, readable, repeatable, brand-specific communication system.
