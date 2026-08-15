# Prompt Library v3.1 — Refined Production Process

## Final Goal

Produce traceable, human-directed, production-ready creative artifacts without silently changing source facts, approved decisions, or authorized scope.

The process succeeds only when it preserves both creative quality and information integrity from customer input through final editable production output.

## Governing Model

```text
SOURCE
  ↓ explicit analysis
DERIVED
  ↓ explicit human or authorized task decision
DECISION
  ↓ controlled execution
OUTPUT
  ↓ evaluation, revision, and approval
APPROVED ARTIFACT
  ↓ optional evidence-backed promotion
SCOPED MEMORY
```

No arrow may be skipped silently.

## Refined Stage Assessment

| Stage | Goal | Required output | Completion test | Assessment |
|---|---|---|---|---|
| 01 Strategy | Establish the authoritative project definition | Approved Strategy Package | Requirements, exclusions, unknowns, and approval are explicit | Executable and contract-controlled |
| 02 Research | Establish relevant evidence | Research Synthesis | Material findings have sources and unsupported claims remain UNKNOWN | Executable and contract-controlled |
| 03 Visual Analysis | Describe supplied visual evidence | Visual Evidence Package | Observation and interpretation remain distinguishable | Executable and contract-controlled |
| 04 Named Style Study | Understand an applicable named visual language responsibly | Approved Style Study Package | Facts, observations, interpretations, transferability, and imitation risk are separated | Conditional; now mapped to STYLE-001 and the process registry |
| 05 Motif & Sign Extraction | Extract recurring visual vocabulary | Controlled Motif Library | Frequency, evidence, role, transferability, risk, and confidence are complete | Protocol-controlled; future executable task recommended |
| 06 Reference Style Synthesis | Convert reference evidence into original transferable principles | Approved Reference Style Synthesis | Formal, emotional, and communication effects are traceable | Protocol-controlled; future executable task recommended |
| 07 Visual DNA | Create project visual-system rules | Visual DNA Package | Every rule traces to approved evidence and contradictions are surfaced | Executable and contract-controlled |
| 08 Platform / Template Synthesis | Translate the visual system into reusable production structure | Approved Template Candidate | Structure, editable zones, content limits, platform constraints, and scope are explicit | Conditional protocol; machine-record format exists |
| 09 Art Direction | Make content-specific creative decisions | Approved Art Direction | Objective, message, hierarchy, concept, references, and constraints are approved | Executable with human approval gates |
| 10 Generation | Operationalize direction and execute it | Specification, Prompt, Generated Output | Inputs and approvals are complete; output remains classified as OUTPUT | Executable and auditable |
| 11 Content Package | Assemble the publishable asset | Content Package | Visual, copy, CTA, alt text, metadata, relationships, and provenance are present | Protocol-controlled; future executable task recommended |
| 12 Human Revision / Style Learning | Apply scoped changes and learn only from approved evidence | Revision Record, Approved Output, optional Style Memory | Requested and preserved elements are documented; promotion scope is approved | Strong governance; persistence/retrieval engine still needed |
| 13 Editable Reconstruction Preparation | Prepare flattened work for faithful editable rebuilding | Editable Reconstruction Package | Approved source remains locked; derived pixels and typography uncertainty are labelled | Conditional production protocol |
| 14 Figma Implementation | Produce the structured editable master | Approved Structured Figma Master | Content, layers, variables, components, exports, and overlay fidelity pass | Production protocol with explicit blocked-state handling |
| 15 Quality Control / Final Approval | Evaluate the complete result and route root-cause correction | Final Approval or Revision Route | Critical failures override scores; failure routes to earliest responsible stage | Executable QC plus specialist protocols |

## Process Refinements Applied

1. Added `00_workflow/process_registry.json` as the canonical machine-readable process map.
2. Mapped all 26 executable task contracts into exactly one of the 15 production stages.
3. Mapped non-prompt protocols and schemas to the stages they govern.
4. Added explicit execution conditions for optional stages instead of pretending every project follows an identical path.
5. Added required output artifacts and memory effects to every stage.
6. Added `tests/validate_process.py` to enforce stage order, upstream dependencies, task coverage, protocol existence, canonical gates, artifacts, goals, conditions, and memory effects.
7. Added process validation to GitHub Actions.
8. Updated the release count from 25 to 26 active prompts and aligned the public workflow summary with the refined process.
9. Made provider failures fail closed through concise runtime errors instead of leaking SDK tracebacks.

## Output Evaluation Rules

Every stage output must pass five questions:

1. **Goal:** Does the output solve only the declared stage goal?
2. **Evidence:** Can every material claim or rule be traced to SOURCE, DERIVED, or approved DECISION inputs?
3. **Boundary:** Did the stage avoid work owned by another stage?
4. **Usability:** Can the declared downstream stage execute from the handoff without repairing hidden assumptions?
5. **Authority:** Are approvals, conditions, blockers, scope, and memory promotion explicit?

Failure in evidence, boundary, or authority is critical even when the artifact is visually strong.

## Remaining Production Gaps

The refined process is structurally coherent, but four implementation gaps remain:

1. Promote motif extraction, reference synthesis, template synthesis, content packaging, style learning, reconstruction, and Figma implementation from protocols into versioned executable task contracts when stable.
2. Implement JSON Schema validation for handoffs, approvals, templates, motif records, style-memory records, and evaluation artifacts.
3. Build scoped memory persistence and retrieval that records which approved memory IDs influenced each run.
4. Harden semantic evaluation with structured model output, evaluator/rubric hashes, persisted results, and injection-resistant evaluation boundaries.

## Final Process Rule

The repository must optimize for **controlled creative continuity**, not maximum autonomous generation.

The best output is not merely attractive. It is attractive, correct, traceable, editable, approved, reusable at the proper scope, and safe from silent drift.
