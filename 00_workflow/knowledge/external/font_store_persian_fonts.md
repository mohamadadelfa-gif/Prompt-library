# Farsi Font Store — Persian/Farsi Font Repository Collection

## Purpose

This record registers the Farsi Font Store GitHub organization as a focused discovery collection for Perso-Arabic typefaces, Persian font-testing tools, webfont packages, and related resources.

The organization is more focused than a general topic page, but organization membership still does not automatically establish authorship, canonical provenance, current maintenance, license applicability, or production suitability for every repository.

```text
KB_ID: FA-FONT-COLLECTION-001
KNOWLEDGE_TYPE: EXTERNAL_FONT_COLLECTION
AUTHOR / CREATOR: Farsi Font Store and individual repository contributors
TITLE: Farsi Font Store GitHub Organization
PUBLISHER / INSTITUTION: Farsi Font Store
SOURCE_FORMAT: Public GitHub organization and repository collection
SOURCE_ID: FA-FONT-COLLECTION-001
STATUS: SOURCE_FACT / REFERENCE_INDEX
SCOPE: SYSTEM_PERSIAN_FONT_DISCOVERY
AUTHORITY: MEDIUM — specialist Perso-Arabic type-foundry collection; repository-level evidence still required
APPROVAL_STATUS: ACTIVE_SOURCE
PROVENANCE: https://github.com/font-store, reviewed 2026-08-15; the organization described itself as a type foundry and design studio focused on Perso-Arabic typefaces and displayed 26 public repositories.
```

## Observed Coverage at Review Time

The organization page presented font families and related projects including:

- Behdad/Farbod, Nika, Ganjnameh, and other Persian/Arabic font repositories;
- an Iranian family-font collection;
- a modified IranNastaliq distribution;
- a Persian-font CDN and presentation site;
- Persian font-testing and OpenType-testing tools;
- auxiliary typography and editing tools.

Several displayed font repositories were labelled OFL-1.1 by GitHub, while tooling repositories showed other licenses. These page-level labels are discovery signals only; verify the actual license files, copyright notices, reserved font names, and asset-specific terms inside each selected repository.

## Permitted Workflow Use

### RES-005 — Visual Reference Research

Use `FA-FONT-COLLECTION-001` to discover focused Persian/Farsi and Perso-Arabic font candidates, specimens, test tools, and production references when those needs are established by the project brief.

Create a separate reference record for each selected repository or font family. Record its canonical URL, creator, version or commit, license, formats, specimen source, intended use, and the project question it addresses.

### VIS-005 — Typography & Graphic Language

Analyze verified specimens or supplied font files from selected repositories. Where bilingual Persian/Latin work is required, evaluate the two scripts both independently and together for hierarchy, weight, proportion, rhythm, contrast, spacing, numerals, and punctuation.

Do not treat a family as suitable merely because it is described as Persian/Arabic or open source. Apply the Persian coverage and shaping checks defined by `FA-FONT-INDEX-001`.

## Source Hierarchy

For a selected font, use this evidence order:

```text
CANONICAL FONT REPOSITORY / RELEASE
        ↓
FONT LICENSE + COPYRIGHT / AUTHORSHIP FILES
        ↓
SOURCE FILES / FONT BINARIES + VERSION METADATA
        ↓
OFFICIAL SPECIMEN / DOCUMENTATION
        ↓
TARGET-APPLICATION RENDER + PERSIAN TEST STRINGS
        ↓
FONT STORE ORGANIZATION PAGE
```

The organization page supports discovery and collection context. It should not replace the higher-priority repository-level evidence above.

## Candidate Verification Checklist

In addition to the checks in `FA-FONT-INDEX-001`, verify:

1. whether the organization repository is the original project, an official continuation, a fork, mirror, package, or modified distribution;
2. whether the font name in the repository description matches internal family and style names;
3. whether downloadable binaries correspond to source files and documented releases;
4. whether OFL reserved font names or modification clauses affect redistribution or renaming;
5. whether the repository license covers every font binary, source, specimen, and webfont package being considered;
6. whether a CDN or third-party package is appropriate for production, or whether a pinned, locally controlled asset is required;
7. whether older repositories still behave correctly in the target shaping and rendering stack;
8. whether a modified historical or proprietary-origin font has sufficiently clear redistribution provenance.

## Tool Routing

When actual font files are obtained from a verified repository:

- use `GFTOOLS-SRC-001` for optional metadata, coverage, features, variable-font data, comparisons, and reproducible renders;
- use Persian/RTL test strings and the target application for shaping verification;
- use the repository's own font-testing pages only as supplemental evidence;
- preserve the downloaded file checksum, source URL, commit or release, and license with the research record.

## Decision Rules

1. **Collection membership is not approval.** Every font remains a candidate until individual review and human selection.
2. **Repository provenance matters.** Prefer canonical releases; explicitly label forks, modifications, mirrors, and repackaged files.
3. **License labels require confirmation.** Read the actual license and copyright files; do not rely only on GitHub's badge.
4. **No remote-CDN default.** Do not introduce a third-party font CDN into production without explicit technical, privacy, availability, and versioning approval.
5. **No silent font modification.** Subsetting, renaming, conversion, hinting, or table repair creates a derived asset and must comply with the license and production provenance rules.
6. **No blanket download or installation.** Retrieve only selected candidates required by the current task.
7. **Current verification required.** Refresh the organization and selected repository before a current production or licensing decision.

## Unknowns and Limits

- Repository count, visibility, activity, ownership, descriptions, and files can change.
- Some displayed projects were last updated several years before the review date.
- A repository may contain multiple artifacts governed by different terms.
- GitHub metadata cannot guarantee font quality, correct Persian shaping, accessibility, security, or legal suitability.
- The collection does not replace review by a Persian typography specialist where cultural or high-visibility accuracy matters.

## Project-Use Caution

This source is `ACTIVE_SOURCE` and `NOT_PROMOTED`. It is a focused candidate collection, not an approved EBL font list. Fonts, tools, packages, and CDN resources require individual verification and explicit project approval before adoption.
