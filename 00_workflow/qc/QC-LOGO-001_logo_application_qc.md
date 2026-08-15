# QC-LOGO-001 — Logo Application QC

## Purpose

Validate that an approved logo is applied to an existing design without changing the approved design itself, while also confirming that the logo remains optically clear, readable, and non-colliding in the real composition.

This QC is for logo placement / replacement on approved artwork. It does not authorize redesign, typography changes, composition changes, or new decorative treatment.

## Core Principle

```text
LOGO = CONTROLLED VARIABLE
APPROVED DESIGN = LOCKED
```

When the human requests logo placement or replacement:

```text
PLACE / REPLACE LOGO
→ PRESERVE EVERYTHING ELSE
→ TEST ACTUAL OPTICAL CLEARANCE
```

A geometrically consistent placement is not automatically a visually correct placement.

---

## Required Inputs

- approved / locked design artifact;
- approved logo master;
- human placement instruction;
- target output dimensions;
- existing-logo state (present / absent);
- requested anchor / size rule;
- multi-slide set when consistency is required;
- review preview at realistic viewing size.

---

# Mandatory Gates

## LOGO-01 Master Fidelity — mandatory

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

If the human explicitly approves a production variant, such as a small-use version, that variant must be recorded and then used consistently. Do not create per-slide logo surgery silently.

Failure => FAIL.

## LOGO-02 Design Preservation — mandatory

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

## LOGO-03 Fixed Anchor Consistency — mandatory for carousel / multi-slide systems

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

## LOGO-04 Existing Logo Replacement — mandatory

If an old logo exists:

- remove / cover only the old logo area;
- replace it with the approved logo;
- do not alter nearby design elements to make room.

If no old logo exists:

- add the approved logo at the defined anchor;
- do not move surrounding content.

## LOGO-05 Clarity Without Extra Objects — mandatory

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

## LOGO-06 Scale / Hierarchy

Check that the logo:

- is large enough to remain identifiable;
- is not so large that it competes with the content;
- preserves its aspect ratio;
- is not distorted;
- remains consistent across related assets.

## LOGO-07 Edge / Crop Safety

Check:

- no accidental clipping;
- sufficient distance from output edges;
- logo remains fully visible;
- no unintended overlap that obscures the logo.

Do not solve overlap by moving other approved design elements.

## LOGO-08 Human Review — mandatory

Logo placement is not final until the human reviews the multi-slide preview and explicitly approves:

- master fidelity;
- position;
- scale;
- clarity;
- consistency;
- preservation of the original design.

AI QC cannot grant final approval.

## LOGO-09 Optical Bounds & Clear-Space — mandatory

Do not assess the logo only by its image rectangle or bounding box.

Distinguish:

```text
GEOMETRIC BOUNDS = file / layer rectangle
OPTICAL BOUNDS = actual visible outermost logo elements
```

The clear-space test must use the optical bounds.

Check every visible extreme element, including:

- long vertical or horizontal lines;
- dots;
- protruding arches;
- extended shapes;
- glow / halo if part of the approved master;
- typography extending beyond the main symbol mass.

The logo fails this gate if any visible logo element:

- touches text;
- crosses text;
- visually merges with a letterform;
- touches an unrelated design element in a way that creates ambiguity;
- enters a reading zone and competes with content;
- appears attached to a nearby element unintentionally.

A fixed coordinate can still FAIL if optical clearance fails.

## LOGO-10 Worst-Case Slide Test — mandatory for multi-slide systems

For a carousel using one fixed logo position, do not approve the placement by checking an average slide.

Identify the slide with the smallest available clear-space around the logo anchor.

```text
TEST MOST CONSTRAINED SLIDE FIRST
→ DEFINE UNIVERSAL SIZE / ANCHOR
→ APPLY IDENTICALLY TO ALL SLIDES
```

If one slide fails, the universal logo placement fails.

Preferred correction order:

