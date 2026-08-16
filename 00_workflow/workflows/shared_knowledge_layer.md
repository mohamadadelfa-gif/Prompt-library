# Shared Knowledge Layer — Design + Writing

## Purpose

The Prompt Library contains two sibling execution workflows:

```text
WRITING WORKFLOW
DESIGN WORKFLOW
```

They may share evidence, research, project knowledge, external references, structures, and tools, but they keep execution state, decisions, approvals, versions, and QC authority separate.

## Governance Principle

```text
SHARE EVIDENCE.
SHARE KNOWLEDGE.
SHARE TOOLS.
DO NOT SHARE AUTHORITY SILENTLY.
```

## What May Be Shared

- project briefs;
- customer/audience research;
- cultural/context research;
- brand memory;
- approved project rules;
- terminology/glossaries;
- source registries;
- external research references;
- platform constraints;
- typography/readability references;
- shared tools and technical methods;
- approved factual source material;
- provenance records.

## Shared-Knowledge Metadata

When useful, shared knowledge should declare:

```text
PRIMARY_WORKFLOW
SECONDARY_WORKFLOW
AUTHORITY_SCOPE
PROJECT_SCOPE
PROVENANCE_REQUIRED
PROMOTION_STATE
```

Recommended `AUTHORITY_SCOPE` values:

- `EVIDENCE_ONLY`
- `METHOD_REFERENCE`
- `PROJECT_RULE`
- `SYSTEM_RULE`

A shared source marked `EVIDENCE_ONLY` may inform both workflows but cannot itself approve content or design decisions.

## What Must Remain Separate

The following never transfer automatically:

- workflow execution state;
- task completion;
- approval;
- revision state;
- QC result;
- content decision;
- visual decision;
- generated output;
- version authority.

A Writing PASS does not imply a Design PASS. A Design approval does not imply content approval.

## Cross-Workflow Handoff

All cross-workflow transfers use:

`00_workflow/workflows/cross_workflow_handoff_contract.md`

### Writing → Design

Transfers approved content version, lock/flexibility state, semantic hierarchy, language/tone constraints, claim/fact status, caption/CTA state, alt-text intent, source references, and unresolved unknowns.

### Design → Writing

Transfers visual/platform constraints that require textual reconsideration: available text area, maximum recommended length, reading order, text density, platform limitation, semantic emphasis need, and requested Writing action.

The receiving workflow owns the resulting decision in its own domain.

## Shared Research Rule

A research result may be reused by both workflows when provenance and scope remain explicit.

```text
AUDIENCE RESEARCH
├── Writing → tone, vocabulary, topic relevance, reader action
└── Design  → hierarchy, density, format, visual communication
```

Reuse avoids duplicate research; interpretation remains domain-specific.

## Shared Tool Rule

A methodology or tool may be registered once and consumed by both workflows when genuinely useful.

Examples:

- article/document explainer → primarily Writing, optionally shared research support;
- typography/readability systems → primarily Design, optionally Writing accessibility support;
- audience/cultural research → shared evidence.

## Final Combined Production

```text
CONTENT NEED
→ WRITING WORKFLOW
→ WRITING QC
→ HUMAN CONTENT APPROVAL
→ WRITING_TO_DESIGN HANDOFF
→ DESIGN WORKFLOW
→ VISUAL QC
→ HUMAN VISUAL APPROVAL
→ COMBINED PACKAGE QC
→ HUMAN FINAL APPROVAL
```

If Design exposes a content problem, route it back to Writing. If Writing changes invalidate layout, issue a new Writing version and rerun the affected Design stages.
