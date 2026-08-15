# FINAL-AI Closed-Loop Production Protocol

## Purpose

Turn late-stage AI creative refinement into a controlled production loop rather than a one-pass beautification step.

This protocol governs the relationship between:

- `FINAL-AI-001 — Creative AI Final Edit`;
- `FINAL-AI-002 — Creative Synthesis, Heavy QC & Final Output`;
- human final approval;
- final master / platform derivative production;
- reusable learning promotion.

## Governing Principle

```text
FINAL QUALITY = MAXIMUM COHERENCE
                WITH
                MINIMUM NECESSARY CHANGE
```

A strong final-stage decision may be **PRESERVE**.

AI is not required to change a slide merely because a final-edit stage exists.

---

## Closed-Loop Sequence

```text
SOURCE LOCK
   ↓
WHOLE-WORK READ
   ↓
MEANING / FUNCTION MAP
   ↓
PRESERVE OR INTERVENE?
   ↓
FINAL-AI-001 CREATIVE FINAL EDIT
   ↓
DELTA REVIEW
   ↓
FINAL-AI-002 HEAVY QC
   ↓
MANDATORY FAILURE?
   ↙            ↘
 YES             NO
  ↓               ↓
ROOT-CAUSE      PASS_FOR_HUMAN_FINAL_REVIEW
DIAGNOSIS            ↓
  ↓               HUMAN FINAL APPROVAL
SMALLEST SAFE         ↓
CORRECTION        FINAL_PUBLISHING_MASTER
  ↓                   ↓
RERUN AFFECTED     PLATFORM DERIVATIVES
QC + GLOBAL CHECK      ↓
  └──────────────→ LEARNING REVIEW
```

The loop continues until mandatory failures are resolved or the human stops / redirects the process.

---

# 1. Source Lock

Before final editing, identify the authoritative source for each layer / asset.

Record:

- approved copy source;
- approved visual master;
- approved textless master if available;
- editable text source if available;
- approved logo master / variant;
- approved project rules;
- content-specific decisions;
- target master resolution;
- target platform derivative.

Never treat a previously damaged raster export as the best available source if a cleaner approved source exists.

---

# 2. Clean-Source Hierarchy

When repairing a final asset, use the cleanest source available in this order:

```text
1. EDITABLE / LIVE SOURCE
2. APPROVED CLEAN MASTER
3. APPROVED TEXTLESS / ELEMENT-FREE MASTER
4. CLEAN REGION FROM THE SAME ARTWORK
5. TARGETED LOCAL REPAIR
6. GENERATIVE RECONSTRUCTION — LAST RESORT + HUMAN REVIEW
```

This prevents repeated raster damage and patch accumulation.

### Learned rule

```text
DO NOT REPAIR A DAMAGED DERIVATIVE
WHEN A CLEANER APPROVED SOURCE EXISTS
```

---

# 3. Whole-Work Read Before Local Editing

Always inspect the entire set before changing one slide.

For each frame, record:

```text
MESSAGE
FUNCTION
PRIMARY FOCAL POINT
SECONDARY READING ORDER
PROTECTED ELEMENTS
KNOWN DEFECTS
SYSTEM RELATIONSHIP
```

For a carousel also map:

```text
ENTRY → DEVELOPMENT → SHIFT → PAYOFF
```

No local edit should be approved without checking its effect on the whole sequence.

---

# 4. Intervention Classification

Every slide / asset receives one intervention state.

## P0 — PRESERVE

The asset already performs its semantic, visual, brand, and platform role.

Action:

- make no creative change;
- include it in QC;
- preserve source fidelity.

## P1 — CLEANUP

Correct only accidental production defects:

- ghost marks;
- repair patches;
- halos;
- clone seams;
- unintended dots / lines;
- masking residue;
- compression or export artifacts where safely recoverable.

## P2 — MICRO-REFINE

Make controlled changes to approved expression:

- typography hierarchy;
- line breaks;
- alignment;
- spacing;
- local contrast;
- optical balance;
- semantic emphasis;
- minor painterly integration.

Meaning and identity remain locked.

## P3 — SOURCE-BASED RECONSTRUCTION

Rebuild a damaged area from a cleaner approved source when local repair would preserve defects.

Examples:

- rebuild typography from live text or clean textless master;
- restore an approved logo from the master rather than sharpening a degraded copy;
- reconstruct a background from an approved clean source.

## P4 — CONCEPTUAL CHANGE

Changes to:

- approved wording;
- narrative order;
- brand identity;
- major composition concept;
- approved logo geometry;
- strategic message.

**Human authorization required before execution.**

---

# 5. Defect Precedence

Resolve failures in this order:

```text
1. CONTENT / FACTUAL FIDELITY
2. APPROVED MASTER / IDENTITY FIDELITY
3. TYPOGRAPHY / LOGO READABILITY
4. ARTIFACT / RASTER INTEGRITY
5. SYSTEM / CAROUSEL CONSISTENCY
6. PLATFORM READABILITY
7. OPTIONAL AESTHETIC POLISH
```

A mandatory defect outranks optional creative improvement.

Do not spend a final pass beautifying a slide while obvious text, logo, artifact, or content failures remain.

---

# 6. Preservation Is an Active Creative Decision

A final AI stage must not create change for its own sake.

Use:

```text
IF CURRENT FORM ALREADY SUPPORTS
MEANING + IDENTITY + SEQUENCE + READABILITY
THEN PRESERVE
```

Record preservation explicitly in the change log.

### Learned rule

```text
NO CHANGE CAN BE THE HIGHEST-QUALITY FINAL EDIT
```

---

# 7. Semantic Consistency vs Mechanical Uniformity

