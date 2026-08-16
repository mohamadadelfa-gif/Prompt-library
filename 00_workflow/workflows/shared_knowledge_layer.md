# Shared Knowledge Layer — Design + Writing

## Purpose

The Prompt Library now contains two sibling execution workflows:

```text
DESIGN WORKFLOW
WRITING WORKFLOW
```

They remain operationally separate but may consult a controlled Shared Knowledge Layer.

The purpose of this layer is to prevent duplicate research while preventing silent cross-workflow authority leaks.

## What May Be Shared

Both workflows may consult:

- project briefs
- customer/audience research
- cultural/context research
- brand memory
- approved project rules
- terminology/glossaries
- source registries
- external research references
- platform constraints
- typography and readability references
- shared tools and technical methods
- approved factual source material
- provenance records

## What Must Remain Separate

The following do not transfer authority automatically:

- workflow execution state
- task completion status
- approvals
- revisions
- QC results
- creative decisions
- content decisions
- visual decisions
- generated outputs

A Writing PASS does not imply a Design PASS.
A Design approval does not imply content approval.

## Cross-Workflow Handoff

The workflows communicate through explicit handoffs rather than by editing each other's state.

### Writing → Design

Use when approved text needs visual production.

Transfer:
- approved copy
- semantic hierarchy
- language/tone constraints
- source status
- flexibility/lock state
- CTA/caption/alt-text intent

### Design → Writing

Use when visual/platform constraints require textual reconsideration.

Transfer:
- available text area
- reading-order constraints
- recommended maximum length
- slide/story role
- text-density issue
- platform limitations
- semantic emphasis needs

The receiving workflow owns the resulting decision in its own domain.

## Shared Research Rule

A research result may be used by both workflows when provenance and scope remain clear.

Example:

```text
AUDIENCE RESEARCH
├── Writing uses it for tone, vocabulary, topic relevance
└── Design uses it for visual communication, density, format, hierarchy
```

The interpretation may differ because the workflows have different responsibilities.

## Shared Tool Rule

A tool or external methodology may be registered for both workflows when genuinely useful to both. Registration should declare the consumers rather than copying the knowledge file.

Examples:

- article/document explainer → primarily Writing, optionally shared research support
- typography systems → primarily Design, optionally Writing readability support
- audience/cultural research → shared

## Governance Principle

```text
SHARE EVIDENCE.
SHARE KNOWLEDGE.
SHARE TOOLS.
DO NOT SHARE AUTHORITY SILENTLY.
```

## Final Combined Production

When one deliverable needs both text and design:

```text
WRITING WORKFLOW
→ APPROVED WRITING HANDOFF
→ DESIGN WORKFLOW
→ APPROVED VISUAL OUTPUT
→ COMBINED PACKAGE QC
→ HUMAN FINAL APPROVAL
```

If the design process exposes a content problem, route it back to Writing; if writing changes invalidate layout, route the approved revision back to Design.
