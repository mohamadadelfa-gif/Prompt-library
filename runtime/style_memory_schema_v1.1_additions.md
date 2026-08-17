# Style Memory Schema — proposed v1.1 additions

These are additive fields only — no existing field is renamed or removed,
so v1.0 records remain valid. Bump `schema_version` to "1.1" once applied.

Add to `fields`:

```json
"status": "ACTIVE|SUPERSEDED|RETIRED",
"applicable_tasks": ["string"],
"confidence": "LOW|MEDIUM|HIGH"
```

- `status` — set to `ACTIVE` on promotion. When a new record's `supersedes`
  references an older `revision_id`, that older record's `status` must be
  set to `SUPERSEDED` in the same transaction — never leave two ACTIVE
  records in the same lineage.
- `applicable_tasks` — task IDs or task-ID prefixes (e.g. `"VIS-*"`,
  `"ART-001"`, `"GEN-*"`) that may retrieve this memory. Empty array means
  "not yet scoped for retrieval" — should block promotion to ACTIVE until
  filled in, since an un-scoped SYSTEM_RULE is exactly the kind of silent
  drift the governing model forbids.
- `confidence` — evidential strength backing the promotion decision itself
  (distinct from any confidence values inside individual `changes[]`
  entries). PROJECT_REFERENCE may be Low; SYSTEM_RULE should require
  Medium or High per the existing promotion_policy text about "repeated
  evidence across projects."

## New artifact type: MEMORY_USAGE_LOG

Not part of style_memory_schema.json itself — a separate log written by
whichever task *consults* memory (primarily GEN-001/GEN-002), so that
"which approved memory IDs influenced each run" is answerable without
inferring it after the fact.

```json
{
  "run_id": "string",
  "task_id": "string",
  "project_id": "string",
  "memory_ids_considered": ["revision_id"],
  "memory_ids_applied": ["revision_id"],
  "timestamp": "datetime"
}
```

`memory_ids_considered` vs `memory_ids_applied` matters: it lets you audit
not just what influenced an output, but what was available and *rejected*
— useful when QC later asks "why wasn't project rule X followed here."
