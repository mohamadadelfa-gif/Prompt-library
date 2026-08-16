# BySages Typography — External Typography Engineering Reference

## Source

- Repository: https://github.com/bysages/typography
- Maintainer: By Sages
- License: MIT
- Source type: external technical typography engineering toolkit
- Scope: Unicode confusable detection, OCR abstraction, font parsing, glyph creation/manipulation, font generation, and glyph rendering

## Why this belongs in the knowledge base

This source complements visual-typography and font-engineering references by covering text integrity and glyph-level operations. It is useful when typography work must move beyond font choice and layout into Unicode normalization, OCR ingestion, glyph inspection, custom font generation, or machine-readable font manipulation.

It should not be treated as an art-direction or typographic-style source. Its value is operational and technical.

## Main knowledge areas

### 1. Unicode confusable detection

The `unconfusables` package provides methods for detecting characters that look similar, normalizing strings, and checking whether two strings are visually confusable.

Potential workflow use:
- text-integrity QC
- detecting deceptive or accidental look-alike characters
- multilingual typography validation
- OCR cleanup
- preventing character substitution errors in brand names, captions, and publication copy

### 2. OCR abstraction

The `unocr` package provides a unified OCR layer with support for multiple drivers, including Tesseract.js and AI-based models.

Potential workflow use:
- extracting text from visual references
- recovering typography content from screenshots or scans
- reference-analysis preprocessing
- comparing source text against generated output

OCR results should be verified before being treated as authoritative source text.

### 3. Font parsing and glyph inspection

The `unglyph` package supports parsing font files and exposing font and glyph data programmatically.

Potential workflow use:
- technical font inspection
- glyph inventory checks
- Unicode coverage analysis
- custom-font research
- font QC alongside gftools-derived practices

### 4. Glyph creation and manipulation

The toolkit can create and modify glyph definitions, including Unicode mapping, advance width, paths, and glyph metadata.

Potential workflow use:
- experimental/custom typography
- logo or display-glyph prototyping
- checking how typographic forms are structurally represented
- generating controlled test glyphs

This capability should not imply that modifying a licensed font is permitted. Font licenses must be checked independently.

### 5. Font generation and SVG glyph rendering

The toolkit can generate font data and render glyphs to SVG.

Potential workflow use:
- visual glyph inspection
- automated comparison artifacts
- font-generation experiments
- typography QA outputs

## Relationship to existing Prompt-library sources

### gftools

`gftools` remains the stronger source for production-oriented font engineering, validation, metadata, and Google Fonts workflows.

BySages Typography adds:
- Unicode confusable detection
- OCR integration
- programmatic glyph creation/manipulation
- lightweight glyph rendering

### Tailwind CSS Typography

Tailwind Typography concerns readable prose hierarchy and layout implementation.

BySages Typography concerns the underlying characters, OCR text, font files, and glyph structures. These sources therefore serve different layers and should not be merged conceptually.

## Suggested consumers

Primary:
- RES-005 — typography/font research
- VIS-005 — typography analysis
- QC-001 — technical typography/text-integrity QC

Secondary:
- GEN-001 / GEN-002 when custom glyph or programmatic font operations are explicitly required
- FINAL-AI-001 / FINAL-AI-002 when final-output text integrity needs machine checks

## Retrieval guidance

Use this source when the task includes:

- Unicode confusables
- visually similar characters
- text normalization
- OCR
- extracting text from images
- glyph inspection
- font parsing
- custom glyph creation
- font generation
- glyph SVG rendering
- character-level typography QC

Do not use it as evidence for choosing a visual style, font pairing, type hierarchy, or brand voice.

## Provenance note

This file summarizes the external repository for technical discovery. The original repository remains the provenance source for implementation details and APIs.
