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
4. Visual DNA — convert evidence into transferable visual rules.
5. Art Direction — make and select creative decisions.
6. Generation — operationalize approved direction for visual generation.
7. Quality Control — evaluate results, diagnose failures, and route revision.
8. Content Packaging — assemble the complete platform-ready content package.
9. Figma Implementation — convert approved visual content into an editable production master and, when appropriate, a reusable platform template.
10. Final Production Approval — approve the complete package for export and publishing.

## Content Production Loop

For social/content outputs, the post is treated as a controlled Content Package rather than a single image.

```text
CONTENT STRATEGY
      ↓
CONTENT ARTIFACT
      ├── On-Canvas Copy
      ├── Caption
      ├── CTA
      ├── Alt Text
      └── Publishing Metadata
      ↓
GEN-002
      ↓
Generated Visual
      ↓
Human Revision
      ↓
Approved Visual
      ↓
CONTENT PACKAGE APPROVAL
      ├── Approved Visual
      ├── Approved Caption
      └── Approved Metadata
      ↓
FIGMA IMPLEMENTATION
      ↓
Figma QA
      ↓
Approved Figma Master
      ↓
Template Review
      ├── No promotion
      ├── Project Template
      └── Published Platform Template
      ↓
FINAL PRODUCTION APPROVAL
      ↓
EXPORT / PUBLISH
```

## Figma Implementation Principle

The Figma layer is the editable production layer. It does not replace the original generated output or the approved visual artifact.

Every approved visual content output that requires editable production must produce a Figma Implementation Package containing the exact file, page, section, frame, component, style, variable, editable/locked fields, export specification, and provenance needed to reproduce the production state.

The Figma master must remain traceable to:

- the Content Package;
- the generation output;
- the approved human revision;
- approved style references and rules;
- the template version used, if any.

See `figma_output_contract.md` and `figma_build_record_template.md` for the required package and audit record.

## Template Promotion

A Figma implementation becomes a reusable template only after explicit review.

```text
CONTENT INSTANCE
      ↓
FIGMA MASTER
      ↓
TEMPLATE CANDIDATE
      ↓
HUMAN REVIEW
      ↓
PROMOTION DECISION
      ├── NO PROMOTION
      ├── PROJECT TEMPLATE
      └── PUBLISHED PLATFORM TEMPLATE
```

A template captures reusable structure, components, variables, safe areas, and editable zones. It must not silently absorb campaign-specific content.

## Human Feedback and Style Learning

After human revision, preserve:

1. generated output;
2. human revision;
3. approved output;
4. revision record;
5. style-reference decision;
6. style-rule decision;
7. template decision.

A single correction must not automatically become a global style rule.

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
9. If the output is production-bound, validate the required downstream artifact package before final approval.
10. When a human revises an output, preserve both the original and revised artifacts and record the revision before extracting reusable style or template knowledge.

## Failure Policy

The system must stop rather than invent information when a required input is unavailable, contradictory, or insufficient for the task.

Missing information must be represented explicitly as UNKNOWN, not filled with plausible content.

## Revision Routing

When QC identifies a failure, route the failure to the earliest responsible stage rather than automatically regenerating.

- Source / requirement failure → Strategy
- Evidence / research failure → Research
- Reference interpretation failure → Visual Analysis
- Visual rule failure → Visual DNA
- Creative decision failure → Art Direction
- Specification / prompt failure → Generation
- Model execution failure → Generation
- Content/copy failure → Content Packaging
- Figma implementation failure → Figma Implementation
- Template failure → Template Review
- Human preference discovered during approved revision → Human Feedback & Style Learning
- Acceptable variation → no revision

## Approval Rule

A stage is complete only when its decision gate is satisfied and its handoff package is complete.

A Figma production package is complete only when its QA gate passes and its file/node provenance is recorded.

A style reference or style rule is complete only when its approval metadata, scope, provenance, and version are complete.

A high numerical score never overrides a critical failure.

## Version

3.0-production-candidate.4

## Status

Active architecture
