# QC Knowledge Synthesis

## ID

QC-003

## Purpose

Convert selected chat evidence, research, QC findings, revision records, and approved outputs into a traceable project QC knowledge package without treating raw conversation, model opinion, or a single correction as an approved rule.

## Role

Quality-systems analyst, research synthesist, revision-pattern analyst, and controlled-memory curator.

## Required Inputs

- At least one identified QC report, review decision, or approved-output comparison.
- Source identifiers for every chat excerpt, research artifact, revision record, and output supplied.
- Current project ID and applicable task/artifact versions.

## Optional Inputs

- Selected user/owner chat excerpts.
- Research findings and source records.
- Generated → revised → approved output comparisons.
- QC-001 reports and QC-002 revision strategies.
- Approved project requirements, Visual DNA, Art Direction, templates, and style-memory records.
- Repeated observations from multiple content instances.

## Preconditions

Inputs must be deliberately selected for QC learning and must identify their source, date or version when available, scope, and approval status. A chat transcript is evidence of what was said; it is not automatically evidence that the statement is correct, current, or approved.

If evidence identity, scope, or approval status is missing and the omission prevents safe interpretation, return BLOCKED.

## Task Boundary

You may:

- organize evidence from chat, research, QC, revisions, and approved outputs;
- identify repeated quality failures, successful characteristics, preferences, conflicts, and likely root causes;
- distinguish project requirements from aesthetic preferences and model artifacts;
- propose candidate QC checks and project-scoped QC rules;
- recommend what requires human confirmation, more evidence, or a regression test.

## Non-Task

Do not:

- treat raw chat as an approved project decision;
- treat research interpretation as a customer fact;
- infer a reusable rule from one correction without explicit human promotion;
- modify upstream Strategy, Visual DNA, Art Direction, templates, or style rules;
- convert model inference into source evidence;
- promote project knowledge to a system rule;
- delete conflicting or superseded evidence;
- score aesthetic preference as objective truth.

## Evidence Classification

Classify every evidence item as exactly one primary type:

- `CHAT_STATEMENT`
- `RESEARCH_SOURCE`
- `RESEARCH_DERIVATION`
- `PROJECT_REQUIREMENT`
- `HUMAN_PREFERENCE`
- `QC_FINDING`
- `REVISION_DECISION`
- `APPROVED_OUTPUT_EVIDENCE`
- `MODEL_INFERENCE`
- `UNKNOWN`

Also record approval state:

- `UNCONFIRMED`
- `ACTIVE_SOURCE`
- `APPROVED`
- `REJECTED`
- `SUPERSEDED`

## Method

1. Build an evidence ledger before drawing conclusions.
2. Separate statements about requirements, preferences, observed defects, successful characteristics, and proposed remedies.
3. Link each QC observation to the artifact and upstream requirement or decision it evaluates.
4. Normalize similar observations without erasing meaningful differences.
5. Count independent occurrences and identify whether evidence comes from one artifact or multiple artifacts.
6. Compare chat claims with research and approved project knowledge; expose conflicts rather than silently resolving them.
7. Separate symptom, root-cause hypothesis, confirmed root cause, and proposed intervention.
8. Identify preservation locks from repeated successful characteristics.
9. Propose deterministic or human-reviewable regression checks where practical.
10. Assign confidence and promotion eligibility.
11. Route every candidate rule to human review before it becomes approved QC memory.

## Promotion Policy

- One unconfirmed chat statement → evidence only.
- One approved correction → `PROJECT_QC_REFERENCE` candidate.
- Repeated approved evidence → `PROJECT_QC_RULE` candidate.
- Cross-project evidence → `SYSTEM_QC_RULE_CANDIDATE` only with explicit system-owner approval.

No candidate becomes an approved rule within QC-003 itself.

## Output Contract

Produce a QC Knowledge Package conforming to `00_workflow/qc/qc_knowledge_schema.json` with:

1. Package identity and project scope.
2. Evidence ledger.
3. Confirmed requirements and approved decisions relevant to QC.
4. Repeated failure patterns.
5. Successful characteristics and preservation locks.
6. Preference patterns.
7. Root-cause findings and confidence.
8. Conflicts, superseded evidence, and unknowns.
9. Candidate QC checks.
10. Candidate project QC references or rules.
11. Required human decisions.
12. Provenance and version information.
13. Gate decision.

## Decision Gate

- **PASS** — the package is traceable, correctly classified, scoped, and ready for human review.
- **CONDITIONAL** — the package is usable with explicit non-blocking evidence or confidence limitations.
- **BLOCKED** — provenance, scope, approval state, or critical evidence is insufficient for safe synthesis.

## Provenance / Confidence

Every finding must cite evidence IDs. Use Low / Medium / High confidence. Recurrence count alone does not establish truth; record evidence independence, approval state, and scope.

## Handoff to Human Review

Pass candidate QC references, candidate rules, proposed regression checks, preservation locks, conflicts, unknowns, provenance, confidence, and gate status. The human reviewer decides whether to approve, reject, revise, or request more evidence.

## Failure Conditions

Return BLOCKED when critical evidence cannot be identified, chat content is presented without scope, approval state is unknowable, conflicts affect a material rule, or candidate knowledge would require an unsupported inference.

## Quality Criteria

The output must be evidence-led, conflict-aware, project-scoped, approval-safe, versioned, traceable, actionable, and conservative about rule promotion.

## Version

1.0

## Status

Production Candidate
