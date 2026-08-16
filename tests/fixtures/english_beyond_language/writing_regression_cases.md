# English Beyond Language — Writing Regression Cases

These cases are controlled fixtures for future semantic execution of the Writing workflow.

## Case A — A Line for Today

Goal: produce a short Story-ready quote package.

Required invariants:

- quotation must not be paraphrased when exact quotation is requested;
- author/work/date attribution must be verified or explicitly marked unresolved;
- no invented context;
- writing remains concise enough for Story use;
- Design receives locked quote wording plus flexible layout guidance;
- any supporting explanation must follow current EBL language-level rules.

## Case B — Complex Source to B1 Story

Goal: turn a difficult cultural or educational source into an accessible EBL Story.

Required invariants:

- preserve the source's core meaning;
- identify claims, evidence, key terms, and uncertainty before drafting;
- explain difficult concepts rather than deleting them;
- default public-facing explanation approximately CEFR B1;
- intellectual depth may remain above B1 while language remains accessible;
- no elitist positioning;
- content must have a clear EBL purpose;
- source references remain attached to material claims.

## Case C — Motivational Educational Content

Goal: produce social content that motivates learners without generic slogans.

Required invariants:

- motivation is realistic and learner-centered;
- no shame, fear, superiority, or exaggerated transformation claims;
- content connects to an EBL learning purpose;
- main message is understandable at approximately B1;
- CTA is appropriate to the content purpose;
- no random topic, visual request, or filler copy is introduced merely to satisfy a schedule.

## Future Semantic Result Record

Each executed case should store:

```text
CASE_ID
PROMPT_ID
PROMPT_VERSION
MODEL_RUNTIME
SOURCE_SET
ACTUAL_OUTPUT
WRITING_RUBRIC_SCORES
CRITICAL_FAILURES
ROOT_CAUSE_STAGE
REGRESSION_STATUS
HUMAN_REVIEW_STATE
```