Consistency means stable **role and grammar**, not pixel-identical treatment.

For repeated system elements such as numbering, logo signatures, labels, or metadata, preserve:

- semantic role;
- format;
- anchor logic;
- size / weight relationship;
- spacing logic;
- hierarchy;
- family resemblance.

Allow local adaptation only when function requires it, for example:

- light / dark color inversion for contrast;
- optical compensation against a different local background;
- small positional compensation only when the project rule allows optical rather than fixed geometric anchoring.

Do not confuse adaptive consistency with arbitrary variation.

---

# 8. FINAL-AI-001 — Creative Final Edit

Run after source lock and intervention classification.

For P0 assets:

- preserve;
- verify.

For P1–P3 assets:

- apply the smallest high-value change;
- maintain protected elements;
- record before / after;
- inspect at native resolution;
- review the full set after the local change.

Output:

`Creative Final Candidate`

Never `FINAL_PUBLISHING_MASTER`.

---

# 9. Delta Review

Before Heavy QC, compare the candidate to its approved source.

For each changed asset record:

```text
WHAT CHANGED?
WHY?
WHICH RULE AUTHORIZED IT?
WHAT WAS PRESERVED?
WHAT NEW RISK WAS INTRODUCED?
```

Reject any unexplained change.

---

# 10. FINAL-AI-002 — Heavy QC

Run the full mandatory QC stack.

Minimum required checks:

- content fidelity;
- typography integrity;
- logo integrity;
- visual identity;
- painterly / artistic quality;
- carousel / system consistency;
- platform readability;
- audience communication;
- artifact / raster integrity;
- native-size inspection;
- realistic feed-size inspection;
- export / derivative verification.

Result states:

```text
REVISION_REQUIRED
PASS_FOR_HUMAN_FINAL_REVIEW
```

AI cannot grant final human creative approval.

---

# 11. Failure Re-Entry Rule

If Heavy QC finds a mandatory failure:

1. identify the exact failed gate;
2. identify the root cause;
3. classify the correction P1 / P2 / P3 / P4;
4. return to the cleanest valid source;
5. apply the smallest safe correction;
6. rerun the affected QC gate;
7. rerun full-set coherence review;
8. rerun any downstream gate that could have been affected.

Do not restart or redesign unaffected assets.

### Learned rule

```text
LOCAL FAILURE → LOCAL CORRECTION
                 +
                 GLOBAL RE-CHECK
```

---

# 12. Master-First Output Architecture

Keep the final approved working resolution as the archival / project master.

Example:

```text
MASTER = 1254×1254
INSTAGRAM DERIVATIVE = 1080×1080
```

Rules:

- do not overwrite the master with the platform derivative;
- do not repeatedly resize the working master during revisions;
- create the publishing derivative once from the approved final master;
- perform a final platform-size inspection on the derivative.

---

# 13. Required Evidence Package

For any final visual set, produce:

1. individual archival masters;
2. platform derivatives;
3. master contact sheet;
4. platform-size contact sheet;
5. native-resolution critical-area QC sheet;
6. logo / identity critical-area QC where applicable;
7. before / after evidence for meaningful final changes;
8. Heavy QC report;
9. unresolved-risk record;
10. final package / ZIP.

Evidence is part of the finalization process, not optional documentation.

---

# 14. Human Final Approval

Allowed AI state:

```text
PASS_FOR_HUMAN_FINAL_REVIEW
```

Only explicit human approval promotes the asset to:

```text
FINAL_PUBLISHING_MASTER
```

Production readiness and human creative acceptance remain separate states.

---

# 15. Learning Promotion After Finalization

After the run, separate lessons into three classes.

## A. Project-Specific Decision

Example:

- exact phrase color on a particular post;
- exact slide number format for one carousel;
- a project-specific CTA treatment.

Store in project knowledge only.

## B. Reusable Project Rule

Example:

- brand-specific semantic typography grammar;
- brand-specific logo application behavior.

Promote only with human approval.

## C. System-Level Production Learning

Example:

- preserve strong assets instead of forcing edits;
- use clean-source hierarchy;
- repair local failures locally then rerun global coherence;
- create platform derivatives only from the approved master;
- native critical-area evidence is mandatory.

These may be promoted to the reusable workflow when explicitly approved by the human.

---

# 16. Final AI Run Record

Each run should record:

```text
RUN_ID
PROJECT_ID
ASSET_ID
SOURCE_MASTER
CONTEXT_RETRIEVED
SLIDE / FRAME FUNCTION MAP
INTERVENTION_CLASS_PER_ASSET
CHANGES_APPLIED
PRESERVATIONS
QC_FAILURES
ROOT_CAUSES
CORRECTIONS
FINAL_QC_RESULTS
MASTER_OUTPUTS
PLATFORM_DERIVATIVES
HUMAN_DECISION
LEARNINGS
PROMOTION_DECISIONS
DATE
```

---

## Promoted Learnings from EBL Post 01

The human explicitly requested that the finalization process be learned, structuralized, and refined.

Reusable lessons promoted from that run:

```text
PRESERVATION IS A VALID FINAL EDIT
CLEAN SOURCE > PATCHING A DAMAGED DERIVATIVE
SEMANTIC CONSISTENCY > MECHANICAL UNIFORMITY
MANDATORY DEFECTS > OPTIONAL POLISH
LOCAL FAILURE → LOCAL FIX + GLOBAL RE-CHECK
MASTER FIRST → PLATFORM DERIVATIVE ONCE
QC EVIDENCE IS PART OF PRODUCTION
AI PASS ≠ HUMAN FINAL APPROVAL
```

Post 01-specific copy, exact emphasis, exact logo placement, and exact composition remain project-scoped and are not promoted here.
