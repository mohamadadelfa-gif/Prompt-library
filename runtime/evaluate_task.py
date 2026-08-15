from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from runner import RunnerError, create_provider

ROOT = Path(__file__).resolve().parents[1]
RUBRIC = ROOT / "tests" / "evaluation_rubric.md"

JUDGE_INSTRUCTIONS = """You are the semantic evaluator for a controlled creative-production task.
Evaluate the candidate output against the supplied task prompt, input, and rubric.
Do not reward plausibility when the source does not support it.
Return strict JSON with:
{
  \"decision\": \"PASS\" | \"FAIL\",
  \"average_score\": number,
  \"scores\": {\"task_adherence\":0-4,\"source_fidelity\":0-4,\"unknown_handling\":0-4,\"completeness\":0-4,\"classification\":0-4,\"traceability\":0-4,\"contract_compliance\":0-4,\"handoff_quality\":0-4},
  \"critical_failures\": [],
  \"findings\": [],
  \"recommended_action\": \"KEEP\" | \"REVISE\" | \"REJECT\"
}
A critical hallucination, source contradiction, or boundary violation forces FAIL.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate a Prompt Library task output with an LLM judge.")
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--provider", default=os.getenv("LLM_PROVIDER", "openai"))
    parser.add_argument("--model", default=os.getenv("EVAL_MODEL", os.getenv("LLM_MODEL", "gpt-5")))
    args = parser.parse_args()

    try:
        prompt = Path(args.prompt).read_text(encoding="utf-8")
        task_input = Path(args.input).read_text(encoding="utf-8")
        candidate = Path(args.output).read_text(encoding="utf-8")
        rubric = RUBRIC.read_text(encoding="utf-8")
        provider = create_provider(args.provider)
        evaluation_input = (
            f"TASK PROMPT:\n{prompt}\n\n"
            f"TASK INPUT:\n{task_input}\n\n"
            f"CANDIDATE OUTPUT:\n{candidate}\n\n"
            f"RUBRIC:\n{rubric}\n\n"
            "Return JSON only."
        )
        raw = provider.generate(instructions=JUDGE_INSTRUCTIONS, input_text=evaluation_input, model=args.model)
        evaluation = json.loads(raw)
    except (RunnerError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    required = {"decision", "average_score", "scores", "critical_failures", "findings", "recommended_action"}
    missing = required - set(evaluation)
    if missing:
        print(f"ERROR: evaluator missing fields: {sorted(missing)}", file=sys.stderr)
        return 3
    if evaluation["critical_failures"]:
        evaluation["decision"] = "FAIL"
    if evaluation["decision"] == "PASS" and evaluation["average_score"] < 3.0:
        evaluation["decision"] = "FAIL"

    print(json.dumps(evaluation, ensure_ascii=False, indent=2))
    return 0 if evaluation["decision"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
