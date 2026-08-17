# DESIGN.md Generation Protocol

## Purpose

Convert observable website design evidence into an agent-readable `DESIGN.md` while preserving the Prompt Library distinction between source observations, derived principles, approved target decisions and production outputs.

This protocol adds implementation-oriented token capture to Visual Analysis and Visual DNA. It must not turn third-party website details into automatically approved target design rules.

## Activation

Use when the requested output is a `DESIGN.md`, website design-system record, reusable UI specification, or implementation handoff derived from a live website, screenshot, DOM/CSS source, or existing interface.

It belongs to Stage 08 — Platform / Template Synthesis. Source interpretation remains owned by Visual Analysis and VDNA-001.

## Required Inputs

- explicit source URL, screenshot, DOM/CSS source, or interface artifact;
- approved scope for inspection;
- target use and originality requirements;
- available browser/DOM evidence or an explicit evidence limitation;
- applicable Visual Analysis and `VISUAL_DNA_PACKAGE` outputs.

## Evidence Capture

Capture, when accessible:

- screenshots at relevant viewport sizes;
- DOM structure and meaningful component roles;
- computed colors and CSS custom properties;
- font families, sizes, weights, line heights and letter spacing;
- spacing values, grids, widths and alignment behavior;
- borders, radii, shadows, transparency and elevation;
- buttons, cards, inputs, navigation, badges and their visible states;
- breakpoints, collapsing behavior and touch-target dimensions;
- imagery, iconography, motion and interaction behavior.

Record each extracted value as `SOURCE_OBSERVATION`, including source URL/artifact, viewport, state, capture time and confidence. Sampling frequency does not prove semantic importance.

If a website is inaccessible, authenticated, blocked, dynamically incomplete or protected against inspection, do not guess. Request screenshots or source snippets, reduce confidence, or return `BLOCKED` when the missing evidence is essential.

## Three-Layer Token Rule

Never collapse these layers:

```text
OBSERVED_SOURCE_TOKENS
        ↓ interpretation
TRANSFERABLE_DESIGN_PRINCIPLES
        ↓ human approval / target adaptation
APPROVED_TARGET_TOKENS
```

- `OBSERVED_SOURCE_TOKENS` are evidence and may include exact values.
- `TRANSFERABLE_DESIGN_PRINCIPLES` are derived abstractions with provenance and confidence.
- `APPROVED_TARGET_TOKENS` are project decisions. They must be original, target-appropriate and explicitly approved.

Exact third-party values, proprietary components and distinctive layouts cannot silently enter the target-token layer.

## Originality Firewall

Do not transfer source logos, names, copy, data, screenshots, proprietary components, exact layouts, distinctive navigation, icon sets, illustrations, photographs, mascots or other identity markers.

Rewrite attractive source details through:

```text
source evidence -> abstract design behavior -> original target implementation
```

The final `DESIGN.md` must clearly label source-only observations and target-approved rules. If the user requests a source-faithful internal audit, preserve exact observations in the evidence appendix but do not misclassify them as reusable target rules.

## Required DESIGN.md Structure

Follow `assets/templates/DESIGN_MD_TEMPLATE.md` and include:

1. Evidence, Scope and Confidence
2. Visual Theme and Atmosphere
3. Color Roles and Approved Tokens
4. Typography Rules
5. Component Styling and States
6. Layout and Spacing Principles
7. Depth, Surface and Elevation
8. Imagery, Iconography and Motion
9. Responsive and Interaction Behavior
10. Do / Avoid Guardrails
11. Agent Implementation Guide
12. Source-Only Evidence Appendix

The structure deliberately separates observed source values from approved target values.

## Component-State Requirement

For every applicable interactive component document:

- default;
- hover;
- active/pressed;
- focus-visible;
- disabled;
- loading, error, success or selected state where relevant.

Unknown states remain `UNKNOWN`. Do not infer invisible states solely from a static screenshot.

## Responsive Requirement

Record observed breakpoints only when evidence exists. Otherwise describe responsive principles and mark exact thresholds `UNKNOWN` or `DECISION_REQUIRED`.

Include navigation collapse, grid changes, sidebar behavior, hero/type scaling, media treatment, overflow strategy and a minimum 44px touch-target rule for interactive mobile controls.

## Agent Implementation Guide

The guide must identify:

- authoritative approved target tokens;
- token naming and fallback rules;
- required components and states;
- responsive constraints;
- accessibility and contrast requirements;
- prohibited source-identity transfer;
- applicable Producer Handoff and HTML-production QC;
- unresolved decisions that must not be guessed.

Ready-to-use prompts are optional derived conveniences, not the source of truth.

## Optional Preview

When requested, produce an HTML visual catalog showing approved target colors, type scale, spacing, components, states, surfaces and responsive behavior. The preview must use approved target tokens, not unapproved source values.

The preview is evaluated under `html_visual_production_protocol.md` and `QC-HTML-001_originality_anti_slop_qc.md`.

## Output Contract

- `DESIGN.md` following the canonical template;
- optional machine-readable token record following `design_md_token_schema.json`;
- explicit evidence/confidence and source-only appendix;
- provenance for every material target rule;
- optional preview only when requested;
- canonical gate: `PASS`, `CONDITIONAL` or `BLOCKED`.

When reusable implementation tokens are required, route approved target tokens through `design_token_system_protocol.md`. Structure them as Global, Alias, and Component tiers; the `DESIGN.md` remains the human-readable design authority while the controlled token record is its machine-readable implementation layer.

## Failure Routing

- inaccessible or insufficient source → Visual Analysis / evidence acquisition;
- incorrect source interpretation → Visual Analysis;
- unsafe or non-original transfer → VDNA-001 / originality firewall;
- target-token conflict → Strategy / Art Direction;
- incomplete medium translation → this protocol;
- preview/runtime failure → HTML Visual Production;
- final design-system quality failure → QC.

## Provenance

Adapted conceptually from `wavmson/openclaw-skill-design-md-generator` under the MIT License. The Prompt Library implementation changes the source format to enforce evidence classification, target-token approval, originality controls and integration with the controlled production pipeline.

## Version

1.0-production-candidate

## Status

Active conditional protocol
