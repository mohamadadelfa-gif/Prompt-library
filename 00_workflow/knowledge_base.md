# Knowledge Base Architecture

## Purpose

The Prompt Library uses separated knowledge layers so project-specific knowledge, external research, source evidence, and creative interpretation are never silently conflated.

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

### 2. External / Named-Style Knowledge

Stores knowledge about artists, movements, books, articles, exhibitions, and other external sources.

Examples:

- Paul Klee
- Bauhaus
- museum publications
- academic books/articles
- artist interviews

External knowledge requires source provenance.

### 3. Project Reference Knowledge

Stores observations extracted from project-supplied visual references, audio, video, screenshots, moodboards, and other reference material.

### 4. Derived Creative Knowledge

Stores approved interpretations and transferable principles derived from the above sources.

Examples:

- EBL style rules
- motif classifications
- approved visual grammar
- reusable Instagram template rules

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

## Retrieval Rule

Tasks should retrieve knowledge from the appropriate domain before execution:

```text
EBL task
  → EBL Project Knowledge

Named artist task
  → External / Named-Style Knowledge

Reference analysis
  → Project Reference Knowledge

Template / production task
  → Approved Project Rules + Platform Rules
```

## Priority Rule

When sources conflict:

1. explicit current client decision;
2. approved project rule;
3. supplied project source evidence;
4. authoritative external source;
5. model inference.

Conflicts must be surfaced rather than silently reconciled.

## Privacy / Scope

Client knowledge must remain project-scoped. Do not promote confidential client information into the global/system knowledge layer.
