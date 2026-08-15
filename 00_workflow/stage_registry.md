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
| 13 Quality Control | QC-001–QC-002 + `stepwise_creative_review.md` | Review outputs, diagnose root causes, and route revision | Final Approval / Revision Route |

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
