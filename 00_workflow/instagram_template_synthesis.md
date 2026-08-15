# Instagram Template Synthesis Protocol

## Purpose

Convert approved visual language from the Reference Style Synthesis step into an original, reusable Instagram template system.

This is a translation task, not a reproduction task.

## Inputs

Required:

- approved reference style analysis
- customer / brand requirements
- existing Visual DNA
- content objective
- Instagram content type
- platform dimensions

Optional:

- approved style references
- prior approved templates
- approved human revision records

## Project Memory Retrieval — mandatory when available

Before synthesizing a project template, retrieve the project's durable memory / approved-rule package if one exists.

For English Beyond Language retrieve:

- `00_workflow/knowledge/project/EBL_project_memory.md`
- `00_workflow/knowledge/project/EBL_approved_project_rules.md`
- `00_workflow/qc/QC-EBL-001_project_master_qc.md`

For Story work also retrieve:

- `00_workflow/knowledge/project/EBL_story_template_rules.md`

A template must not silently contradict an approved logo, typography, naming, or final-production rule already learned by the project.

## Step 1 — Define Platform Role

Identify:

- platform: Instagram
- content type: carousel, single post, Story, reel cover, etc.
- dimensions
- number of slides / frames
- mobile readability requirement
- safe areas
- expected viewing distance
- native platform interaction needs where relevant

## Step 2 — Define Communication Hierarchy

Establish:

- primary message
- secondary message
- supporting information
- CTA
- brand signature

Typography must remain the dominant communication layer unless the content explicitly requires another hierarchy.

## Step 3 — Translate Emotional Effect

The template must preserve the intended emotional experience from the reference analysis.

For English Beyond Language, preserve the intended qualities:

- curious
- human
- thoughtful
- warm
- artistic
- culturally aware
- intelligent
- exploratory

Do not achieve these qualities through random decoration. Achieve them through composition, mark-making, texture, shape, pacing, and whitespace.

## Step 4 — Define Graphic Vocabulary

Create a controlled library of:

- organic shapes
- geometric fields
- hand-drawn lines
- symbols
- grids
- texture treatments
- accent marks

Each element should have a functional role.

## Step 5 — Define Template Zones

Every reusable Instagram template should have explicit zones such as:

```text
HEADLINE_ZONE
SUPPORTING_COPY_ZONE
GRAPHIC_ZONE
BRAND_ZONE
CTA_ZONE
FOOTER_ZONE
```

Zones should be flexible enough for new content but constrained enough to preserve the visual identity.

## Step 6 — Define Repeatable Components

Examples:

- headline block
- question headline
- quote block
- vocabulary block
- pillar label
- decorative field
- hand-drawn line
- symbol
- footer
- slide number
- brand signature

## Step 7 — Define Slide / Frame Roles

For a carousel or Story sequence, explicitly define each frame role.

Example carousel:

```text
SLIDE 01 — HOOK
SLIDE 02 — QUESTION / TENSION
SLIDE 03 — EXPLANATION
SLIDE 04 — EXAMPLE / CONTRAST
SLIDE 05 — SUMMARY / CTA
```

Example Story sequence:

```text
STORY 01 — HOOK / QUESTION
STORY 02 — INSIGHT / TENSION
STORY 03 — TEACHING POINT / EXAMPLE
STORY 04 — INTERACTION / POLL / QUESTION
STORY 05 — CTA / CONTINUATION
```

The role should derive from content strategy, not from the reference artwork.

## Step 8 — Define Editable vs Controlled Elements

Each template element must be classified:

- EDITABLE — content changes freely.
- CONTROLLED — visual value changes through approved variables or component properties.
- LOCKED — structural brand element requiring design approval.

## Step 9 — Define Figma / Editable Implementation

The template must be implementable as editable layers when editable production is required.

Required implementation details:

- page
- frame dimensions
- frame naming
- components
- variables / styles
- text styles
- color styles
- layout grid
- spacing tokens
- auto-layout relationships
- safe zones
- editable fields
- locked fields
- export settings

## Step 10 — Separate Template from Content

Never embed post-specific copy into the reusable template unless the text is explicitly defined as a structural label.

```text
CONTENT INSTANCE
      ↓
TEMPLATE SYSTEM
      ↓
NEW CONTENT CAN REUSE STRUCTURE
```

