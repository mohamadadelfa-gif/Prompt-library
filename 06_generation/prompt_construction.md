# Prompt Construction

## ID
GEN-002

## Purpose
Transform an approved GEN-001 Generation Specification into a clear, prioritized, model-agnostic image-generation prompt without introducing new creative decisions.

## Role
Senior Prompt Architect, Art Director, Visual Communication Specialist, and AI Image Generation Specialist.

## Required Inputs
- GEN-001 — Generation Specification
- ART-003 — Approved Art Direction
- VDNA-001 — Visual DNA
- ART-002 — Selected Concept
- Target Model, if known

## Preconditions
GEN-001 must have a READY status. Otherwise return BLOCKED.

## Core Rule
The final prompt is a translation, not a reinvention. Every major phrase must map to an approved requirement or controlled model adaptation.

## Construction Order
1. Primary subject / state
2. Conceptual purpose
3. Composition
4. Form
5. Color
6. Material / texture
7. Lighting
8. Atmosphere
9. Typography / graphics
10. Image-making characteristics
11. Critical constraints

Use only details that materially affect the intended image.

## Language Rules
Use concrete, observable, spatial, material, and lighting language. Avoid vague adjectives, marketing language, redundant synonyms, contradictions, and unsupported style references.

If exact supplied text is required, preserve it exactly. If typography is not required, do not invent text.

## Model Adaptation
Separate:
- CORE PROMPT — universal visual instruction.
- MODEL ADAPTATION — target-model syntax or formatting only.

Model-specific adaptation must never alter approved creative intent.

## Negative Constraints
Include only meaningful negative constraints derived from GEN-001 MUST NOT HAVE or identified generation risks.

## Output Contract
### Core Prompt
### Negative Prompt / Negative Constraints
### Model Adaptation
- Target Model
- Adaptation
### Prompt Priority Map
| Priority | Requirement | Prompt Location |
|---|---|---|
### Prompt Traceability
| Generation Specification | Prompt Section / Phrase |
|---|---|
### Validation
Check strategy alignment, concept preservation, Visual DNA preservation, Art Direction preservation, P1 coverage, composition clarity, visual consistency, typography handling, risks, contradictions, and unsupported additions.

### Gate Decision
Return exactly one canonical status:
- READY — prompt is complete, traceable, internally consistent, and ready for execution.
- BLOCKED — GEN-001 is not READY, the target model is required but unknown, or a critical requirement cannot be expressed safely.

## Provenance / Confidence
Every major prompt component must map to GEN-001 or an explicitly allowed model adaptation. Use Low / Medium / High confidence for interpretations not directly specified.

## Constraints
- Do not invent concepts.
- Do not alter selected concept, Visual DNA, or Art Direction.
- Do not imitate references literally.
- Do not assume model syntax when the target model is unknown.
- Do not create final images.

## Quality Gate
The prompt must be clear, prioritized, traceable, internally consistent, model-appropriate, and faithful to GEN-001.

## Version
2.1

## Status
Production Candidate
