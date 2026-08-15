# Awesome Typography — External Resource Index

## Purpose

This record registers Awesome Typography as a curated discovery index for digital-typography specifications, libraries, tools, validators, fonts, books, and videos.

The index helps locate candidate resources. It is not primary evidence for claims made by the linked projects, and inclusion does not constitute a project recommendation, security review, maintenance guarantee, license approval, or endorsement.

```text
KB_ID: TYPO-INDEX-001
KNOWLEDGE_TYPE: EXTERNAL_REFERENCE_INDEX
AUTHOR / CREATOR: Jolg42 and repository contributors
TITLE: Awesome Typography
PUBLISHER / INSTITUTION: Community-maintained GitHub repository
SOURCE_FORMAT: Public curated link collection
SOURCE_ID: TYPO-INDEX-001
STATUS: SOURCE_FACT / REFERENCE_INDEX
SCOPE: SYSTEM_DIGITAL_TYPOGRAPHY_DISCOVERY
AUTHORITY: MEDIUM — curated discovery source; linked primary sources require separate verification
APPROVAL_STATUS: ACTIVE_SOURCE
PROVENANCE: https://github.com/Jolg42/awesome-typography, main-branch README and repository metadata reviewed 2026-08-15.
LICENSE: CC0-1.0 applies to the index repository; linked resources retain their own licenses and terms.
```

## Source-Supported Coverage

The repository describes itself as a curated list about digital typography. Its catalogue includes:

- font-format and platform specifications;
- OpenType learning resources;
- font parsing, shaping, rendering, conversion, subsetting, and generation libraries across multiple programming languages;
- UFO resources;
- GUI font tools;
- font validators and testing websites;
- font projects and TrueType resources;
- books and videos.

The index includes gftools-adjacent resources such as FontTools, fontmake, FontBakery, FreeType, HarfBuzz, OpenType.js, specifications, renderers, validators, and font-difference utilities. Their presence in the list is only a discovery fact.

## Permitted Workflow Use

### RES-005 — Visual Reference Research

Use `TYPO-INDEX-001` when a project question specifically requires digital-typography resources, technical references, font tooling, type specimens, or typography-learning material. Select only links tied to an explicit research question. Follow each selected link and verify the resource at its primary source before recording substantive claims.

The catalogue itself is normally a `Structural` or `Exploratory` research reference, not a visual reference demonstrating an approved aesthetic direction.

### VIS-005 — Typography & Graphic Language

Use the index to discover specialist sources that clarify observed typographic mechanisms, terminology, OpenType behavior, rendering, or testing. Evidence in the final analysis must cite the verified primary specification, documentation, project, book, video, or supplied visual—not merely the catalogue entry.

## Discovery Routing

```text
TYPOGRAPHY QUESTION
        ↓
TYPO-INDEX-001 CATEGORY / CANDIDATE LINK
        ↓
PRIMARY SOURCE CHECK
        ↓
RELEVANCE + RECENCY + LICENSE / ACCESS CHECK
        ↓
PROJECT RESEARCH RECORD OR REJECTED CANDIDATE
```

Suggested routes:

- file-format or OpenType behavior → official Microsoft, Apple, Adobe, or relevant format specification;
- shaping and rendering → primary FreeType, HarfBuzz, Raqm, browser, or platform documentation;
- Python font engineering → primary FontTools, fontmake, FontBakery, gftools, or selected project documentation;
- web typography → primary library documentation plus current browser/platform documentation;
- tool selection → current upstream repository, release history, supported platforms, security posture, and license;
- books or videos → publisher, author, conference, or original-host metadata where available.

## Decision Rules

1. **Discovery is not verification.** Never cite a one-line catalogue description as sufficient support for a technical or historical claim.
2. **Verify current status.** Check the linked primary source for maintenance state, compatibility, release recency, and documentation before recommending or using a tool.
3. **Review each license.** CC0-1.0 for the index does not transfer to linked code, fonts, images, books, videos, or websites.
4. **No automatic installation.** Inclusion in the catalogue does not authorize adding a package or service to project dependencies.
5. **No automatic aesthetic transfer.** A typeface, specimen, or resource must pass normal relevance, provenance, project interpretation, and approval gates.
6. **Prefer authoritative sources.** For specifications and platform behavior, use the original standards owner or platform documentation after discovery.
7. **Record failures.** Broken, archived, unavailable, obsolete, or unsuitable links should be documented as rejected candidates rather than silently replaced by an unsupported claim.

## Unknowns and Limits

- The index changes over time and may contain stale, archived, moved, or unmaintained links.
- Catalogue descriptions may be brief, subjective, or outdated.
- The repository does not guarantee tool safety, correctness, platform compatibility, accessibility, or production readiness.
- Broad technical coverage does not make every entry relevant to visual art direction.
- Linked sources may have commercial, restrictive, incompatible, or unclear licenses.

## Project-Use Caution

This source is `ACTIVE_SOURCE` and `NOT_PROMOTED`. It may expand research coverage and help locate primary sources. It must not become an approved typography direction, implementation dependency, or system rule without normal verification and decision gates.
