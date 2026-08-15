# Executable Task Contract

Every active prompt is an executable task and must conform to this contract through its prompt content plus the machine-readable contract in `00_workflow/task_contracts.json`.

## 1. TASK
State exactly what the task is responsible for.

## 2. INPUT CONTRACT
Declare required, optional, conditional, and prohibited inputs. Required inputs must correspond to the task contract manifest.

## 3. PRECONDITIONS
State approvals, artifacts, reference availability, and upstream gates required before execution.

## 4. TASK BOUNDARY
Define what the task may classify, infer, transform, decide, or produce.

## 5. NON-TASK
State what the task must not do, especially work owned by another stage.

## 6. METHOD
Define the required analytical, research, synthesis, creative, generation, or evaluation method.

## 7. OUTPUT CONTRACT
Define the mandatory output sections, identifiers, statuses, and handoff contents.

## 8. PROVENANCE
Every material claim, requirement, rule, finding, or decision must identify its supporting source or upstream artifact ID.

## 9. CONFIDENCE
Use **Low / Medium / High** where evidential certainty matters. Confidence describes evidence strength, not writing quality.

## 10. UNKNOWN HANDLING
Unknown information must remain **UNKNOWN**. Never convert an assumption, hypothesis, or plausible completion into a fact.

## 11. DECISION GATE
The final status must use the canonical vocabulary defined in `00_workflow/decision_gates.md` and the task's contract entry.

## 12. HANDOFF
The task must identify the exact downstream task(s) and pass the required artifact fields defined by the handoff contract.

## 13. FAILURE CONDITIONS
State when execution must stop rather than proceed with unsupported information.

## 14. VERSION / STATUS
Every active prompt carries a version and lifecycle status. The machine-readable contract is authoritative for compatibility and gate definitions.

## 15. HUMAN APPROVAL
When the task contract marks `approval_required: true`, execution may not advance until the required approval record exists.

## Universal Invariants

- Preserve upstream source facts.
- Distinguish SOURCE, DERIVED, DECISION, and OUTPUT.
- Do not invent missing inputs.
- Do not silently alter approved decisions.
- Do not duplicate another task's responsibility.
- Keep material outputs traceable.
- Make blockers explicit.
- Keep handoffs structured and auditable.
- Never use a deprecated prompt ID as an active dependency.
