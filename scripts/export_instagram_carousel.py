from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import struct
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


PRESETS = {
    "square": (1080, 1080),
    "portrait": (1080, 1350),
    "story": (1080, 1920),
}


@dataclass(frozen=True)
class ExportConfig:
    target_width: int
    target_height: int
    design_width: int
    design_height: int

    @property
    def device_scale_factor(self) -> float:
        return self.target_width / self.design_width

    def validate(self) -> None:
        target_ratio = self.target_width / self.target_height
        design_ratio = self.design_width / self.design_height
        if abs(target_ratio - design_ratio) > 0.0005:
            raise ValueError(
                "Target and design aspect ratios differ. Set --design-width/--design-height "
                "to a viewport matching the selected output format."
            )
        if min(self.target_width, self.target_height, self.design_width, self.design_height) <= 0:
            raise ValueError("All target and design dimensions must be positive.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export HTML carousel slides to controlled Instagram PNG artifacts."
    )
    parser.add_argument("html", help="Path to the source HTML file.")
    parser.add_argument("--preset", choices=sorted(PRESETS), default="portrait")
    parser.add_argument("--width", type=int, help="Custom output width; requires --height.")
    parser.add_argument("--height", type=int, help="Custom output height; requires --width.")
    parser.add_argument("--design-width", type=int, help="CSS design viewport width.")
    parser.add_argument("--design-height", type=int, help="CSS design viewport height.")
    parser.add_argument("--slide-selector", default=".slide")
    parser.add_argument("--output-dir", default="runs/carousel_exports")
    parser.add_argument("--font-wait-ms", type=int, default=1000)
    parser.add_argument("--background", default="#ffffff")
    parser.add_argument("--approval", required=True, help="Required export authorization record/reference.")
    parser.add_argument("--check-only", action="store_true", help="Validate inputs without launching a browser.")
    return parser.parse_args()


def resolve_dimensions(args: argparse.Namespace) -> ExportConfig:
    if (args.width is None) != (args.height is None):
        raise ValueError("--width and --height must be supplied together.")
    target_width, target_height = (
        (args.width, args.height) if args.width is not None else PRESETS[args.preset]
    )
    design_width = args.design_width or target_width
    design_height = args.design_height or target_height
    config = ExportConfig(target_width, target_height, design_width, design_height)
    config.validate()
    return config


