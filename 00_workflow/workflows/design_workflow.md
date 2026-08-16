# Design Workflow

## Purpose

The Design Workflow is the visual-production branch of the Prompt Library.

It owns:

- visual strategy and visual research;
- reference analysis;
- named-style study and motif extraction;
- Visual DNA;
- platform/template synthesis;
- art direction;
- image generation;
- editable reconstruction;
- Figma/production implementation;
- visual QC;
- approved visual output.

It does **not** independently research, author, simplify, approve, or rewrite substantial textual content.

## Core Pipeline

```text
PROJECT / APPROVED CONTENT INPUT
→ DESIGN STRATEGY
→ VISUAL RESEARCH
→ VISUAL ANALYSIS
→ OPTIONAL NAMED STYLE STUDY
→ OPTIONAL MOTIF EXTRACTION
→ REFERENCE STYLE SYNTHESIS
→ VISUAL DNA
→ PLATFORM / TEMPLATE SYNTHESIS
→ ART DIRECTION
→ GENERATION SPECIFICATION
→ VISUAL GENERATION
→ HUMAN VISUAL REVIEW
→ OPTIONAL EDITABLE RECONSTRUCTION
→ FIGMA / PRODUCTION IMPLEMENTATION
→ VISUAL QC
→ APPROVED VISUAL OUTPUT
```

The existing Design task registry, task contracts, process registry, and validators remain authoritative for the Design branch.

## Approved Writing Input

When meaningful text is involved, Design should receive a `WRITING_TO_DESIGN` handoff through:

`00_workflow/workflows/cross_workflow_handoff_contract.md`

The handoff identifies the exact approved Writing version, source/fact status, locked wording, flexible wording, semantic hierarchy, language level, CTA/caption state, and unresolved unknowns.

## Design Authority Over Text

Design may:

- set line breaks;
- group text spatially;
- choose visual hierarchy;
- apply typography;
- emphasize approved semantic terms;
- adapt spacing and layout;
- request a shorter/alternative text version.

Design may not silently:

- change factual meaning;
- paraphrase locked wording;
- change source claims;
- alter the approved language level;
- invent or rewrite the CTA;
- rewrite the caption;
- remove required uncertainty or qualification;
- introduce unsupported claims.

When a rewrite is required, issue a `DESIGN_TO_WRITING` handoff. Writing owns the new wording and must create a new Writing version before Design continues.

## Content Package Boundary

Design may assemble approved Writing artifacts into the final Content Package, but assembly is not authorship.

Writing owns:

```text
CORE MESSAGE
ON-CANVAS COPY
CAPTION
CTA
HASHTAGS / KEYWORDS
ALT-TEXT INTENT
```

Design owns:

```text
VISUAL ARTIFACT
VISUAL HIERARCHY
TYPOGRAPHIC IMPLEMENTATION
VISUAL DESCRIPTION EVIDENCE
TEMPLATE / FIGMA IMPLEMENTATION
VISUAL QC
```

The combined package owns final linking, metadata, final alt text, and mutual version traceability.

## Shared Resources

Design may use the Shared Knowledge Layer for project briefs, audience/cultural research, brand memory, terminology, external references, typography/readability knowledge, platform constraints, tools, and factual source material.

Shared evidence never silently transfers Writing decisions or approval into Design.

## Output Contract

A final Design output involving text must preserve traceability to:

- approved Writing output/version;
- Writing → Design handoff ID;
- Design decisions;
- visual references;
- approved assets;
- visual QC evidence;
- unresolved cross-workflow constraints.

## Boundary Rule

```text
WRITING OWNS WHAT THE CONTENT SAYS.
DESIGN OWNS HOW APPROVED CONTENT IS VISUALLY COMMUNICATED.
```
