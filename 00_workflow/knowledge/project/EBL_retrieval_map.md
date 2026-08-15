# English Beyond Language — Retrieval Map

## Purpose

Make EBL memory operational by retrieving only the memory required for the current task while never omitting mandatory identity/QC context.

## Core Rule

```text
TASK
→ IDENTIFY ASSET / PLATFORM / ACTION
→ RETRIEVE REQUIRED MEMORY SET
→ CHECK CONFLICT / SUPERSESSION
→ EXECUTE
→ RUN MEMORY-COMPLIANCE QC
```

Do not retrieve the entire project indiscriminately when a smaller authoritative set is sufficient. Do not omit mandatory core memory merely to save context.

---

# Always-Retrieve Core

For any EBL visual creation or revision:

1. `EBL_memory_registry.json`
2. `EBL_project_memory.md`
3. `EBL_approved_project_rules.md`
4. `EBL_decision_log.md`
5. `EBL_failure_memory.md`
6. `QC-EBL-MEM-001_memory_compliance_qc.md`

Then add task-specific memory below.

---

# Task Routing

## A. Logo Use / Logo Replacement

Retrieve:

- core set;
- `EBL_asset_registry.json`;
- `EBL_logo_application_rules.md`;
- `QC-LOGO-001_logo_application_qc.md`;
- `QC-EBL-001_project_master_qc.md`;
- approved source artwork being revised.

Required asset resolution:

```text
EBL-ASSET-LOGO-001
or explicitly approved child variant
```

If the canonical binary cannot be resolved, do **not** regenerate a substitute. State `CANONICAL_ASSET_UNRESOLVED` and request/use the verified supplied asset.

---

## B. Carousel / Feed Post Creation

Retrieve:

- core set;
- content-specific decision record;
- `EBL_visual_examples.md`;
- `QC-EBL-001_project_master_qc.md`;
- Instagram visual/audience QC;
- chosen-logo rules if branding is present;
- approved Visual DNA / art-direction sources.

For an existing approved carousel, also retrieve its exact decision file before revising.

---

## C. Carousel Revision

Retrieve:

- all Carousel Creation memory;
- approved source slide/set;
- `human_feedback_style_learning.md`;
- relevant failure records;
- typography/logo QC if touched.

Execution rule:

```text
AUTHORIZED DELTA ONLY
→ PRESERVE UNRELATED APPROVED ELEMENTS
```

---

## D. Typography Repair / Typography Refinement

Retrieve:

- core set;
- exact approved copy decision;
- `QC-TYPE-001_typography_integrity_qc.md`;
- `typography_native_reconstruction.md`;
- cleanest approved source/textless master;
- relevant visual example/failure records.

If text is raster-damaged, source-based native reconstruction takes precedence over repeated recoloring.

---

## E. Instagram Story Creation

Retrieve:

- core set;
- `EBL_story_template_rules.md`;
- `EBL_asset_registry.json`;
- `EBL_visual_examples.md`;
- `QC-EBL-001_project_master_qc.md` Story gate;
- content-specific Story objective/copy.

Remember:

- 1080×1920 / 9:16;
- Story-native reading path;
- usable interaction/sticker zone;
- secondary branding;
- no fake Instagram UI in clean reusable master;
- current exact Story-template composition remains a review candidate until human-approved.

---

## F. Profile / Teacher Portrait

Retrieve:

- core set;
- teacher identity source/reference;
- `QC-IG-PROFILE-001_instagram_profile_picture_qc.md`;
- project profile-image rule;
- chosen-logo memory only if branded avatar is explicitly requested.

Priority:

```text
RECOGNITION > DECORATION
```

---

## G. Final Creative AI Edit

Retrieve:

- core set;
- `EBL_asset_registry.json`;
- `EBL_visual_examples.md`;
- content-specific decisions;
- approved source/master/textless master;
- `final_ai_closed_loop_production.md`;
- `final_ai_production_learnings.md`;
- `creative_synthesis_sources.md`;
- all applicable asset-specific QC.

Classify each asset P0–P4 before editing.

---

## H. Heavy QC / Final Output

Retrieve:

- everything from Final Creative AI Edit;
- `QC-EBL-001_project_master_qc.md`;
- `QC-EBL-MEM-001_memory_compliance_qc.md`;
- platform export requirements;
- final candidate set.

Mandatory output includes memory-compliance result plus normal creative/technical QC evidence.

---

## I. Learning / Structuralization

Retrieve:

- current human learning instruction;
- core memory;
- decision log;
- failure memory;
- visual examples;
- system promotion policy.

Classify the new learning:

```text
ONE_OFF
CONTENT_SPECIFIC
REUSABLE_EBL_PROJECT_RULE
CROSS_PROJECT_SYSTEM_RULE
```

Do not promote exact one-off composition/coordinates to durable project rules without explicit approval.

---

# Conflict Resolution

When retrieved records disagree:

1. current explicit human instruction;
2. newest non-superseded approved EBL decision;
3. approved project memory/rule;
4. canonical asset registry;
5. content-specific record;
6. approved example/reference;
7. external evidence;
8. model inference.

If two approved records remain genuinely incompatible, stop and surface the conflict instead of silently choosing.

---

# Retrieval Evidence

Every final EBL QC report should record at minimum:

```text
MEMORY_REGISTRY_VERSION
MEMORY_FILES_RETRIEVED
DECISION_IDS_APPLIED
ASSET_IDS_APPLIED
FAILURE_IDS_CHECKED
UNRESOLVED_UNKNOWN_FIELDS
CONFLICTS_FOUND
```
