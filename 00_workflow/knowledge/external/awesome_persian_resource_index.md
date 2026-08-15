# Awesome Persian — Persian-Language Resource Index

## Purpose

This record registers Awesome Persian as a broad discovery index for Persian-supporting fonts, RTL frameworks, CSS resources, text-processing tools, calendars, localization libraries, interface guidance, and development resources.

For this Prompt Library, its primary permitted role is to expand Persian typography and production research beyond font binaries: text normalization, Unicode handling, RTL interfaces, Persian numerals, localization, and implementation tooling can materially affect whether Persian typography works correctly in a final artifact.

```text
KB_ID: FA-RESOURCE-INDEX-001
KNOWLEDGE_TYPE: EXTERNAL_REFERENCE_INDEX
AUTHOR / CREATOR: fffaraz and repository contributors
TITLE: Awesome Persian
PUBLISHER / INSTITUTION: Community-maintained GitHub repository
SOURCE_FORMAT: Public curated link collection
SOURCE_ID: FA-RESOURCE-INDEX-001
STATUS: SOURCE_FACT / REFERENCE_INDEX
SCOPE: SYSTEM_PERSIAN_LANGUAGE_RESOURCE_DISCOVERY
AUTHORITY: LOW TO MEDIUM — broad discovery source; linked primary sources require independent verification
APPROVAL_STATUS: ACTIVE_SOURCE
PROVENANCE: https://github.com/fffaraz/awesome-persian, master-branch README and repository metadata reviewed 2026-08-15.
LICENSE: UNKNOWN at review time; no repository-level license was visible in the reviewed root listing. Every linked resource retains its own license and terms.
```

## Source-Supported Coverage

The repository describes itself as a curated list of Persian-supporting tools, fonts, and development resources. Its visible categories included:

- RTL-capable web frameworks and CSS resources;
- modern Persian webfont links;
- Persian and Gregorian/Jalali calendar libraries;
- Persian OCR, character conversion, normalization, spell-checking, and NLP;
- Persian GUI guidance;
- font installers, font galleries, and text-rendering helpers;
- JavaScript, Python, C#, Ruby, Go, and other localization utilities.

The fonts section was small at review time and linked to Farsi Font Store plus an icon/font project. The broader value of this index is therefore contextual discovery around Persian-language production, not a comprehensive or vetted font catalogue.

## Permitted Workflow Use

### RES-005 — Visual Reference Research

Use `FA-RESOURCE-INDEX-001` when a Persian-language visual or content project needs research into fonts, RTL presentation, Persian interface conventions, web typography, text-processing constraints, or implementation references.

Only promote a listed entry into the reference set after opening its primary source and checking current relevance, maintenance, license, provenance, and fit with the explicit project question.

### VIS-005 — Typography & Graphic Language

Use the index to discover sources that help test or explain Persian typography behavior, including RTL flow, Unicode normalization, Persian/Arabic character distinctions, numeral conventions, mixed-script layout, punctuation, ZWNJ behavior, and webfont delivery.

Do not cite Awesome Persian itself as proof that a linked font renders correctly or that a development library implements Persian text safely. Cite verified primary documentation and actual test evidence.

## Relationship to Other Registered Sources

```text
FA-RESOURCE-INDEX-001
  broad Persian language / RTL / implementation discovery

FA-FONT-INDEX-001
  dynamic GitHub topic for Persian-font candidates

FA-FONT-COLLECTION-001
  focused Farsi Font Store collection

GFTOOLS-SRC-001
  optional technical inspection of actual font files
```

Use the smallest relevant source path. Do not query every index mechanically when one verified primary source already answers the research question.

## Candidate Verification Checklist

For each selected linked resource, record and verify:

1. canonical upstream URL, owner, and project identity;
2. resource type: font, framework, CSS package, text library, calendar, interface guide, installer, gallery, or service;
3. current maintenance state, release/version, supported environments, and deprecation status;
4. code, font, data, content, and asset licenses as separately applicable;
5. whether Persian support is native, partial, legacy, patched, or merely claimed;
6. Unicode normalization and Persian-versus-Arabic code-point behavior where text processing is involved;
7. RTL, bidirectional, mixed-script, numeral, punctuation, and ZWNJ behavior in the target environment;
8. security and privacy implications before adopting installers, browser code, remote services, or dependencies;
9. accessibility and compatibility with the required platform and production pipeline;
10. independent test evidence for any critical behavior.

## Decision Rules

1. **Curated inclusion is not validation.** A list entry is a discovery lead, not a technical, cultural, security, or legal endorsement.
2. **Expect legacy resources.** Some linked frameworks or libraries may target obsolete platform versions; verify current applicability before use or recommendation.
3. **Separate font and software decisions.** A typography task does not authorize installing a framework, extension, package, or system font installer.
4. **No license inheritance.** The index's unknown repository license and any linked project's license are separate; verify both when reuse of index content or linked assets matters.
5. **Persian support must be tested.** Claims of RTL or Arabic support do not prove correct Persian characters, shaping, normalization, or mixed-script behavior.
6. **Prefer primary and current sources.** Use current Unicode, browser, platform, framework, library, or font documentation after discovery.
7. **No automatic project promotion.** A discovered resource becomes a project choice only through normal evidence, compatibility, security, licensing, and human-approval gates.

## Unknowns and Limits

- The catalogue may contain moved, archived, obsolete, unmaintained, or insecure resources.
- Descriptions may be brief, misspelled, incomplete, or outdated.
- The reviewed repository root did not expose a license file, so reuse terms for the list itself remain unknown.
- Persian-language correctness can depend on content conventions and target context, not only software behavior.
- The list is not a substitute for a Persian-language editor, typographer, accessibility reviewer, or security review.

## Project-Use Caution

This source is `ACTIVE_SOURCE` and `NOT_PROMOTED`. It broadens discovery of Persian-language production resources. It does not create an approved font list, authorize a dependency, or establish a reusable EBL typography rule.
