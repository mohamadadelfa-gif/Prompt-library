# Production Candidate v1

## Scope

This release packages the controlled creative-production workflow and its structural CI validation.

## Production Guarantees

- 25 active prompts with unique stage-aligned IDs.
- Deprecated reference-selection file excluded from active execution.
- Controlled SOURCE / DERIVED / DECISION / OUTPUT information model.
- Explicit handoff package and decision-gate architecture.
- Automated repository validation in GitHub Actions.
- Synthetic semantic-test fixture and evaluation rubric included for future LLM execution.

## Known Boundary

Structural CI validates repository integrity and prompt contracts. It does not by itself prove semantic quality of LLM responses. LLM execution requires a configured model runner and evaluator.

## Release Gate

Production use requires:

1. Structural CI passing.
2. No duplicate or invalid IDs.
3. No unresolved critical workflow dependency.
4. Prompt versions/statuses present.
5. Semantic test suite executed with the selected model/runtime before a production prompt change is released.

## Version

Production Candidate v1
