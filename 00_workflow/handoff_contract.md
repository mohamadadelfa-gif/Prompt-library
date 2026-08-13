# Handoff Contract

A handoff is a controlled package, not a copy of the previous prompt's entire response.

## Required Handoff Fields

```text
HANDOFF_ID
SOURCE_STAGE
SOURCE_TASKS
STATUS
APPROVED_OUTPUTS
SOURCE_FACTS
DERIVED_FINDINGS
APPROVED_DECISIONS
UNKNOWN_ITEMS
OPEN_BLOCKERS
CONSTRAINTS
PROVENANCE
CONFIDENCE
NEXT_STAGE
ALLOWED_ASSUMPTIONS
FORBIDDEN_INFERENCES
```

## Rules

1. Approved outputs are authoritative for the next stage unless explicitly superseded.
2. Source facts remain immutable.
3. Derived findings must remain labelled as derived.
4. Decisions must remain labelled as decisions.
5. Unknown items must be carried forward when relevant.
6. Open blockers must be resolved before a dependent stage can PASS.
7. The next stage may use only the information included in the handoff and its permitted external inputs.
8. A downstream task must not treat a derived finding as a source fact.
9. A downstream task must not invent a missing value merely because it would improve continuity.
10. When an upstream output is superseded, the handoff must identify both the old and new versions.

## Handoff Status

- COMPLETE — all required outputs are present and approved.
- CONDITIONAL — usable only with listed conditions.
- BLOCKED — required information or approval is missing.
- SUPERSEDED — replaced by a later approved version.
