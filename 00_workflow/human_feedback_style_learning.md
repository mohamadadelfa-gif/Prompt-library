# Human Feedback & Style Learning Layer

## Purpose

Capture human revision after generation and convert validated revision patterns into reusable, traceable style knowledge without silently modifying the core prompt library.

This layer sits after generation and quality control:

```text
GEN-002
  ↓
Generated Output
  ↓
Human Revision
  ↓
Approved Output
  ↓
Revision Record
  ↓
Style Knowledge Extraction
  ↓
Approved Style Reference / Style Rule
```

## Core Principle

Do not call the raw generated image a style reference.
Do not call every human correction a style rule.

A style rule becomes reusable knowledge only after explicit human approval and provenance capture.

## Artifact Types

### 1. Generated Output

The unmodified output produced from the approved generation prompt.

State: `OUTPUT`

### 2. Revision Record

A structured record describing what the human changed, removed, preserved, or requested.

State: `DERIVED` + human decision metadata.

### 3. Approved Output

The final human-approved result after revision.

State: `OUTPUT`

### 4. Style Reference

A selected approved output used as a visual reference for future work.

State: `DECISION`

A style reference is project-scoped unless explicitly promoted to a broader scope.

### 5. Style Rule

A generalized, reusable principle extracted from one or more approved outputs.

Examples:

- typography should use a bold condensed editorial sans-serif treatment
- headline text should dominate over decorative texture
- geometric marks should remain secondary to communication
- warm paper background with muted primary color fields

A style rule must never be inferred from a single output without human approval.

## Required Revision Record

```text
REVISION_ID
PROJECT_ID
TASK_ID
PROMPT_VERSION
INPUT_ARTIFACT
GENERATED_OUTPUT
HUMAN_REVISION
APPROVED_OUTPUT
CHANGES_MADE
WHAT_WAS_PRESERVED
WHY_IT_WAS_CHANGED
STYLE_ATTRIBUTES_AFFECTED
HUMAN_DECISION
APPROVER
APPROVED_AT
SCOPE
PROVENANCE
```

## Change Classification

Every human revision should classify each change as one or more of:

- TYPOGRAPHY
- COMPOSITION
- COLOR
- SHAPE / FORM
- TEXTURE / MATERIAL
- LIGHTING
- SCALE / HIERARCHY
- SPACING
- CONTENT / COPY
- BRANDING
- MODEL_ARTIFACT
- OTHER

## Style Extraction Rule

The extraction process should compare:

`Generated Output → Human Revision → Approved Output`

and ask:

1. What specifically changed?
2. Was the change intentional or corrective?
3. Is it a one-off correction or a recurring preference?
4. Does it represent project-specific style or a general system rule?
5. Should it affect future generation specifications, reference selection, or neither?

## Promotion Levels

### PROJECT STYLE REFERENCE

Reusable only within the same project.

### PROJECT STYLE RULE

A recurring preference supported by at least one approved reference and explicit human approval.

### SYSTEM STYLE RULE

A reusable design principle demonstrated across multiple approved projects or references and explicitly promoted by a human owner.

Never promote a project-specific choice to a system rule automatically.

## Integration With Existing Pipeline

Human feedback may inform future work through controlled inputs:

- `GEN-001` may use approved style references and style rules.
- `GEN-002` may use approved style references as reference context.
- `VDNA-001` may receive style evidence only when it is explicitly approved as a style source.
- `QC-001` may compare new outputs against approved style references.

Human feedback must not silently overwrite STR, RES, VIS, VDNA, or ART decisions.

## Approval Gate

A human revision becomes an approved reference only when:

- the output is explicitly marked APPROVED;
- the revision record is complete;
- provenance is captured;
- scope is specified;
- the reviewer confirms that the change represents intentional preference rather than accidental correction.

## Style Memory Rules

1. Preserve the original generated output.
2. Preserve the revised output.
3. Preserve the differences between them.
4. Record why the change was made.
5. Do not train or alter a prompt from a single correction automatically.
6. Require repeated evidence or explicit human promotion before creating system-level rules.
7. Keep style references separate from factual project requirements.
8. Keep aesthetic preference separate from customer requirements.
9. Version every approved style rule.
10. Allow style rules to be superseded without deleting historical evidence.
