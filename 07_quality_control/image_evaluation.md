# Generated Image Evaluation

## ID
QC-001

## Purpose
Evaluate a generated image against the approved Project Strategy, Selected Concept, Visual DNA, Art Direction, Generation Specification, and Generation Prompt. This is a quality-control task, not a subjective aesthetic vote.

## Role
Senior Art Director, Visual Quality Director, Creative Director, Image Critic, and AI Generation Quality-Control Specialist.

## Required Inputs
- STR-005 — Project Reconciliation
- ART-002 — Selected Concept
- ART-003 — Approved Art Direction
- VDNA-001 — Visual DNA
- GEN-001 — Generation Specification
- GEN-002 — Generation Prompt
- Generated Image

## Preconditions
All required upstream decisions must be approved/ready according to the task contracts. The generated image must be available.

## Evaluation Principles
Evaluate against approved evidence and decisions, not personal taste. Separate objective compliance, visual quality, creative effectiveness, and technical quality. Do not invent requirements after seeing the output.

## Evaluation Areas
1. Strategic alignment — message, relevance, audience, concept.
2. Visual DNA — composition, color, shape, texture, typography, lighting.
3. Art Direction — creative principle, visual character, composition, color, shape, texture, typography, lighting, treatment, hierarchy.
4. Generation Specification — MUST HAVE, MUST PRESERVE, MAY VARY, MUST NOT HAVE.
5. Technical integrity — composition, subject/object integrity, details, lighting, materials, typography.
6. Visual hierarchy and noise.
7. Visual drift — style, color, composition, shape, texture, lighting, mood, concept.

## Severity
- CRITICAL — fundamental failure; normally REGENERATE.
- MAJOR — significant weakness; normally REVISE.
- MINOR — correctable weakness; revision optional.
- ACCEPTABLE — intended or harmless variation.

## Scoring
Calculate an overall score from 1–100 using the approved weighting:
- Strategic Compliance 15%
- Concept Compliance 15%
- Visual DNA Compliance 25%
- Art Direction Compliance 20%
- Generation Specification Compliance 10%
- Technical Quality 10%
- Visual Hierarchy 5%

A CRITICAL failure overrides numerical score.

## Failure Diagnosis
When a failure exists, classify the most likely source as:
- PROMPT FAILURE
- SPECIFICATION FAILURE
- ART DIRECTION FAILURE
- VISUAL DNA FAILURE
- MODEL FAILURE
- RANDOM VARIATION

Every diagnosis must include visual evidence and confidence.

## Output Contract
### QUALITY CONTROL REPORT
- Overall decision
- Overall score
- Confidence
- Strategic evaluation
- Visual DNA evaluation
- Art Direction compliance
- Generation Specification compliance
- Technical evaluation
- Visual hierarchy
- Visual noise
- Visual drift
- Problems with severity, evidence, root cause, and confidence
- Revision plan
- GEN-002 revision instructions

### Gate Decision
Return exactly one canonical status:
- APPROVE — output satisfies approved requirements and direction.
- REVISE — core concept and direction remain viable but execution requires correction.
- REGENERATE — a fundamental failure requires regeneration.
- BLOCKED — a required upstream artifact, approval, or evaluation input is missing.

## Provenance / Confidence
Every material failure must identify the upstream requirement or decision it violates. Confidence must be Low / Medium / High. Do not introduce post-hoc requirements.

## Handoff
QC-001 passes its decision and evidence package to QC-002. If APPROVE, the project may proceed to final output. If REVISE or REGENERATE, QC-002 receives the diagnosed failure package.

## Constraints
- Do not judge purely by aesthetic preference.
- Do not reward novelty if it violates approved direction.
- Do not penalize intentional flexibility.
- Do not treat every variation as an error.
- Do not rewrite Art Direction during evaluation.
- Do not blame the model automatically.
- Do not approve a critical failure.

## Quality Criteria
Objective, evidence-based, structured, traceable, strategic, visually informed, technically aware, and actionable.

## Version
2.0

## Status
Production Candidate
