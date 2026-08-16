# CardPrinter — External Technical Production & QC Reference

## Source

- Repository: https://github.com/gongnyang/cardprinter
- Maintainer: gongnyang
- License: MIT
- Source type: open-source automated social-content production pipeline
- Scope: Instagram carousel generation, Reels generation, design tokens, copy contracts, rendering, measurable QC gates, fact-fidelity checks, safe-zone enforcement, typography floors, layout-diversity checks, and automated regeneration

## Why this belongs in the knowledge base

CardPrinter is directly relevant to the Prompt-library content-automation workflow because it demonstrates a production architecture that converts a topic into multiple social formats while enforcing measurable quality gates.

Its strongest value is not its visual style. Its value is its system logic:

- one source contract driving multiple output formats
- deterministic production stages
- explicit pass/fail gates
- automated regeneration when a gate fails
- separation of content, tokens, layout, rendering, and QC
- machine-checkable constraints rather than subjective quality claims

Treat this repository as a technical workflow and QC reference, not as an authoritative visual-design rule.

## Core architecture

Conceptual pipeline:

`topic → brief → copy → tokens → gates → images/layout → rendered carousel → gates → Reels → gates`

This pattern is useful for designing Prompt-library orchestration because each stage has a defined artifact and each artifact can be checked before downstream production continues.

## Transferable principles

### 1. Shared content contract

Carousel and Reels outputs should derive from the same approved content/copy contract so wording, claims, hierarchy, and narrative sequence do not drift between formats.

Potential use:
- GEN-001 / GEN-002
- FINAL-AI-001 / FINAL-AI-002
- cross-format consistency QC

### 2. Hard quality gates

CardPrinter uses explicit gates instead of treating QC as informal review.

Relevant gate categories include:
- contrast / readability
- overflow and safe-zone containment
- typography minimums
- fact fidelity
- chart integrity
- layout diversity
- output-spec compliance

Potential use:
- QC-001 / QC-002 / QC-003
- automated preflight checks
- machine-readable PASS / FAIL logic

### 3. Safe-zone and bounding-box validation

Visual elements should remain within output-specific safe regions and should not overflow their intended containers.

Potential use:
- Instagram Story / Carousel / Reels layouts
- ART and GEN stages
- final-output QC

### 4. Typography floor

Typography should have minimum readable-size thresholds rather than relying only on aesthetic judgment.

Potential use:
- VIS-005
- GEN-001 / GEN-002
- QC-001

This principle should be adapted to the project's audience, format, script, and viewing conditions instead of copying CardPrinter's exact values blindly.

### 5. Fact-fidelity gate

Generated content should not introduce unsupported figures or numerical claims. Facts and displayed values must remain traceable to approved source material.

Potential use:
- research-derived social posts
- data graphics
- educational content
- QC-002 / QC-003

### 6. Honest data visualization

Charts should preserve numerical truth and avoid visual exaggeration.

Potential use:
- data-driven posts
- infographic QC
- visual-veracity rules

### 7. Self-healing production loop

When an output fails a machine-checkable gate, the failure reason can be returned to the generation stage for controlled regeneration.

Conceptual loop:

`generate → validate → FAIL → structured correction instruction → regenerate → validate`

Potential use:
- future Prompt-library automation
- batch generation
- QC-driven revision

Important: cap retries and surface unresolved failures rather than hiding them.

### 8. Stage separation

Brief, copy, design tokens, layout, render, and QC should exist as distinct artifacts/stages rather than one monolithic generation prompt.

Potential use:
- workflow architecture
- prompt chaining
- debugging
- provenance tracking

### 9. Output-derived motion

Motion/video outputs can be derived from already-approved static cards rather than generated independently, reducing brand and content drift.

Potential use:
- carousel → Reels adaptation
- social-content repurposing
- FINAL-AI stages

## Relevance to Prompt-library

Primary consumers:
- GEN-001
- GEN-002
- QC-001
- QC-002
- QC-003
- FINAL-AI-001
- FINAL-AI-002

Secondary consumers:
- VIS-005 — typography/readability constraints
- ART-002 / ART-003 — layout-system and production constraints
- STR / RES stages when defining automation requirements

## Retrieval guidance

Retrieve this source when the workflow task concerns:

- automated Instagram production
- carousel generation
- Reels generation
- batch content production
- design tokens
- safe zones
- layout overflow
- typography minimums
- contrast validation
- fact fidelity
- data visualization integrity
- automated QC
- hard quality gates
- retry / regeneration loops
- self-healing pipelines
- multi-format consistency

## Adoption rule

Do not copy the implementation or thresholds automatically.

For each candidate principle:

1. identify the underlying production or QC concept;
2. compare it against Prompt-library architecture and project needs;
3. convert it into an explicit workflow rule only after testing;
4. keep project-specific visual decisions separate from technical QC rules.

## Provenance note

This file summarizes transferable workflow and QC concepts from the CardPrinter repository. The original repository remains the provenance source for its implementation, documentation, scripts, gates, and code.
