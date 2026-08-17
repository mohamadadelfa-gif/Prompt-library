from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "00_workflow" / "design_token_system_schema.json"
TEMPLATE = ROOT / "assets" / "templates" / "DESIGN_TOKEN_SYSTEM_TEMPLATE.json"
REFERENCE = re.compile(r"^\{([^{}]+)\}$")


def find_cycle(graph: dict[str, str]) -> list[str]:
    visited: set[str] = set()
    active: list[str] = []

    def visit(node: str) -> list[str]:
        if node in active:
            start = active.index(node)
            return active[start:] + [node]
        if node in visited:
            return []
        visited.add(node)
        active.append(node)
        target = graph.get(node)
        cycle = visit(target) if target in graph else []
        active.pop()
        return cycle

    for node in graph:
        cycle = visit(node)
        if cycle:
            return cycle
    return []


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    record = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    errors: list[str] = []

    missing = set(schema["required"]) - record.keys()
    if missing:
        errors.append(f"Template missing fields: {sorted(missing)}")

    tokens = record.get("tokens", {})
    global_tokens = tokens.get("global", {})
    aliases = tokens.get("alias", {})
    components = tokens.get("component", {})
    naming = re.compile(schema["naming_pattern"])

    themes = record.get("themes", [])
    if set(themes) != set(aliases):
        errors.append("Theme list and alias theme maps differ")
    alias_sets = [set(aliases[theme]) for theme in themes if theme in aliases]
    if alias_sets and any(names != alias_sets[0] for names in alias_sets[1:]):
        errors.append("Alias token parity differs between themes")

    for name in global_tokens:
        if not naming.fullmatch(name) or not name.startswith("global."):
            errors.append(f"Invalid global token name: {name}")
    for theme, theme_tokens in aliases.items():
        for name, token in theme_tokens.items():
            if not naming.fullmatch(name) or not name.startswith("alias."):
                errors.append(f"Invalid alias token name: {theme}:{name}")
            match = REFERENCE.fullmatch(str(token.get("value", "")))
            if match and match.group(1) not in global_tokens and match.group(1) not in theme_tokens:
                errors.append(f"Unresolved alias reference: {theme}:{name}")
    alias_names = set.intersection(*alias_sets) if alias_sets else set()
    for name, token in components.items():
        if not naming.fullmatch(name) or not name.startswith("component."):
            errors.append(f"Invalid component token name: {name}")
        match = REFERENCE.fullmatch(str(token.get("value", "")))
        if not match:
            errors.append(f"Raw component value lacks exception: {name}")
        elif match.group(1) not in global_tokens and match.group(1) not in alias_names and match.group(1) not in components:
            errors.append(f"Unresolved component reference: {name}")

    states = {name.rsplit(".", 1)[-1] for name in components}
    required_states = set(schema["required_component_states"])
    if not required_states.issubset(states):
        errors.append(f"Missing component states: {sorted(required_states - states)}")

    for theme, theme_tokens in aliases.items():
        combined = {**global_tokens, **theme_tokens, **components}
        graph = {}
        for name, token in combined.items():
            match = REFERENCE.fullmatch(str(token.get("value", "")))
            if match:
                graph[name] = match.group(1)
        cycle = find_cycle(graph)
        if cycle:
            errors.append(f"Reference cycle in {theme}: {' -> '.join(cycle)}")

    print(f"Global tokens: {len(global_tokens)}")
    print(f"Alias tokens per theme: {len(alias_sets[0]) if alias_sets else 0}")
    print(f"Component tokens: {len(components)}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
