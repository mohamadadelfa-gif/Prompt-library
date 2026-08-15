# Stage Registry

| Stage | Active Tasks / Protocols | Primary Task | Required Handoff |
|---|---|---|---|
| 01 Strategy | STR-001–STR-005 | Define problem, audience, requirements, clarification, reconciliation | Approved Strategy Package |
| 02 Research | RES-001–RES-006 | Establish evidence and synthesize relevant context | Research Synthesis |
| 03 Visual Analysis | VIS-001–VIS-006 | Analyze supplied visual references | Visual Evidence Package |
| 04 Named Style Study | STYLE-001 / `named_style_study.md` | Learn a named artist, movement, school, or visual language deeply | Approved Style Study Package |
| 05 Reference Style Synthesis | `reference_style_synthesis.md` | Combine style study and supplied references into transferable visual principles | Approved Reference Style Synthesis |
| 06 Visual DNA | VDNA-001 | Convert validated visual evidence and style principles into transferable rules | Visual DNA Package |
| 07 Platform / Template Synthesis | `instagram_template_synthesis.md` when Instagram is the target | Translate visual language + Visual DNA into an original reusable platform system | Approved Platform Template Candidate |
| 08 Art Direction | ART-001–ART-003 | Make and select content-specific creative decisions | Approved Art Direction |
| 09 Generation | GEN-001–GEN-002 | Operationalize approved direction into generation specifications and prompts | Generated Output |
| 10 Content Package | `content_package_contract.md` | Assemble visual, copy, caption, CTA, accessibility, and publishing outputs | Approved Content Package |
| 11 Human Revision / Style Learning | `human_feedback_style_learning.md` | Capture revision, approval, and reusable style knowledge | Approved Revision / Style Knowledge |
| 12 Figma Implementation | `editable_reconstruction_preparation.md` → `live_editable_text_layers.md` → `figma_file_structure.md` → `figma_output_contract.md` | Prepare approved raster visuals, rebuild live editable text, organize the production file, and create the editable production master | Approved Structured Figma Master |
| 13 Quality Control | QC-001–QC-002 + `stepwise_creative_review.md` + Instagram-specific QC modules | Review outputs, diagnose root causes, and route revision | Final Approval Candidate / Revision Route |
| 14 Creative AI Final Edit | FINAL-AI-001 / `creative_ai_final_edit.md` + `final_ai_closed_loop_production.md` | Perform semantic + visual finishing using approved content, brand knowledge, slide function, typography, layout, and source-informed design principles; explicitly classify each asset as preserve / cleanup / micro-refine / source-based reconstruction / conceptual change | Creative Final Candidate |
| 15 AI Creative Synthesis + Heavy QC | FINAL-AI-002 / `final_ai_creative_synthesis_heavy_qc.md` + `final_ai_closed_loop_production.md` | Holistically refine the completed work, run all applicable mandatory QC gates, return failed assets through root-cause correction, prepare final master and platform derivatives, and route to human final approval | PASS_FOR_HUMAN_FINAL_REVIEW → human-approved Final Publishing Master |

## Stage Boundaries

### Strategy
May interpret customer information and define requirements. Must not invent research findings or visual conclusions.

### Research
May investigate and synthesize evidence. Must not turn evidence into final visual decisions.

### Visual Analysis
May analyze supplied visual references. Must not define the final brand system or creative concept.

### Named Style Study
May learn and explain a named artistic language and derive transferable principles. Must not generate the client template or treat interpretation as historical fact.

### Reference Style Synthesis
May determine what is actually present in the supplied references and combine it with an approved style study. Must not copy source artwork or redefine customer requirements.

### Visual DNA
May convert validated visual evidence into transferable rules. Must not invent unsupported reference characteristics.

### Platform / Template Synthesis
May translate approved visual language into platform-specific reusable structure. Must preserve communication clarity and must not reproduce reference layouts.

### Art Direction
May create and select concepts and make content-specific creative decisions using approved strategy and visual systems. Must not silently alter strategic requirements.

### Generation
May operationalize approved Art Direction into generation specifications and model-adapted prompts. Must not redefine the concept or Art Direction.

### Content Package
May assemble approved content components. Must not introduce new strategic claims through captions, CTAs, or metadata.

### Human Revision / Style Learning
May record human changes and extract approved reusable style knowledge. Must not silently rewrite upstream decisions or promote one-off corrections to system rules.

### Figma Implementation
For flattened/raster approved visuals, must first run `editable_reconstruction_preparation.md` to source-lock the approved visual, derive textless artwork, map editable elements, and create a controlled reconstruction handoff. Rasterized typography intended for manual editing must follow `live_editable_text_layers.md`. The production file must then be organized according to `figma_file_structure.md` before final validation under `figma_output_contract.md`.