def sanitize_stem(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-") or "carousel"


def next_run_dir(output_root: Path, source_stem: str) -> Path:
    output_root = output_root.resolve()
    safe_stem = sanitize_stem(source_stem)
    pattern = re.compile(rf"^{re.escape(safe_stem)}_run_(\d{{3}})$")
    items = output_root.iterdir() if output_root.is_dir() else []
    used = [int(match.group(1)) for item in items if (match := pattern.match(item.name))]
    return output_root / f"{safe_stem}_run_{(max(used, default=0) + 1):03d}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as stream:
        header = stream.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError(f"Not a valid PNG: {path}")
    return struct.unpack(">II", header[16:24])


def validate_source(html_path: Path, selector: str, font_wait_ms: int, approval: str) -> None:
    if not html_path.is_file() or html_path.suffix.lower() not in {".html", ".htm"}:
        raise ValueError(f"Readable HTML source is required: {html_path}")
    if not selector.strip():
        raise ValueError("Slide selector cannot be empty.")
    if font_wait_ms < 0:
        raise ValueError("Font wait must be zero or greater.")
    if not approval.strip():
        raise ValueError("An explicit export approval/reference is required.")


async def export_slides(
    html_path: Path,
    run_dir: Path,
    config: ExportConfig,
    selector: str,
    font_wait_ms: int,
    background: str,
) -> list[Path]:
    try:
        from playwright.async_api import async_playwright
    except ImportError as exc:
        raise RuntimeError(
            "Playwright is not installed. Create/activate a virtual environment, run "
            "'python -m pip install -r requirements-carousel-export.txt', then run "
            "'python -m playwright install chromium'. Nothing was installed automatically."
        ) from exc

    run_dir.parent.mkdir(parents=True, exist_ok=True)
    run_dir.mkdir(parents=False, exist_ok=False)
    source_uri = html_path.resolve().as_uri()
    exported: list[Path] = []

    async with async_playwright() as playwright:
        try:
            browser = await playwright.chromium.launch(headless=True)
        except Exception as exc:
            raise RuntimeError(
                "Chromium could not launch. Run 'python -m playwright install chromium' explicitly."
            ) from exc

        page = await browser.new_page(
            viewport={"width": config.design_width, "height": config.design_height},
            device_scale_factor=config.device_scale_factor,
        )
        await page.goto(source_uri, wait_until="networkidle")
        await page.emulate_media(media="screen", reduced_motion="reduce")
        await page.add_style_tag(
            content=f"""
                html, body {{ background: {background}; }}
                *, *::before, *::after {{
                    animation: none !important;
                    transition: none !important;
                    caret-color: transparent !important;
                }}
            """
        )
        await page.evaluate("() => document.fonts ? document.fonts.ready : Promise.resolve()")
        if font_wait_ms:
            await page.wait_for_timeout(font_wait_ms)

        slides = page.locator(selector)
        count = await slides.count()
        if count == 0:
            await browser.close()
            raise RuntimeError(f"No slides matched selector: {selector}")

        for index in range(count):
            slide = slides.nth(index)
            await slide.evaluate(
                """(el, size) => {
                    el.style.width = size.width + 'px';
                    el.style.height = size.height + 'px';
                    el.style.minWidth = size.width + 'px';
                    el.style.minHeight = size.height + 'px';
                    el.style.maxWidth = size.width + 'px';
                    el.style.maxHeight = size.height + 'px';
                    el.style.overflow = 'hidden';
                    el.style.margin = '0';
                    el.style.transform = 'none';
                }""",
                {"width": config.design_width, "height": config.design_height},
            )
            output = run_dir / f"{sanitize_stem(html_path.stem)}_{index + 1:02d}.png"
            await slide.screenshot(path=str(output), type="png", animations="disabled")
            actual = png_dimensions(output)
            expected = (config.target_width, config.target_height)
            if actual != expected:
                await browser.close()
                raise RuntimeError(f"Slide {index + 1} exported at {actual}; expected {expected}.")
            exported.append(output)

        await browser.close()

    return exported


def write_manifest(
    run_dir: Path,
    html_path: Path,
    config: ExportConfig,
    selector: str,
    approval: str,
    exported: list[Path],
) -> Path:
    manifest = {
        "schema_version": "1.0",
        "artifact_type": "INSTAGRAM_CAROUSEL_EXPORT",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source": {
            "path": str(html_path.resolve()),
            "sha256": sha256_file(html_path),
            "slide_selector": selector,
        },
        "approval": approval,
        "render": {
            "target_size": [config.target_width, config.target_height],
            "design_viewport": [config.design_width, config.design_height],
            "device_scale_factor": config.device_scale_factor,
        },
        "slides": [
            {
                "index": index,
                "path": item.name,
                "dimensions": list(png_dimensions(item)),
                "sha256": sha256_file(item),
            }
            for index, item in enumerate(exported, start=1)
        ],
        "qc_state": "AWAITING_MANDATORY_QC",
        "required_qc": ["QC-IG-001", "QC-IQA-001", "applicable typography/logo/audience gates"],
    }
    path = run_dir / "export-manifest.json"
    path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return path


def main() -> int:
    args = parse_args()
    try:
        html_path = Path(args.html).resolve()
        config = resolve_dimensions(args)
        validate_source(html_path, args.slide_selector, args.font_wait_ms, args.approval)
        run_dir = next_run_dir(Path(args.output_dir), html_path.stem)
        if args.check_only:
            print(
                json.dumps(
                    {
                        "status": "PASS",
                        "source": str(html_path),
                        "planned_run_dir": str(run_dir),
                        "target_size": [config.target_width, config.target_height],
                        "design_viewport": [config.design_width, config.design_height],
                        "selector": args.slide_selector,
                    },
                    indent=2,
                )
            )
            return 0

        exported = asyncio.run(
            export_slides(
                html_path,
                run_dir,
                config,
                args.slide_selector,
                args.font_wait_ms,
                args.background,
            )
        )
        manifest = write_manifest(run_dir, html_path, config, args.slide_selector, args.approval, exported)
        print(f"Exported {len(exported)} slide(s) to {run_dir}")
        print(f"Manifest: {manifest}")
        print("QC state: AWAITING_MANDATORY_QC")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
