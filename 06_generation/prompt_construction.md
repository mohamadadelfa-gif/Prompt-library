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

GEN-001 must state **READY FOR GEN-002**. Otherwise return **DO NOT PROCEED**.

## Core Rule
The final prompt is a translation, not a reinvention. Every major phrase must map to an approved requirement or controlled model adaptation.

## Construction Order
Use the highest-value order appropriate to the target model:
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

Do not include irrelevant details merely to increase prompt length.

## Language Rules
Use concrete, observable, spatial, material, and lighting language. Avoid vague adjectives, marketing language, redundant synonyms, contradictions, and unsupported style references.

If exact supplied text is required, preserve it exactly. If typography is not required, do not invent text.

## Model Adaptation
Separate:
- **CORE PROMPT** — universal visual instruction.
- **MODEL ADAPTATION** — target-model syntax or formatting only.

Model-specific adaptation must never alter the approved creative intent.

## Negative Constraints
Include only meaningful negative constraints derived from GEN-001 MUST NOT HAVE or identified generation risks. Do not create generic negative lists.

## Output
# FINAL GENERATION PROMPT

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
Check:
- Strategy alignment
- Concept preservation
- Visual DNA preservation
- Art Direction preservation
- All P1 requirements represented
- Composition clarity
- Color / shape / texture consistency
- Typography handling
- Major risks addressed
- No contradictions
- No unsupported creative additions
- Prompt is no longer than necessary

### Readiness
State **READY FOR GENERATION** or **DO NOT PROCEED**, with reasons.

## Constraints
- Do not invent concepts.
- Do not alter selected concept, Visual DNA, or Art Direction.
- Do not imitate references literally.
- Do not assume model syntax when the target model is unknown.
- Do not create final images.

## Quality Gate
The prompt must be clear, prioritized, traceable, internally consistent, model-appropriate, and faithful to GEN-001.

## Version
2.0

## Status
Testing