Figma implementation must preserve a clear distinction between APPROVED REFERENCE, EDITABLE MASTER, STYLE SYSTEM, and EXPORT output. It must not redesign, reinterpret, or silently replace approved content.

If Figma MCP access is blocked by a plan, permission, rate, or tool-call limit, the blocked operation is not considered applied unless explicit created/mutated node IDs are returned. Record the blocker and preserve the last confirmed file state.

### Quality Control
May evaluate outputs and diagnose root causes. Must not rewrite upstream decisions while evaluating them.

Instagram-specific QC modules currently include:

- `00_workflow/qc/QC-IG-001_instagram_visual_qc.md` — feed/carousel visual QC;
- `00_workflow/qc/QC-AUD-001_audience_catcher_qc.md` — audience relevance and stopping-power QC;
- `00_workflow/qc/QC-SOC-001_social_visual_audience_gate.md` — combined social visual/audience gate;
- `00_workflow/qc/QC-IG-PROFILE-001_instagram_profile_picture_qc.md` — profile/avatar identity QC;
- `00_workflow/qc/QC-LOGO-001_logo_application_qc.md` — logo master fidelity, optical clearance, replacement cleanup and multi-slide consistency;
- `00_workflow/qc/QC-TYPE-001_typography_integrity_qc.md` — typography integrity, native-resolution reconstruction and carousel numbering consistency.

Use the asset-specific QC rather than forcing one Instagram QC model onto every asset type.

### Creative AI Final Edit
May make controlled late-stage typography, alignment, hierarchy, spacing, line/form relationship, contrast, and optical-balance refinements only after retrieving approved project context and analyzing the semantic role of the content.

It must follow:

- `creative_ai_final_edit.md`;
- `final_ai_closed_loop_production.md`;
- `knowledge/external/creative_synthesis_sources.md` as evidence;
- relevant project rules and QC modules.

Before editing, every asset must be classified:

```text
P0 PRESERVE
P1 CLEANUP
P2 MICRO-REFINE
P3 SOURCE-BASED RECONSTRUCTION
P4 CONCEPTUAL CHANGE — HUMAN AUTHORIZATION REQUIRED
```

A P0 decision is a completed creative decision, not skipped work.

The clean-source hierarchy in `final_ai_closed_loop_production.md` must be used before patching a damaged derivative.

External references may improve creative judgment but may not override approved meaning, logo identity, brand rules, or human decisions.

This stage produces a **Creative Final Candidate**, not a publishing master.

### AI Creative Synthesis + Heavy QC
May use broader holistic creative judgment to make the completed work cohere as one authored system, but content/factual freedom remains locked.

It must:

- follow `final_ai_creative_synthesis_heavy_qc.md`;
- follow the orchestration loop in `final_ai_closed_loop_production.md`;
- run all applicable mandatory QC modules;
- inspect native-resolution critical areas;
- inspect realistic feed-size output;
- evaluate the carousel/set sequentially;
- preserve an archival/project master;
- create platform derivatives only from the approved master;
- return mandatory failures through root-cause diagnosis and smallest-safe correction;
- rerun the failed gate plus whole-set coherence after correction;
- route the result to human final approval.

AI cannot label an output `FINAL_PUBLISHING_MASTER` until all mandatory gates pass and the human explicitly approves the final candidate.

---

## Finalization Orchestration — Stages 14–15

Stages 14 and 15 operate as one controlled closed loop rather than two isolated linear steps.

Authoritative orchestrator:

`00_workflow/final_ai_closed_loop_production.md`

Reusable system learnings:

`00_workflow/knowledge/system/final_ai_production_learnings.md`

The finalization loop is:

```text
SOURCE LOCK
→ WHOLE-WORK READ
→ FUNCTION MAP
→ PRESERVE / INTERVENE CLASSIFICATION
→ FINAL-AI-001
→ DELTA REVIEW
→ FINAL-AI-002 HEAVY QC
→ ROOT-CAUSE REVISION IF REQUIRED
→ PASS_FOR_HUMAN_FINAL_REVIEW
→ HUMAN FINAL APPROVAL
→ FINAL_PUBLISHING_MASTER
→ PLATFORM DERIVATIVES
→ LEARNING REVIEW
```

### Failure-routing rule

A mandatory local failure must not trigger unnecessary redesign of unaffected assets.

Use:

```text
LOCAL FAILURE
→ LOCAL ROOT-CAUSE CORRECTION
→ RERUN FAILED GATE
→ RERUN GLOBAL COHERENCE
```

### Output architecture rule

The approved archival/project master and the platform derivative are separate outputs.

Do not repeatedly resize the working master during revision. Create platform derivatives only after the final master is approved.

### Learning-promotion rule

After finalization, separate:

1. project-specific decisions;
2. reusable project rules;
3. system-level production learnings.

Only promote knowledge to the system layer when the human explicitly authorizes learning / structuralization or the existing promotion policy allows it.
