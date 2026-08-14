# Controlled Creative Production Workflow

## Purpose

This document defines the execution system for the Prompt Library. The repository is a controlled creative-production system, not a loose collection of prompts.

Each prompt is an executable task with a defined input contract, task boundary, output contract, provenance requirements, confidence requirements, and decision gate.

## Core Rule

No stage may silently rewrite upstream facts, requirements, decisions, or approved constraints.

Information is classified as:

- SOURCE — directly supplied or observed evidence.
- DERIVED — an explicit analysis or inference based on source evidence.
- DECISION — an intentional approved creative or project choice.
- OUTPUT — an execution result to be evaluated.

A downstream stage may transform information only within its task boundary.

## Pipeline

1. Strategy — define the problem and requirements.
2. Research — establish evidence and context.
3. Visual Analysis — extract visual evidence from references.
4. Reference Style Synthesis — analyze formal language, mark-making, materiality, shape language, composition, emotional effect, communication effect, and transferable principles.
5. Visual DNA — convert validated visual evidence and approved style synthesis into transferable visual rules.
6. Instagram Template Synthesis — when the destination is Instagram, translate approved visual language and Visual DNA into an original reusable platform template.
7. Art Direction — make and select creative decisions.
8. Generation — operationalize approved direction for image generation.
9. Content Package — assemble visual, copy, caption, CTA, accessibility, and publishing outputs.
10. Figma Implementation — build the approved content as an editable production file and reusable template candidate.
11. Quality Control — evaluate results, diagnose failures, and route revision.

## Reference Style Synthesis Checkpoint

Reference analysis must answer two separate questions:

1. **What does the reference look like?**
2. **What does the reference make the viewer feel and why?**

The second question is mandatory. Style must be translated through emotional and communication effects rather than through superficial copying of shapes or brush marks.

For the English Beyond Language Instagram system, the approved reference direction emphasizes a human, curious, thoughtful, warm, culturally aware, artistic, exploratory, and intelligent feeling; this is treated as a hypothesis derived from supplied references and must remain traceable to the reference set and customer direction.

See `reference_style_synthesis.md`.

## Instagram Template Synthesis Checkpoint

When Instagram is the target platform, the visual language must be combined with platform constraints before generation.

The template synthesis step defines:

- format and dimensions
- mobile-first readability
- communication hierarchy
- content zones
- slide roles
- shape and line vocabulary
- texture behavior
- reusable components
- editable / controlled / locked elements
- Figma implementation requirements

The reference is used as a style source, not as a layout to reproduce.

See `instagram_template_synthesis.md` and `figma_output_contract.md`.

## Human Feedback & Style Learning Loop

After a generated output is reviewed by a human, the system may capture the result as controlled style knowledge.

```text
GEN-002
  ↓
Generated Output
  ↓
Human Revision
  ↓
Approved Output
  ↓
Revision Record
  ↓
Style Knowledge Extraction
  ↓
Approved Style Reference / Style Rule
  ↓
Future GEN / VDNA / Instagram Template / QC inputs when explicitly approved
```

The generated output, revised output, and approved output are separate artifacts.

A human revision is not automatically a prompt correction and is not automatically a style rule.

Style knowledge must be explicitly classified as:

- PROJECT STYLE REFERENCE
- PROJECT STYLE RULE
- SYSTEM STYLE RULE

Project-specific preferences must not silently become system-wide rules.

See `human_feedback_style_learning.md` and `style_memory_schema.json` for the controlled artifact model.

## Execution Loop

For every task:

1. Resolve required inputs.
2. Validate preconditions.
3. Execute only the assigned task.
4. Produce the required output schema.
5. Attach provenance and confidence.
6. Run the decision gate.
7. If blocked, stop and identify the missing or conflicting input.
8. If passed, create the handoff package for the next task.
9. When a human revises an output, preserve both the original and revised artifacts and record the revision before extracting reusable style knowledge.

## Failure Policy

The system must stop rather than invent information when a required input is unavailable, contradictory, or insufficient for the task.

Missing information must be represented explicitly as UNKNOWN, not filled with plausible content.

## Revision Routing

When QC identifies a failure, route the failure to the earliest responsible stage rather than automatically regenerating.

- Source / requirement failure → Strategy
- Evidence / research failure → Research
- Reference interpretation failure → Visual Analysis / Reference Style Synthesis
- Visual rule failure → Visual DNA
- Template structure failure → Instagram Template Synthesis
- Creative decision failure → Art Direction
- Specification / prompt failure → Generation
- Model execution failure → Generation
- Content packaging failure → Content Package
- Figma implementation failure → Figma Implementation
- Human preference discovered during approved revision → Human Feedback & Style Learning
- Acceptable variation → no revision

## Approval Rule

A stage is complete only when its decision gate is satisfied and its handoff package is complete.

A style reference or style rule is complete only when its approval metadata, scope, provenance, and version are complete.

A reusable Instagram template is complete only when its platform structure, content zones, component behavior, editable/controlled/locked fields, Figma implementation, provenance, and approval status are complete.

A high numerical score never overrides a critical failure.

## Version

3.0-production-candidate.4

## Status

Active architecture
