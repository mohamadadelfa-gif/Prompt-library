# QC-HTML-001 — HTML Originality and Anti-Slop QC

## Purpose

Evaluate browser-rendered visual artifacts for source independence, content integrity, medium fit and non-generic design quality.

## Required Evidence

- approved `PRODUCER_HANDOFF`;
- source/target/brand role classification;
- HTML artifact and applicable runtime evidence;
- approved Visual DNA, Strategy and Art Direction when used.

## P0 Blocking Checks

- source identity, exact layout, exact copy, asset or proprietary component survives;
- unauthorized logo, brand asset or target-brand rule is used;
- unsupported claim, testimonial, metric, price, capability or research finding is presented as fact;
- real target context was ignored;
- artifact route materially conflicts with the requested medium;
- HTML does not open or execute its required core behavior;
- brand mode is unresolved or `BRAND_ON` lacks authorized evidence.

## P1 Checks

- filler content or unmarked placeholders;
- arbitrary gradients, glass cards, blobs, sparkles, emoji, icons or decorative SVGs;
- repetitive generic card grids without informational purpose;
- default-looking typography without an approved rationale;
- weak hierarchy, spacing, scale, alignment, interaction or responsive behavior;
- Visual DNA used as a template copy instead of abstract direction;
- unnecessary secondary outputs or invented sections.

## Originality Questions

All must resolve to `No`:

1. Could the artifact be mistaken for the reference brand?
2. Did an exact reference layout, asset, copy block or proprietary component survive?
3. Does the artifact reproduce the old reference instead of solving the target brief?
4. Does it depend on brand context that was never supplied or authorized?

## Decision

- `APPROVE` — no P0 failures and the artifact passes the approved quality threshold.
- `REVISE` — one or more correctable P1 failures exist.
- `BLOCKED` — required evidence or essential target context is unavailable.

Route failures to the Producer Handoff, Platform Synthesis, Art Direction, Generation or earliest responsible upstream stage.

## Version

1.0-production-candidate

## Status

Active conditional QC module
