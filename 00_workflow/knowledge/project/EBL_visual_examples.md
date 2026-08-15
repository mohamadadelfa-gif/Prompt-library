# English Beyond Language — Visual Example Index

## Purpose

Provide visual calibration memory for EBL without pretending that a written rule alone is sufficient for visual judgment.

This index records **what an example teaches**. Actual image binaries should be added to the approved/rejected example folders only when their repository asset is available and verified.

## Status Vocabulary

```text
APPROVED_CALIBRATION
REJECTED_CALIBRATION
PROJECT_REFERENCE
REVIEW_CANDIDATE
ASSET_NOT_YET_INGESTED
```

---

# Approved Calibration Examples

## EBL-EX-A-001 — Post 01 Overall Visual Family

**Status:** APPROVED_CALIBRATION.  
**Artifact reference:** Approved/finalized EBL Post 01 six-slide visual essay from the production cycle. Exact repository image path is not asserted here.  
**Teaches:**

- warm paper/painterly identity;
- editorial visual essay rather than infographic;
- shared visual grammar with meaningful slide variation;
- rust/ochre/navy/olive/charcoal relationships;
- asymmetry and negative space;
- semantic progression across a carousel.

## EBL-EX-A-002 — Slide 1 Solid Typography

**Status:** APPROVED_CALIBRATION.  
**Artifact reference:** Refined Post 01 Slide 1 native typography reconstruction.  
**Teaches:**

- full optical stroke density;
- no faded/gray halo;
- exact word-level color emphasis;
- native-resolution type reconstruction after raster degradation.

## EBL-EX-A-003 — Chosen Logo Identity

**Status:** APPROVED_CALIBRATION / CANONICAL BINARY PENDING INGESTION.  
**Asset ID:** `EBL-ASSET-LOGO-001`.  
**Teaches:**

- exact Geometric Reader Integrated Logo construction;
- integrated brand typography is part of the logo;
- identity asset is placed, not regenerated.

## EBL-EX-A-004 — Small Production Signature

**Status:** APPROVED APPLICATION PATTERN / BINARY PENDING INGESTION.  
**Asset ID:** `EBL-ASSET-LOGO-001-APP-SMALL`.  
**Teaches:**

- branding remains secondary to content;
- repeated-set anchor/scale logic;
- optical clearance is more important than geometric bounds alone.

---

# Rejected Calibration Examples

## EBL-EX-R-001 — Faded Raster Typography

**Status:** REJECTED_CALIBRATION.  
**Failure ID:** `EBL-FAIL-001`.  
**Teaches:** Dark RGB values do not guarantee visually solid typography. Gray edge halos and weak stroke density are failures.

## EBL-EX-R-002 — Logo Cleanup Gray Blobs

**Status:** REJECTED_CALIBRATION.  
**Failure ID:** `EBL-FAIL-002`.  
**Teaches:** Removing the previous logo is not enough; the repaired paper/texture must look untouched.

## EBL-EX-R-003 — Regenerated Similar Logo

**Status:** REJECTED_CALIBRATION.  
**Failure ID:** `EBL-FAIL-003`.  
**Teaches:** Stylistic similarity is not identity fidelity.

## EBL-EX-R-004 — Numbering Drift

**Status:** REJECTED_CALIBRATION.  
**Failure ID:** `EBL-FAIL-005`.  
**Teaches:** Repeated components are system memory, not per-slide decoration.

## EBL-EX-R-005 — Visible Repair Rectangle

**Status:** REJECTED_CALIBRATION.  
**Failure ID:** `EBL-FAIL-006`.  
**Teaches:** Source-based reconstruction is preferable to accumulated raster patching.

## EBL-EX-R-006 — Generic Infographic / Language-School Drift

**Status:** REJECTED_CALIBRATION.  
**Failure ID:** `EBL-FAIL-010`.  
**Teaches:** A technically clean output still fails if it abandons EBL's editorial/painterly identity.

---

# Story Template Reference

## EBL-EX-C-001 — Current Story Template Candidate

**Status:** REVIEW_CANDIDATE.  
**Asset ID:** `EBL-ASSET-STORY-TPL-001`.  
**Teaches provisionally:**

- 1080×1920 Story-native space;
- large central content zone;
- edge-weighted painterly identity;
- secondary logo signature;
- interaction/sticker room;
- no fake Instagram UI in the clean reusable template.

**Important:** Exact composition/coordinates are not approved permanent memory until explicit human approval.

---

# Example Ingestion Discipline

When adding a real image example to the repository:

```text
1. ASSIGN EXAMPLE_ID
2. ADD VERIFIED REPO PATH
3. ADD FILE HASH IF USED AS CANONICAL CALIBRATION
4. STATE APPROVED / REJECTED / CANDIDATE
5. STATE WHAT IT TEACHES
6. LINK DECISION OR FAILURE ID
7. DO NOT INFER APPROVAL FROM FILE PRESENCE ALONE
```

Repository folders:

- `00_workflow/examples/EBL/approved/`
- `00_workflow/examples/EBL/rejected/`
