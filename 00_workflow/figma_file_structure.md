# Figma Production File Structure

## ID

`PROD-FIG-STRUCT-001`

## Purpose

Define the required organization of a production Figma file after an approved raster visual has been prepared for editable reconstruction.

This structure separates source-of-truth references, editable production masters, reusable system assets, and publish/export frames so manual editing cannot silently overwrite approved evidence.

## Governing Principle

> APPROVED REFERENCE verifies the design. EDITABLE MASTER is where production work happens. STYLE SYSTEM stores reusable rules/assets. EXPORT contains publish-ready output.

The approved PNG must never be replaced by a reconstructed or manually edited version.

## Top-Level Figma Structure

```text
EBL — POST 01 / ENGLISH INDEPENDENCE
│
├── 00_README
│   ├── File Purpose
│   ├── Source-of-Truth Rule
│   ├── Editing Rules
│   └── Version / Status
│
├── 01_APPROVED_REFERENCE
│   ├── Slide 01 — Approved PNG [LOCKED]
│   ├── Slide 02 — Approved PNG [LOCKED]
│   ├── Slide 03 — Approved PNG [LOCKED]
│   ├── Slide 04 — Approved PNG [LOCKED]
│   ├── Slide 05 — Approved PNG [LOCKED]
│   └── Slide 06 — Approved PNG [LOCKED]
│
├── 02_EDITABLE_MASTER
│   ├── POST-001 / Slide 01
│   ├── POST-001 / Slide 02
│   ├── POST-001 / Slide 03
│   ├── POST-001 / Slide 04
│   ├── POST-001 / Slide 05
│   └── POST-001 / Slide 06
│
├── 03_STYLE_SYSTEM
│   ├── Typography
│   ├── Colors
│   ├── Slide Number
│   ├── Brand Mark
│   └── Reusable Motifs
│
└── 04_EXPORT
    ├── Slide 01 — 1254×1254
    ├── Slide 02 — 1254×1254
    ├── Slide 03 — 1254×1254
    ├── Slide 04 — 1254×1254
    ├── Slide 05 — 1254×1254
    └── Slide 06 — 1254×1254
```

The content ID, post title, slide count, and dimensions are project-specific and must be derived from the approved artifact.

## Internal Editable Slide Structure

Every editable slide should follow this hierarchy when the asset is reconstructed from a flattened/raster source:

```text
POST-001 / SLIDE XX
│
├── 00_REFERENCE
│   └── Approved PNG [LOCKED]
│
├── 01_ARTWORK
│   └── Textless Background [CONTROLLED]
│
├── 02_EDITABLE_TEXT
│   ├── 01_Slide_Number [EDITABLE]
│   ├── 02_Headline [EDITABLE]
│   ├── 03_Supporting_Copy [EDITABLE]
│   ├── 04_Emphasis [EDITABLE]
│   ├── 05_CTA [EDITABLE]
│   └── 06_Brand_Text [EDITABLE]
│
├── 03_EDITABLE_GRAPHICS
│   ├── Logo [CONTROLLED or LOCKED]
│   ├── Simple Signs [CONTROLLED]
│   └── Reusable Shapes [CONTROLLED]
│
└── 04_QC
    └── Overlay Reference / Comparison Controls
```

Not every slide requires every text or graphic layer. Empty categories may be omitted, but the numbering logic should remain deterministic.

## Layer Status Vocabulary

### LOCKED

Must not be changed during normal production.

Examples:

- approved source PNG;
- approved logo source when alteration is prohibited;
- final reference evidence.

### CONTROLLED

May be modified only when a defined production rule permits it.

Examples:

- textless raster artwork;
- simple motifs;
- reusable brand shapes;
- template structure.

### EDITABLE

Native Figma production content intended for normal manual editing.

Examples:

- live text;
- slide number;
- CTA;
- post-specific copy.

### REFERENCE

Evidence used to compare or validate the production master. It is not itself the editable production object.

## 00_README Requirements

The file README should record:

- Figma package ID;
- content/post ID;
- approved visual version;
- frame dimensions;
- slide count;
- source-of-truth artifact;
- typography status;
- editable/controlled/locked definitions;
- current approval status;
- known reconstruction uncertainties;
- export naming convention.

## 01_APPROVED_REFERENCE Rules

- Preserve the exact approved PNGs.
- Do not crop, retouch, recolor, or resize them independently.
- Keep deterministic slide order.
- Lock all approved reference frames/layers.
- Use these assets for overlay validation.

## 02_EDITABLE_MASTER Rules

This is the only normal working area for manual production changes.

Requirements:

- exact approved frame size;
- textless artwork as controlled base when applicable;
- native live Figma text layers;
- deterministic layer names;
- approved line breaks and hierarchy;
- editable fields separated from controlled/locked fields;
- no silent redesign;
- visual match checked against approved reference.

## 03_STYLE_SYSTEM Rules

Store only reusable approved system assets and specifications.

Examples:

- display serif text style;
- body sans text style;
- emphasis style;
- slide-number style;
- color styles/variables;
- brand mark component;
- approved reusable motifs.

A one-off correction must not be promoted into the style system without human approval.

## 04_EXPORT Rules

Export frames are downstream production outputs.

Requirements:

- derived from the approved editable master;
- exact platform dimensions;
- deterministic slide order;
- correct file naming;
- no hidden reference PNG accidentally included when the editable master is intended to supply final appearance;
- export only after Figma QC passes.

## Overlay Validation

For reconstructed visuals:

1. Keep approved PNG visible as a locked reference.
2. Align editable reconstruction exactly over it.
3. Toggle visibility or change opacity.
4. Compare typography, position, line breaks, artwork registration, visual weight, and color.
5. Record PASS / PASS_WITH_REVISION / FAIL.
6. Hide the reference after validation, but keep it available in the file.

## Figma Runtime Failure Handling

Figma MCP access can be blocked by account plan limits, permission limits, or rate/tool-call limits.

When a Figma write/read operation returns a plan or MCP limit error:

```text
REQUESTED FIGMA OPERATION
        ↓
MCP LIMIT / ACCESS ERROR
        ↓
STOP
        ↓
DO NOT CLAIM THE STRUCTURE WAS APPLIED
        ↓
PRESERVE EXISTING FILE STATE
        ↓
RECORD BLOCKER
        ↓
RETRY ONLY AFTER ACCESS/LIMIT IS AVAILABLE
```

A failed atomic `use_figma` operation must be treated as **NO CHANGE APPLIED** unless the tool explicitly reports created or mutated node IDs.

## Current EBL Test Incident

During the EBL Post 01 restructuring attempt, Figma returned:

`You've reached the Figma MCP tool call limit on the Starter plan.`

Therefore:

- the requested new top-level production structure was **not applied** by that blocked call;
- no mutation should be claimed from that attempt;
- the previously created Figma content remains the last confirmed state;
- restructuring must resume only when MCP access becomes available again.

This incident is operational evidence, not a design failure.

## Decision Gate

The Figma file structure passes when:

- top-level production areas are clearly separated;
- approved references are locked;
- editable masters are identifiable;
- live text is native/editable;
- artwork status is controlled/locked as defined;
- style-system assets are separated from post-specific content;
- export frames are clearly distinguished;
- overlay comparison is possible;
- no approved reference was overwritten;
- all known runtime blockers are resolved or explicitly recorded.

## Output

`FIGMA_STRUCTURED_PRODUCTION_FILE`

Status:

- `STRUCTURED_AND_READY`
- `STRUCTURED_WITH_REVIEW_REQUIRED`
- `BLOCKED_BY_FIGMA_ACCESS`
- `FAILED_QC`
