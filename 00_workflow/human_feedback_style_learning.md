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

---

# PROD-REV-001 — Human-Directed Output + Visual Revision

## Governing Relationship

```text
HUMAN = decides WHAT to edit
REFERENCE = shows / informs HOW the requested edit should look
AI = applies the requested edit
```

The AI must not independently redesign areas that the human did not request to change.

## Required Inputs

```text
EXISTING_OUTPUT
VISUAL_REFERENCE
HUMAN_EDITING_INSTRUCTIONS
```

The human editing instructions define the authorized change scope.

## Revision Rules

Apply only the requested changes.

Preserve everything that was not requested.

Do not:

- redesign the entire output;
- introduce unrelated elements;
- change content without permission;
- change the visual identity without instruction;
- add new concepts;
- remove existing elements unless requested;
- copy the reference literally.

The result must remain an **edited version of the existing output**, not a new design disguised as a revision.

## Reference Analysis Scope

Use the reference only where relevant to the requested change. It may inform:

- composition;
- hierarchy;
- proportions;
- spacing;
- typography;
- color;
- imagery;
- shapes;
- graphic elements;
- texture;
- lighting;
- visual weight;
- alignment;
- overall visual character.

Do not transfer reference characteristics unrelated to the human request.

## Necessary Execution Adjustment

Distinguish:

```text
REQUESTED_CHANGE
```

from:

```text
NECESSARY_EXECUTION_ADJUSTMENT
```

A necessary execution adjustment is a minimal technical change required to make the requested edit work—for example, a small text-box width change required to preserve an approved line break. It must not become permission for unrelated redesign.

## Required Revision Output

Every human-directed revision should produce:

### 01. Applied Changes

List exactly what changed.

### 02. Preserved Elements

List important elements intentionally left unchanged.

### 03. Revised Design Specification

Provide the complete revised specification or production description.

### 04. Revised Visual

Produce or update the visual so the requested change is visible as design proof.

The preferred comparison model is:

```text
ORIGINAL OUTPUT
      ↓
REFERENCE
      ↓
REVISED OUTPUT
```

The revised visual is not merely an illustration of the idea. It is evidence that the requested edit was correctly executed while non-requested elements were preserved.

## Revision QC

Before marking a revision complete, check:

1. Did every requested change occur?
2. Was any unrequested content changed?
3. Was any unrequested visual element redesigned?
4. Were approved copy and meaning preserved?
5. Did the reference influence only the authorized scope?
6. Were necessary execution adjustments minimal and declared?
7. Can a human compare original → reference → revised output and immediately verify the result?

If an unrelated change occurred, route back to revision rather than accepting it as creative improvement.

---

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
REFERENCE_ARTIFACT
HUMAN_EDITING_INSTRUCTIONS
REQUESTED_CHANGES
NECESSARY_EXECUTION_ADJUSTMENTS
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
11. Never use a reference as permission to redesign outside the human-requested scope.
12. Treat preservation of non-requested elements as an explicit success criterion.
