# Tailwind CSS Typography — External Typography System Reference

## Source

- Repository: https://github.com/tailwindlabs/tailwindcss-typography
- Maintainer: Tailwind Labs
- Source type: official typography implementation reference
- Scope: long-form prose typography, type scale, readable line length, heading rhythm, semantic element styling, responsive typography, dark-mode inversion, and brand-aware prose theming

## Why this belongs in the knowledge base

Tailwind CSS Typography is useful as a practical implementation reference for readable long-form content. It formalizes typographic defaults across headings, paragraphs, lists, blockquotes, tables, figures, code, images, and other semantic HTML elements through a coherent prose system.

For Prompt-library, it should not be treated as a universal visual style. Its value is in the structural relationships it demonstrates: hierarchy, readable measure, type-scale relationships, spacing rhythm, semantic consistency, responsive scaling, and controlled customization.

## Transferable principles

### 1. Prose as a coordinated system

Typography should be evaluated as a system rather than as isolated font-size choices.

Useful variables include:
- body size
- heading scale
- heading/body contrast
- line height
- vertical rhythm
- paragraph spacing
- list rhythm
- blockquote treatment
- figure/caption hierarchy
- code/table readability

### 2. Context-dependent type scale

The reference provides multiple prose size tiers instead of assuming one scale fits every context.

Transferable principle:
- define typography tiers for compact, standard, large, and display-oriented reading contexts
- preserve proportional relationships when scaling the system

### 3. Readable content width

The typography system includes a maximum readable width for prose.

Transferable principle:
- treat line length/content measure as a typography variable
- do not optimize typography only by font size
- allow intentional overrides when prose is part of a larger grid

### 4. Responsive typography

Type scale can change by viewport while retaining the same semantic hierarchy.

Transferable principle:
- responsive typography should preserve hierarchy and reading rhythm, not simply shrink every value uniformly

### 5. Semantic element hierarchy

The system separately accounts for:
- h1–h4
- lead text
- paragraphs
- links
- strong/emphasis
- blockquotes
- lists
- definition lists
- tables
- captions
- code/preformatted blocks
- media
- horizontal rules

Transferable principle:
- typography QC should inspect semantic roles individually rather than checking only headings and body copy

### 6. Brand-aware customization

The prose system allows element-level and theme-level customization while preserving the underlying structural model.

Transferable principle:
- separate typographic structure from brand styling
- preserve hierarchy and rhythm while adapting color, font family, image treatment, links, headings, and accents to a project identity

### 7. Light/dark inversion

The implementation defines paired light and dark prose roles.

Transferable principle:
- contrast relationships should be tested as semantic role mappings across light and dark surfaces rather than inverted mechanically

## Suggested Prompt-library use

Primary consumers:
- VIS-005 — typography analysis
- VDNA-001 — typography-system synthesis
- ART-001 / ART-002 — typography direction and hierarchy
- GEN-001 / GEN-002 — implementation-aware layout generation
- QC-001 / QC-002 / QC-003 — readability, hierarchy, rhythm, and semantic consistency checks

Secondary consumers:
- RES-005 when researching practical digital typography systems
- FINAL-AI-001 / FINAL-AI-002 when validating long-form or editorial outputs

## Retrieval guidance

Use this reference when tasks involve:
- long-form readability
- prose hierarchy
- type scale
- heading rhythm
- line length
- semantic typography
- responsive typography
- editorial web typography
- dark-mode prose
- typography implementation
- readable Markdown/CMS output

Do not copy Tailwind's default visual appearance into a project unless explicitly appropriate. Extract structural and implementation principles first, then reconcile them with the project's own visual DNA, language requirements, font choices, and brand direction.

## Provenance note

This knowledge file summarizes Tailwind Labs' official typography plugin as an external implementation reference. The original repository remains the source of truth for its classes, defaults, and implementation details.
