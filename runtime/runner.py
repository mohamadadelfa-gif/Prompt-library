from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Protocol


class RunnerError(RuntimeError):
    """Raised when a model execution cannot be completed safely."""


class Provider(Protocol):
    def generate(self, *, instructions: str, input_text: str, model: str) -> str:
        ...


@dataclass(frozen=True)
class RunConfig:
    provider: str
    model: str


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RunnerError(f"Missing required environment variable: {name}")
    return value


class OpenAIProvider:
    def __init__(self) -> None:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RunnerError("OpenAI provider requires the 'openai' package") from exc
        self.client = OpenAI(api_key=_require_env("OPENAI_API_KEY"))

    def generate(self, *, instructions: str, input_text: str, model: str) -> str:
        response = self.client.responses.create(
            model=model,
            instructions=instructions,
            input=input_text,
        )
        text = getattr(response, "output_text", None)
        if not text:
            raise RunnerError("OpenAI returned no output_text")
        return str(text)


class GeminiProvider:
    def __init__(self) -> None:
        try:
            from google import genai
        except ImportError as exc:
            raise RunnerError("Gemini provider requires the 'google-genai' package") from exc
        self.client = genai.Client(api_key=_require_env("GEMINI_API_KEY"))

    def generate(self, *, instructions: str, input_text: str, model: str) -> str:
        # Keep instructions explicit inside the stateless input for portability.
        combined = f"SYSTEM TASK INSTRUCTIONS:\n{instructions}\n\nTASK INPUT:\n{input_text}"
        response = self.client.models.generate_content(model=model, contents=combined)
        text = getattr(response, "text", None)
        if not text:
            raise RunnerError("Gemini returned no text output")
        return str(text)


def create_provider(provider: str) -> Provider:
    normalized = provider.strip().lower()
    if normalized == "openai":
        return OpenAIProvider()
    if normalized == "gemini":
        return GeminiProvider()
    raise RunnerError(f"Unsupported provider '{provider}'. Use 'openai' or 'gemini'.")
