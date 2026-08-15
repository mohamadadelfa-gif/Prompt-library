# English Beyond Language — Failure Memory

## Purpose

Store known EBL failure patterns so future production can detect and reject them before human review.

This is **negative memory**. It exists to prevent repeated mistakes.

Each failure record must include:

```text
FAILURE_ID
SYMPTOM
ROOT CAUSE
DETECTION
REQUIRED CORRECTION
PREVENTION RULE
STATUS
```

---

## EBL-FAIL-001 — Faded / Haloed Raster Typography

**Symptom:** Black text is technically dark but looks gray, weak, soft, outlined, translucent or uneven.  
**Root cause:** Repeated raster recoloring, inpainting, resizing or repair degrades antialiasing and optical stroke density.  
**Detection:** Native-resolution inspection of glyph interiors and edges.  
**Required correction:** Use cleanest approved source → reconstruct local background → redraw exact approved copy once at final native resolution → full-opacity type → no post-render resize.  
**Prevention:** Run `QC-TYPE-001` and reject `DARK RGB ≠ OPTICALLY SOLID TYPE`.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-002 — Logo Replacement Ghosts / Gray Blobs

**Symptom:** Gray blobs, smudges, clone seams, halos or residual marks remain after old-logo removal.  
**Root cause:** Cleanup judged only at normal size or by whether the old mark disappeared, not by repair integrity.  
**Detection:** 100% crop of the repaired zone + realistic Instagram-size review.  
**Required correction:** Repair only authorized area from clean source; inspect before and after new logo placement.  
**Prevention:** Treat cleanup region itself as part of the QC surface.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-003 — Regenerated Logo Substitute

**Symptom:** AI creates a logo that is visually similar to the chosen mark but not the exact approved identity asset.  
**Root cause:** Treating logo description/style as permission to generate instead of retrieving canonical asset memory.  
**Detection:** Compare against `EBL-ASSET-LOGO-001` and chosen-logo construction.  
**Required correction:** Retrieve and place exact approved master/approved variant.  
**Prevention:** `CHOSEN LOGO → PLACE MASTER → DO NOT REGENERATE`.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-004 — Geometric Bounds Pass but Optical Collision Fails

**Symptom:** Logo layer rectangle appears correctly positioned, but a visible line, dot, beret, glow or semicircle touches/merges with text or artwork.  
**Root cause:** Bounding-box consistency mistaken for optical clearance.  
**Detection:** Inspect visible extreme elements on the most constrained asset first.  
**Required correction:** Find one safe universal anchor/scale or approved reusable variant; do not silently alter one slide's logo geometry.  
**Prevention:** Optical-bounds QC is mandatory.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-005 — Carousel Numbering Inconsistency

**Symptom:** One slide uses a different format such as `05` while the set uses `NN / total`.  
**Root cause:** Numbering treated as local decoration instead of a repeated system component.  
**Detection:** Cross-slide comparison of format, anchor, scale, weight relationship, slash spacing and contrast.  
**Required correction:** Restore the repeated numbering grammar.  
**Prevention:** Carousel system QC.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-006 — Visible Repair Rectangles / Texture Patches

**Symptom:** A text or cleanup repair leaves rectangular paper patches, seams, tone shifts or texture discontinuity.  
**Root cause:** Patching a damaged derivative instead of returning to a clean approved/textless source.  
**Detection:** Native-scale artifact inspection and large-area tone/texture comparison.  
**Required correction:** Rebuild from cleanest valid source according to the source hierarchy.  
**Prevention:** `DO NOT REPAIR A DAMAGED DERIVATIVE WHEN A CLEANER APPROVED SOURCE EXISTS`.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-007 — Incorrect Semantic Color Emphasis

**Symptom:** More words are emphasized than the human-approved meaning requires, or emphasis becomes decorative rather than semantic.  
**Root cause:** Treating a sentence segment as one visual unit instead of preserving exact word-level emphasis.  
**Detection:** Compare emphasized tokens against content-specific decisions.  
**Required correction:** Apply accent color only to approved words; preserve all other copy treatment.  
**Prevention:** Content fidelity + typography emphasis gate.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-008 — Unrequested Redesign During Correction

**Symptom:** A logo/text/artifact correction also moves unrelated shapes, changes typography, alters colors or introduces new decoration.  
**Root cause:** AI interprets revision as general redesign permission.  
**Detection:** Delta comparison against approved source.  
**Required correction:** Revert unrelated changes and edit only authorized area.  
**Prevention:** `HUMAN = WHAT; REFERENCE = HOW; AI = APPLY`.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-009 — Story Becomes a Stretched Feed Post

**Symptom:** Story uses feed composition enlarged vertically, crowds Instagram interaction zones, or lacks a native Story reading path.  
**Root cause:** Platform function ignored.  
**Detection:** 1080×1920 layout review with usable interaction/sticker zone and mobile-size preview.  
**Required correction:** Recompose for Story: large usable vertical negative space, edge-weighted painterly identity, semantic typography, secondary branding, interaction room.  
**Prevention:** Story rules + `QC-EBL-001` Story gate.  
**Status:** ACTIVE KNOWN FAILURE.

---

## EBL-FAIL-010 — Generic Language-School / Infographic Drift

**Symptom:** Flags, classroom clichés, icon grids, dashboard cards, stock-corporate layout or generic explainer design replaces the approved editorial/painterly system.  
**Root cause:** General social-media defaults override project memory.  
**Detection:** Compare against EBL project memory and visual examples.  
**Required correction:** Restore project-specific visual grammar and meaning-to-form relationship.  
**Prevention:** Mandatory EBL memory retrieval before creation.  
**Status:** ACTIVE KNOWN FAILURE.

---

# Failure Review Rule

Every EBL QC run should ask:

```text
DOES THIS OUTPUT REPRODUCE ANY ACTIVE EBL FAILURE PATTERN?
```

If yes, the relevant gate cannot pass.

When a new repeated failure is discovered:

```text
OBSERVE
→ IDENTIFY ROOT CAUSE
→ DEFINE DETECTION SIGNAL
→ DEFINE CORRECTION
→ DEFINE PREVENTION
→ HUMAN REVIEW
→ ADD TO FAILURE MEMORY
→ ADD QC CHECK IF TESTABLE
```
