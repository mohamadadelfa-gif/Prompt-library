# Image Aesthetics Assessment — External Knowledge Package

## Purpose
Register external image- and graphic-design-aesthetics research as controlled knowledge for research and QC design. This package describes what the sources and model families can support; it does not turn model scores into aesthetic truth or project approval.

## Source records

### AES-SRC-001 — Awesome Image Quality Assessment

```text
KB_ID: AES-SRC-001
KNOWLEDGE_TYPE: EXTERNAL_DYNAMIC_REFERENCE_INDEX
TITLE: Awesome Image Quality Assessment
CREATOR: Chaofeng Chen and contributors
SOURCE_FORMAT: GitHub curated index
SOURCE_URL: https://github.com/chaofengc/Awesome-Image-Quality-Assessment
STATUS: SOURCE_FACT / REFERENCE_INDEX
SCOPE: SYSTEM_IMAGE_QUALITY_AND_AESTHETICS_DISCOVERY
AUTHORITY: MEDIUM — curated discovery index; linked primary sources remain authoritative
APPROVAL_STATUS: ACTIVE_SOURCE
PROVENANCE: Human-supplied URL reviewed 2026-08-15.
```

Supported use: discover full-reference, no-reference, AIGC-quality, explainable-quality, and image-aesthetic methods. The project currently implements selected methods through PyIQA.

### AES-SRC-002 — Awesome Aesthetics Assessment

```text
KB_ID: AES-SRC-002
KNOWLEDGE_TYPE: EXTERNAL_DYNAMIC_REFERENCE_INDEX
TITLE: Aesthetics Assessment Sources (Graphic Designs)
CREATOR: Sahil Goyal and contributors
SOURCE_FORMAT: GitHub curated index
SOURCE_URL: https://github.com/sahilg06/Awesome-Aesthetics-Assessment
STATUS: SOURCE_FACT / REFERENCE_INDEX
SCOPE: SYSTEM_GRAPHIC_DESIGN_AESTHETICS_DISCOVERY
AUTHORITY: MEDIUM — graphic-design-specific discovery index
APPROVAL_STATUS: ACTIVE_SOURCE
PROVENANCE: Human-supplied URL reviewed 2026-08-15.
```

Supported use: discover research on layout, visual importance, typography, color, graphic-design scoring, design-principle evaluation, posters, and human preference.

### AES-SRC-003 — GitHub image-aesthetics-assessment topic

```text
KB_ID: AES-SRC-003
KNOWLEDGE_TYPE: EXTERNAL_DYNAMIC_REFERENCE_INDEX
TITLE: GitHub image-aesthetics-assessment Topic
CREATOR: GitHub community repositories
SOURCE_FORMAT: Dynamic self-tagged repository index
SOURCE_URL: https://github.com/topics/image-aesthetics-assessment
STATUS: SOURCE_FACT / DISCOVERY_INDEX
SCOPE: SYSTEM_IMAGE_AESTHETICS_DISCOVERY
AUTHORITY: LOW — self-tagged and dynamic; every candidate requires independent verification
APPROVAL_STATUS: ACTIVE_SOURCE
PROVENANCE: Human-supplied URL reviewed 2026-08-15.
```

Supported use: discover candidate systems such as TANet, color-aesthetics assessment, EAT, ArtiMuse, UniPercept, explainable IAA, and personalized IAA. Inclusion on the topic page is not evidence of quality, compatibility, safety, or licensing.

### AES-SRC-004 — Regression Over Classification / ROC4MLLM

```text
KB_ID: AES-SRC-004
KNOWLEDGE_TYPE: EXTERNAL_PRIMARY_RESEARCH_IMPLEMENTATION
TITLE: Regression Over Classification: Assessing Image Aesthetics via Multimodal Large Language Models
CREATOR: Xingyuan Ma, Shuai He, Anlong Ming, Haobin Zhong, and Huadong Ma
SOURCE_FORMAT: AAAI 2026 paper and official GitHub implementation
SOURCE_URL: https://github.com/woshidandan/Assessing-Image-Aesthetics-via-Multimodal-Large-Language-Models
STATUS: SOURCE_FACT / RESEARCH_ONLY
SCOPE: CONTINUOUS_AESTHETIC_SCORE_REPRESENTATION
AUTHORITY: HIGH FOR CLAIMED METHOD; PROJECT VALIDATION STILL REQUIRED
APPROVAL_STATUS: ACTIVE_KNOWLEDGE / RUNTIME_NOT_INSTALLED
PROVENANCE: Human-supplied URL reviewed 2026-08-15.
```

