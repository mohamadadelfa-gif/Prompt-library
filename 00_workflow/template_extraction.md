# Template Extraction Task

## Task
Convert an approved content artifact into a reusable content template without transferring campaign-specific content or requirements.

## Input Contract

Required:

- Approved Content Artifact
- Human Revision Record
- Approved Style References, when applicable
- Content Type
- Platform
- Brand Rules

## Boundary

May extract:

- layout structure
- typography roles
- spacing
- grids
- safe areas
- graphic zones
- editable zones
- reusable color roles
- reusable texture treatment

Must not extract as reusable template rules:

- campaign-specific copy
- customer-specific requirements
- audience assumptions
- one-off imagery
- temporary campaign messages
- accidental rendering artifacts

## Output

Produce:

1. Template record
2. Reusable layout rules
3. Editable zones
4. Content limits
5. Style references
6. Known exclusions
7. Template scope
8. Version
9. Approval state

## Gate

- PASS — template is reusable and structurally separated from campaign content.
- CONDITIONAL — reusable with explicit restrictions.
- BLOCKED — the artifact is too content-specific or insufficiently understood.

## Human Approval

A template requires human approval before it becomes reusable in future production.

## Example

An approved five-slide Instagram carousel can produce:

- `TPL-IG-001` — reusable five-slide editorial carousel structure.

It does not automatically become:

- a universal brand style;
- a new customer requirement;
- a replacement for Art Direction.
