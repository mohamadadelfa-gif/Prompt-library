# Design DNA Agent Method — External Methodology Reference

## Source

- Repository: https://github.com/zanwei/design-dna
- Maintainer: zanwei
- License: MIT
- Source type: external methodology / agent-skill reference
- Core purpose: extract, structure, and reapply visual identity as machine-readable Design DNA

## Why this belongs in the knowledge base

This repository is directly relevant to the Prompt-library visual workflow because it formalizes a repeatable bridge from visual references to structured design knowledge and then from structured design knowledge to generated output.

Its core model separates visual identity into three coordinated dimensions:

1. **Design System** — measurable tokens and structural rules
2. **Design Style** — qualitative visual character and perception
3. **Visual Effects** — advanced rendering and interaction behavior

This makes it useful as a methodology reference for improving the transition from VIS analysis into VDNA synthesis, ART direction, generation, and QC.

It should remain an external methodology source rather than an automatic system rule. Its schema can inspire and benchmark Prompt-library outputs, but fields should only be adopted where they improve the existing workflow and fit the project medium.

## Core workflow pattern

The repository defines a three-phase process:

### 1. Structure

Surface the full Design DNA schema and field meanings before analysis.

Transferable principle:
- define the target schema before extraction
- prevent arbitrary analysis categories
- maintain consistent output across projects

### 2. Analyze

Convert screenshots, images, or URLs into a complete structured profile.

Transferable principle:
- separate direct observation from estimated values
- quantify measurable properties when possible
- record conflicts between references instead of silently averaging them
- preserve source references and provenance

### 3. Generate

Use Design DNA plus new content to produce an implementation that retains the extracted visual language.

Transferable principle:
- treat Design DNA as a reusable intermediate artifact
- keep content independent from visual-system specification
- support Analyze → Generate chaining
- version and refine the DNA instead of repeatedly restarting from references

## Three-dimensional Design DNA model

### Dimension A — Design System

Measurable and structural properties, including:

- color palette and semantic roles
- typography scale, weight, line height, tracking, font roles
- spacing base unit, scale, density, section rhythm
- layout grid, columns, gutters, breakpoints, alignment tendency
- shape and border-radius system
- elevation and depth cues
- iconography
- motion timing and easing
- component patterns

### Dimension B — Design Style

Qualitative and perceptual properties, including:

- mood
- visual metaphor
- era influence
- genre
- personality traits
- complexity
- ornamentation
- whitespace behavior
- visual-weight distribution
- focal strategy
- hierarchy method
- balance type
- flow direction
- grouping strategy
- imagery treatment
- interaction feel
- brand voice in UI

### Dimension C — Visual Effects

Advanced visual behavior and rendering, including:

- animated backgrounds
- particles
- 3D elements
- shaders
- parallax and scroll-triggered motion
- animated text
- cursor effects
- image distortion/reveal effects
- glassmorphism / neumorphism
- canvas drawings
- SVG animation
- performance and fallback strategy

## High-value concepts for Prompt-library

### Machine-readable visual identity

The most important transferable concept is that visual identity should not end as prose alone. It can be represented as a structured, portable specification that downstream prompts and tools can consume.

### Separation of structural and perceptual evidence

Do not collapse measurable values and subjective interpretation into one category.

Example:
- `font_size: 64px` is structural evidence
- `editorial / authoritative / restrained` is perceptual evidence

### Portable intermediate artifact

Design DNA should function as an intermediate artifact between analysis and generation:

`References → VIS analysis → Design DNA → ART direction → Generation → QC`

This reduces repeated interpretation and creates a stable handoff between workflow stages.

### Conflict-aware synthesis

When multiple references disagree, record:
- dominant pattern
- secondary variant
- conflict
- confidence

Do not erase disagreement through naive averaging.

### Refinement loop

A generated result can be audited against the original references for:
- hierarchy
- ornamentation
- typographic rhythm
- motion
- materiality
- overall visual richness

The audit findings can then be merged back into the Design DNA or implementation.

## Suggested consumers in Prompt-library

Primary:
- VIS-001 — composition analysis
- VIS-002 — color analysis
- VIS-003 — shape analysis
- VIS-004 — texture / material analysis
- VIS-005 — typography analysis
- VIS-006 — lighting / effect analysis
- VDNA-001 — Visual DNA synthesis
- ART-001 / ART-002 / ART-003 — art-direction translation
- GEN-001 / GEN-002 — generation using structured identity
- QC-001 / QC-002 / QC-003 — reference-faithfulness and consistency checks

Secondary:
- FINAL-AI-001 / FINAL-AI-002 when validating whether final outputs preserve the intended visual language

## Retrieval guidance

Use this source when the task involves:

- Visual DNA
- Design DNA
- machine-readable visual identity
- structured visual analysis
- design tokens
- qualitative visual style
- reference-to-generation workflow
- visual identity transfer
- visual consistency
- structured style schema
- design-system extraction
- reference-faithfulness audit

## Adoption rule

Do not replace the current Prompt-library Visual DNA framework wholesale with the repository schema.

Instead:
1. compare its fields with existing VIS and VDNA prompts;
2. identify missing or stronger categories;
3. test those categories during the existing prompt-testing cycle;
4. promote only validated improvements into system prompts after human review.

## Provenance note

This file summarizes the methodology exposed by `zanwei/design-dna`, particularly its README and Design DNA schema. The original repository remains the authoritative source for its implementation and field definitions.
