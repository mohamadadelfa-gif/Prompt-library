# QC-IG-001 — Instagram Visual QC

## Purpose
Validate that an approved-content visual candidate works as an Instagram asset and remains faithful to the project visual system. This QC is applied after each visual generation/revision and before Figma implementation.

## Input
- Approved/locked copy
- Generated visual candidate
- Content-to-visual mapping / slide narrative roles
- Approved EBL visual grammar and motif rules
- Platform specification
- Relevant human revision decisions

## Output
- PASS / PASS_WITH_REVISION / FAIL
- Findings by gate
- Critical failures
- Revision instructions
- Evidence record

## Gates

### IG-01 Content Fidelity — mandatory
Check exact approved meaning, slide order, CTA, brand naming, spelling, omissions, additions and unauthorized rewriting.
Critical failure: generated content changes approved meaning or invents project claims.

### IG-02 Narrative Function
Verify that each slide performs its assigned communication role and that the carousel has perceptible progression, not merely visual consistency.

### IG-03 Instagram Readability
Check feed/mobile readability, hierarchy, text density, contrast, line length, margins, crop safety and cover comprehension at thumbnail/feed size.

### IG-04 EBL Visual Identity
Check approved typography, palette, painterly/material character, asymmetrical visual-weight composition, negative space and the intended intelligent/human/editorial character.

### IG-05 Visual Grammar & Motifs
Every non-text visual element must have a compositional, semantic, narrative or brand function. Apply motif classes CORE / SUPPORTING / CONTEXTUAL / EXCLUDE. Reject decorative clutter and literal infographic substitution when it conflicts with the approved visual grammar.

### IG-06 Painterly / Artistic Quality
Evaluate visual weight, rhythm, tension, gesture, material variation, organic/geometric relationships, irregularity and typography-image integration. Texture alone does not constitute painterly composition.

### IG-07 Carousel System
Check family resemblance plus meaningful variation, cross-slide rhythm, motif recurrence without repetition, palette development and correspondence between visual progression and narrative progression.

### IG-08 Human Approval
AI QC cannot grant final creative approval. Human approval is required before Figma handoff.

## Scoring
Content Fidelity is a mandatory gate and cannot be compensated by score.
- Narrative: 15
- Instagram usability: 20
- EBL identity: 20
- Visual grammar/motifs: 15
- Painterly quality: 15
- Carousel coherence: 15
Total: 100

A critical failure => FAIL regardless of total score.

## Evidence
For each finding record: candidate ID, slide(s), gate, observation, expected rule, severity, revision action, and whether the finding is post-specific or a reusable learning candidate.

## Handoff
PASS/PASS_WITH_REVISION + HUMAN_APPROVED -> Figma implementation.
FAIL -> human-directed revision -> regenerate -> rerun QC-IG-001.
