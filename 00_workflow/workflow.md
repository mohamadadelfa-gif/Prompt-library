# Controlled Creative Production Workflow

## Purpose

This document defines the execution system for the Prompt Library. The repository is a controlled creative-production system, not a loose collection of prompts.

Each prompt is an executable task or controlled production protocol with a defined input contract, task boundary, output contract, provenance requirements, confidence requirements, and decision gate.

## Core Rule

No stage may silently rewrite upstream facts, requirements, decisions, or approved constraints.

Information is classified as:

- SOURCE — directly supplied or observed evidence.
- DERIVED — an explicit analysis or inference based on source evidence.
- DECISION — an intentional approved creative or project choice.
- OUTPUT — an execution result to be evaluated.

A downstream stage may transform information only within its task boundary.

## Production Pipeline

```text
01 Strategy
   ↓
02 Research
   ↓
03 Visual Analysis
   ↓
04 Named Style Study (when applicable)
   ↓
05 Reference Style Synthesis
   ↓
06 Visual DNA
   ↓
07 Platform / Instagram Template Synthesis
   ↓
08 Art Direction
   ↓
09 Generation
   ↓
10 Content Package
   ↓
11 Human Revision + Style Learning
   ↓
12 Figma Implementation
   ↓
13 Quality Control / Final Approval
```

## Style-Learning Rule

When a brief names a specific artist, movement, school, historical style, or recognizable visual language, the system must study the named style before synthesizing the supplied references.

Use:

`named_style_study.md`

The Named Style Study and Reference Style Synthesis are separate layers:

- **Named Style Study** learns the underlying artistic language and perceptual logic.
- **Reference Style Synthesis** determines what is actually present in the supplied project references and what can transfer responsibly.

Do not skip the study merely because the supplied references appear visually clear.

## Reference Style Synthesis Checkpoint

Reference analysis must answer two separate questions:

1. **What does the reference look like?**
2. **What does the reference make the viewer feel and why?**

The second question is mandatory. Style must be translated through emotional and communication effects rather than through superficial copying of shapes or brush marks.

For the English Beyond Language Instagram system, candidate reference-derived qualities include human, curious, thoughtful, warm, culturally aware, artistic, exploratory, and intelligent. These remain hypotheses until validated against the customer direction.

See `reference_style_synthesis.md`.

## Platform / Instagram Translation Checkpoint

When Instagram is the destination, approved style principles and Visual DNA must be translated into the medium before art direction or generation.

The platform synthesis must define:

- exact format and dimensions
- mobile-first readability
- communication hierarchy
- content zones
- slide roles
- shape and line vocabulary
- texture and brush behavior
- color behavior
- spacing and safe areas
- reusable components
- editable / controlled / locked elements
- Figma implementation requirements

The reference is a style source, not a layout to reproduce.

For painterly or artist-derived references, think in terms of **composition, visual weight, gesture, rhythm, material, and emotional atmosphere** before assigning boxes or coordinates.

See `instagram_template_synthesis.md` and `figma_output_contract.md`.

## Stepwise Human Review

Creative work must be inspectable at controlled checkpoints. Do not generate the full downstream chain before a required checkpoint is approved.

```text
CHECKPOINT 01  Named Style Study
CHECKPOINT 02  Reference Style Synthesis
CHECKPOINT 03  Platform Translation
CHECKPOINT 04  Template Candidate
CHECKPOINT 05  Art Direction
CHECKPOINT 06  Generation Output
CHECKPOINT 07  Human Revision / Style Learning
CHECKPOINT 08  Figma Implementation
CHECKPOINT 09  Final Content Package
```

Use `stepwise_creative_review.md` for checkpoint criteria and gate states.

## Human Feedback & Style Learning Loop

After a generated output is reviewed by a human, capture the result as controlled style knowledge only when the evidence warrants it.

```text
Generated Output
     ↓
Human Revision
     ↓
Approved Output
     ↓
Revision Record
     ↓
Style Knowledge Extraction
     ├── Project Style Reference
     ├── Project Style Rule
     └── System Style Rule
```

The generated output, revised output, and approved output are separate artifacts.

A human revision is not automatically a prompt correction, template change, or style rule.

Style knowledge must be explicitly classified and approved.

## Template Learning Rule

A successful content output may produce a reusable template candidate when its structure is repeatable.

```text
CONTENT INSTANCE
      ↓
TEMPLATE CANDIDATE
      ↓
HUMAN REVIEW
      ↓
APPROVED TEMPLATE
```

The template stores reusable structure, not post-specific content.

A style reference stores an approved visual example.

A style rule stores a generalized aesthetic principle.

Do not collapse these artifact types.

## Figma Rule

Every approved visual output intended for production must have a Figma implementation package.

The Figma master is the editable production artifact, while the generated image remains provenance evidence / visual reference unless explicitly approved as the production asset.

See `figma_output_contract.md`.

## Content Package Rule

A production-ready social asset is not complete until it includes:

- approved visual
- on-canvas copy
- caption
- CTA
- alt text
- publishing metadata
- template relationship
- style-reference relationship where applicable
- Figma implementation
- provenance

See `content_package_contract.md`.

## Execution Loop

For every task or production protocol:

1. Resolve required inputs.
2. Validate preconditions.
3. Execute only the assigned responsibility.
4. Produce the required output schema.
5. Attach provenance and confidence.
6. Run the decision gate.
7. Stop when blocked.
8. Create the controlled handoff package when passed.
9. Preserve original outputs when human revision occurs.
10. Classify the revision before extracting reusable knowledge.

## Failure Policy

The system must stop rather than invent information when a required input is unavailable, contradictory, or insufficient.

Missing information must be represented explicitly as UNKNOWN, not filled with plausible content.

## Revision Routing

When QC identifies a failure, route the failure to the earliest responsible stage rather than automatically regenerating.

- Source / requirement failure → Strategy
- Evidence / research failure → Research
- Reference interpretation failure → Visual Analysis / Named Style Study / Reference Style Synthesis
- Visual rule failure → Visual DNA
- Platform/template structure failure → Platform / Instagram Template Synthesis
- Creative decision failure → Art Direction
- Specification / prompt failure → Generation
- Model execution failure → Generation
- Content packaging failure → Content Package
- Human preference discovered during approved revision → Human Revision / Style Learning
- Figma implementation failure → Figma Implementation
- Final output quality failure → Quality Control
- Acceptable variation → no revision

## Approval Rule

A stage is complete only when its gate is satisfied and its handoff package is complete.

A Named Style Study is complete only when source, observation, interpretation, transferable principles, and confidence are separated.

A style reference or style rule is complete only when approval metadata, scope, provenance, and version are complete.

A reusable Instagram template is complete only when its platform structure, communication hierarchy, component behavior, editable/controlled/locked fields, Figma implementation, provenance, and approval status are complete.

A Content Package is complete only when all required publishable assets are present and approved.

A high numerical score never overrides a critical failure.

## Version

3.0-production-candidate.5

## Status

Active architecture
