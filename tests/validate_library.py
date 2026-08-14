from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_DIRS = [ROOT / f"{i:02d}_{name}" for i, name in enumerate([
    "strategy", "research", "visual_analysis", "visual_dna",
    "art_direction", "generation", "quality_control"
], start=1)]
DEPRECATED_FILES = {"02_research/reference_selection.md"}

ID_RE = re.compile(r"^##\s+ID\s*$", re.M)
VERSION_RE = re.compile(r"^##\s+Version\s*$", re.M)
STATUS_RE = re.compile(r"^##\s+Status\s*$", re.M)
ID_VALUE_RE = re.compile(r"^([A-Z]+-\d{3})$", re.M)

errors = []
warnings = []
ids = {}
files_checked = 0


def has_section(text: str, aliases: list[str]) -> bool:
    pattern = r"^##\s+.*(?:" + "|".join(re.escape(a) for a in aliases) + r").*$"
    return re.search(pattern, text, re.M | re.I) is not None


for directory in ACTIVE_DIRS:
    if not directory.exists():
        errors.append(f"Missing active stage directory: {directory.relative_to(ROOT)}")
        continue

    for path in sorted(directory.glob("*.md")):
        rel = path.relative_to(ROOT)
        rel_string = str(rel).replace("\\", "/")
        if path.name.startswith("README") or rel_string in DEPRECATED_FILES:
            continue

        files_checked += 1
        text = path.read_text(encoding="utf-8")

        if not ID_RE.search(text):
            errors.append(f"{rel}: missing ## ID")
        else:
            match = re.search(r"^##\s+ID\s*\n+\s*([^\n]+)", text, re.M)
            if not match:
                errors.append(f"{rel}: ID heading has no value")
            else:
                prompt_id = match.group(1).strip()
                if not ID_VALUE_RE.fullmatch(prompt_id):
                    errors.append(f"{rel}: invalid ID '{prompt_id}'")
                elif prompt_id in ids:
                    errors.append(f"Duplicate ID {prompt_id}: {ids[prompt_id]} and {rel}")
                else:
                    ids[prompt_id] = rel

        if not VERSION_RE.search(text):
            errors.append(f"{rel}: missing ## Version")
        if not STATUS_RE.search(text):
            errors.append(f"{rel}: missing ## Status")

        if not has_section(text, ["Input", "Required Inputs"]):
            warnings.append(f"{rel}: no explicit input contract section")
        if not has_section(text, ["Output", "Output Format"]):
            warnings.append(f"{rel}: no explicit output contract section")
        if not has_section(text, ["Constraints", "Core Rules", "Failure Conditions"]):
            warnings.append(f"{rel}: no explicit constraint/boundary section")

expected_prefixes = {
    "01_strategy": "STR-",
    "02_research": "RES-",
    "03_visual_analysis": "VIS-",
    "04_visual_dna": "VDNA-",
    "05_art_direction": "ART-",
    "06_generation": "GEN-",
    "07_quality_control": "QC-",
}

for prompt_id, path in ids.items():
    directory = path.parts[0]
    prefix = expected_prefixes[directory]
    if not prompt_id.startswith(prefix):
        errors.append(f"{path}: ID {prompt_id} does not match stage prefix {prefix}")

if warnings:
    errors.extend(warnings)

print(f"Checked {files_checked} active prompt files")
print(f"Unique IDs: {len(ids)}")
print(f"Warnings: {len(warnings)}")
print(f"Errors: {len(errors)}")

for item in warnings:
    print(f"WARNING: {item}")
for item in errors:
    print(f"ERROR: {item}")

sys.exit(1 if errors else 0)
