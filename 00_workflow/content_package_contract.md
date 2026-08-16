# Content Package Contract

## Purpose

A publishable asset is complete only when approved Writing, approved Design, accessibility, publishing metadata, and implementation artifacts are linked into one controlled Content Package.

The Content Package is an **assembly layer**, not an authoring loophole. It must preserve domain ownership.

## Ownership Model

### Writing owns

- OBJECTIVE / CORE MESSAGE where content-led;
- TITLE / HOOK;
- ON_CANVAS_COPY;
- CAPTION_HOOK;
- CAPTION_BODY;
- CTA;
- HASHTAGS_OR_KEYWORDS;
- language level and tone constraints;
- factual/claim status;
- ALT_TEXT_INTENT;
- textual source references.

### Design owns

- VISUAL_ARTIFACT;
- visual hierarchy;
- typography and layout implementation;
- approved visual assets;
- template relationship;
- Figma/production implementation;
- visual-description evidence;
- visual QC.

### Combined Package owns

- linking exact Writing and Design versions;
- final ALT_TEXT based on Writing semantic intent + final Design evidence;
- publishing metadata;
- package-level QC;
- final human approval state.

## Canonical Lifecycle

```text
WRITING WORKFLOW
→ WRITING QC
→ HUMAN CONTENT APPROVAL
→ WRITING_TO_DESIGN HANDOFF
→ DESIGN WORKFLOW
→ VISUAL QC
→ HUMAN VISUAL APPROVAL
→ CONTENT PACKAGE ASSEMBLY
→ COMBINED PACKAGE QC
→ HUMAN FINAL APPROVAL
```

For visual-only assets with no meaningful authored text, the Writing branch may be not applicable. For text-only publication, the Design branch may be not applicable. Applicability must be explicit.

## Required Identity Fields

```text
CONTENT_ID
PROJECT_ID
PLATFORM
CONTENT_TYPE
FORMAT
PACKAGE_VERSION
PACKAGE_STATUS
WRITING_APPLICABLE
DESIGN_APPLICABLE
APPROVED_WRITING_VERSION
APPROVED_DESIGN_VERSION
WRITING_HANDOFF_ID
```

Use `NOT_APPLICABLE` rather than inventing a missing workflow version.

## Writing Components

When Writing applies:

```text
CONTENT_PURPOSE
AUDIENCE
LANGUAGE_LEVEL
TITLE_OR_HOOK
ON_CANVAS_COPY
SEMANTIC_HIERARCHY
CAPTION_HOOK
CAPTION_BODY
CTA
HASHTAGS_OR_KEYWORDS
ALT_TEXT_INTENT
SOURCE_REFERENCES
CLAIM_STATUS
FACT_STATUS
WRITING_QC_STATUS
HUMAN_CONTENT_APPROVAL
```

Design may place these components but may not silently rewrite them. Any meaningful rewrite routes through `cross_workflow_handoff_contract.md` and produces a new Writing version.

## Design Components

When Design applies:

```text
VISUAL_ARTIFACT
VISUAL_VERSION
VISUAL_HIERARCHY
TYPOGRAPHY_IMPLEMENTATION
APPROVED_ASSET_REFERENCES
TEMPLATE_REFERENCE
FIGMA_IMPLEMENTATION_REFERENCE
VISUAL_DESCRIPTION_EVIDENCE
VISUAL_QC_STATUS
HUMAN_VISUAL_APPROVAL
```

## Accessibility

Final alt text is a combined artifact because it must communicate the approved semantic content and accurately describe the final visual.

Required fields:

```text
ALT_TEXT_INTENT
VISUAL_DESCRIPTION_EVIDENCE
FINAL_ALT_TEXT
ACCESSIBILITY_NOTES
ALT_TEXT_STATUS
```

Final alt text must not introduce factual claims absent from approved Writing and must not describe visual elements that are not present in the approved Design.

## Publishing Metadata

- PUBLISHING_DATE
- POSTING_SEQUENCE
- PLATFORM
- CONTENT_PILLAR
- CAMPAIGN
- CTA_TYPE
- STATUS

## Figma / Production Implementation

When an editable design master is required, link the exact Figma Implementation Package to the approved Design version. The implementation may not silently redefine the approved content or art direction.

Required reference:

`00_workflow/figma_output_contract.md`

## Template and Memory Separation

Keep separate:

- CONTENT INSTANCE;
- WRITING OUTPUT;
- DESIGN OUTPUT;
- TEMPLATE;
- STYLE REFERENCE;
- STYLE RULE;
- FIGMA IMPLEMENTATION;
- FINAL CONTENT PACKAGE.

Approval of one does not automatically approve or promote the others.

## Package QC

Before final approval verify:

1. exact approved Writing version is linked when Writing applies;
2. exact approved Design version is linked when Design applies;
3. no Design-side semantic rewrite occurred without a new Writing version;
4. caption/CTA match the approved Writing output;
5. final alt text matches both semantic intent and final visual evidence;
6. source/fact status remains traceable;
7. unresolved unknowns are not hidden;
8. publishing metadata is complete;
9. all required human approvals are recorded.

## Revision Rules

A change to Writing does not automatically alter Design. A changed Writing version invalidates any Design/package state that depends on changed text until the affected Design stages are rechecked.

A change to Design does not automatically alter Writing. If the visual change requires a semantic rewrite, route to Writing.

Every changed component must be versioned independently and the combined package must reference the exact approved versions.
