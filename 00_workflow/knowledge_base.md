# Knowledge Base Architecture

## Purpose

The Prompt Library uses separated knowledge layers so project-specific knowledge, external research, source evidence, creative interpretation, and reusable system workflow knowledge are never silently conflated.

The machine-readable index is `00_workflow/knowledge/knowledge_registry.json`. Every active knowledge source must declare its scope, approval state, promotion state, permitted task consumers, provenance requirement, and unknown-handling requirement there.

## Knowledge Domains

### 1. Project Knowledge — EBL

The client/project knowledge base is the authoritative store for approved English Beyond Language information.

It may contain:

- customer brief
- brand purpose and positioning
- audience definition
- TEAP framework
- launch strategy
- content pillars
- posting rhythm
- promotional model
- approved platform requirements
- approved typography preferences
- approved visual preferences
- approved tone and emotional objectives
- approved template decisions
- approved human revisions
- client feedback
- decisions and exclusions
- content-specific requirements

Project knowledge must be scoped to EBL and must not become system-wide knowledge unless explicitly promoted.

#### Active EBL project package

Current human-approved EBL production knowledge is registered in:

- `00_workflow/knowledge/project/EBL_approved_project_rules.md`
- `00_workflow/knowledge/project/EBL_post_01_approved_decisions.md`

Use the first file for reusable EBL project rules and the second for Post 01-specific decisions. Post-specific copy/layout decisions must not be silently generalized to future posts.

#### Active supplied EBL brief

Registered in:

`00_workflow/knowledge/project/english_beyond_language_content_brief.md`

Source ID: `EBL-SRC-001`. The record is project-scoped and pending confirmation as the current approved brief. Its directions must pass through Strategy reconciliation before becoming authoritative downstream decisions.

### 2. External / Named-Style Knowledge

Stores knowledge about artists, movements, books, articles, exhibitions, professional design guidance, platform-owner guidance, and other external sources.

Examples:

- Paul Klee
- Bauhaus
- museum publications
- academic books/articles
- artist interviews
- professional typography/layout guidance
- platform-owner publishing guidance

External knowledge requires source provenance.

#### Active Paul Klee source package

Registered in:

`00_workflow/knowledge/external/paul_klee_sources.md`

Current supplied sources:

- `KLEE-SRC-001` — Annie Bourneuf, *Paul Klee: The Visible and the Legible* (University of Chicago Press, 2015)
- `KLEE-SRC-002` — Stephen H. Watson, *Crescent Moon over the Rational: Philosophical Interpretations of Paul Klee* (Stanford University Press, 2009)
- `KLEE-SRC-003` — *Collected Works of Paul Klee* (Delphi Masters of Art / Delphi Classics, 2015)

These sources are external evidence. They do **not** automatically become EBL style rules. Any transfer into EBL must pass through source-derived knowledge → project interpretation → human review → approved project rule.

#### Active Creative Synthesis reference package

Registered in:

`00_workflow/knowledge/external/creative_synthesis_sources.md`

The package currently includes source-derived guidance from:

- Adobe layout principles;
- Adobe typesetting / reading-experience guidance;
- Meta visual / carousel / resolution guidance;
- MoMA curatorial interpretation of Klee line, color, movement, and multiple readings;
- The Met curatorial interpretation of Klee's changing line character according to subject.

These sources may improve late-stage creative judgment, but they do **not** override:

1. current human instruction;
2. approved project rules;
3. approved content / artifacts;
4. supplied project sources.

Their main consumers are:

- `FINAL-AI-001 — Creative AI Final Edit`;
- `FINAL-AI-002 — Creative Synthesis, Heavy QC & Final Output`.

### 3. Project Reference Knowledge

Stores observations extracted from project-supplied visual references, audio, video, screenshots, moodboards, and other reference material.

### 4. Derived Creative Knowledge

Stores approved interpretations and transferable principles derived from the above sources.

Examples:

- EBL style rules
- motif classifications
- approved visual grammar
- reusable Instagram template rules
- source-informed creative synthesis heuristics

### 5. System Workflow Knowledge

Stores reusable cross-project production behavior that has passed the promotion process and is explicitly approved as a system rule.

Examples:

- revision isolation rules;
- clean-source hierarchy;
- preserve-vs-intervene logic;
- closed-loop finalization behavior;
- master-versus-platform-derivative handling;
- required QC evidence structure.

System workflow knowledge must not contain client-specific copy, confidential details, exact project coordinates, or one-off aesthetic preferences.

#### Active Final AI system knowledge

Registered in:

`00_workflow/knowledge/system/final_ai_production_learnings.md`

This file contains approved cross-project lessons from the finalization workflow, including:

