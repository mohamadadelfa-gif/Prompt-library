# Knowledge Base Architecture

## Purpose

The Prompt Library uses separated knowledge layers so project-specific knowledge, external research, source evidence, creative interpretation, and reusable system workflow knowledge are never silently conflated.

The machine-readable index is `00_workflow/knowledge/knowledge_registry.json`. Every active knowledge source must declare its scope, approval state, promotion state, permitted task consumers, provenance requirement, and unknown-handling requirement there.

## Knowledge Domains

### 1. Project Knowledge — EBL

The client/project knowledge base is the authoritative store for approved English Beyond Language information.

It may contain:

- customer brief;
- brand purpose and positioning;
- audience definition;
- TEAP framework;
- approved platform requirements;
- approved typography and visual preferences;
- approved human revisions;
- decisions and exclusions;
- content-specific requirements;
- chosen identity assets;
- project-specific QC rules;
- durable production memory;
- negative/failure memory;
- visual calibration examples;
- task-specific retrieval rules.

Project knowledge must be scoped to EBL and must not become system-wide knowledge unless explicitly promoted.

#### Durable EBL project memory — mandatory retrieval

Registered in:

`00_workflow/knowledge/project/EBL_project_memory.md`

Source ID: `EBL-MEM-001`.

This durable project-memory layer records:

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

#### EBL operational memory system

EBL memory is not treated as one large prose file. It is separated into operational memory classes:

```text
EBL_memory_registry.json
→ EBL_project_memory.md
→ EBL_decision_log.md
→ EBL_asset_registry.json
→ EBL_failure_memory.md
→ EBL_visual_examples.md
→ EBL_retrieval_map.md
→ QC-EBL-MEM-001
→ QC-EBL-001
```

Roles:

- `EBL_memory_registry.json` — machine-readable memory inventory, status, scope and required consumers;
- `EBL_project_memory.md` — durable project synthesis;
- `EBL_decision_log.md` — what was decided, why, scope, status and supersession;
- `EBL_asset_registry.json` — canonical asset IDs, fingerprints, parent/variant relationships and unresolved metadata;
- `EBL_failure_memory.md` — negative memory / known failure patterns;
- `EBL_visual_examples.md` — approved, rejected and candidate visual calibration index;
- `EBL_retrieval_map.md` — task-specific memory routing;
- `QC-EBL-MEM-001_memory_compliance_qc.md` — verifies memory was retrieved and applied correctly;
- `QC-EBL-001_project_master_qc.md` — verifies the actual EBL asset after memory compliance.

Core principle:

```text
MEMORY EXISTS
≠ MEMORY RETRIEVED
≠ MEMORY APPLIED CORRECTLY
```

All three must be verified.

#### Canonical asset discipline

Identity assets use explicit asset IDs.

Current chosen logo:

`EBL-ASSET-LOGO-001 — Geometric Reader Integrated Logo`

The source binary fingerprint has been verified and is stored in `EBL_asset_registry.json`, while the repository binary path remains unresolved. Missing repository path must not be invented.

A written logo description is memory, not a substitute for the exact canonical binary when exact placement is required.

#### Active EBL project package

Current EBL production knowledge includes:

- `00_workflow/knowledge/project/EBL_memory_registry.json`
- `00_workflow/knowledge/project/EBL_project_memory.md`
- `00_workflow/knowledge/project/EBL_approved_project_rules.md`
- `00_workflow/knowledge/project/EBL_decision_log.md`
- `00_workflow/knowledge/project/EBL_asset_registry.json`
- `00_workflow/knowledge/project/EBL_failure_memory.md`
- `00_workflow/knowledge/project/EBL_visual_examples.md`
- `00_workflow/knowledge/project/EBL_retrieval_map.md`
- `00_workflow/knowledge/project/EBL_logo_application_rules.md`
- `00_workflow/knowledge/project/EBL_post_01_approved_decisions.md`
- `00_workflow/knowledge/project/EBL_story_template_rules.md`

Post-specific copy/layout decisions must not be silently generalized to future posts.

The exact current Story template remains a `PROJECT_REFERENCE / REVIEW_CANDIDATE` until explicit human approval promotes it.

#### EBL memory compliance QC

Registered in:

`00_workflow/qc/QC-EBL-MEM-001_memory_compliance_qc.md`

This QC verifies:

- correct memory registry loaded;
- task-specific retrieval set loaded;
- current human instruction has highest priority;
- newest non-superseded decisions used;
- canonical asset IDs/states respected;
- missing metadata not invented;
- candidate vs approved states preserved;
- failure memory checked;
- memory-to-QC trace recorded.

A memory-compliance failure blocks final project QC.

#### EBL project master QC

Registered in:

`00_workflow/qc/QC-EBL-001_project_master_qc.md`

This QC is project-specific and mandatory for EBL final visual review. It orchestrates specialized QC modules and checks:

