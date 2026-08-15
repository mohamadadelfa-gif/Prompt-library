# GitHub `persian-font` Topic — Persian/Farsi Font Discovery Index

## Purpose

This record registers GitHub's `persian-font` topic page as a dynamic discovery index for repositories related to Persian/Farsi fonts, Arabic-script typography, RTL support, and adjacent tooling.

The topic page is not a vetted font library. Repositories self-associate with topics, results change over time, and some results are applications or unrelated projects rather than usable font families.

```text
KB_ID: FA-FONT-INDEX-001
KNOWLEDGE_TYPE: EXTERNAL_DYNAMIC_REFERENCE_INDEX
AUTHOR / CREATOR: GitHub topic participants and repository owners
TITLE: GitHub Topic: persian-font
PUBLISHER / INSTITUTION: GitHub
SOURCE_FORMAT: Dynamic public topic aggregation
SOURCE_ID: FA-FONT-INDEX-001
STATUS: SOURCE_FACT / REFERENCE_INDEX
SCOPE: SYSTEM_PERSIAN_FONT_DISCOVERY
AUTHORITY: LOW TO MEDIUM — useful discovery surface; every repository requires primary-source verification
APPROVAL_STATUS: ACTIVE_SOURCE
PROVENANCE: https://github.com/topics/persian-font, reviewed 2026-08-15; the page reported 14 matching public repositories at review time.
```

## Observed Coverage at Review Time

The topic results included a mixture of:

- Persian/Arabic and Latin companion font repositories;
- Persian pixel fonts;
- Nastaliq and other Persian-script font projects;
- Persian webfont or CSS projects;
- browser extensions and Android customization tools;
- RTL/Persian-capable applications;
- repositories only incidentally tagged with `persian-font`.

These observations describe the topic page at the review date. They do not establish the quality, authenticity, license, safety, completeness, or continued availability of any listed repository.

## Permitted Workflow Use

### RES-005 — Visual Reference Research

Use `FA-FONT-INDEX-001` when the reconciled project requires Persian/Farsi typography, Arabic-script support, RTL behavior, bilingual Persian/Latin typography, Persian type specimens, or culturally relevant font references.

Each candidate selected from the page must receive its own reference ID and primary-repository review. Record why it answers a project question; do not select it merely because it carries the topic tag.

### VIS-005 — Typography & Graphic Language

Use verified candidate repositories and their supplied specimens or font binaries—not the topic listing itself—as evidence. Distinguish:

- Persian/Farsi support from generic Arabic-script support;
- a font family from a browser extension, CSS package, application, or system modification;
- visual character from technical script coverage;
- Latin companion quality from Persian letterform quality;
- metadata claims from tested shaping and rendering behavior.

## Candidate Verification Checklist

Before recommending, testing, downloading, or using a candidate font, verify:

1. **Repository identity** — owner, canonical upstream, project description, releases, and whether the repository contains actual font sources or binaries.
2. **License** — explicit font and code licenses; confirm embedding, modification, redistribution, webfont, application, and commercial-use rights as applicable.
3. **Persian coverage** — required Persian characters and punctuation, not only an `Arabic` label or a topic tag.
4. **Shaping behavior** — joining forms, contextual alternates, marks, ligatures where relevant, RTL ordering, and OpenType layout behavior in the target environment.
5. **Persian distinctions** — test Persian Yeh and Kaf forms, Persian digits where required, Arabic-script punctuation, and project-specific character coverage.
6. **Text behavior** — spacing, diacritics, mixed Persian/Latin text, numerals, punctuation, line breaking, and zero-width non-joiner behavior where relevant.
7. **Technical metadata** — family/style names, weights, widths, variable axes, version, supported formats, and internal consistency.
8. **Maintenance and provenance** — recent activity, releases, issue state, documented sources, authorship, and whether the project is an authorized distribution.
9. **Target compatibility** — Figma, web, print, operating system, browser, export pipeline, or other required production context.
10. **Visual suitability** — hierarchy, legibility, tone, bilingual harmony, and consistency with approved project direction.

## Evidence and Tool Routing

```text
PERSIAN TYPOGRAPHY REQUIREMENT
        ↓
FA-FONT-INDEX-001 CANDIDATE
        ↓
PRIMARY REPOSITORY + LICENSE REVIEW
        ↓
FONT FILE / SPECIMEN INSPECTION
        ↓
PERSIAN TEST STRING + RTL SHAPING TEST
        ↓
OPTIONAL GFTOOLS-SRC-001 TECHNICAL EVIDENCE
        ↓
VISUAL / CULTURAL REVIEW + HUMAN DECISION
```

When real font files are available, `GFTOOLS-SRC-001` may support metadata, character-set, language-support, feature, variable-font, comparison, or render evidence. It does not replace script-expert review, target-application testing, license review, or visual judgment.

## Decision Rules

1. **Topic membership is discovery metadata only.** It is not proof that a repository contains a font or properly supports Persian.
2. **Do not batch-adopt results.** Assess candidates individually and record rejected as well as selected candidates.
3. **Do not assume Arabic equals Persian.** Confirm Persian-specific glyphs, characters, language-system behavior, and test strings.
4. **Do not assume open repository equals open font.** Require an explicit applicable license from the canonical source.
5. **Do not install applications or system modifications during font research.** Those require a separate authorized technical and security review.
6. **Do not promote a candidate into a project font choice automatically.** Selection requires normal art-direction, licensing, production, and human-approval gates.
7. **Recheck dynamic facts.** Refresh the topic page and candidate repositories when the result will inform a current production decision.

## Unknowns and Limits

- Topic results, ordering, counts, descriptions, and update dates can change without notice.
- GitHub does not guarantee that topic tags are accurate or curated.
- Some repositories may be forks, mirrors, unauthorized distributions, incomplete packages, or abandoned projects.
- Metadata and character coverage do not guarantee correct Persian shaping or high-quality typography.
- A font may render differently across Figma, browsers, operating systems, PDF exporters, and image-generation workflows.

## Project-Use Caution

This source is `ACTIVE_SOURCE` and `NOT_PROMOTED`. It expands Persian-font discovery only. No listed font becomes an approved EBL font, global recommendation, bundled asset, or project dependency without individual verification and explicit approval.
