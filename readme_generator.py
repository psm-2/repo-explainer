from __future__ import annotations

import os
from dataclasses import dataclass

from openai import OpenAI


SYSTEM_PROMPT = """You are an expert technical writer helping a developer publish a GitHub project.

Write a polished README.md in Markdown only. Keep it practical, clear, and concise.

Include these sections when relevant:
- Project title
- Overview
- Features
- Tech stack
- Installation
- Usage
- API reference
- Configuration
- Project structure
- Roadmap
- Contributing
- License

Rules:
- Return only Markdown.
- Do not wrap the output in code fences.
- Prefer sensible defaults and realistic placeholders where details are missing.
- If the supplied input is brief, infer a small but coherent project README.
"""


class ReadmeGenerationError(RuntimeError):
    pass


def _client() -> OpenAI:
    return OpenAI()


def generate_readme(project_input: str) -> str:
    model = os.getenv("OPENAI_MODEL", "gpt-5.5")

    try:
        client = _client()
        response = client.responses.create(
            model=model,
            instructions=SYSTEM_PROMPT,
            input=project_input,
        )
        output = (response.output_text or "").strip()
    except Exception as exc:  # noqa: BLE001 - surface a helpful message to the caller
        raise ReadmeGenerationError(
            "Failed to generate the README. Check that OPENAI_API_KEY is set and the model name is valid."
        ) from exc

    if not output:
        raise ReadmeGenerationError("The model returned an empty README.")

    return output
