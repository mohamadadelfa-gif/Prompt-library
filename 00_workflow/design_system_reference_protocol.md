# Design-System Reference Protocol

## Purpose

Use established design systems as research evidence without silently importing their brand identity, proprietary assets, components, or implementation decisions into a project.

This protocol adapts the useful cataloging idea from `DragorWW/awesome-design-language-system` into a governed reference layer for Prompt Library.

## Activation

Use during Research, Visual Analysis, Visual DNA, Design DNA, `DESIGN.md`, presentation, HTML, or platform-template work when an external design-system precedent would materially support a decision.

## Reference Selection

Start with `design_system_reference_registry.json`. Select no more than three references for a single decision and record why each applies to the target medium, audience, accessibility needs, and technical environment.

Prefer an official maintained source whose scope matches the target, documents accessibility and interaction behavior, and has explicit usage terms. Inclusion in the registry does not prove that every linked rule is current. Revisit the official URL and record the verification date, inspected page, and any access limitation.

## Evidence Boundary

Classify external guidance as `SOURCE`. A comparison or abstraction is `DERIVED`. A rule becomes a project `DECISION` only after target-specific adaptation and approval.

```text
OFFICIAL REFERENCE -> SOURCE EVIDENCE -> DERIVED PRINCIPLE -> APPROVED TARGET RULE
```

Never copy a source system's logo, brand colors, proprietary typeface, icons, illustrations, distinctive component appearance, wording, or code unless its terms and project authorization explicitly permit it.

## Required Decision Record

Record the registry ID and official page, verification date, reason for selection, observed guidance, derived principle, approved original target rule, confidence, conflicts, and any license or usage constraints.

If authoritative systems disagree, do not average them. Select according to the approved audience, platform, accessibility, and brand requirements, and explain the conflict.

## Integration

- `design_md_generation_protocol.md`: references support transferable principles, never automatic target tokens.
- `presentation_design_dna_protocol.md`: use references for layout, accessibility, data-display, and interaction reasoning, not style cloning.
- `html_visual_production_protocol.md`: verify states, responsive behavior, semantics, and accessibility against applicable official guidance.
- `named_style_study.md`: keep named style evidence separate from reusable project decisions.

## Gate

- `PASS`: official source verified, applicability explained, evidence and decisions separated.
- `CONDITIONAL`: currency, access, or licensing remains uncertain.
- `BLOCKED`: the decision depends on unverifiable guidance or unauthorized copying.

## Provenance

The curated-reference concept was adapted from `DragorWW/awesome-design-language-system` under the MIT License. Prompt Library uses a smaller official-source registry with freshness, applicability, evidence-state, originality, and approval controls.

## Version

1.0-production-candidate
