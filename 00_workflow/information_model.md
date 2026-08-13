# Information Model

The system distinguishes four states of information.

## SOURCE

Directly supplied, observed, measured, or cited information.

Examples:

- customer statement
- research source
- observed visual property
- technical specification

Source information must not be silently rewritten.

## DERIVED

An analysis, classification, interpretation, pattern, or hypothesis derived from source information.

Derived information must identify its supporting source(s) and confidence.

## DECISION

An intentional project or creative choice made by an authorized stage or human decision-maker.

A decision is not evidence. It may be evaluated, changed, or superseded, but it must remain identifiable as a decision.

## OUTPUT

A generated artifact or execution result, including generated images, concepts, or production specifications.

Outputs are evaluated against approved decisions and requirements; they do not automatically become new requirements.

## Forbidden State Changes

The system must never silently perform:

SOURCE → DECISION
DERIVED → SOURCE
OUTPUT → REQUIREMENT
ASSUMPTION → FACT

Any such transition requires explicit evidence or an explicit decision.
