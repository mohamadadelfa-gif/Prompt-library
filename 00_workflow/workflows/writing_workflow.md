# Writing Workflow

## Purpose

The Writing Workflow is the textual-content branch of the Prompt Library. It operates independently from Design while using the same controlled information model: `SOURCE → DERIVED → DECISION → OUTPUT`.

Writing owns:

- textual research and source evaluation;
- article/document analysis;
- claim and key-term extraction;
- content strategy and synthesis;
- outlining and reading structure;
- drafting and rewriting;
- summarization and explanation;
- language-level, tone, and audience adaptation;
- captions, hooks, CTAs, keywords, scripts, and textual accessibility intent;
- factual/claim review;
- Writing QC;
- human content approval;
- approved handoff to Design.

Writing does not approve visual composition, style, generation, or visual QC.

## Canonical Machine Layer

- `00_workflow/writing_task_registry.json`
- `00_workflow/writing_task_contracts.json`
- `00_workflow/writing_process_registry.json`
- `tests/validate_writing.py`
- `tests/writing_evaluation_rubric.md`
- `00_workflow/workflows/cross_workflow_handoff_contract.md`

The Writing workflow may exist structurally with zero active prompts. Every future Writing prompt must be registered in the Writing task registry and contracts before it can pass CI.

## Canonical Stages

```text
01 WST   Writing Strategy
   ↓
02 WRES  Textual Research
   ↓
03 WAN   Source Analysis
   ↓
04 WSYN  Content Synthesis
   ↓
05 WSTR  Content Structure
   ↓
06 WDR   Drafting
   ↓
07 WLANG Language Adaptation
   ↓
08 WQC   Writing Quality Control
   ↓
09 WAPP  Human Content Approval
   ↓
10 WHOFF Design Handoff
```

### 01 — Writing Strategy

Define content purpose, audience, platform, language level, tone, source needs, constraints, desired reader response, and approval requirements before research or drafting.

### 02 — Textual Research

Search for and record useful textual sources with provenance, reliability, date, scope, and intended use.

### 03 — Source Analysis

Understand the source before writing. Extract structure, key terms, claims, evidence, complexity, limitations, uncertainty, and useful explanatory relationships.

### 04 — Content Synthesis

Select and combine source-backed ideas into a coherent content thesis. Synthesis must not convert interpretation into fact.

### 05 — Content Structure

Build the reading order, hierarchy, outline, content units, and platform-specific text structure before drafting.

### 06 — Drafting

Create the text inside the approved brief and structure. Drafting must not invent unsupported claims or silently change requirements.

### 07 — Language Adaptation

Adapt vocabulary, sentence complexity, tone, and register while preserving meaning and factual status. A simpler linguistic form must not become a simpler or different idea.

### 08 — Writing QC

Evaluate at minimum:

- source quality;
- factual accuracy;
- claim-evidence relationship;
- unknown handling;
- purpose and relevance;
- audience fit;
- language-level fit;
- meaning preservation;
- clarity and structure;
- tone/voice;
- grammar/style;
- project-specific rules;
- downstream handoff quality.

Use `tests/writing_evaluation_rubric.md`.

### 09 — Human Content Approval

Writing intended for publication or Design handoff requires the applicable human approval. Writing approval does not imply Design approval.

### 10 — Design Handoff

Transfer only an approved Writing version through `cross_workflow_handoff_contract.md`.

## Accessible Explanation Pattern

For complex material:

```text
SOURCE
→ CORE IDEA
→ KEY TERMS
→ CLAIMS + EVIDENCE
→ COMPLEXITY / UNCERTAINTY
→ EXAMPLE OR ANALOGY WHEN USEFUL
→ AUDIENCE-APPROPRIATE EXPLANATION
→ MEANING-PRESERVING LANGUAGE ADAPTATION
→ FACT CHECK
→ WRITING QC
```

## Research and Shared Knowledge

Writing may use shared project research, brand memory, terminology, cultural/context research, external sources, tools, and approved platform constraints. Shared evidence does not carry Design approval or creative authority into Writing.

Visual references are not factual textual sources unless they contain reliable textual evidence that is explicitly extracted and evaluated.

## Boundary Rule

```text
WRITING OWNS MEANING, CLAIMS, LANGUAGE, AND TEXTUAL STRUCTURE.
DESIGN OWNS VISUAL COMMUNICATION OF APPROVED WRITING.
```

If Design needs a semantic rewrite because of space or platform constraints, it must send a Design → Writing handoff. Writing issues a new version; Design never silently edits meaning.