## Step 11 — Human Review Checkpoint

The first generated implementation is a **candidate**, not a final template.

Human review must assess:

- typography
- hierarchy
- readability
- emotional effect
- style fidelity
- originality
- consistency across slides/frames
- template reusability
- brand signature behavior
- safe-zone behavior
- platform-native usability

Human revisions must be captured as revision records.

## Step 12 — Template Approval

A template becomes APPROVED only when:

- the content instance / template candidate is approved;
- the template structure is judged reusable;
- style references are identified;
- editable / controlled / locked elements are documented;
- production implementation is complete where required;
- provenance is recorded;
- the template version is assigned;
- applicable project/master QC passes.

---

# Instagram Story Synthesis — required when CONTENT_TYPE = STORY

## Story Principle

A Story template is not a feed post stretched vertically.

It is a live 9:16 communication surface that must support:

- rapid phone reading;
- top/bottom UI obstruction;
- interaction stickers;
- short sequential pacing;
- live/temporary content variation;
- clear brand recognition without over-branding.

## Story Canvas

Default working canvas:

`1080 × 1920 px` (`9:16`)

## Story Safe-Zone Logic

Define practical safe zones for:

- essential headline/copy;
- brand signature;
- interactive sticker space;
- CTA.

Do not assume the whole 1080×1920 area is equally usable.

Essential information must remain clear of likely platform UI obstruction.

## Story Content Architecture

Prefer flexible zones rather than hard decorative boxes:

```text
TOP_SAFE / ENTRY
MAIN_MESSAGE_ZONE
SECONDARY_COPY_ZONE
INTERACTIVE_STICKER_ZONE
BRAND_SIGNATURE_ZONE
BOTTOM_SAFE / CTA SUPPORT
```

## Story Visual Weight

For editorial/painterly brands such as EBL:

- preserve large central negative space;
- place painterly weight near edges/corners;
- use marks/signs sparingly;
- keep the reading/sticker area open;
- do not let edge decoration become the focal point unless the content requires it.

## Story Typography

Use semantic typography rather than one decorative Story font treatment.

```text
STORY MEANING
→ STORY ROLE
→ READING ORDER
→ FONT ROLE
→ ALIGNMENT / SPACE
→ EMPHASIS
```

## Story Branding

Use the approved project logo / production signature.

Do not regenerate branding.

Do not infer that feed-post logo coordinates are automatically correct for Story format.

Keep brand signature clear of interaction zones and platform UI.

## Clean Template vs Presentation Mockup

A reusable clean Story master should **not** bake fake Instagram UI into the artwork unless the user explicitly asks for a mockup/presentation view.

Keep these outputs separate:

```text
CLEAN STORY TEMPLATE
≠
INSTAGRAM UI MOCKUP / PRESENTATION
```

## Story Candidate Status

The first Story template is:

`REVIEW_CANDIDATE`

Do not promote exact coordinates, composition, or decorative placements to locked project rules until the human explicitly approves the template as reusable.

For EBL Story candidates run:

`00_workflow/qc/QC-EBL-001_project_master_qc.md` — Story Gate 10.

---

## Output

```text
TEMPLATE_ID
PLATFORM
CONTENT_TYPE
FRAME_SPEC
SLIDE_OR_FRAME_ROLES
CONTENT_ZONES
TYPOGRAPHY_SYSTEM
COLOR_SYSTEM
SHAPE_SYSTEM
LINE_SYSTEM
TEXTURE_SYSTEM
GRID_SYSTEM
COMPONENT_SYSTEM
EDITABLE_FIELDS
CONTROLLED_FIELDS
LOCKED_FIELDS
SAFE_ZONE_RULES
INTERACTION_ZONE_RULES
BRAND_SIGNATURE_RULES
IMPLEMENTATION
STYLE_REFERENCES
STYLE_RULES
HUMAN_REVISIONS
PROVENANCE
VERSION
DECISION_GATE
```

## Core Principle

The final Instagram template should feel like it belongs to the project's visual world while remaining an original, readable, repeatable, brand-specific communication system.

For Stories additionally:

```text
BRAND IDENTITY
+
PLATFORM-NATIVE USABILITY
+
NEGATIVE SPACE
+
INTERACTION FLEXIBILITY
>
DECORATIVE DENSITY
```

Updated: 2026-08-16
