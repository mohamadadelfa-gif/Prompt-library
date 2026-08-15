# Runtime

The runtime turns a Prompt Library markdown task into an executable, auditable model call.

## Providers

- `openai` — official OpenAI Python SDK and Responses API.
- `gemini` — official Google GenAI Python SDK.

## Environment

Set one provider key:

```text
OPENAI_API_KEY=...
```

or

```text
GEMINI_API_KEY=...
```

Then choose:

```text
LLM_PROVIDER=openai|gemini
LLM_MODEL=<approved-model-id>
```

## Execute a task

```bash
python runtime/run_task.py \
  --prompt 01_strategy/customer_analysis.md \
  --input tests/fixtures/noura_coffee/project_input.md \
  --provider openai \
  --model gpt-5
```

The runner writes an auditable artifact under `runs/<run-id>/` containing run metadata, source hashes, and the model output.

## Evaluate an output

```bash
python runtime/evaluate_task.py \
  --prompt 01_strategy/customer_analysis.md \
  --input tests/fixtures/noura_coffee/project_input.md \
  --output runs/<run-id>/output.md \
  --provider openai \
  --model <evaluation-model>
```

## Production rules

- Never commit API keys or generated private project artifacts.
- Keep `runs/` out of version control unless a sanitized regression artifact is intentionally captured.
- Pin the model used for a release test and record it in the evaluation artifact.
- A semantic test PASS is required before changing a production prompt version.

The runner deliberately fails closed when the provider package, API key, input, prompt, or model output is unavailable.