- memory compliance;
- content/meaning fidelity;
- public brand name;
- chosen-logo fidelity;
- visual identity;
- meaning-to-form synthesis;
- semantic typography;
- painterly/material integrity;
- known failure memory;
- artifact/repair integrity;
- carousel/system consistency;
- Story-specific behavior;
- export/master/derivative handling;
- final-AI closed-loop compliance;
- evidence package completeness;
- human final approval state.

For EBL run:

```text
QC-EBL-MEM-001
→ specialized asset QC
→ QC-EBL-001
```

#### Active supplied EBL brief

Registered in:

`00_workflow/knowledge/project/english_beyond_language_content_brief.md`

Source ID: `EBL-SRC-001`. The record is project-scoped and pending confirmation as the current approved brief. Its directions must pass through Strategy reconciliation before becoming authoritative downstream decisions.

### 2. External / Named-Style Knowledge

Stores knowledge about artists, movements, books, articles, exhibitions, professional design guidance, platform-owner guidance, and other external sources.

Examples:

- Paul Klee;
- Bauhaus;
- museum publications;
- academic books/articles;
- artist interviews;
- professional typography/layout guidance;
- platform-owner publishing guidance.

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

The package currently includes source-derived guidance from Adobe, Meta, MoMA and The Met.

These sources may improve late-stage creative judgment, but they do **not** override:

1. current human instruction;
2. approved project memory/rules;
3. approved content / artifacts;
4. supplied project sources.

### 3. Project Reference Knowledge

Stores observations extracted from project-supplied visual references, audio, video, screenshots, moodboards, approved output candidates, and other reference material.

A candidate may inform later work without automatically becoming an approved reusable rule.

### 4. Derived Creative Knowledge

Stores approved interpretations and transferable principles derived from the above sources.

Examples:

- EBL style rules;
- motif classifications;
- approved visual grammar;
- reusable Instagram template rules;
- source-informed creative synthesis heuristics.

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

Its orchestration protocol is:

`00_workflow/final_ai_closed_loop_production.md`

### 6. External Technical Knowledge

Stores authoritative tooling and production references that may support evidence-based execution without becoming aesthetic or project rules.

Current references include:

- `gftools_font_engineering.md`;
- `awesome_typography_resource_index.md`;
- `github_persian_font_topic.md`;
- `font_store_persian_fonts.md`;
- `awesome_persian_resource_index.md`.

Treat discovery indexes as routes to primary sources rather than primary evidence.

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

## Unknown Discipline

Never fabricate unknown canonical metadata.

Use explicit values such as:

```text
UNKNOWN
PENDING_VERIFICATION
null
```

for unresolved:

- asset paths;
- hashes;
- dimensions;
- provenance;
- licenses;
- approval states.

If an unknown blocks exact execution, surface the blocker.

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

## Retrieval Rule

### Any EBL visual task

```text
EBL_memory_registry.json
→ EBL_retrieval_map.md
→ EBL_project_memory.md
→ EBL_approved_project_rules.md
→ EBL_decision_log.md
→ EBL_failure_memory.md
→ task-specific asset/content/platform memory
→ QC-EBL-MEM-001
→ specialized QC
→ QC-EBL-001
```

### EBL logo task

Add:

```text
EBL_asset_registry.json
→ EBL_logo_application_rules.md
→ QC-LOGO-001
```

### EBL Story task

Add:

```text
EBL_story_template_rules.md
→ EBL_asset_registry.json
→ Story content objective
```

### EBL typography repair

Add:

```text
exact content decision
→ QC-TYPE-001
→ typography_native_reconstruction.md
→ cleanest approved source/textless master
```

### EBL Final AI / Heavy QC

Add:

```text
EBL_visual_examples.md
→ final_ai_production_learnings.md
→ final_ai_closed_loop_production.md
→ creative_synthesis_sources.md
→ all applicable QC
```

## Priority Rule

When sources conflict:

1. explicit current human decision;
2. newest non-superseded approved project decision;
3. approved project memory / project rule;
4. canonical asset registry;
5. content-specific approved decision;
6. approved system workflow rule for process behavior;
7. supplied project source evidence;
8. authoritative external source;
9. model inference.

A system workflow rule controls **how the process is executed**; it must not override project-specific creative/content decisions.

Conflicts must be surfaced rather than silently reconciled.

## Human-Directed Revision Knowledge

Human-directed output revision is governed by:

`00_workflow/human_feedback_style_learning.md`

```text
HUMAN = decides WHAT to edit
REFERENCE = informs HOW the requested edit should look
AI = applies the requested edit
```

A specific aesthetic correction becomes reusable style knowledge only through the normal approval/promotion process.

## Privacy / Scope

Client knowledge must remain project-scoped. Do not promote confidential client information into the global/system knowledge layer.

Updated: 2026-08-16
