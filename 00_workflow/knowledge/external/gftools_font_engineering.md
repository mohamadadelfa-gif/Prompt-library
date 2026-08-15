# gftools — External Font Engineering Reference

## Purpose

This record provides source-backed technical knowledge for inspecting, comparing, rendering, validating, and repairing font files when a workflow task has access to actual font binaries or a font-family repository.

It is an optional engineering reference, not a default runtime dependency and not a source of aesthetic, licensing, brand, or project decisions.

```text
KB_ID: GFTOOLS-SRC-001
KNOWLEDGE_TYPE: EXTERNAL_TECHNICAL_SOURCE
AUTHOR / CREATOR: Google Fonts contributors
TITLE: Google Fonts Tools (gftools)
PUBLISHER / INSTITUTION: Google Fonts
SOURCE_FORMAT: Public source-code repository and project documentation
SOURCE_ID: GFTOOLS-SRC-001
STATUS: SOURCE_FACT / SOURCE_DERIVED
SCOPE: SYSTEM_FONT_ENGINEERING_REFERENCE
AUTHORITY: HIGH — official upstream repository and package metadata
APPROVAL_STATUS: ACTIVE_SOURCE
PROVENANCE: https://github.com/googlefonts/gftools and its main-branch README.md and pyproject.toml, reviewed 2026-08-15.
```

## Source-Supported Capabilities

The upstream project describes gftools as command-line tooling for testing font projects and working with the Google Fonts collection. Relevant capabilities include:

- comparing font binaries;
- inspecting font names, weights, widths, subsets, language support, OpenType features, bounding boxes, versions, and variable-font data;
- rendering text for visual inspection;
- running family QA, including optional FontBakery-based checks;
- checking or repairing metadata, hinting, vertical metrics, name tables, mappings, and selected OpenType fields;
- generating static instances and selected font metadata;
- packaging work intended for the `google/fonts` repository.

The current upstream package metadata on the reviewed main branch requires Python 3.10 or later. Treat upstream `pyproject.toml` as authoritative when older README installation text conflicts with package metadata.

## Permitted Workflow Use

Use this reference only when the task includes real `.ttf`, `.otf`, variable-font, UFO, Glyphs, or font-family project files and technical evidence would materially improve the result.

### VIS-005 — Typography & Graphic Language

gftools may supplement visual observation with technical evidence such as font metadata, supported axes, instances, features, subsets, and reproducible render comparisons. Tool output must be cited as machine-derived evidence. It does not by itself prove that a font visible in a raster reference is the same font.

### QC-001 — Generated Image Evaluation

Use gftools only for separately supplied or reconstructed font files. It cannot validate rasterized or AI-generated letterforms as a working font, and it does not replace visual typography QC.

### Editable Reconstruction / Production

When a candidate font file is supplied, gftools may help verify internal naming, style/weight metadata, variable axes, supported characters, metrics, and render behavior before a live-text handoff. Record the exact file, command, tool version, output, and interpretation.

## Decision Rules

1. **No font binary, no gftools claim.** Do not infer technical font properties from a screenshot alone.
2. **Evidence, not identity proof.** Matching metadata or a similar render supports a candidate identification but does not establish identity without adequate provenance and comparison evidence.
3. **No silent repair.** Inspection is read-only by default. Any command that modifies or emits a repaired font requires explicit production scope, a new output file, provenance, and human review.
4. **No aesthetic authority.** Passing technical checks does not make a typeface appropriate for the brand, concept, hierarchy, or audience.
5. **No licensing inference.** Repository or font metadata is not a substitute for reviewing the actual font license and distribution rights.
6. **No automatic dependency.** Do not add gftools to the base project requirements merely to make this knowledge available. Install it in an isolated environment only when an authorized task needs executable font QA.
7. **Version-sensitive commands.** Confirm command availability and options against the installed version or current upstream documentation before execution.

## Installation Guidance When Execution Is Authorized

Prefer an isolated Python environment and record the installed version.

```text
python -m pip install gftools
python -m pip install "gftools[qa]"   # only when the extended QA stack is required
```

Some QA or rendering features have platform-specific system dependencies. Installation success does not guarantee that every optional command is available.

## Example Evidence Routes

These are capability examples, not commands that must run in every typography task:

```text
gftools compare-font font1.ttf font2.ttf
gftools varfont-info family-variable.ttf
gftools find-features family.ttf
gftools lang-support family.ttf
gftools render-text ...
gftools qa ...
```

Before use, inspect `gftools --help` and the relevant subcommand help for the installed version.

## Unknowns and Limits

- Upstream commands, dependencies, and minimum Python versions may change.
- Some Google Fonts publishing workflows are irrelevant to general design production.
- Font QA cannot determine whether rendered typography matches an approved raster composition without a separate overlay or visual comparison.
- Raster text may be modified, outlined, composited, or generated and therefore may not map cleanly to any font binary.
- Exact typeface identification may remain `TYPOGRAPHY_REVIEW_REQUIRED` even after technical comparison.

## Project-Use Caution

This source is registered as `ACTIVE_SOURCE` but remains `NOT_PROMOTED`. It may inform technical inspection and QC; it must not become an EBL rule, a typography selection, or a required production dependency without an explicit project decision.
