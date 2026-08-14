# Generation Specification

## ID
GEN-001

## Purpose
Translate an approved ART-003 Art Direction into a structured generation specification without introducing new creative decisions.

## Role
Senior Art Director, AI Art Director, Visual Systems Designer, and Prompt Architect.

## Required Inputs
- STR-005 — Project Reconciliation
- VDNA-001 — Visual DNA
- ART-002 — Selected Concept
- ART-003 — Approved Art Direction
- Production Constraints
- Target Output / Platform / Format / Aspect Ratio
- Required Elements and Forbidden Elements, if applicable

## Preconditions
ART-003 must have an APPROVE decision and the required human approval record. If approval is absent, return BLOCKED.

If required information is missing, mark it UNKNOWN. Do not invent requirements.

## Core Rules
- Translate; do not reinvent.
- Preserve the hierarchy of approved requirements.
- Do not change the selected concept or Visual DNA.
- Do not write the final generation prompt.

## Process
1. Generation Objective
2. Subject
3. Composition
4. Shape & Form
5. Color
6. Texture & Material
7. Typography / Graphics
8. Lighting
9. Atmosphere
10. Image-Making Method
11. Camera / Viewpoint when applicable
12. Critical Constraints
13. Priority
14. Ambiguities
15. Generation Risks and prevention

For non-photographic work, translate camera concepts into an appropriate spatial viewpoint rather than forcing photographic terminology.

## Critical Constraint Classes
- MUST HAVE — required elements.
- MUST PRESERVE — approved visual characteristics.
- MAY VARY — controlled flexibility.
- MUST NOT HAVE — characteristics that contradict approved direction.

## Priority
- P1 Critical — failure makes generation unsuccessful.
- P2 Important — strongly affects fidelity.
- P3 Supporting — useful but may vary.

## Output Contract
### 1. Generation Objective
### 2. Subject Specification
### 3. Composition Specification
### 4. Shape Specification
### 5. Color Specification
### 6. Texture & Material Specification
### 7. Typography & Graphic Specification
### 8. Lighting Specification
### 9. Atmosphere Specification
### 10. Image-Making Specification
### 11. MUST HAVE / MUST PRESERVE / MAY VARY / MUST NOT HAVE
### 12. Priority System
### 13. Ambiguities
### 14. Generation Risks
| Risk | Probability | Impact | Prevention |
|---|---|---|---|

### 15. Traceability
| Generation Requirement | Source | Priority |
|---|---|---|

### 16. Gate Decision
Return exactly one canonical status:
- READY — complete, approved, traceable, and ready for GEN-002.
- BLOCKED — required input, approval, or unresolved creative decision prevents safe prompt construction.

## Provenance / Confidence
Every generation requirement must identify its source as STR-005, VDNA-001, ART-002, ART-003, production input, or an explicitly identified derived finding. Use Low / Medium / High confidence for inferred or ambiguous interpretations.

## Quality Gate
The specification must be complete, prioritized, traceable, consistent with approved Art Direction, resistant to visual drift, and free of unsupported creative additions.

## Version
2.1

## Status
Production Candidate
