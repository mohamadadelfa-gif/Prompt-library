from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "00_workflow" / "design_system_reference_registry.json"


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []
    references = data.get("references", [])
    ids = [item.get("id") for item in references]
    if len(references) < 5:
        errors.append("Registry must contain a useful starter set")
    if len(ids) != len(set(ids)):
        errors.append("Reference IDs must be unique")
    policy = data.get("policy", {})
    if policy.get("live_verification_required") is not True:
        errors.append("Live verification must remain mandatory")
    if policy.get("automatic_target_token_adoption") is not False:
        errors.append("Automatic target-token adoption must remain disabled")

    required = {"id", "name", "owner", "official_url", "best_for", "status"}
    for item in references:
        missing = required - item.keys()
        if missing:
            errors.append(f"{item.get('id', 'UNKNOWN')} missing: {sorted(missing)}")
        parsed = urlparse(item.get("official_url", ""))
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{item.get('id', 'UNKNOWN')} must use an HTTPS official URL")
        if item.get("status") != "VERIFY_BEFORE_USE":
            errors.append(f"{item.get('id', 'UNKNOWN')} bypasses freshness verification")

    print(f"Design-system references: {len(references)}")
    print(f"Errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
