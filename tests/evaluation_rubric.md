# Semantic Evaluation Rubric

Score each dimension 0–4.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Task adherence | Wrong task | Partially follows task | Performs exact task boundary |
| Source fidelity | Invents/contradicts | Mostly faithful | All material claims traceable |
| Unknown handling | Fills unknowns as facts | Marks some unknowns | Preserves all relevant unknowns |
| Completeness | Major omissions | Minor omissions | Required output complete |
| Classification | Misclassifies materially | Some ambiguity | Correct and justified |
| Traceability | No useful provenance | Partial provenance | Material outputs traceable |
| Contract compliance | Output unusable | Partially compliant | Fully compliant |
| Handoff quality | Next stage cannot use | Usable with repair | Next stage can execute directly |

## Pass Criteria

- No critical hallucination or source contradiction.
- No critical contract violation.
- Average score >= 3.0.
- Source fidelity, unknown handling, and handoff quality each >= 3.

## Critical Failures

Any of the following is an automatic FAIL:

- Treating a supplied UNKNOWN as a fact.
- Inventing customer requirements.
- Silently changing an approved constraint.
- Producing an output that causes the next stage to rely on unsupported information.
- Crossing the task boundary in a way that changes project decisions.
