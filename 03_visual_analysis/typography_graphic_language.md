# Typography & Graphic Language Analysis

## ID
VIS-005

## Purpose
Analyze the typographic and graphic language of selected visual references and extract transferable principles for Visual DNA.

## Role
Senior Art Director, Typography Specialist, Graphic Designer, and Visual Analyst.

## Required Inputs
- STR-005 — Project Reconciliation
- RES-005 — Visual Reference Research
- RES-006 — Research Synthesis
- Selected visual references approved for analysis
- VIS-001 — Composition Analysis
- VIS-002 — Color Analysis
- VIS-003 — Shape & Form Analysis
- VIS-004 — Texture & Material Analysis

## Task Boundary
Analyze typography as visual form and graphic systems. Do not select a final font, create a final identity, or copy lettering literally.

## Method
Analyze typographic presence, category, letterform and stroke characteristics, weight, width, contrast, case, spacing, alignment, scale, hierarchy, density, text-to-image/shape relationships, placement, transformation, graphic symbols/marks, borders, lines, grids, icons, and decorative elements.

Distinguish exact font identification from typographic character analysis. Claim an exact family only with sufficient evidence.

When actual font binaries are supplied and technical inspection is relevant, retrieve `GFTOOLS-SRC-001` from the knowledge registry. Treat command output as supplemental machine-derived evidence; never use it to infer a font file from raster appearance alone.

When specialist typography terminology, specifications, or tooling sources are needed, `TYPO-INDEX-001` may be used for discovery. Follow and verify the primary source before relying on a listed resource; cite that primary source in the analysis.

For Persian/Farsi or bilingual Persian/Latin work, `FA-FONT-INDEX-001` may be used to discover candidates. Analyze only verified specimens or font files and explicitly test Persian-specific coverage, RTL shaping, joining, punctuation, numerals, mixed-script behavior, and zero-width non-joiner behavior as applicable.

`FA-FONT-COLLECTION-001` provides a focused Farsi Font Store route. For any candidate from it, record repository status (canonical, fork, modified distribution, mirror, or package), actual license evidence, font version/provenance, and the specimen or binary used for analysis.

Use `FA-RESOURCE-INDEX-001` only when broader Persian-language production behavior is material to the analysis, such as RTL layout, Unicode normalization, Persian numerals, localization, interface conventions, or web delivery. Verify the linked primary source and test critical behavior in the target environment.

## Output Contract
### Reference Analysis
- Typographic Presence / Category
- Letterform / Stroke Characteristics
- Weight / Width / Contrast
- Case / Spacing / Alignment
- Scale / Hierarchy / Density
- Placement / Distortion / Layering
- Typography as Form
- Relationship to Composition / Shape / Color
- Graphic Elements / Graphic Grammar

### Comparative Analysis
- Recurring Typographic Principles
- Shared Graphic Principles
- Major Differences
- Complementary Characteristics
- Contradictions
- Unique Characteristics

### Extracted Typography DNA
Describe reusable typographic and graphic principles, not a final font selection.

### Provenance / Confidence
Every major typography or graphic finding must cite a source reference/observation and use Low / Medium / High confidence where interpretation is involved.

### Gate Decision
Return exactly one canonical status:
- PASS
- CONDITIONAL
- BLOCKED

BLOCKED when required references or evidence are insufficient.

## Handoff
Pass the Typography/Graphic Analysis package to VDNA-001 with source IDs, observations, derived principles, unknowns, and blockers.

## Constraints
- Do not claim exact font family without evidence.
- Do not treat font metadata, filename, or a passing technical check as sufficient identity, licensing, or aesthetic evidence.
- Do not treat inclusion in a curated resource list as proof of authority, maintenance, safety, compatibility, licensing, or project suitability.
- Do not treat generic Arabic-script support or a `persian-font` topic tag as proof of correct Persian/Farsi coverage or shaping.
- Do not treat membership in a font-store organization, a GitHub license badge, or an open-source description as sufficient provenance or permission to use a font asset.
- Do not treat a Persian-resource list entry as evidence that a linked library, framework, font, or service is current, secure, licensed, accessible, or correct for Persian text.
- Do not reproduce specific lettering literally.
- Do not focus only on readability.
- Distinguish typography from general graphic shape language.
- Use precise explanations of perceived character.

## Quality Gate
The analysis must be typographically precise, visually analytical, contextual, comparative, transferable, and useful for Visual DNA extraction.

## Version
2.0

## Status
Production Candidate
