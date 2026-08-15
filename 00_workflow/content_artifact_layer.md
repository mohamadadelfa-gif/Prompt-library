# Content Artifact & Template Layer

## Purpose

Separate the creative output of a task from the reusable production template derived from that output.

A generated Instagram post is not automatically a template. A template is a reusable production structure extracted from an approved output and explicitly approved for reuse.

## Artifact Chain

```text
CUSTOMER / PROJECT INPUT
        ↓
CONTENT BRIEF
        ↓
GENERATION SPECIFICATION
        ↓
GENERATION PROMPT
        ↓
GENERATED CONTENT ARTIFACT
        ↓
HUMAN REVISION
        ↓
APPROVED CONTENT ARTIFACT
        ↓
TEMPLATE EXTRACTION
        ↓
APPROVED CONTENT TEMPLATE
        ↓
STYLE REFERENCE / STYLE RULE
```

## Content Artifact

A concrete communication asset created for a specific content item.

Examples:

- Instagram carousel
- Instagram single image
- Instagram Reel cover
- Story frame
- LinkedIn post visual
- YouTube thumbnail

A content artifact contains actual copy, composition, imagery, graphics, and production dimensions.

## Content Template

A reusable production structure derived from one or more approved content artifacts.

A template defines structure rather than campaign-specific content.

For an Instagram carousel, a template may define:

- canvas dimensions
- slide count range
- safe areas
- grid
- typography hierarchy
- headline zones
- body-copy zones
- image/graphic zones
- CTA zone
- branding zone
- pagination behavior
- spacing system
- reusable geometric elements
- color-role assignments
- texture treatment

The template must not contain campaign-specific copy unless explicitly marked as placeholder content.

## Style Reference vs Template

### Style Reference
Answers:

> What should the work feel/look like?

Contains approved visual characteristics and aesthetic examples.

### Content Template
Answers:

> How should this type of content be constructed?

Contains reusable layout and production rules.

### Style Rule
Answers:

> What recurring visual principle should future work follow?

Contains generalized aesthetic rules.

These three artifact types must remain distinct.

## Example — English Beyond Language

```text
APPROVED OUTPUT
Instagram Carousel — Post 01

        ↓

CONTENT TEMPLATE
"EBL Editorial Carousel — 5 Slide"

        ↓

STYLE REFERENCE
Approved EBL typography + geometric visual treatment

        ↓

STYLE RULES
- strong editorial sans-serif hierarchy
- 70% communication clarity / 30% texture
- restrained geometric accents
- warm paper-based palette
```

The approved Post 01 should therefore become both:

1. a project content artifact; and
2. a candidate reusable Instagram carousel template.

It should not automatically become a global style rule.

## Template Extraction Gate

A human may promote an approved content artifact to a reusable template only when:

- the layout is intentionally reusable;
- content-specific elements are separated from structural elements;
- typography roles are defined;
- spacing and alignment rules are captured;
- editable zones are identified;
- the intended content format is defined;
- the template has been explicitly approved.

## Template Scope

Templates must have a scope:

- PROJECT — reusable within one project.
- BRAND — reusable across one brand/account.
- SYSTEM — reusable across multiple projects.

A template should not move to a broader scope without explicit approval.

## Template Record

```text
TEMPLATE_ID
PROJECT_ID
CONTENT_TYPE
PLATFORM
FORMAT
DIMENSIONS
SOURCE_ARTIFACT
APPROVED_REFERENCE
LAYOUT_RULES
TYPOGRAPHY_RULES
COLOR_RULES
GRAPHIC_RULES
SAFE_AREAS
EDITABLE_ZONES
PLACEHOLDERS
CONTENT_LIMITS
STYLE_REFERENCES
SCOPE
VERSION
STATUS
APPROVER
APPROVED_AT
PROVENANCE
```

## Reuse Rule

When a future generation task requests the same content type, the system may retrieve an approved template as a production constraint.

The template informs structure and hierarchy; it does not replace the new content brief, Art Direction, or current project decisions.

## Anti-Drift Rule

A reused template must not silently transfer:

- old campaign messaging
- old customer requirements
- old audience assumptions
- old content-specific imagery
- old project constraints

Only explicitly reusable template attributes may transfer.
