# Cross-Workflow Handoff Contract — Writing ↔ Design

## Purpose

This contract controls transfers between the Writing and Design workflows. It prevents silent re-authoring, authority leakage, version confusion, and unsupported assumptions.

A handoff is a versioned artifact. It is not permission for the receiving workflow to change the sending workflow's approved decisions.

## Writing → Design

Use only after Writing QC and required human content approval.

Required fields:

```text
HANDOFF_ID
HANDOFF_TYPE = WRITING_TO_DESIGN
PROJECT_ID
CONTENT_ID
WRITING_OUTPUT_ID
WRITING_VERSION
CONTENT_PURPOSE
AUDIENCE
PLATFORM
LANGUAGE_LEVEL
TITLE_OR_HOOK
ON_CANVAS_COPY
SEMANTIC_HIERARCHY
LOCKED_WORDING
FLEXIBLE_WORDING
EMPHASIS_TERMS
CAPTION_HOOK
CAPTION_BODY
CTA
HASHTAGS_OR_KEYWORDS
ALT_TEXT_INTENT
SOURCE_REFERENCES
CLAIM_STATUS
FACT_STATUS
UNRESOLVED_UNKNOWNS
WRITING_QC_STATUS
HUMAN_CONTENT_APPROVAL
```

### Design authority after receipt

Design may:

- create line breaks;
- group approved text spatially;
- apply typographic hierarchy;
- select visual emphasis consistent with `EMPHASIS_TERMS`;
- adapt layout to platform constraints;
- request shorter or alternative wording through a return handoff.

Design may not silently:

- change facts;
- alter claim meaning;
- change approved language level;
- paraphrase locked wording;
- invent a new CTA;
- rewrite captions;
- remove required qualifications or uncertainty;
- add unsupported claims.

## Design → Writing

Use when visual or platform constraints make the approved writing difficult or impossible to implement faithfully.

Required fields:

```text
HANDOFF_ID
HANDOFF_TYPE = DESIGN_TO_WRITING
PROJECT_ID
CONTENT_ID
DESIGN_OUTPUT_OR_STAGE
SOURCE_WRITING_VERSION
CONSTRAINT_TYPE
AVAILABLE_TEXT_AREA
MAX_RECOMMENDED_LENGTH
READING_ORDER_CONSTRAINT
TEXT_DENSITY_ISSUE
PLATFORM_CONSTRAINT
SEMANTIC_EMPHASIS_NEED
LOCKED_VISUAL_CONSTRAINTS
REQUESTED_WRITING_ACTION
URGENCY_OR_BLOCKING_STATE
UNRESOLVED_UNKNOWNS
```

Writing owns the resulting rewrite decision and must issue a new Writing version before Design continues.

## Version Rule

```text
WRITING v1
→ DESIGN HANDOFF references v1
→ DESIGN requests rewrite
→ WRITING v2
→ NEW DESIGN HANDOFF references v2
```

Never overwrite an earlier approved Writing version in place.

## Combined-Package Rule

The final package must record both:

```text
APPROVED_WRITING_VERSION
APPROVED_DESIGN_VERSION
```

If either changes, the combined package returns to applicable QC.

## Authority Rule

```text
WRITING APPROVAL ≠ DESIGN APPROVAL
DESIGN APPROVAL ≠ WRITING APPROVAL
BOTH ARE REQUIRED WHEN BOTH DOMAINS ARE PRESENT
```

## Provenance

Every cross-workflow handoff must preserve source references, approval state, unresolved unknowns, and the exact upstream version it consumes.
