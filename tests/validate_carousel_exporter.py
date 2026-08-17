from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "export_instagram_carousel.py"


def load_module():
    spec = importlib.util.spec_from_file_location("carousel_exporter", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load carousel exporter")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    errors: list[str] = []

    portrait = module.ExportConfig(1080, 1350, 420, 525)
    portrait.validate()
    if round(portrait.device_scale_factor, 4) != 2.5714:
        errors.append("Portrait device scale factor is incorrect")

    try:
        module.ExportConfig(1080, 1080, 420, 525).validate()
        errors.append("Mismatched aspect ratios were accepted")
    except ValueError:
        pass

    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        html = root / "test carousel.html"
        html.write_text('<section class="slide">Test</section>', encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(html),
                "--preset",
                "square",
                "--approval",
                "TEST-APPROVAL",
                "--output-dir",
                str(root / "runs"),
                "--check-only",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            errors.append(f"Check-only preflight failed: {result.stderr}")
        else:
            payload = json.loads(result.stdout)
            if payload.get("target_size") != [1080, 1080]:
                errors.append("Square preset dimensions are incorrect")
            if (root / "runs").exists():
                errors.append("Check-only preflight created output directories")

    print(f"Carousel exporter errors: {len(errors)}")
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
