# QC-PRES-001 — Presentation Layout and Design-System QC

## Purpose

Validate presentation artifacts created under `presentation_design_dna_protocol.md` without replacing human creative approval.

## Required Evidence

- approved Presentation Design Contract;
- Presentation Blueprint and Page Specs;
- generated HTML/PDF/PPTX artifact as applicable;
- source-level layout-guard report for HTML when Node is available;
- source and asset-role provenance.

## P0 Blocking Checks

- missing or failed `layout_box_budget` for a multi-element slide;
- title/body/card/footer/navigation collisions;
- hidden or clipped readable text;
- unreadable surface/ink pair;
- missing safe-zone reservation;
- reference subject copied, traced, redrawn, or approximated without content-asset approval;
- generic empty image placeholder;
- unplanned CJK or mixed-script orphan line;
- decoration, media, or navigation covering content;
- missing layout-guard report when Node was available.

## P1 Checks

- inconsistent tokens or hierarchy across the deck;
- slide density outside the approved adapter strategy;
- repeated layout without a narrative reason;
- motion inconsistent with Design DNA or unreadable at rest;
- content image introduced after layout planning;
- weak sequence, pacing, or section rhythm.

## Decision

- `APPROVE` — all P0 checks pass and the deck satisfies the approved contract.
- `REVISE` — a correctable layout, hierarchy, sequence, or consistency failure exists.
- `BLOCKED` — required evidence, source content, approval, or executable guard capability is unavailable.

Route each failure to the earliest responsible artifact: Design Contract, Blueprint, Page Specs, Generation, or upstream Visual DNA.

## Version

1.0-production-candidate

## Status

Active conditional QC module
