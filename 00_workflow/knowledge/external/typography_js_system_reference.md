# Typography.js — External Typography System Reference

## Source

- Repository: https://github.com/KyleAMathews/typography.js
- Maintainer: Kyle Mathews
- Source type: external technical typography-system reference
- Scope: programmable typography systems, vertical rhythm, modular scale, theme configuration, reusable typography themes, generated CSS

## Why this belongs in the knowledge base

Typography.js treats typography as a coordinated system rather than a collection of isolated declarations. It is useful to the Prompt-library workflow because it formalizes relationships between base font size, line height, heading scale, vertical rhythm, font families, weights, colors, block spacing, and theme overrides.

This complements other typography sources already in the knowledge base:

- Tailwind Typography: practical prose defaults and readable content styling
- gftools / BySages Typography: font engineering and glyph-level tooling
- Typography.js: ratio-driven typography systems and reusable theme logic

## Key transferable principles

### 1. Typography is an interrelated system

A typographic change can affect many downstream relationships. Font size, heading scale, line height, block spacing, and rhythm should be coordinated rather than tuned independently.

### 2. Base metrics drive the system

Typography.js exposes a small set of high-leverage parameters such as:

- base font size
- base line height
- scale ratio
- heading font family
- body font family
- heading and body weights
- body and heading colors
- block spacing

These parameters can serve as high-level typography tokens in VDNA and art-direction stages.

### 3. Modular scale

The system uses a scale ratio to derive larger typographic sizes from the base size. This is useful when defining coherent heading hierarchies and avoiding arbitrary font-size choices.

### 4. Vertical rhythm

Block spacing is tied to rhythm units derived from line height. This creates a consistent vertical cadence across headings, paragraphs, blockquotes, lists, and other text elements.

Potential workflow use:
- VIS-005 typography analysis
- VDNA-001 typography-system synthesis
- ART-001 / ART-002 typography direction
- GEN-001 / GEN-002 implementation guidance
- QC-001 / QC-002 / QC-003 rhythm and hierarchy checks

### 5. Typography themes as reusable objects

Themes are represented as reusable configuration objects. This supports the idea that typography systems should be portable, shareable, version-controlled, and reusable across outputs.

Potential adaptation:
- define typography DNA as structured tokens
- save project typography systems as reusable data
- separate project-specific overrides from global typography logic

### 6. Controlled overrides

Typography.js supports systematic overrides instead of abandoning the underlying system. This is relevant for art-direction workflows where a strong base system should remain coherent while individual elements are customized.

### 7. Separation of intent from generated implementation

The user defines design intent through high-level configuration, while the engine expands that into many coordinated CSS rules. This is a valuable architectural model for AI-assisted design workflows: store intent and relationships rather than only final pixel values.

## Suggested consumers

Primary:
- RES-005
- VIS-005
- VDNA-001
- ART-001
- ART-002

Secondary:
- GEN-001
- GEN-002
- QC-001
- QC-002
- QC-003
- FINAL-AI-001
- FINAL-AI-002

## Retrieval guidance

Use this source when the task involves:

- typography system
- modular scale
- type scale
- vertical rhythm
- baseline rhythm
- heading/body relationships
- reusable typography themes
- typography tokens
- line-height systems
- programmatic typography
- coordinated text spacing

Do not treat Typography.js default values or bundled themes as project rules. Extract transferable principles and compare them against the active brand brief, typography references, and project Visual DNA.

## Provenance note

This file summarizes concepts from the external Typography.js repository for internal discovery and workflow reference. The upstream repository remains the source of provenance for implementation details and examples.
