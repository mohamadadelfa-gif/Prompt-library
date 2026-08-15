# QC-IG-PROFILE-001 — Instagram Profile Picture QC

## Purpose

Evaluate whether an Instagram profile picture is recognizable, trustworthy, readable at very small size, technically clean, and compatible with the project brand.

This QC is for profile/avatar images. It is not a substitute for feed-post, story, reel, or carousel QC.

## Core Principle

An Instagram profile picture is an identity asset, not a content graphic.

Priority order:

```text
RECOGNITION > DECORATION
NATURALNESS > STYLIZATION
FACE > BRANDING
SMALL-SIZE CLARITY > DETAIL
HUMAN APPROVAL > AUTOMATED SCORE
```

## Required Inputs

- source portrait
- refined portrait
- square master
- circular-crop preview
- 320 px preview
- 110 px preview
- 64 px preview
- 40 px preview
- optional brand-context preview beside recent Instagram posts

## Mandatory Gates

### PROFILE-01 Identity Fidelity — mandatory

The person must remain recognizably the same person.

Check:

- facial proportions preserved
- eyes preserved
- nose preserved
- mouth preserved
- moustache/beard preserved where applicable
- hairstyle preserved
- age not artificially changed
- no AI-generated facial reconstruction
- no excessive beauty retouching

Failure => FAIL regardless of score.

### PROFILE-02 Circular Crop Safety — mandatory

Check:

- hair has breathing room
- chin remains safe
- ears are not awkwardly clipped
- shoulders support the portrait
- face remains visually centered
- important features do not touch the circular boundary

Failure => revise crop before approval.

### PROFILE-03 Tiny-Size Recognition — mandatory

Test at:

```text
320 px → 110 px → 64 px → 40 px
```

At 40 px, the person should still be immediately recognizable.

Inspect:

- face silhouette
- eyes
- distinctive facial hair
- hair shape
- background separation

Failure => revise scale/crop/contrast.

### PROFILE-04 Image Integrity — mandatory

Reject visible:

- masking halos
- jagged hair edges
- AI artifacts
- duplicated hairs
- malformed eyes
- strange teeth
- plastic skin
- compression damage
- sharpening halos
- inconsistent lighting

### PROFILE-05 Human Approval — mandatory

AI QC cannot grant final approval. Human approval is required before publishing.

## Scored QC — 100 Points

| Category | Weight |
|---|---:|
| Recognition & Facial Presence | 20 |
| Crop & Composition | 15 |
| Small-Size Performance | 15 |
| Natural Retouching | 15 |
| Lighting / Color / Contrast | 15 |
| Background Separation | 10 |
| Brand Compatibility | 5 |
| Technical Output | 5 |
| **TOTAL** | **100** |

## A. Recognition & Facial Presence — 20

Check whether the face immediately dominates the image, whether the person is recognizable without study, and whether distinctive features are preserved.

## B. Crop & Composition — 15

Preferred structure:

```text
        breathing room

          HEAD
       ┌────────┐
       │  FACE  │
       └────────┘

      upper shoulders
```

Avoid a face that is either too small to recognize or so large that hair/chin feel cramped.

## C. Small-Size Performance — 15

At every reduction level inspect:

```text
face → eyes → distinctive features → silhouette → background separation
```

The avatar must survive reduction without becoming muddy.

## D. Natural Retouching — 15

Allowed:

- subtle skin cleanup
- color correction
- controlled sharpening
- slight local contrast
- minor clothing cleanup
- hair-edge cleanup
- small background corrections

Avoid:

- artificial skin
- facial reshaping
- eye enlargement
- nose reshaping
- excessive whitening
- artificial smile
- aggressive wrinkle removal
- artificial age reduction

Rule: improve the photograph, not the person.

## E. Lighting / Color / Contrast — 15

Check:

- natural skin tone
- controlled highlights
- readable shadow detail
- clear eyes
- hair/background separation
- clothing remains secondary to the face

Desired hierarchy:

```text
1. Face
2. Eyes / expression
3. Hair + distinctive facial features
4. Clothing
5. Background
```

## F. Background Separation — 10

Preferred background:

- simple
- quiet
- low-detail
- enough tonal contrast from hair/skin
- natural transition around hair

Avoid distracting texture, hard cutout edges, and backgrounds more visually dominant than the person.

## G. Brand Compatibility — 5

A teacher/founder portrait should remain a portrait first.

Brand compatibility may come through:

- warmth
- color temperature
- professionalism
- intellectual/cultural tone
- background choice

Do not automatically add logo, typography, graphic shapes, or decorative motifs unless a separate branded-avatar version is explicitly requested.

## H. Technical Output — 5

Check:

- square master
- circular-crop preview
- clean edges
- no visible compression artifacts
- consistent color
- sufficient resolution
- final-size sharpening
- source + final archived

Recommended working master: at least 1080 × 1080 px.

## Result Thresholds

```text
90–100  APPROVED
85–89   PASS — MINOR QC NOTES
75–84   REVISION REQUIRED
<75     FAIL
```

Mandatory-gate failure overrides the score.

## Workflow

```text
SOURCE PORTRAIT
      ↓
TECHNICAL CLEANUP
      ↓
NATURAL RETOUCH
      ↓
SQUARE CROP
      ↓
CIRCULAR CROP TEST
      ↓
TINY-SIZE TEST
320 → 110 → 64 → 40
      ↓
QC-IG-PROFILE-001
      ↓
HUMAN REVIEW
      ↓
APPROVED PROFILE MASTER
      ↓
INSTAGRAM EXPORT
```

## EBL Current Application

For English Beyond Language, when the teacher portrait is used as the Instagram profile image:

- the teacher's face is the primary information;
- the portrait should not be converted into a miniature poster;
- teacher identity fidelity is mandatory;
- branding must remain secondary to facial recognition;
- portrait refinement may improve masking, skin texture, color balance, local contrast, background naturalness, clothing dominance, and crop without changing recognizable facial features.

Status: `APPROVED_RULE` for project workflow after human instruction on 2026-08-15.