1. preserve all approved slide content;
2. preserve the approved logo master;
3. adjust universal logo scale if allowed;
4. adjust universal anchor if allowed;
5. re-test all slides;
6. only alter internal logo geometry if the human explicitly approves a reusable logo variant.

Do not solve a single-slide collision by moving text, resizing text, moving artwork, or silently changing only that slide's logo.

---

# Logo Usage Assessment — 100 Points

The score supports diagnosis but cannot override a mandatory-gate failure.

| Assessment Area | Weight |
|---|---:|
| Master Fidelity | 20 |
| Design Preservation | 15 |
| Optical Clear-Space / Collision Safety | 20 |
| Scale & Legibility | 15 |
| Multi-slide Position Consistency | 10 |
| Visual Hierarchy / Secondary Presence | 10 |
| Edge / Crop Safety | 5 |
| Clean Application / No Extra Objects | 5 |
| **TOTAL** | **100** |

## Result Bands

```text
90–100  PASS_FOR_HUMAN_REVIEW
80–89   REVISION_REQUIRED
Below 80 FAIL
```

Any mandatory-gate failure => FAIL or REVISION_REQUIRED regardless of numerical score.

---

# Assessment Questions

Before presenting a logo-placement review, answer:

1. Is this the exact approved logo master or approved variant?
2. Are all non-logo pixels / elements preserved?
3. Is the logo at the required fixed coordinate and size?
4. What are the logo's actual optical bounds?
5. What is the nearest text or design element to those optical bounds?
6. Is there visible breathing room between the logo and that element?
7. Does any line, dot, glow, or protruding logo element enter the reading zone?
8. Is the logo legible at realistic Instagram viewing size?
9. Is the logo visually secondary to the slide content?
10. For a carousel, which slide is the worst-case clearance slide?
11. Does that worst-case slide pass without changing the approved design?
12. Were any extra support objects added around the logo?
13. Has the human approved the review candidate?

---

# EBL Carousel Application Rule

For English Beyond Language Post 01:

- use the chosen Geometric Reader Integrated Logo master or a human-approved reusable small-use variant;
- do not regenerate it;
- use one identical fixed bottom-left anchor on all six slides;
- use one identical logo size on all six slides;
- keep the logo clear but not eye-catching;
- add no extra object around the logo;
- do not change any text size, font, line break, alignment, shape, painterly form, color, texture, numbering, or composition;
- if an old logo exists, replace only that logo area;
- if no logo exists, add the chosen logo at the fixed anchor without changing the design;
- assess optical bounds, not just the 185×185 or other placement rectangle;
- Slide 1 is currently a known stress case because the final copy line extends lower toward the logo zone;
- any universal logo placement must pass Slide 1 before being approved for all six slides.

The exact placement coordinates remain a review candidate until human approval.

---

# Review Output

Before final production, provide:

1. six-slide contact sheet;
2. identical-logo-position check;
3. identical-logo-size check;
4. optical-clearance check;
5. worst-case-slide identification;
6. note confirming no non-logo changes were authorized;
7. assessment score + mandatory-gate result;
8. HUMAN APPROVAL gate.

---

# Result States

```text
PASS_FOR_HUMAN_REVIEW
PASS
REVISION_REQUIRED
FAIL
```

A mandatory-gate failure overrides any subjective visual score.

---

## Learned Failure Pattern — 2026-08-15

Observed issue:

A logo could pass fixed-coordinate and pixel-preservation checks while a thin vertical logo line still entered the Slide 1 text zone.

Root cause:

- QC evaluated placement geometry more strongly than optical clearance;
- the logo's tall internal line extended beyond the apparent main visual mass;
- Slide 1 had the lowest text block and therefore the smallest available clear-space.

Learning promoted into QC:

```text
BOUNDING-BOX CONSISTENCY ≠ VISUAL CLEARANCE
```

Future logo assessment must verify the actual visible extremes of the logo against the nearest content before approval.
