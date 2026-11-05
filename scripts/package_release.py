#!/usr/bin/env python3
"""
scripts/package_release.py
Automated packaging script for Skill_LN release assets.
Generates hermetic ZIP archives for:
  1. erp-ln-progguide (Knowledge base & standalone 4GL audit engine)
  2. ln_studio_skill (Headless JCA automation, generators, SCM & MCP server)
  3. skill-ln-vscode (TextMate grammar, completions, snippets)

Usage:
  python scripts/package_release.py [--version v1.0.0] [--output-dir dist]
"""

import os
import sys
import shutil
import zipfile
import argparse
from pathlib import Path
from typing import List, Set

REPO_ROOT = Path(__file__).resolve().parent.parent

EXCLUDE_NAMES: Set[str] = {
    "__pycache__",
    ".DS_Store",
    "Thumbs.db",
    ".git",
    ".gitignore",
    ".pytest_cache",
}

EXCLUDE_EXTS: Set[str] = {
    ".pyc",
    ".pyo",
    ".pyd",
    ".swp",
    ".swo",
}


def should_exclude(path: Path) -> bool:
    """Returns True if the file or directory should be excluded from release zips."""
    for part in path.parts:
        if part in EXCLUDE_NAMES:
            return True
    if path.suffix.lower() in EXCLUDE_EXTS:
        return True
    # Exclude authentic jar binaries from distribution (BYOJ policy)
    if path.suffix.lower() == ".jar":
        return True
    return False


def zip_directory(src_dir: Path, zip_file: zipfile.ZipFile, arcname_prefix: str) -> int:
    """Recursively adds files from src_dir to zip_file under arcname_prefix."""
    file_count = 0
    for root, dirs, files in os.walk(src_dir):
        # Filter directories in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_NAMES and not d.endswith(".egg-info")]
        root_path = Path(root)

        for f in files:
            file_path = root_path / f
            if should_exclude(file_path):
                continue
            rel_path = file_path.relative_to(src_dir)
            arcname = (Path(arcname_prefix) / rel_path).as_posix()
            zip_file.write(file_path, arcname)
            file_count += 1
    return file_count


def package_erp_ln_progguide(version_str: str, dist_dir: Path) -> Path:
    skill_dir = REPO_ROOT / "erp-ln-progguide"
    target_zip = dist_dir / f"erp-ln-progguide-{version_str}.zip"
    print(f"Packaging {target_zip.name} ...")
    with zipfile.ZipFile(target_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        count = zip_directory(skill_dir, zf, "erp-ln-progguide")
    print(f"  -> Added {count} files to {target_zip.name} ({target_zip.stat().st_size:,} bytes)")
    return target_zip


def package_ln_studio_skill(version_str: str, dist_dir: Path) -> Path:
    skill_dir = REPO_ROOT / "ln_studio_skill"
    target_zip = dist_dir / f"ln_studio_skill-{version_str}.zip"
    print(f"Packaging {target_zip.name} ...")
    with zipfile.ZipFile(target_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        count = zip_directory(skill_dir, zf, "ln_studio_skill")
    print(f"  -> Added {count} files to {target_zip.name} ({target_zip.stat().st_size:,} bytes)")
    return target_zip


def package_vscode_assets(version_str: str, dist_dir: Path) -> Path:
    vscode_dir = REPO_ROOT / "export" / "vscode"
    target_zip = dist_dir / f"skill-ln-vscode-{version_str}.zip"
    print(f"Packaging {target_zip.name} ...")
    with zipfile.ZipFile(target_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        count = zip_directory(vscode_dir, zf, "skill-ln-vscode")
    print(f"  -> Added {count} files to {target_zip.name} ({target_zip.stat().st_size:,} bytes)")
    return target_zip


def main():
    parser = argparse.ArgumentParser(description="Package Skill_LN release assets")
    parser.add_argument("--version", default="v1.0.0", help="Release version tag (e.g. v1.0.0)")
    parser.add_argument("--output-dir", default="dist", help="Output directory for archives")
    args = parser.parse_args()

    version_str = args.version.strip()
    if not version_str.startswith("v"):
        version_str = f"v{version_str}"

    dist_dir = REPO_ROOT / args.output_dir
    dist_dir.mkdir(parents=True, exist_ok=True)

    print(f"==================================================")
    print(f"Building Skill_LN Release Packages for: {version_str}")
    print(f"Output Directory: {dist_dir}")
    print(f"==================================================")

    p1 = package_erp_ln_progguide(version_str, dist_dir)
    p2 = package_ln_studio_skill(version_str, dist_dir)
    p3 = package_vscode_assets(version_str, dist_dir)

    print(f"\n[SUCCESS] Successfully packaged 3 release assets in {dist_dir}:")
    for p in (p1, p2, p3):
        print(f"  * {p.name} ({p.stat().st_size / (1024 * 1024):.2f} MB)")


if __name__ == "__main__":
    main()
