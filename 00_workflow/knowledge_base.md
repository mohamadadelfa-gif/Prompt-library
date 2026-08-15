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
- chosen identity assets
- project-specific QC rules
- durable production memory

Project knowledge must be scoped to EBL and must not become system-wide knowledge unless explicitly promoted.

#### Durable EBL project memory — mandatory retrieval

Registered in:

`00_workflow/knowledge/project/EBL_project_memory.md`

Source ID: `EBL-MEM-001`.

This is the first durable project-memory layer for EBL visual production. It records:

- public brand-name preference;
- core communication direction;
- chosen Geometric Reader Integrated Logo;
- primary-master versus production-signature distinction;
- visual-language memory;
- semantic typography rules;
- raster typography repair learning;
- human revision preservation;
- final-AI closed-loop behavior;
- Story-template principles and current candidate status;
- master-versus-platform-output handling.

Every EBL visual production/revision task must retrieve this memory before applying project-specific creative decisions.

#### Active EBL project package

Current human-approved EBL production knowledge is registered in:

- `00_workflow/knowledge/project/EBL_project_memory.md`
- `00_workflow/knowledge/project/EBL_approved_project_rules.md`
- `00_workflow/knowledge/project/EBL_logo_application_rules.md`
- `00_workflow/knowledge/project/EBL_post_01_approved_decisions.md`
- `00_workflow/knowledge/project/EBL_story_template_rules.md`

Use:

- `EBL_project_memory.md` for durable project memory;
- `EBL_approved_project_rules.md` for reusable approved EBL rules;
- `EBL_logo_application_rules.md` for chosen-logo application behavior;
- `EBL_post_01_approved_decisions.md` for Post 01-only decisions;
- `EBL_story_template_rules.md` for the current Story system/candidate.

Post-specific copy/layout decisions must not be silently generalized to future posts.

The exact current Story template remains a `PROJECT_REFERENCE / REVIEW_CANDIDATE` until explicit human approval promotes it.

#### EBL project master QC

Registered in:

`00_workflow/qc/QC-EBL-001_project_master_qc.md`

Source ID: `EBL-QC-001`.

This QC is project-specific and mandatory for EBL final visual review. It orchestrates specialized QC modules and checks:

- content/meaning fidelity;
- public brand name;
- chosen-logo fidelity;
- visual identity;
- meaning-to-form synthesis;
- semantic typography;
- painterly/material integrity;
- artifact/repair integrity;
- carousel/system consistency;
- Story-specific behavior;
- export/master/derivative handling;
- final-AI closed-loop compliance;
- evidence package completeness;
- human final approval state.

A specialized module such as logo or typography QC does not replace the EBL project master gate.

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

Stores observations extracted from project-supplied visual references, audio, video, screenshots, moodboards, approved output candidates, and other reference material.

A candidate may inform later work without automatically becoming an approved reusable rule.

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

### 6. External Technical Knowledge

Stores authoritative tooling and production references that may support evidence-based execution without becoming aesthetic or project rules.

Current font-engineering reference:

`00_workflow/knowledge/external/gftools_font_engineering.md`

Source ID: `GFTOOLS-SRC-001`. Retrieve it for VIS-005 or QC-001 only when actual font files are available and technical font inspection or QA is relevant. It is not a base runtime dependency, does not identify fonts from raster images by itself, and does not authorize font modification or establish licensing.

Current digital-typography discovery index:

`00_workflow/knowledge/external/awesome_typography_resource_index.md`

Source ID: `TYPO-INDEX-001`. Retrieve it for RES-005 or VIS-005 when a typography question would benefit from specialist specifications, tools, libraries, validators, books, or videos. Treat it as a route to primary sources, not as primary evidence or authorization to adopt a linked resource.

Current Persian/Farsi font discovery index:

`00_workflow/knowledge/external/github_persian_font_topic.md`

Source ID: `FA-FONT-INDEX-001`. Retrieve it for RES-005 or VIS-005 when Persian/Farsi, Arabic-script, RTL, or bilingual Persian/Latin typography is in scope. The GitHub topic is dynamic and self-tagged: verify every candidate repository, font file, license, Persian coverage, shaping behavior, provenance, and target-platform compatibility independently.

Current focused Persian/Farsi font collection:

`00_workflow/knowledge/external/font_store_persian_fonts.md`

Source ID: `FA-FONT-COLLECTION-001`. Retrieve it alongside `FA-FONT-INDEX-001` when a focused Perso-Arabic foundry collection would improve candidate discovery. Verify whether each repository is canonical, forked, modified, mirrored, or packaged; confirm its actual font license and provenance before use.

Current broad Persian-language resource index:

`00_workflow/knowledge/external/awesome_persian_resource_index.md`

Source ID: `FA-RESOURCE-INDEX-001`. Retrieve it for RES-005 or VIS-005 when Persian typography research also requires RTL frameworks, CSS, text normalization, Unicode handling, Persian numerals, interface guidance, localization, or other implementation context. Verify each linked primary source; the list itself is not implementation evidence and its repository-level license was unknown at review time.

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
ANY EBL VISUAL TASK
  → EBL_project_memory.md
  → EBL_approved_project_rules.md
  → content-specific decisions if present
  → EBL_logo_application_rules.md when logo/branding is present
  → approved artifact / clean master / textless master
  → QC-EBL-001 + asset-specific QC

EBL Post 01 task
  → EBL_project_memory.md
  → EBL_approved_project_rules.md
  → EBL_post_01_approved_decisions.md
  → QC-EBL-001

EBL Story task
  → EBL_project_memory.md
  → EBL_approved_project_rules.md
  → EBL_story_template_rules.md
  → instagram_template_synthesis.md
  → QC-EBL-001 Story gate

EBL profile-picture task
  → EBL_project_memory.md
  → EBL_approved_project_rules.md
  → QC-IG-PROFILE-001
  → QC-EBL-001

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
  → approved project memory/rules
  → content-specific decisions
  → approved artifact / visual DNA / revision history
  → applicable QC findings
  → creative_synthesis_sources.md

Final AI Creative Synthesis + Heavy QC
  → final_ai_production_learnings.md
  → final_ai_closed_loop_production.md
  → FINAL-AI-001 candidate
  → all approved project/context sources
  → project master QC if one exists
  → creative_synthesis_sources.md
  → all applicable mandatory QC modules
  → platform export requirements

Font-file inspection / technical typography QA
  → gftools_font_engineering.md + actual font binaries + recorded tool evidence

Digital-typography source/tool discovery
  → awesome_typography_resource_index.md → verified primary source

Persian/Farsi font discovery
  → github_persian_font_topic.md → candidate repository → license + Persian shaping verification

Focused Farsi Font Store discovery
  → font_store_persian_fonts.md → canonical-status check → repository/license + Persian shaping verification

Broad Persian-language production discovery
  → awesome_persian_resource_index.md → verified primary source → target-environment test

Heavy QC aesthetic evidence
  → image_aesthetics_assessment_sources.md
  → same-model, same-asset-class approved calibration examples
  → QC-AES-001 + HEAVY-QC-001
  → authorized human decision
```

## Priority Rule

When sources conflict:

1. explicit current client decision;
2. approved project memory / project rule;
3. content-specific approved decision;
4. approved system workflow rule for process behavior;
5. supplied project source evidence;
6. authoritative external source;
7. model inference.

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

Updated: 2026-08-16
