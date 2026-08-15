# Motif & Sign Extraction

## Purpose

Extract the recurring visual vocabulary of a named artistic style and its supplied reference set before translating that style into a platform-specific template.

This step answers:

> What are the actual signs, shapes, objects, marks, and recurring visual motifs that make this visual language recognizable?

The goal is to create a **controlled motif library**, not to reproduce an individual artwork.

## Position in Workflow

```text
Named Style Study
      ↓
Motif & Sign Extraction
      ↓
Reference Style Synthesis
      ↓
Visual DNA
      ↓
Instagram Template Synthesis
```

## What Must Be Extracted

### 1. Signs

Identify recurring symbolic signs such as:

- eyes
- spirals
- stars / rays
- arrows
- dots
- crosses
- ladders
- grids
- frames
- directional marks

Do not assume a sign is meaningful merely because it appears once. Record frequency and evidence.

### 2. Shapes

Identify recurring shape families:

- circles
- squares
- rectangles
- irregular blocks
- organic blobs
- simplified natural forms
- geometric fragments
- line-based shapes

Describe the formal behavior of each family rather than copying a particular instance.

### 3. Significant Objects

Identify recurring recognizable objects or object-like forms, for example:

- faces
- eyes
- birds
- houses
- plants
- architectural fragments
- ladders
- tools or everyday objects

Record whether the object is literal, simplified, symbolic, or abstracted.

### 4. Mark Types

Extract recurring mark behaviors:

- contour lines
- gestural lines
- sketch marks
- crosshatching / grids
- dots
- short strokes
- underlines
- framing marks
- directional strokes

Record stroke quality, irregularity, density, and relationship to surrounding forms.

### 5. Material Motifs

Identify repeated material behaviors that function as visual motifs:

- painted fields
- rough edges
- pigment variation
- translucent layers
- paper interruptions
- brush deposits
- worn or uneven areas

These are recorded as **material behaviors**, not as image filters.

## Extraction Method

For every candidate motif, record:

```text
MOTIF_ID
CATEGORY
NAME
DESCRIPTION
VISUAL_ATTRIBUTES
VARIANTS
FREQUENCY
REFERENCE_EVIDENCE
FORMAL_ROLE
SEMANTIC_ROLE_IF_SUPPORTED
EMOTIONAL_EFFECT_IF_SUPPORTED
MATERIAL_BEHAVIOR
TRANSFERABILITY
RISK_LEVEL
PROVENANCE
CONFIDENCE
```

## Frequency Rules

Classify each motif as:

- RECURRING — appears repeatedly across the reference set.
- OCCASIONAL — appears in several but not most references.
- UNIQUE — appears once or is strongly tied to a single artwork/reference.

A recurring motif may become candidate library material.

A unique motif must not automatically become a brand or template element.

## Fidelity Rule

The extraction should preserve the **formal character observed in the named style/reference**:

- proportions
- irregularity
- gesture
- simplicity
- edge behavior
- line quality
- material behavior
- relationship to surrounding space

However, extraction must describe the motif as a **generalized vocabulary item**, not reproduce a specific artwork or composition.

## Style vs. Brand Separation

The motif library represents **style evidence**.

It does not automatically become the English Beyond Language brand language.

Promotion happens only after:

```text
STYLE EVIDENCE
   ↓
REFERENCE SYNTHESIS
   ↓
BRAND RELEVANCE
   ↓
APPROVAL
   ↓
EBL MOTIF LIBRARY
```

## Instagram Translation Boundary

The motif extraction stage must not decide the final Instagram layout.

It may define:

- which motifs exist
- how they behave
- which are recurring
- which are safe to simplify
- which carry strong visual character

Instagram Template Synthesis decides:

- size
- placement
- hierarchy
- frequency per slide
- mobile readability
- template usage
- editable/controlled/locked behavior

## Required Output

```text
MOTIF_LIBRARY
SIGN_LIBRARY
SHAPE_LIBRARY
OBJECT_LIBRARY
MARK_LIBRARY
MATERIAL_LIBRARY
FREQUENCY_MAP
FORMAL_ATTRIBUTES
EMOTIONAL_ATTRIBUTES
TRANSFERABILITY_MAP
NON_TRANSFERABLE_ITEMS
INSTAGRAM_TRANSLATION_NOTES
PROVENANCE
CONFIDENCE
DECISION_GATE
```

## Decision Gate

PASS — recurring visual vocabulary is sufficiently extracted and evidence-backed.

CONDITIONAL — vocabulary is usable but some categories or frequencies remain uncertain.

BLOCKED — references are insufficient or the extraction would require unsupported invention.

## Non-Task

This step must not:

- reproduce an artwork
- copy a specific composition
- define final brand identity
- define final Instagram layout
- invent symbolic meaning without evidence
- promote every observed motif into the brand system
