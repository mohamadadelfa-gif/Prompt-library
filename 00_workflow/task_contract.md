# Executable Task Contract

Every prompt in the library must behave as an executable task.

## 1. TASK

State exactly what the task is responsible for.

## 2. INPUT CONTRACT

List required, optional, conditional, and prohibited inputs.

## 3. PRECONDITIONS

State what must be approved or available before execution.

## 4. TASK BOUNDARY

Define what the task may transform, classify, infer, decide, or produce.

## 5. NON-TASK

Explicitly state what the task must not do. In particular, it must not perform work assigned to a downstream or upstream stage.

## 6. METHOD

Define the required reasoning procedure, evidence handling, classification, or evaluation method.

## 7. OUTPUT CONTRACT

Define the mandatory output sections, fields, identifiers, and status values.

## 8. PROVENANCE

Every material claim, requirement, rule, or decision must identify its source. Use the strongest available reference: input ID, source statement, upstream output ID, or evidence item.

## 9. CONFIDENCE

Use Low, Medium, or High. Confidence describes evidential support, not writing quality.

## 10. UNKNOWN HANDLING

Unknown information must remain UNKNOWN. Never convert an assumption into a fact.

## 11. DECISION GATE

Every task must end with a gate appropriate to its role, such as PASS, CONDITIONAL, BLOCKED, APPROVE, REVISE, or REJECT.

## 12. HANDOFF

Define exactly what the next task receives and what it is permitted to rely on.

## 13. FAILURE CONDITIONS

State when the task must stop rather than continue with invented or unsupported information.

## 14. VERSION

Every executable prompt must carry a version and status.

## Universal Invariants

- Preserve upstream source facts.
- Distinguish source, derived analysis, and decisions.
- Do not invent missing inputs.
- Do not silently change approved decisions.
- Do not duplicate another stage's responsibility.
- Make important outputs traceable.
- Make blocking conditions explicit.
- Prefer structured outputs over prose-only handoffs.
