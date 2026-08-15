# QC-LOGO-001 — Logo Application QC

## Purpose

Validate that an approved logo is applied to an existing design without changing the approved design itself.

This QC is for logo placement / replacement on approved artwork. It does not authorize redesign, typography changes, composition changes, or new decorative treatment.

## Core Principle

```text
LOGO = VARIABLE
APPROVED DESIGN = LOCKED
```

When the human requests logo placement or replacement:

```text
PLACE / REPLACE LOGO
→ PRESERVE EVERYTHING ELSE
```

## Required Inputs

- approved / locked design artifact
- approved logo master
- human placement instruction
- target output dimensions
- existing-logo state (present / absent)
- requested anchor / size rule

## Mandatory Gates

### LOGO-01 Master Fidelity — mandatory

Use the approved logo master as the source of truth.

Check:

- exact logo artwork is used;
- no regenerated substitute;
- no altered geometry;
- no altered color;
- no altered typography;
- no altered tracking / spacing;
- no unauthorized crop;
- no unauthorized background / glow removal;
- no unauthorized simplification.

Failure => FAIL.

### LOGO-02 Design Preservation — mandatory

Everything outside the explicitly authorized logo area must remain unchanged.

Do not change:

- text content;
- text size;
- font;
- line breaks;
- text alignment;
- text shape;
- design shapes;
- illustration elements;
- colors;
- texture;
- numbering;
- spacing;
- composition;
- background artwork.

If a non-logo element changes without explicit instruction => FAIL.

### LOGO-03 Fixed Anchor Consistency — mandatory for carousel / multi-slide systems

When the human specifies one consistent logo position, the logo must use the same:

- X coordinate;
- Y coordinate;
- left-edge distance;
- bottom-edge distance;
- width;
- height / proportions;
- optical scale;

on every slide.

Do not reposition the logo to suit individual slide compositions unless the human explicitly authorizes per-slide placement.

Failure => FAIL.

### LOGO-04 Existing Logo Replacement — mandatory

If an old logo exists:

- remove / cover only the old logo area;
- replace it with the approved logo;
- do not alter nearby design elements to make room.

If no old logo exists:

- add the approved logo at the defined anchor;
- do not move surrounding content.

### LOGO-05 Clarity Without Extra Objects — mandatory

The logo must remain visually clear without adding unrelated support graphics.

Do not add:

- extra frames;
- extra circles;
- extra stars;
- extra dots;
- extra lines;
- extra shadows;
- extra labels;
- extra decorative shapes;
- extra background panels;

unless they are part of the approved logo master itself or explicitly requested by the human.

The logo should be readable but visually secondary when used as a signature.

### LOGO-06 Scale / Hierarchy

Check that the logo:

- is large enough to remain identifiable;
- is not so large that it competes with the content;
- preserves its aspect ratio;
- is not distorted;
- remains consistent across related assets.

### LOGO-07 Edge / Crop Safety

Check:

- no accidental clipping;
- sufficient distance from output edges;
- logo remains fully visible;
- no unintended overlap that obscures the logo.

Do not solve overlap by moving other approved design elements.

### LOGO-08 Human Review — mandatory

Logo placement is not final until the human reviews the multi-slide preview and explicitly approves:

- master fidelity;
- position;
- scale;
- clarity;
- consistency;
- preservation of the original design.

AI QC cannot grant final approval.

## EBL Carousel Application Rule

For English Beyond Language Post 01:

- use the chosen Geometric Reader Integrated Logo master;
- do not regenerate it;
- use one identical fixed bottom-left anchor on all six slides;
- use one identical logo size on all six slides;
- keep the logo clear but not eye-catching;
- add no extra object around the logo;
- do not change any text size, font, line break, alignment, shape, painterly form, color, texture, numbering, or composition;
- if an old logo exists, replace only that logo area;
- if no logo exists, add the chosen logo at the fixed anchor without changing the design.

The exact placement coordinates remain a review candidate until human approval.

## Review Output

Before final production, provide:

1. six-slide contact sheet;
2. identical-logo-position check;
3. identical-logo-size check;
4. note confirming no non-logo changes were authorized;
5. HUMAN APPROVAL gate.

## Result States

```text
PASS_FOR_HUMAN_REVIEW
PASS
REVISION_REQUIRED
FAIL
```

A mandatory-gate failure overrides any subjective visual score.
