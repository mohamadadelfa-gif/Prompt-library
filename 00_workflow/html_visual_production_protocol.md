# HTML Visual Production Protocol

## Purpose

Translate approved project context and Visual DNA into an original HTML visual artifact for websites, landing pages, interfaces, dashboards, prototypes, posters, cards, carousels, or other browser-rendered formats.

This protocol extends the Prompt Library's downstream production capability. It does not replace Visual Analysis, VDNA-001, platform synthesis, Art Direction, Generation, or Quality Control.

## Activation

Use when HTML is the requested production medium or the most appropriate editable visual source. Presentation HTML remains governed additionally by `presentation_design_dna_protocol.md`.

## Production Input Priority

Resolve production inputs in this order:

1. `PRODUCER_HANDOFF` — approved, target-specific production contract;
2. approved `VISUAL_DNA_PACKAGE` plus approved Strategy and Art Direction;
3. standalone approved brief when no Visual DNA is required.

Higher-priority input cannot be silently overridden by a lower-priority input. Real target context—code, copy, data, screenshots, assets, URLs, requirements, and brand material—must be read before structure or content is invented.

## Artifact Routing

Route the target before authoring:

| Target | Primary HTML artifact | Critical adaptation |
|---|---|---|
| Website / landing page | Responsive page | Narrative hierarchy and conversion path |
| App UI | Interactive prototype | States, affordances and realistic task flow |
| Dashboard | Dense dashboard | Scan path, filters, data hierarchy and states |
| Presentation | Fixed-stage HTML deck | Use presentation protocol, slide rhythm and layout guard |
| Poster | Fixed-canvas HTML poster | Single-glance hierarchy and export dimensions |
| Social card / carousel | Fixed or responsive card set | Mobile-first hierarchy and per-card role |
| Product prototype | Clickable HTML prototype | Navigation, state transitions and feedback |

If the target remains materially ambiguous, stop with `BLOCKED` rather than generate the wrong medium.

## Brand Modes

### BRANDLESS

Default when no approved target-brand context exists. Use approved Visual DNA and the new brief without inventing a brand identity or requiring a hidden brand path.

### BRAND_ON

Activate only when the user supplies or explicitly authorizes target-brand assets, rules, tokens, typography, voice, components, or existing brand evidence.

Keep the layers separate:

```text
source references -> abstract transferable Visual DNA
target brand -> authorized identity layer
new brief -> content, purpose and audience
```

When target-brand rules conflict with reference-derived DNA, target-brand identity governs marks, palette, typography and voice. Visual DNA may still guide mood, composition, rhythm, density and interaction behavior where compatible.

## Originality Firewall

Use the transformation:

```text
observed source detail -> abstract principle -> original target implementation
```

Transferable material may include mood, energy, density, color-role behavior, hierarchy rhythm, spacing logic, grid tendencies, abstract component behavior, material qualities, imagery logic, motion feeling and composition grammar.

Do not transfer source logos, names, slogans, exact copy, protected layouts, proprietary components, distinctive navigation structures, source data, screenshots, icon sets, illustrations, photos, mascots or identity markers.

Before delivery, all answers must be `No`:

- Could a viewer mistake the artifact for the source brand?
- Did an exact source layout, asset, copy block or proprietary component survive?
- Does the artifact display the old reference instead of solving the new brief?
- Does the result depend on brand context that was never supplied or approved?

If any answer is `Yes`, revise. After two unsuccessful revisions, omit the disputed transfer and mark the artifact `CONDITIONAL` or `BLOCKED` according to severity.

## Producer Handoff

Before generation, produce the contract defined in `producer_handoff_schema.json`. It must identify:

- production brief and target route;
- authoritative inputs and real target context;
- approved Visual DNA rules and tokens;
- brand mode and authorized brand evidence;
- transferable and non-transferable source elements;
- content/data policy;
- engineering and quality checks;
- unknowns, assumptions, provenance and approval.

## Content Integrity

- Use supplied copy and data where available.
- Never invent claims, testimonials, metrics, prices, research findings or product capabilities.
- Use clearly marked placeholders only when structure cannot be demonstrated otherwise.
- Ask before adding major sections, screens or content beyond the approved brief.
- Every visual element must serve information, navigation, interaction, emphasis or intentional rhythm.

## Anti-Slop Gate

Block delivery when the artifact relies on filler, fake data, unnecessary icons, decorative clutter, repetitive generic cards, arbitrary gradients, random emoji, meaningless glass panels, decorative blobs, sparkle/orbit motifs, stock-like abstract SVGs or other unsupported AI-default styling.

Require:

- clear hierarchy, spacing, scale, rhythm and alignment;
- medium-appropriate density and interaction;
- deliberate typography rather than an unexamined default font stack;
- colors grounded in approved DNA or brand evidence;
- realistic states and content behavior;
- an original composition solving the target brief.

## HTML Engineering Contract

- Prefer a self-contained HTML file unless the project requires a multi-file implementation.
- Use descriptive artifact names.
- Do not reference unavailable local-only assets.
- Pin external runtime dependencies to exact versions and use integrity metadata when supported.
- Avoid duplicate global identifiers and unsafe cross-script assumptions.
- Do not call `scrollIntoView()` in embedded prototypes; control the intended container directly.
- Fixed-canvas artifacts must scale uniformly without clipping external controls.
- Mobile interaction targets must be at least 44px.
- Presentation text and layout must also satisfy the presentation protocol.
- Preserve current position for decks or other position-bearing artifacts when iterative refresh would otherwise lose user state.
- Validate balanced markup, reachable dependencies, runtime errors, responsive/fixed-stage behavior and requested interactions before handoff.

## Output Contract

Deliver:

- primary HTML artifact;
- selected artifact route;
- brand mode;
- authoritative production-input class;
- provenance summary;
- originality and anti-slop gate result;
- limitations or unresolved manual work.

Secondary exports, prompts, tokens or outlines are produced only when requested or required by another approved contract.

## Failure Routing

- missing or contradictory target context → Strategy / Project Reconciliation;
- unsupported source interpretation → Visual Analysis;
- faulty transferable visual rule → VDNA-001;
- wrong medium or structure → Platform / Template Synthesis;
- weak concept or target adaptation → Art Direction;
- HTML/runtime failure → Generation;
- originality or anti-slop failure → this protocol, then earliest responsible upstream stage;
- final quality failure → QC.

## Provenance Note

This original Prompt Library protocol was informed by the public repository `BruceL017/visual-dna-skills`, specifically its published concepts of producer handoff priority, artifact routing, optional brand integration, originality separation and anti-slop review. No upstream source code or skill text is incorporated because the repository did not provide a license at the time of review.

## Version

1.0-production-candidate

## Status

Active conditional protocol
