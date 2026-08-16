# Writing Semantic Evaluation Rubric

Score each dimension from 0 to 4.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| Task adherence | Wrong task | Partial task | Exact task boundary |
| Source quality | Weak/unverified sources | Mixed quality | Appropriate, reliable, clearly scoped sources |
| Factual accuracy | Material errors | Minor uncertainty | Claims are accurate and checked |
| Claim-evidence relationship | Unsupported claims | Partial support | Material claims traceable to evidence |
| Unknown handling | Invents missing facts | Some unknowns preserved | All relevant unknowns explicit |
| Purpose/relevance | Random or off-purpose | Partly relevant | Clear reason for every content choice |
| Audience fit | Wrong audience | Mixed fit | Appropriate for intended audience |
| Language-level fit | Wrong complexity | Some drift | Consistent requested level/register |
| Meaning preservation | Meaning distorted | Mostly preserved | Adaptation preserves factual/semantic meaning |
| Clarity/structure | Confusing | Understandable | Clear hierarchy and reading flow |
| Tone/voice | Wrong or inconsistent | Mostly suitable | Controlled, brand-appropriate tone |
| Grammar/style | Distracting errors | Minor issues | Clean, natural, intentional prose |
| Non-elitist/accessibility fit | Exclusionary or status-driven | Mixed | Inviting and intellectually open when required |
| Motivation/action value | Manipulative/empty | Weak action value | Realistic, useful learner/reader motivation when required |
| Originality/non-randomness | Filler or generic | Some generic choices | Purposeful synthesis with justified content choices |
| Contract/handoff quality | Unusable downstream | Needs repair | Next workflow can execute directly |

## Pass Criteria

A Writing output passes only when:

- no critical failure exists;
- average score is at least 3.0;
- factual accuracy >= 3;
- claim-evidence relationship >= 3;
- unknown handling >= 3;
- meaning preservation >= 3;
- contract/handoff quality >= 3;
- any project-specific mandatory rule passes independently.

A high average cannot compensate for a critical failure.

## Critical Failures

Automatic FAIL:

- fabricated quotation, attribution, statistic, source, or factual claim;
- unsupported claim presented as established fact;
- changing approved meaning during simplification or rewriting;
- silently changing a locked wording requirement;
- failing a mandatory language-level rule when that rule is explicit;
- elitist/exclusionary positioning when a project rule forbids it;
- random filler content with no defensible content purpose;
- design-side re-authoring of approved Writing content without a new Writing version;
- missing provenance for a material factual claim;
- downstream handoff that does not identify the approved Writing version.

## Root-Cause Routing

- wrong objective/audience → Writing Strategy
- weak/missing sources → Textual Research
- misunderstood source → Source Analysis
- unsupported synthesis → Content Synthesis
- poor reading order → Content Structure
- weak prose → Drafting
- language/tone mismatch → Language Adaptation
- factual or quality failure → Writing QC, then route to earliest responsible stage
- approval disagreement → Human Content Approval
- Design constraint requiring rewrite → Design-to-Writing handoff, then issue a new Writing version
