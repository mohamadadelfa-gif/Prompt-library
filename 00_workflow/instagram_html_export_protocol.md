# Instagram HTML Carousel Export Protocol

## Purpose

Render an approved HTML carousel into non-destructive, dimension-verified Instagram PNG slides while preserving source provenance and routing every export through mandatory QC.

## Preconditions

- approved HTML source and explicit export authorization;
- complete fonts and assets or declared limitations;
- selected Instagram format and design viewport;
- HTML production/originality checks passed;
- output location resolved inside the intended workspace.

## Supported Presets

- `square` — 1080×1080;
- `portrait` — 1080×1350;
- `story` — 1080×1920;
- custom dimensions only when explicitly requested and aspect-ratio compatible.

The CSS design viewport may be smaller than the output. Device-scale rendering preserves layout while producing the required pixel dimensions.

## Dependency Policy

Dependencies are never installed automatically.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-carousel-export.txt
.\.venv\Scripts\python.exe -m playwright install chromium
```

The browser download is an explicit user/environment setup action, not a hidden export side effect.

## Preflight

Run `--check-only` first to validate the source, selector, dimensions, aspect ratio, approval record and planned non-destructive output directory without launching Chromium.

## Export

```powershell
python scripts\export_instagram_carousel.py <carousel.html> --preset portrait --approval <approval-record>
```

For a 420×525 CSS design exported to 1080×1350:

```powershell
python scripts\export_instagram_carousel.py <carousel.html> --preset portrait --design-width 420 --design-height 525 --approval <approval-record>
```

The exporter:

- waits for `document.fonts.ready` plus an optional bounded delay;
- disables animation during capture;
- captures each configured slide element;
- validates every PNG's exact dimensions;
- creates a new numbered run directory rather than overwriting prior exports;
- records source/output SHA-256 hashes and rendering parameters;
- emits `export-manifest.json` with `AWAITING_MANDATORY_QC`.

## Safety

- Do not export arbitrary untrusted HTML with network access or local secrets available to the page.
- Inspect remote scripts, fonts and assets before rendering.
- Never treat a successful screenshot as design approval.
- Do not resize a previously exported PNG when an authoritative HTML source can be rendered directly.
- Keep the source HTML, export manifest and QC evidence distinct.

## Mandatory QC

At minimum run:

- `QC-IG-001` for carousel/platform quality;
- `QC-IQA-001` for technical image integrity;
- `QC-TYPE-001` when typography integrity is material;
- `QC-LOGO-001` when logos are present;
- `QC-AUD-001` / `QC-SOC-001` when audience and stopping power are in scope.

The manifest may become publishable only after applicable gates pass and human approval is recorded. Exact dimensions do not prove safe areas, readability, source fidelity or publish readiness.

## Failure Routing

- source/asset failure → HTML Visual Production;
- incorrect dimensions or clipping → exporter configuration / HTML layout;
- font mismatch → typography reconstruction or source asset resolution;
- design/audience failure → Art Direction or Platform Synthesis;
- corrupt/low-quality PNG → technical image QC and rerender;
- missing human approval → `BLOCKED`.

## Provenance

The rendering approach was adapted from `Hanseldemulcent167/html-to-Instagram-carousel`, Copyright 2026 DJ Vekariya, under the MIT License. This implementation removes automatic dependency installation, adds multiple formats, explicit approval, source/output hashing, dimension verification, non-destructive run directories and mandatory QC routing.

## Version

1.0-production-candidate

## Status

Active conditional protocol
