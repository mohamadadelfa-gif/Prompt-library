# Learn–Structure–Refine Design Token System

## Purpose

Turn approved design evidence into an original, maintainable token system without confusing observed source values with project decisions.

The system combines Prompt Library's evidence controls with a three-tier token architecture:

```text
LEARN -> STRUCTURE -> REFINE
           |
           +-- GLOBAL -> ALIAS -> COMPONENT
```

## 1. Learn

Collect only approved inputs from Strategy, Visual Analysis, Visual DNA, `DESIGN.md`, brand rules, accessibility requirements, platform constraints, and verified design-system references.

For every candidate token, record:

- evidence or decision source;
- information state (`SOURCE`, `DERIVED`, or `DECISION`);
- confidence and scope;
- originality and licensing constraints;
- responsible owner and approval reference.

Learning may propose candidates. It cannot promote observations or third-party tokens into the target system automatically.

## 2. Structure

### Global tokens

Primitive values without product meaning: palette steps, font families, type sizes, spacing, radii, borders, shadows, durations, easing, opacity, and breakpoints.

Examples: `global.color.blue.600`, `global.space.4`, `global.duration.fast`.

### Alias tokens

Semantic roles that reference global tokens. They express intent and theme behavior rather than raw values.

Examples: `alias.text.primary`, `alias.surface.canvas`, `alias.action.primary.background`.

### Component tokens

Component- and state-specific decisions that reference alias tokens wherever possible.

Examples: `component.button.primary.background.default`, `component.input.border.focus`.

Dependencies flow one way only:

```text
COMPONENT -> ALIAS -> GLOBAL
```

Global tokens cannot reference aliases or components. Aliases cannot reference components. Circular references are forbidden. Raw component values require an explicit exception and rationale.

## Themes and Modes

Keep semantic token names stable across themes. Themes change resolved values, not the meaning of token names. Every supported theme must define all required aliases and component states. High-contrast behavior is validated separately; it is not assumed from dark mode.

## 3. Refine

Run refinement after initial creation and after any material change:

1. validate schema, names, references, cycles, and required states;
2. inspect duplicates and near-duplicates;
3. test contrast, focus visibility, touch targets, responsive behavior, and theme parity;
4. preview representative components and edge states;
5. record conflicts and proposed changes;
6. obtain human approval;
7. create a new immutable version and change log.

Refinement may merge redundant tokens, improve naming, or redirect references. It must not silently alter an approved brand meaning or overwrite an earlier version.

## Naming Rules

- lowercase dot-separated paths;
- names express role, not a current visual value;
- no brand names in generic primitives;
- component paths include component, variant, property, and state when applicable;
- deprecated tokens remain resolvable for the declared migration window.

## Required Artifact

Use `design_token_system_schema.json` and begin with `assets/templates/DESIGN_TOKEN_SYSTEM_TEMPLATE.json`. A production record must include provenance, approval, version, supported themes, all three tiers, exceptions, refinement evidence, and gate state.

## Gates

- `PASS`: all references resolve, theme parity holds, required states exist, checks pass, and approval is recorded.
- `CONDITIONAL`: non-critical exceptions have owners and deadlines.
- `BLOCKED`: unresolved references, cycles, missing approval, unsafe source transfer, or critical accessibility failures exist.

## Provenance

The Global–Alias–Component architecture and multi-format/theme approach were informed by `linode/design-language-system`, Copyright 2023 Linode LLC, under Apache License 2.0. This protocol is an original governance implementation; it does not include Linode brand tokens or source code.

## Version

1.0-production-candidate
