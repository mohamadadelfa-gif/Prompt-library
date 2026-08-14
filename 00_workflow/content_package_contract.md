# Content Package Contract

## Purpose

A generated social asset is not production-complete until the visual artifact, reusable template information, caption, accessibility text, CTA, and publishing metadata are captured as one controlled Content Package.

## Content Package Lifecycle

```text
PROJECT INPUT
    ↓
CONTENT STRATEGY
    ↓
CONTENT ARTIFACT
    ├── Visual Direction
    ├── Copy / On-Canvas Text
    ├── Caption
    ├── CTA
    ├── Hashtags / Keywords
    ├── Alt Text
    └── Publishing Metadata
         ↓
GEN-002
         ↓
Generated Visual
         ↓
Human Revision
         ↓
Approved Content Package
         ├── Approved Visual
         ├── Approved Caption
         ├── Approved CTA
         ├── Approved Alt Text
         └── Template Candidate
```

## Required Components

### 1. Content Identity

- CONTENT_ID
- PROJECT_ID
- PLATFORM
- CONTENT_TYPE
- FORMAT
- VERSION
- STATUS

### 2. Creative Content

- OBJECTIVE
- CORE_MESSAGE
- AUDIENCE
- CONTENT_PILLAR
- ON_CANVAS_COPY
- VISUAL_ARTIFACT

### 3. Caption

The caption is a first-class content artifact, not an afterthought.

Required fields:

- CAPTION_HOOK
- CAPTION_BODY
- CTA
- HASHTAGS_OR_KEYWORDS
- CAPTION_VERSION
- CAPTION_STATUS

Caption rules:

- Support the post objective.
- Add context rather than redundantly repeating every slide.
- Maintain the approved brand voice.
- Preserve factual accuracy and approved claims.
- Match the audience and platform.
- Never introduce a new strategic claim that is absent from the approved project definition.

### 4. Accessibility

- ALT_TEXT
- ACCESSIBILITY_NOTES

Alt text must describe the meaningful content of the final approved visual, not merely its aesthetic style.

### 5. Publishing Metadata

- PUBLISHING_DATE
- POSTING_SEQUENCE
- PLATFORM
- CONTENT_PILLAR
- CAMPAIGN
- CTA_TYPE
- STATUS

## Template Extraction

When a content artifact is approved, evaluate whether its structure can become a reusable platform template.

Separate:

- CONTENT INSTANCE — the specific post.
- TEMPLATE — reusable layout and structural rules.
- STYLE REFERENCE — approved visual example.
- STYLE RULE — generalized aesthetic principle.

Example:

```text
Post 01 — What Is English Independence?
        ↓
CONTENT INSTANCE
        ↓
TPL-IG-001 — EBL Editorial Carousel / 5 Slides
        +
STYLE-REF-001 — Approved EBL Typography / Visual Reference
        +
STYLE-RULE-001 — Typography-dominant editorial hierarchy
```

## Approval

A Content Package is approved only when the visual artifact, caption, CTA, alt text, and required metadata are complete and reviewed.

Human approval may approve the package while independently rejecting or revising the template/style promotion.

## Revision Rules

A change to the visual does not automatically change the caption.
A change to the caption does not automatically change the visual template.
A change to a project style rule does not automatically change historical content artifacts.

Every changed component must be versioned independently and linked to the approved package version.
