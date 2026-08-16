# React Native Typography — External Technical Reference

## Source

- Repository: https://github.com/hectahertz/react-native-typography
- Maintainer: hectahertz
- License: MIT
- Source type: cross-platform typography implementation reference
- Scope: native-looking text systems for React Native across iOS, Android, and web

## Why this belongs in the knowledge base

This source contributes platform-aware typography engineering rather than visual style direction. It is useful when the workflow needs to translate a type system into mobile or cross-platform interfaces while preserving native conventions, weight behavior, spacing, script support, and accessibility-sensitive defaults.

It complements the existing typography sources by focusing specifically on implementation differences between iOS, Android, and web.

## Transferable principles

### 1. Platform-aware type systems

The repository exposes predefined typography collections aligned with major native design conventions such as Material Design, Apple Human Interface Guidelines, and iOS UIKit.

Potential workflow use:
- compare platform-specific hierarchy systems
- map design tokens to native mobile contexts
- prevent one-size-fits-all typography implementation

### 2. Weight normalization across platforms

React Native font weight behavior can differ by platform and typeface. The project uses helpers to normalize visually comparable weights across native system fonts.

Potential workflow use:
- implementation QC
- cross-platform consistency
- weight token translation

### 3. Kerning and letter-spacing adaptation

The source documents the mismatch between native kerning behavior and React Native letter-spacing controls, including helpers for San Francisco spacing.

Potential workflow use:
- typography fidelity checks
- mobile implementation notes
- spacing token conversion

### 4. Native defaults and accessibility-aware behavior

The project favors native platform typefaces where appropriate so typography works naturally with each operating system and its accessibility conventions.

Potential workflow use:
- mobile accessibility review
- native-feeling UI implementation
- fallback strategy design

### 5. Dense and tall script support

The repository explicitly supports dense/tall scripts and demonstrates CJK-oriented typography handling.

Potential workflow use:
- multilingual typography QC
- script-specific line-height and density review
- preventing Latin-only assumptions

### 6. Extendable typography objects

Typography styles are exposed both as StyleSheets and plain objects, making them reusable and overridable without forcing component-level abstraction.

Potential workflow use:
- design-token implementation
- reusable typography primitives
- modular style systems

## Suggested consumers in Prompt-library

Primary:
- RES-005 — typography research
- VIS-005 — typography analysis
- VDNA-001 — typography system synthesis
- GEN-001 / GEN-002 — implementation-aware generation
- QC-001 / QC-002 / QC-003 — typography consistency and cross-platform checks

Secondary:
- ART-001 / ART-002 when mobile-native typography constraints affect art direction
- FINAL-AI-001 / FINAL-AI-002 when final output targets React Native or cross-platform UI

## Retrieval guidance

Use this source when a task involves:

- React Native typography
- iOS / Android typography differences
- native mobile type hierarchy
- system font weights
- San Francisco / Roboto handling
- letter spacing / kerning conversion
- cross-platform font consistency
- dense or tall scripts
- multilingual mobile typography
- mobile text accessibility

Do not use this source as a universal visual-style authority. Platform presets should be treated as implementation references and compared against the current project's visual DNA and product context.

## Provenance note

This file summarizes transferable implementation concepts from the external repository. The original repository remains the source of provenance for its code, examples, and platform-specific details.
