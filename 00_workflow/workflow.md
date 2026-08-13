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
6. Generation — operationalize approved direction for image generation.
7. Quality Control — evaluate results, diagnose failures, and route revision.

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
- Acceptable variation → no revision

## Approval Rule

A stage is complete only when its decision gate is satisfied and its handoff package is complete.

A high numerical score never overrides a critical failure.

## Version

3.0

## Status

Active architecture
