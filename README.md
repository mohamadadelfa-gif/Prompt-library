# Prompt Library v2

A version-controlled library of prompts for creative strategy, visual research, art direction, AI generation, and quality control.

## Workflow

Customer Information → Strategy → Research → Visual Analysis → Visual DNA → Art Direction → Generation → Quality Control

## Categories

### 01 — Strategy
- STR-001 — Customer Analysis
- STR-002 — Brief Analysis
- STR-003 — Requirement Extraction
- STR-004 — Clarification Questions
- STR-005 — Project Reconciliation

### 02 — Research
- RES-001 — Research Strategy
- RES-002 — Audience Research
- RES-003 — Competitor & Market Research
- RES-004 — Cultural & Context Research
- RES-005 — Visual Reference Research
- RES-006 — Research Synthesis

### 03 — Visual Analysis
- VIS-001 — Composition Analysis
- VIS-002 — Color Analysis
- VIS-003 — Shape & Form Analysis
- VIS-004 — Texture & Material Analysis
- VIS-005 — Typography & Graphic Language
- VIS-006 — Lighting, Mood & Atmosphere Analysis

### 04 — Visual DNA
- VDNA-001 — Visual DNA Extraction & Synthesis

### 05 — Art Direction
- ART-001 — Creative Concept Generation
- ART-002 — Concept Evaluation & Selection
- ART-003 — Art Direction Development

### 06 — Generation
- GEN-001 — Generation Specification
- GEN-002 — Prompt Construction

### 07 — Quality Control
- QC-001 — Generated Image Evaluation
- QC-002 — Revision Strategy

## v2 Execution Contract

Every prompt must define:

1. **Input Contract** — required inputs and missing-input behavior.
2. **Transformation Boundary** — what the prompt may infer, transform, or decide.
3. **Output Contract** — structured outputs required by downstream stages.
4. **Provenance** — source of important claims, requirements, and decisions.
5. **Confidence** — uncertainty must remain explicit.
6. **Handoff** — unresolved items and approved outputs passed to the next stage.

Downstream prompts must not silently rewrite upstream facts, requirements, research findings, Visual DNA, or approved Art Direction.

## Evidence Rules

Use these labels where relevant:

- Confirmed / Fact
- Observation
- Interpretation
- Hypothesis
- Assumption
- Unknown
- Unresolved

Never promote an inference to a confirmed requirement without evidence.

## Decision Gates

A stage may proceed only when its required inputs exist and no unresolved critical dependency blocks the next stage. If a critical dependency is unresolved, explicitly return **DO NOT PROCEED** or **PROCEED WITH CONDITIONS**.

## Versioning

`2.0` = structural revision
`2.1` = minor improvement

## Status

Testing

## Core Principle

**Analyze → Structure → Research → Synthesize → Direct → Generate → Evaluate**
