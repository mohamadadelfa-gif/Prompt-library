# 00 — Workflow Control Layer

This directory contains the orchestration layer for the Prompt Library.

The Prompt Library is a **controlled creative-production system** in which prompts are executable tasks with defined inputs, outputs, boundaries, provenance, confidence, handoffs, and decision gates.

## Files

- `workflow.md` — master execution pipeline and revision routing
- `task_contract.md` — universal contract for executable prompts
- `stage_registry.md` — active stages, tasks, boundaries, and handoffs
- `handoff_contract.md` — controlled information transfer between stages
- `decision_gates.md` — rules for advancing, blocking, revising, and approving work
- `information_model.md` — SOURCE / DERIVED / DECISION / OUTPUT model
- `editable_reconstruction_preparation.md` — source-lock, textless artwork derivation, editable-layer mapping, and Figma reconstruction handoff for approved raster visuals
- `figma_output_contract.md` — editable production implementation requirements for approved visual outputs

## Execution Principle

A prompt is not considered complete merely because it returns text. It is complete only when its output satisfies its contract and its decision gate permits the workflow to continue.
