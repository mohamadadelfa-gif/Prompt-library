# Decision Gates

## Canonical Vocabulary

The workflow uses only these machine-readable gate states:

- **PASS** — task output is complete and suitable for downstream use.
- **CONDITIONAL** — output is usable with explicitly listed non-blocking conditions.
- **BLOCKED** — required input, evidence, approval, or resolution is missing.
- **APPROVE** — an authorized reviewer accepts the decision/output for downstream use.
- **REVISE** — the core direction remains viable but requires correction.
- **REJECT** — the current decision/output should not proceed.
- **READY** — generation/execution package is complete and approved for execution.
- **REGENERATE** — the current generated result fundamentally fails and must be regenerated.

Prompt text may explain a gate in natural language, but the final status must be one canonical value above.

## Strategy

STR-001 through STR-004 use **PASS / CONDITIONAL / BLOCKED**.

STR-005 uses **APPROVE / REVISE / BLOCKED** because reconciliation creates the authoritative project definition and may require human approval.

## Research

RES-001 through RES-006 use **PASS / CONDITIONAL / BLOCKED**.

PASS requires sufficient evidence for the downstream research purpose. CONDITIONAL records non-blocking limitations. BLOCKED means a required conclusion would depend on unsupported evidence.

## Visual Analysis

VIS-001 through VIS-006 use **PASS / CONDITIONAL / BLOCKED**.

PASS requires sufficient usable reference analysis for Visual DNA extraction. BLOCKED applies when required references or evidence are insufficient.

## Visual DNA

VDNA-001 uses **PASS / CONDITIONAL / BLOCKED**.

PASS requires traceable rules, resolved or documented contradictions, and sufficient coverage of all required VIS analyses.

## Art Direction

ART-001 uses **PASS / CONDITIONAL / BLOCKED**.

ART-002 uses **APPROVE / REVISE / REJECT**.

ART-003 uses **APPROVE / REVISE / BLOCKED**.

Human approval is required for ART-002 and ART-003.

## Generation

GEN-001 uses **READY / BLOCKED**.

GEN-002 uses **READY / BLOCKED**.

READY means all required inputs, approvals, constraints, traceability, and model-adaptation rules are complete.

## Quality Control

QC-001 uses **APPROVE / REVISE / REGENERATE / BLOCKED**.

QC-002 uses **REVISE / REGENERATE / BLOCKED**.

QC-003 uses **PASS / CONDITIONAL / BLOCKED**. PASS means the QC knowledge package is traceable and ready for human review; it does not approve or promote candidate rules.

A CRITICAL failure in QC-001 cannot be overridden by a numerical score.

## Human Approval Record

When `approval_required` is true, the task cannot advance without an explicit approval record containing:

- approval status
- approver role
- decision timestamp
- artifact/task version
- decision rationale when not APPROVE

## Revision Loop

The maximum revision cycle count is **3**. After the third unsuccessful cycle, the workflow returns **HUMAN_REVIEW** rather than continuing automatically.
