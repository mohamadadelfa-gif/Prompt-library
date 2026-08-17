# Presentation Design DNA Protocol

## Purpose

Translate an approved `VISUAL_DNA_PACKAGE` into a traceable, scenario-specific presentation system and, when requested, an HTML-first slide deck. This protocol adapts the useful Design DNA concepts from PPT-Design-DNA to the Prompt Library's controlled 15-stage production process.

## Activation

Run this protocol only when the target artifact is a presentation, slide deck, PowerPoint/PPTX, or HTML presentation.

It belongs to Stage 08 — Platform / Template Synthesis. It does not replace Strategy, Research, Visual Analysis, Visual DNA, Art Direction, Generation, or final QC.

## Required Inputs

- approved strategy and presentation purpose;
- approved `VISUAL_DNA_PACKAGE` from VDNA-001;
- presentation target and delivery format;
- explicit content source or an `UNKNOWN` record;
- approved reference roles distinguishing `STYLE_REFERENCE` from `CONTENT_ASSET`.

## Core Invariants

1. Reference images provide style evidence only unless the user explicitly approves them as content assets.
2. Identifiable reference subjects, characters, products, objects, silhouettes, and subject parts must not be copied, traced, redrawn, or approximated as decoration.
3. The approved Visual DNA is the source of truth. A Design Profile, Design Adapter, or generated prompt is a derived artifact.
4. A reusable Design Profile is created only after explicit human approval.
5. Saved profile versions are immutable. Tuning creates a new version plus a Design Diff.
6. Existing deck content remains source-locked unless the user explicitly authorizes rewriting.
7. Unknown topic, audience, content, or export requirements remain `UNKNOWN`; they are not silently defaulted before the relevant decision gate.

## Controlled Gates

### Gate 1 — Design Source

Select exactly one source:

- approved project Visual DNA;
- an explicitly selected saved Design Profile or Adapter;
- a new reference-derived candidate routed through Visual Analysis and VDNA-001;
- no-image Design Discovery routed through the normal evidence, decision, and approval layers.

### Gate 2 — Design DNA Confirmation

Present the active candidate with:

- Mood, Composition, Visual, Content Strategy, and Presentation layers;
- adjustable density, whitespace, hierarchy, imagery, chart, typography, grid, and motion parameters;
- design tokens, negative constraints, fit risks, and reference-subject firewall;
- execution consequences and best/risky presentation scenarios.

Stop for human confirmation or tuning. Do not collect detailed deck requirements before this gate passes.

### Gate 3 — Presentation Requirements

After Design DNA approval, collect topic, purpose, audience, content source, page count, density, narrative form, image strategy, and output needs. Prefer numbered option-first choices, with a custom escape hatch.

### Gate 4 — Scenario Fit and Adapter

Check whether the active Visual DNA can safely carry the content. If it conflicts, offer:

- `VISUAL_FIRST` — preserve expression and compress content;
- `DYNAMIC_DOWNGRADE` — reduce expression to improve density/readability;
- `CELL_DIVISION` — preserve expression and split content across more slides.

An accepted adaptation creates a derived, named `DESIGN_ADAPTER`; it does not overwrite Visual DNA.

### Gate 5 — Generation and Delivery

Generate only after the approved Design Contract, Blueprint, and Page Specs exist. HTML decks cannot be handed off until the source-level layout guard passes when Node is available.

## Required Artifacts

### Presentation Design Contract

Record:

- Visual DNA/profile/adapter identity and provenance;
- rules to preserve and rules allowed to adapt;
- density and slide-splitting strategy;
- typography, chart, formula, image, motion, and accessibility rules;
- approved content assets and prohibited reference-derived subjects;
- minimum type sizes, contrast targets, safe margins, and navigation reservation;
- forbidden failure patterns.

### Presentation Blueprint

For every slide record:

- sequence and section;
- title and page purpose;
- core message and content role;
- density class;
- layout capacity/archetype;
- visual or content-image strategy;
- narrative transition.

### Page Specs

Every slide must define:

- purpose, core message, and source IDs;
- content limits and required elements;
- layout zones and safe/no-text zones;
- surface/ink token pairs for readable regions;
- image role, ratio, fit, caption, and fallback when applicable;
- `visual_subject_policy`;
- `mechanical_layout_preflight`;
- `layout_box_budget` for every slide with more than one major element;
- failure response: recompose, reduce copy, reduce title size slightly, change layout, or split the slide.

## HTML-First Rules

- Use a fixed 1920×1080 internal stage scaled uniformly to the viewport.
- Keep readable content inside declared safe zones.
- Every major readable element must expose a meaningful `data-zone`.
- Reserve navigation and footer zones before placing content.
- Declare explicit surface and ink tokens; body text should meet 4.5:1 contrast and large display text at least 3:1.
- Do not use empty generic image placeholders. Use approved assets, diagrams, typography, abstract non-subject visuals, or intentional whitespace.
- Do not hide text overflow or use z-index to conceal a failed layout.
- Manually plan CJK and mixed-script display line breaks; avoid orphaned one- or two-character final lines.
- Motion must preserve a readable final resting state.

## Mechanical Layout Preflight

Before authoring HTML, calculate each readable zone's required height from expected lines, font size, line height, glyph padding, effects, internal padding, and declared gaps. Check title/body, title/card, body/card, card/navigation, footer/navigation, text/visual, and text/decoration collision pairs.

A failed budget must change the source plan. It must not be patched with hidden overflow, compressed line height, layering, or unreadably small type.

## Source-Level Layout Guard

When an HTML deck is generated and Node is available, run:

```powershell
node scripts/ppt-layout-guard.js <output-html> --report <output-dir>/layout-guard-report.json
```

The guard report is required delivery evidence. A P0 result blocks handoff and routes revision to Page Specs or the Design Contract. Browser screenshots, page-count checks, and file-existence checks do not replace this guard.

If Node is genuinely unavailable, perform the equivalent source-level checks manually and mark the result `CONDITIONAL`, including the missing automated evidence.

## Profile Persistence

Do not create `design-profiles/` by default. When the user explicitly approves saving a reusable profile, follow `presentation_design_profile_schema.json` and record immutable versions, provenance, approved scope, risks, and negative constraints.

## Handoff

Pass the approved Presentation Design Contract, Blueprint, Page Specs, generated artifact, and layout-guard report to Stage 15 Quality Control. Persist transient planning artifacts only when the user requests inspection, audit, editing, or regeneration from specifications.

## Failure Routing

- unsupported or missing content → Strategy / Research;
- misread reference → Visual Analysis;
- faulty visual-system rule → Visual DNA;
- scenario/profile mismatch → this protocol's Adapter gate;
- crowded or colliding slide → Page Specs / Blueprint;
- rendering or model failure → Generation;
- failed layout guard → Page Specs, then rerun the guard;
- broader quality failure → Stage 15 QC and earliest responsible stage.

## Provenance

Adapted from the installed `PPT-Design-DNA` skill under Apache-2.0. The Prompt Library implementation is a project-specific protocol and must retain applicable upstream attribution and license notices when redistributed.

## Version

1.0-production-candidate

## Status

Active conditional protocol
