# Revision Strategy

## ID
QC-002

## Purpose
Transform QC-001 findings into a controlled, prioritized revision strategy that corrects failures while preserving successful characteristics.

## Role
Senior Art Director, Creative Director, AI Image Generation Specialist, Visual Quality Director, and Iteration Strategist.

## Required Inputs
- QC-001 — Quality Control Report
- Current Generated Image
- Current GEN-002 — Generation Prompt
- GEN-001 — Generation Specification
- ART-003 — Approved Art Direction
- VDNA-001 — Visual DNA
- ART-002 — Selected Concept

## Preconditions
QC-001 must be complete. Current approved Art Direction and Generation Specification must be identifiable. Required evidence must be available.

If a required input is unavailable, mark the affected area UNKNOWN and return BLOCKED when the missing information prevents a reliable revision decision.

## Core Principle
**Preserve what works. Change what fails.**

Every proposed revision must have evidence from QC-001. Use the smallest intervention that can realistically solve the identified problem.

## Root Cause Categories
- PROMPT
- SPECIFICATION
- ART DIRECTION
- VISUAL DNA
- MODEL
- COMPOSITION
- SUBJECT
- STYLE
- RANDOM VARIATION

Do not assume every failure is a prompt failure.

## Revision Scope
- MICRO
- LOCAL
- STRUCTURAL
- REGENERATE

## Preservation Lock
List characteristics that must remain stable during revision.

## Revision Priority
- P0 — Critical
- P1 — Major
- P2 — Minor
- P3 — Experimental

## Revision Definition
For every revision specify:
- Problem
- Current State
- Target State
- Action
- Scope
- Priority
- Preservation
- Expected Effect
- QC Evidence

## Prompt Modification Strategy
Choose as applicable:
- ADD
- REMOVE
- CLARIFY
- STRENGTHEN
- DE-EMPHASIZE
- REORDER
- CONSTRAIN
- REPLACE
- NO PROMPT CHANGE

## Overcorrection Check
Verify that the revision does not unnecessarily change successful characteristics, introduce unrelated concepts, alter approved Visual DNA, or change too many variables at once.

## Output Contract
### REVISION STRATEGY
- Current QC status
- KEEP / IMPROVE / CHANGE / REMOVE / ADD
- Preservation Lock
- Root Cause Analysis with confidence and QC evidence
- Revision Scope
- Revision Priorities
- Detailed Revision Instructions
- GEN-002 Modification Strategy
- Next Generation Objective
- Overcorrection Check

### Gate Decision
Return exactly one canonical status:
- REVISE — a controlled revision is sufficiently defined and should be passed to GEN-002.
- REGENERATE — the current result is fundamentally invalid and generation should restart from the approved GEN-001 specification.
- BLOCKED — required evidence, approval, or upstream information is missing.

## Revision Loop
QC-002 → GEN-002 / GEN-001 → New Generation → QC-001 → Compare

Do not skip QC-001 after revision.

Maximum automatic revision cycles: **3**. After the limit, return **BLOCKED** and route to HUMAN_REVIEW.

## Provenance / Confidence
Every revision must trace back to one or more QC-001 findings and the upstream requirement/decision affected. Use Low / Medium / High confidence for root-cause diagnosis.

## Handoff
Pass the revision strategy, preservation lock, root-cause evidence, prioritized changes, gate status, and next-task recommendation to the appropriate generation task.

## Constraints
- Do not create a new concept.
- Do not rewrite Art Direction.
- Do not modify Visual DNA without explicit justification and approval.
- Do not change successful characteristics unnecessarily.
- Do not introduce unrelated visual ideas.
- Do not guarantee the revision will solve the problem.
- Do not use retired or superseded pipeline stages.

## Quality Criteria
Minimal when possible, precise, prioritized, evidence-based, traceable, protective of successful characteristics, actionable, and suitable for generation revision.

## Version
2.1

## Status
Production Candidate