Supported use: preserve fine-grained continuous aesthetic evidence and avoid classification-induced score quantization. The reference implementation uses a large mPLUG-Owl2-derived runtime and separate Python 3.10 environment, so it is retained as method knowledge and a future GPU candidate rather than downloaded into routine Heavy QC.

## Model knowledge map

| Family | Potential evidence | Known limitation | Current role |
|---|---|---|---|
| NIMA | General learned aesthetic-rating prior | AVA/population bias; largely photographic | Installed Heavy QC signal |
| MUSIQ-AVA | Multi-scale learned aesthetic prior | AVA bias; not brand- or project-specific | Installed Heavy QC signal |
| CLIP-IQA | Prompt-conditioned look-and-feel prior | Prompt sensitivity; broad internet semantics | Optional Heavy QC signal |
| TOPIQ-IAA | Semantic/local aesthetic prior | Large model; operationally expensive | Optional Heavy QC signal |
| TANet | Theme-aware aesthetic prior | Legacy runtime; theme taxonomy may not fit graphic design | Research candidate only |
| Color-oriented IAA | Color distribution/composition prior | Weight/runtime availability and legacy dependencies | Research candidate only |
| PosterReward | Poster-specific quality, artifacts, text, fidelity, aesthetics | Qwen3-VL-8B/vLLM/GPU footprint | Future GPU candidate only |
| Personalized IAA | Preference-conditioned aesthetic prior | Requires sufficient approved/rejected user evidence | Future calibrated candidate only |
| ROC4MLLM | Fine-grained regression-based MLLM aesthetic evidence | Large separate runtime; generic score still lacks project authority | Method knowledge / future GPU candidate |

## Derived knowledge candidates

These are `SOURCE_DERIVED / HUMAN_REVIEW_REQUIRED`, not approved universal rules:

1. Aesthetic assessment must separate technical integrity, general learned preference, graphic-design principles, project/brand fit, and individual human preference.
2. Graphic-design assessment should explicitly inspect hierarchy, balance, alignment, spacing, negative space, typography, color, visual complexity, and element consistency.
3. Theme-aware and color-aware models may add useful disagreement evidence but cannot determine meaning, brand direction, or approval.
4. Photography-trained aesthetic scores can misread painterly texture, flat color, text-heavy layouts, intentional irregularity, and graphic abstraction.
5. Model disagreement is uncertainty evidence; never hide it in an untraceable average.
6. Approved and rejected project outputs are more authoritative for preference calibration than generic internet-trained scores.
7. Personalized aesthetic learning requires explicit human labels, provenance, scope, and a minimum evidence set defined before training or calibration.
8. Dynamic catalogues route research to primary papers, official code, model cards, and licenses; catalogue inclusion alone cannot authorize installation.
9. Preserve continuous model precision: classification bins and score-token decoding can discard fine-grained evidence.
10. Cross-model comparisons require model-specific calibration; incompatible numeric ranges must not be averaged directly.

## Retrieval rule

```text
Aesthetic research request
  → retrieve AES-SRC-001 + AES-SRC-002 + AES-SRC-003 + AES-SRC-004
  → identify candidate primary source and official implementation
  → verify maintenance, runtime, weights, license, data assumptions, and asset-class fit
  → classify as INSTALLED / OPTIONAL / RESEARCH_ONLY / REJECTED
  → human approval before download or execution
```

For QC execution, retrieve this package to interpret model scope and bias, then apply `QC-AES-001` and applicable project QC. A source record never overrides an approved project rule or human decision.

## Version
1.1

## Status
Production Candidate
