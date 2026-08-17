from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GUARD = ROOT / "scripts" / "ppt-layout-guard.js"


SAFE_DECK = """<!doctype html>
<html><head><style>
.title { line-height: 1.08; }
.body { line-height: 1.35; }
</style></head><body>
<!-- layout_box_budget: title then body then nav -->
<section class="slide" data-page="01">
  <div data-zone="title"><h1 class="title">A safe presentation title</h1></div>
  <div data-zone="body"><p class="body">Readable supporting content.</p></div>
  <div data-zone="nav_safe_zone"></div>
</section>
</body></html>"""


UNSAFE_DECK = """<!doctype html>
<html><head><style>.title { line-height: .8; overflow: hidden; }</style></head><body>
<section class="slide" data-page="01">
  <h1 class="title">Unsafe title</h1><p>Content without zones or budget.</p>
</section>
</body></html>"""


def run_guard(node: str, deck: Path, report: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [node, str(GUARD), str(deck), "--report", str(report)],
        check=False,
        capture_output=True,
        text=True,
    )


def main() -> int:
    node = shutil.which("node")
    if not node and os.name == "nt":
        bundled = Path.home() / ".cache" / "codex-runtimes" / "codex-primary-runtime" / "dependencies" / "node" / "bin" / "node.exe"
        if bundled.is_file():
            node = str(bundled)
    if not node:
        print("Presentation layout guard: SKIP (Node unavailable)")
        return 0

    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        safe = root / "safe.html"
        unsafe = root / "unsafe.html"
        safe_report = root / "safe-report.json"
        unsafe_report = root / "unsafe-report.json"
        safe.write_text(SAFE_DECK, encoding="utf-8")
        unsafe.write_text(UNSAFE_DECK, encoding="utf-8")

        safe_result = run_guard(node, safe, safe_report)
        unsafe_result = run_guard(node, unsafe, unsafe_report)

        safe_data = json.loads(safe_report.read_text(encoding="utf-8"))
        unsafe_data = json.loads(unsafe_report.read_text(encoding="utf-8"))

        if safe_result.returncode != 0 or safe_data.get("status") != "pass":
            print(safe_result.stdout, safe_result.stderr)
            print("ERROR: safe presentation fixture did not pass")
            return 1
        if unsafe_result.returncode == 0 or unsafe_data.get("status") != "fail":
            print(unsafe_result.stdout, unsafe_result.stderr)
            print("ERROR: unsafe presentation fixture did not fail")
            return 1

    print("Presentation layout guard: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
