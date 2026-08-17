# Knowledge Relationship Protocol

## Purpose

Represent how sources, derived findings, decisions, tasks, protocols, artifacts, outputs and QC evidence relate without collapsing their information states or deleting history.

The authoritative node registry remains `knowledge/knowledge_registry.json`. The authoritative edge registry is `knowledge/knowledge_relationships.json`, governed by `knowledge/knowledge_relationship_schema.json`.

## When to Create an Edge

Create an edge only when the relationship is material to retrieval, provenance, approval, generation, evaluation, revision, promotion, supersession or conflict handling.

Do not create speculative edges merely because two records mention similar words.

## Endpoint Rules

- `KNOWLEDGE` nodes must resolve to a registered `kb_id`.
- `TASK` nodes must resolve to an active task contract.
- `PROTOCOL`, `ARTIFACT`, `DECISION`, `OUTPUT` and `QC_EVIDENCE` nodes must be declared in `external_nodes` until they gain their own authoritative registry.
- Endpoint kinds are explicit and cannot be inferred from naming alone.

## Direction Semantics

Edges use readable direction:

```text
source SUPPORTS decision
knowledge CONSUMED_BY task
task PRODUCES artifact
artifact DERIVED_FROM source
QC_EVIDENCE EVALUATES output
new_rule PROMOTED_FROM project_rule
new_version SUPERSEDES old_version
```

`DERIVED_FROM`, `PROMOTED_FROM`, `REVISES` and `SUPERSEDES` preserve the original node. They never rewrite it in place.

## Information-State Safety

An edge describes a relationship; it never changes an endpoint's classification.

Forbidden implications include:

- `DERIVED_FROM` making a derived claim a source fact;
- `SUPPORTS` turning evidence into an approved decision;
- `PRODUCES` turning an output into a requirement;
- `PROMOTED_FROM` bypassing human approval;
- `SUPERSEDES` erasing historical provenance.

## Promotion and Supersession

`PROMOTED_FROM` requires:

- explicit approval;
- privacy-safe scope;
- provenance to the original knowledge node;
- a distinct target node;
- retention of the lower-scope original.

`SUPERSEDES` requires both versions to remain resolvable and the replacement reason to be captured in provenance or related decision evidence.

## Conflicts

Use `CONFLICTS_WITH` for unresolved or deliberately preserved conflicts. Do not silently select a winner. Resolution requires a separate authorized decision or supersession edge.

## Retrieval

Retrieval may traverse only relationships appropriate to the task and allowed by project scope. A task should prefer:

1. directly governing approved decisions/rules;
2. authorized consumed knowledge;
3. supporting source evidence;
4. derived related artifacts;
5. unresolved conflicts and superseded history for audit only.

Do not traverse across client/project boundaries without explicit permission and privacy-safe scope.

## Validation

CI must reject:

- missing endpoints;
- unknown node kinds or relation types;
- invalid endpoint-kind combinations;
- duplicate edge IDs or duplicate semantic edges;
- invalid confidence/approval values;
- edges without provenance, project or scope;
- pending/rejected knowledge represented as an approved governing relationship;
- knowledge-to-task consumption edges not authorized by `allowed_consumers`.

## Version

1.0-production-candidate

## Status

Active protocol
