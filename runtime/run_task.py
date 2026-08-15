from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from runner import RunnerError, create_provider

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RUN_DIR = ROOT / "runs"


def parse_prompt_id(text: str) -> str:
    match = re.search(r"^##\s+ID\s*$\n+\s*([A-Z]+-\d{3})\s*$", text, re.M)
    if not match:
        raise RunnerError("Prompt file does not contain a valid ## ID section")
    return match.group(1)


def load_prompt(path: Path) -> tuple[str, str]:
    if not path.exists():
        raise RunnerError(f"Prompt file not found: {path}")
    text = path.read_text(encoding="utf-8")
    return parse_prompt_id(text), text


def load_input(path: Path) -> str:
    if not path.exists():
        raise RunnerError(f"Input file not found: {path}")
    return path.read_text(encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Execute one Prompt Library task and persist an audit artifact.")
    parser.add_argument("--prompt", required=True, help="Path to the prompt markdown file")
    parser.add_argument("--input", required=True, help="Path to the task input artifact")
    parser.add_argument("--provider", default=os.getenv("LLM_PROVIDER", "openai"))
    parser.add_argument("--model", default=os.getenv("LLM_MODEL", "gpt-5"))
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--output-dir", default=str(DEFAULT_RUN_DIR))
    args = parser.parse_args()

    prompt_path = Path(args.prompt).resolve()
    input_path = Path(args.input).resolve()
    run_id = args.run_id or datetime.now(timezone.utc).strftime("RUN-%Y%m%dT%H%M%SZ")

    try:
        task_id, prompt_text = load_prompt(prompt_path)
        input_text = load_input(input_path)
        provider = create_provider(args.provider)
        started = datetime.now(timezone.utc)
        output = provider.generate(instructions=prompt_text, input_text=input_text, model=args.model)
        completed = datetime.now(timezone.utc)
    except (RunnerError, OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    artifact = {
        "run_id": run_id,
        "task_id": task_id,
        "provider": args.provider.lower(),
        "model": args.model,
        "started_at": started.isoformat(),
        "completed_at": completed.isoformat(),
        "prompt_path": str(prompt_path.relative_to(ROOT)) if prompt_path.is_relative_to(ROOT) else str(prompt_path),
        "input_path": str(input_path.relative_to(ROOT)) if input_path.is_relative_to(ROOT) else str(input_path),
        "prompt_sha256": sha256_text(prompt_text),
        "input_sha256": sha256_text(input_text),
        "output": output,
        "status": "COMPLETED",
    }

    output_dir = Path(args.output_dir).resolve() / run_id
    output_dir.mkdir(parents=True, exist_ok=False)
    (output_dir / "run.json").write_text(json.dumps(artifact, ensure_ascii=False, indent=2), encoding="utf-8")
    (output_dir / "output.md").write_text(output, encoding="utf-8")

    print(json.dumps({"run_id": run_id, "task_id": task_id, "artifact": str(output_dir)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
