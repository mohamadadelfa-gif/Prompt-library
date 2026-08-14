# Production Candidate v1

## Scope

This release packages the controlled creative-production workflow, executable runtime, structural CI, and semantic-test framework.

## Production Guarantees

- 25 active prompts with unique stage-aligned IDs.
- Deprecated reference-selection file excluded from active execution.
- Controlled SOURCE / DERIVED / DECISION / OUTPUT information model.
- Explicit handoff package and decision-gate architecture.
- Machine-readable stage/task registry.
- Provider-agnostic runtime supporting OpenAI and Gemini.
- Auditable task execution artifacts with prompt/input hashes.
- Semantic evaluation CLI and controlled evaluation rubric.
- Automated repository validation in GitHub Actions.
- Synthetic semantic-test fixture for regression testing.

## Known Boundary

Structural CI and runtime smoke tests validate repository and execution infrastructure. They do not prove semantic quality for a specific model configuration. A semantic release test requires an API credential, approved model, controlled fixture, and evaluator run.

## Release Gate

Production use requires all of the following:

1. Structural CI PASS.
2. Runtime compilation/smoke checks PASS.
3. No duplicate or invalid IDs.
4. No unresolved critical workflow dependency.
5. Prompt version/status present.
6. Relevant semantic tests PASS with the selected model/runtime.
7. Human approval for strategic or creative decision gates.
8. Release record identifies the prompt versions, model, evaluator, and semantic test result.

## Version

Production Candidate v1
