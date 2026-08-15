# QC-EBL-MEM-001 — EBL Memory Compliance QC

## Purpose

Verify that an English Beyond Language task actually used the current project memory correctly.

This QC answers a different question from visual QC:

> **Did the output obey the current EBL memory, decisions, assets, failures, and retrieval rules?**

It must run before an EBL asset can pass final project QC.

---

## Governing Principle

```text
MEMORY EXISTS
≠
MEMORY WAS RETRIEVED
≠
MEMORY WAS APPLIED CORRECTLY
```

All three must be verified.

---

# Required Inputs

- task/request;
- produced/revised asset or output description;
- `EBL_memory_registry.json`;
- `EBL_retrieval_map.md`;
- retrieved-memory evidence;
- `EBL_decision_log.md`;
- `EBL_asset_registry.json` when assets are involved;
- `EBL_failure_memory.md`;
- content-specific decision record where applicable;
- current human instruction.

If retrieval evidence is absent, result cannot exceed `BLOCKED_MEMORY_EVIDENCE_MISSING`.

---

# Gate MEM-01 — Memory Registry Loaded — mandatory

Verify that `EBL_memory_registry.json` was retrieved and its current schema/version was recorded.

Reject:

- working from remembered conversation alone;
- using an unregistered project-memory file as authority without explaining why;
- ignoring a registered mandatory record.

---

# Gate MEM-02 — Task-Specific Retrieval Correct — mandatory

Use `EBL_retrieval_map.md` to verify the correct memory set was retrieved for the task.

Examples:

- logo task must retrieve asset registry + logo rules + logo QC;
- typography repair must retrieve exact copy + typography QC + clean-source rules;
- Story task must retrieve Story rules + Story candidate status;
- final AI must retrieve failure memory + examples + closed-loop rules.

Missing required task memory => `FAIL`.

---

# Gate MEM-03 — Human Instruction Has Highest Priority — mandatory

Verify the current explicit human instruction was not overridden by older memory.

Memory supports continuity; it does not overrule a new human decision.

If the current instruction changes a durable rule, mark the old rule for supersession/update rather than silently keeping both active.

---

# Gate MEM-04 — Decision Freshness / Supersession — mandatory

Check `EBL_decision_log.md` and applicable decision records.

Verify:

- newest approved non-superseded decision used;
- superseded decisions not treated as active;
- one-off old explorations not mistaken for current identity;
- decision rationale preserved when making transferable creative choices.

Conflict unresolved => `BLOCKED_CONFLICT`.

---

# Gate MEM-05 — Canonical Asset Resolution — mandatory when assets are involved

Check `EBL_asset_registry.json`.

Verify:

- correct asset ID selected;
- correct parent/variant relationship;
- asset approval state valid for requested use;
- verified canonical file used when available;
- unknown path/hash/dimensions are not invented.

For the chosen EBL logo:

```text
EBL-ASSET-LOGO-001
```

If the canonical binary is unresolved:

```text
DO NOT GENERATE A SUBSTITUTE
```

Return `CANONICAL_ASSET_UNRESOLVED` for exact placement tasks until a verified binary is supplied/resolved.

A written construction description is memory, not a replacement for the canonical asset binary.

---

# Gate MEM-06 — Project vs Candidate State — mandatory

Verify candidate material has not been silently promoted.

Examples:

- Story template candidate remains `REVIEW_CANDIDATE` until human approval;
- a new logo variant remains unapproved until reviewed;
- a generated visual example is not automatically a project rule.

File existence ≠ approval.

---

# Gate MEM-07 — Failure Memory Checked — mandatory for revision/QC/finalization

Check all relevant active failure IDs from `EBL_failure_memory.md`.

At minimum ask:

```text
DOES THIS OUTPUT REPRODUCE A KNOWN EBL FAILURE?
```

Relevant failures include:

- faded raster typography;
- logo cleanup ghosts;
- regenerated logo substitute;
- optical logo collision;
- numbering drift;
- visible repair rectangles;
- wrong semantic emphasis;
- unrequested redesign;
- stretched-feed Story behavior;
- generic language-school/infographic drift.

Known active failure reproduced => `FAIL`.

---

# Gate MEM-08 — Visual Calibration Used Correctly — when visual references matter

Use `EBL_visual_examples.md`.

Verify:

- approved examples are used for positive calibration;
- rejected examples are used as negative calibration;
- example teaching is applied, not copied mechanically;
- missing image binaries are not falsely claimed as inspected;
- review candidates are not described as approved masters.

---

# Gate MEM-09 — Unknown Handling Discipline — mandatory

Reject invented values for:

- repository asset path;
- SHA/hash;
- dimensions;
- approval status;
- file provenance;
- license;
- exact variant identity.

Use:

```text
UNKNOWN
PENDING_VERIFICATION
null
```

when evidence is unavailable.

Unknowns that block exact execution must remain visible in the final report.

---

# Gate MEM-10 — Scope Discipline — mandatory

Verify memory was not promoted beyond its authorized scope.

Do not convert:

- Post 01-specific wording into a global EBL copy rule;
- exact Story-candidate coordinates into a permanent template rule;
- EBL-specific preferences into cross-project system rules;
- one repair technique into a universal aesthetic rule unless system promotion is authorized.

---

# Gate MEM-11 — Delta / Revision Compliance — for revisions

Verify:

```text
HUMAN = WHAT TO CHANGE
REFERENCE = HOW
AI = APPLY ONLY AUTHORIZED DELTA
```

Compare against approved source.

Unauthorized changes outside the requested surface => `FAIL`.

---

# Gate MEM-12 — Memory-to-QC Traceability — mandatory for final review

Final report must identify which memory affected which check.

Minimum trace record:

```text
MEMORY_FILES_RETRIEVED
DECISION_IDS_APPLIED
ASSET_IDS_APPLIED
FAILURE_IDS_CHECKED
EXAMPLE_IDS_USED
UNRESOLVED_UNKNOWNS
CONFLICTS
MEMORY_COMPLIANCE_RESULT
```

A generic statement such as “memory checked” is insufficient.

---

# Gate MEM-13 — Learning Loop Completion — when human says learn / structuralize

If the human explicitly asks to learn, structuralize or refine memory:

1. identify the observation;
2. classify it as one-off / content-specific / reusable EBL / cross-project;
3. update decision/failure/example memory as appropriate;
4. update QC when the lesson is testable;
5. update registries/retrieval map if a new memory object was created;
6. preserve provenance;
7. avoid duplicate/conflicting active rules.

The learning task is incomplete if only a prose note is added but retrieval/QC cannot use it.

---

# Result States

```text
BLOCKED_MEMORY_EVIDENCE_MISSING
BLOCKED_CONFLICT
CANONICAL_ASSET_UNRESOLVED
FAIL
REVISION_REQUIRED
PASS_MEMORY_COMPLIANCE
```

`PASS_MEMORY_COMPLIANCE` does not mean the design itself is good. It means the project memory was used correctly. The asset must still pass `QC-EBL-001` and relevant specialized QC.

---

# Compact Checklist

```text
[ ] memory registry loaded
[ ] correct task retrieval set loaded
[ ] current human instruction has highest priority
[ ] newest non-superseded decisions used
[ ] canonical asset IDs resolved correctly
[ ] no unverified asset metadata invented
[ ] candidate vs approved status preserved
[ ] relevant failure memory checked
[ ] approved/rejected examples used correctly
[ ] project/content/system scopes not conflated
[ ] revision delta isolated
[ ] memory-to-QC trace recorded
[ ] learning loop completed when requested
```

Updated: 2026-08-16
