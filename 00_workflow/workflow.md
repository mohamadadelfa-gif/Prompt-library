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
05 Motif & Sign Extraction (when applicable)
   ↓
06 Reference Style Synthesis
   ↓
07 Visual DNA
   ↓
08 Platform / Instagram Template Synthesis
   ↓
09 Art Direction
   ↓
10 Generation
   ↓
11 Content Package
   ↓
12 Human Revision + Style Learning
   ↓
13 Editable Reconstruction Preparation (when approved output is raster/flattened)
   ↓
14 Figma Implementation
   ↓
15 Quality Control / Final Approval
```

## Style-Learning Rule

When a brief names a specific artist, movement, school, historical style, or recognizable visual language, the system must study the named style before synthesizing the supplied references.

Use:

`named_style_study.md`

The Named Style Study and Reference Style Synthesis are separate layers:

- **Named Style Study** learns the underlying artistic language and perceptual logic.
- **Motif & Sign Extraction** builds an evidence-backed vocabulary of recurring signs, shapes, objects, marks, and material behaviors.
- **Reference Style Synthesis** determines what is actually present in the supplied project references and what can transfer responsibly.

Do not skip the study or motif extraction merely because the supplied references appear visually clear.

## Motif & Sign Extraction Checkpoint

When a named style is applicable, extract its recurring visual vocabulary before creating an Instagram template.

The extraction must identify:

- recurring signs and symbols
- recurring shape families
- significant recurring objects or object-like forms
- mark types and gesture behavior
- material / brush behaviors that function as visual motifs
- frequency across the reference set
- formal role
- semantic role only when supported by evidence
- emotional effect only when supported by evidence
- transferability and risk

The extraction must preserve the observed formal character without reproducing a specific artwork or composition.

The output is a controlled motif library, not a final brand library.

See `motif_extraction.md` and `motif_library_schema.json`.

## Reference Style Synthesis Checkpoint

Reference analysis must answer two separate questions:

1. **What does the reference look like?**
2. **What does the reference make the viewer feel and why?**

The second question is mandatory. Style must be translated through emotional and communication effects rather than through superficial copying of shapes or brush marks.

For the English Beyond Language Instagram system, candidate reference-derived qualities include human, curious, thoughtful, warm, culturally aware, artistic, exploratory, and intelligent. These remain hypotheses until validated against the customer direction.

See `reference_style_synthesis.md`.

## Platform / Instagram Translation Checkpoint

When Instagram is the destination, approved style principles, the motif library, and Visual DNA must be translated into the medium before art direction or generation.

The platform synthesis must define:

- exact format and dimensions
- mobile-first readability
- communication hierarchy
- content zones
- slide roles
- shape and line vocabulary
- approved motif usage
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
CHECKPOINT 02  Motif & Sign Extraction
CHECKPOINT 03  Reference Style Synthesis
CHECKPOINT 04  Platform Translation
CHECKPOINT 05  Template Candidate
CHECKPOINT 06  Art Direction
CHECKPOINT 07  Generation Output
CHECKPOINT 08  Human Revision / Style Learning
CHECKPOINT 09  Editable Reconstruction Preparation (when applicable)
CHECKPOINT 10  Figma Implementation
CHECKPOINT 11  Final Content Package
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

A motif library stores recurring visual vocabulary extracted from source/style evidence.

Do not collapse these artifact types.

## Editable Reconstruction Preparation Rule

When an approved visual intended for production is rasterized, flattened, generated, or otherwise not directly editable, run:

`editable_reconstruction_preparation.md`

before Figma implementation.

The protocol must:

- lock and preserve the approved PNG as the visual source of truth;
- inventory text, raster artwork, simple vectors/signs, and brand assets;
- derive textless artwork only where editable reconstruction requires it;
- classify reconstructed hidden pixels as DERIVED;
- preserve non-text artwork and composition;
- create an editable layer map;
- create a typography reconstruction specification;
- pass textless-artwork QC;
- produce a complete Figma handoff package.

The approved PNG, textless artwork, and Figma master are separate artifacts.

A textless reconstruction must not become a new art direction or replace the approved PNG as provenance evidence.

## Figma Rule

Every approved visual output intended for production must have a Figma implementation package.

The Figma master is the editable production artifact, while the generated/approved image remains provenance evidence and visual reference unless explicitly approved as the production asset.

When Editable Reconstruction Preparation applies, the approved PNG should remain available in Figma as a locked reference and the editable reconstruction should be validated against it using overlay/visibility comparison.

See `editable_reconstruction_preparation.md` and `figma_output_contract.md`.

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
- Reference interpretation failure → Visual Analysis / Named Style Study / Motif & Sign Extraction / Reference Style Synthesis
- Motif extraction failure → Motif & Sign Extraction
- Visual rule failure → Visual DNA
- Platform/template structure failure → Platform / Instagram Template Synthesis
- Creative decision failure → Art Direction
- Specification / prompt failure → Generation
- Model execution failure → Generation
- Content packaging failure → Content Package
- Human preference discovered during approved revision → Human Revision / Style Learning
- source-lock / text-removal / reconstruction artifact failure → Editable Reconstruction Preparation
- missing or uncertain typography required for reconstruction → Human Typography Review / Editable Reconstruction Preparation
- Figma implementation mismatch after correct reconstruction preparation → Figma Implementation
- Final output quality failure → Quality Control
- Acceptable variation → no revision

## Approval Rule

A stage is complete only when its gate is satisfied and its handoff package is complete.

A Named Style Study is complete only when source, observation, interpretation, transferable principles, and confidence are separated.

A Motif & Sign Extraction is complete only when the motif library is evidence-backed, frequency is recorded, formal character is preserved, and provenance/confidence are captured.

A style reference or style rule is complete only when approval metadata, scope, provenance, and version are complete.

A reusable Instagram template is complete only when its platform structure, communication hierarchy, component behavior, approved motif usage, editable/controlled/locked fields, Figma implementation, provenance, and approval status are complete.

An Editable Reconstruction Package is complete only when the approved raster source is preserved, textless artwork passes QC, reconstructed regions are classified as DERIVED, editable elements are mapped, typography uncertainty is recorded, and the Figma handoff package is complete.

A Figma implementation reconstructed from a raster source is complete only when the approved visual remains traceable and overlay validation confirms that the editable version matches the approved source within the accepted tolerance.

A Content Package is complete only when all required publishable assets are present and approved.

A high numerical score never overrides a critical failure.

## Version

3.0-production-candidate.7

## Status

Active architecture