- preservation as a valid final-edit decision;
- cleanest-approved-source-first repair;
- mandatory-defect precedence over optional polish;
- semantic consistency over mechanical uniformity;
- local failure → local fix + global re-check;
- master-first / derivative-once production;
- QC evidence as part of production;
- AI production pass ≠ human final approval;
- finalization as a closed loop.

Its orchestration protocol is:

`00_workflow/final_ai_closed_loop_production.md`

## Source Separation

Every knowledge record must identify its status:

```text
SOURCE_FACT
SOURCE_DERIVED
PROJECT_DECISION
HUMAN_PREFERENCE
MODEL_INFERENCE
APPROVED_RULE
```

The system must never present a model inference as a client fact or source fact.

## EBL Knowledge Record

Each EBL record should contain:

```text
KB_ID
PROJECT_ID
KNOWLEDGE_TYPE
TITLE
CONTENT
SOURCE_ID
SOURCE_SCOPE
STATUS
SCOPE
APPROVAL_STATUS
VERSION
CREATED_AT
UPDATED_AT
PROVENANCE
NOTES
```

## External Source Record

Each external/named-style source should contain:

```text
KB_ID
KNOWLEDGE_TYPE
AUTHOR / CREATOR
TITLE
PUBLISHER / INSTITUTION
YEAR
SOURCE_FORMAT
SOURCE_ID
STATUS
SCOPE
AUTHORITY
APPROVAL_STATUS
PROVENANCE
SOURCE_SUPPORTED_THEMES
PROJECT_USE_CAUTION
```

When the source is a broad catalogue or compilation rather than a scholarly interpretive source, record that authority difference explicitly.

## Knowledge Promotion

Knowledge moves through controlled levels:

```text
RAW INPUT
   ↓
PROJECT KNOWLEDGE / SOURCE EVIDENCE
   ↓
DERIVED KNOWLEDGE
   ↓
HUMAN REVIEW
   ↓
APPROVED PROJECT RULE
   ↓
OPTIONAL SYSTEM RULE
```

Project-specific knowledge must not become a system rule automatically.

For workflow learning, explicit human instructions such as **learn**, **structuralize**, **refine the process**, or **promote this as a reusable rule** may authorize promotion when the lesson is truly cross-project and privacy-safe.

## Named-Style Source Promotion Rule

For named-style work such as Paul Klee:

```text
EXTERNAL SOURCE
    ↓
SOURCE_FACT / SOURCE_DERIVED
    ↓
NAMED STYLE STUDY
    ↓
MOTIF / SIGN EXTRACTION
    ↓
PROJECT INTERPRETATION
    ↓
HUMAN REVIEW
    ↓
APPROVED EBL RULE
```

Do not copy source artworks literally. Historical description, interpretation, project derivation, and final visual rule must remain distinguishable.

## Retrieval Rule

Tasks should retrieve knowledge from the appropriate domain before execution:

```text
EBL task
  → EBL_approved_project_rules.md
  → EBL Project Knowledge

EBL Post 01 task
  → EBL_approved_project_rules.md
  → EBL_post_01_approved_decisions.md

EBL profile-picture task
  → EBL_approved_project_rules.md
  → QC-IG-PROFILE-001_instagram_profile_picture_qc.md

Named artist task
  → External / Named-Style Knowledge

Paul Klee-informed task
  → paul_klee_sources.md + approved Klee-derived project rules

Reference analysis
  → Project Reference Knowledge

Template / production task
  → Approved Project Rules + Platform Rules

Creative AI Final Edit
  → final_ai_production_learnings.md
  → final_ai_closed_loop_production.md
  → approved project rules
  → content-specific decisions
  → approved artifact / visual DNA / revision history
  → applicable QC findings
  → creative_synthesis_sources.md

Final AI Creative Synthesis + Heavy QC
  → final_ai_production_learnings.md
  → final_ai_closed_loop_production.md
  → FINAL-AI-001 candidate
  → all approved project/context sources
  → creative_synthesis_sources.md
  → all applicable mandatory QC modules
  → platform export requirements
```

## Priority Rule

When sources conflict:

1. explicit current client decision;
2. approved project rule;
3. approved system workflow rule for process behavior;
4. supplied project source evidence;
5. authoritative external source;
6. model inference.

A system workflow rule controls **how the process is executed**; it must not override project-specific creative/content decisions.

Conflicts must be surfaced rather than silently reconciled.

## Human-Directed Revision Knowledge

Human-directed output revision is governed by:

`00_workflow/human_feedback_style_learning.md`

The governing relationship is:

```text
HUMAN = decides WHAT to edit
REFERENCE = informs HOW the requested edit should look
AI = applies the requested edit
```

Revision behavior itself is a workflow rule. A specific aesthetic correction becomes reusable style knowledge only through the normal approval/promotion process.

## Privacy / Scope

Client knowledge must remain project-scoped. Do not promote confidential client information into the global/system knowledge layer.
