"""Unit tests for validating Markdown links and anchors across Skill_LN READMEs."""

import os
import re
import unittest
from pathlib import Path


class TestReadmeLinks(unittest.TestCase):
    """Verifies that all internal anchors and relative file paths in READMEs resolve correctly."""

    @classmethod
    def setUpClass(cls):
        # Resolve repo root relative to this test file
        cls.repo_root = Path(__file__).resolve().parents[3]
        cls.readme_files = [
            cls.repo_root / "README.md",
            cls.repo_root / "ln_studio_skill" / "README.md",
            cls.repo_root / "erp-ln-progguide" / "README.md",
        ]

    def _slugify_heading(self, text: str) -> str:
        """Converts Markdown heading text to a GitHub-compatible anchor slug."""
        # Strip trailing formatting or emojis if any, convert to lowercase
        text = text.strip().lower()
        # Remove backticks, parentheses, colons, commas, periods
        text = re.sub(r"[`:(),.?/*]", "", text)
        # Replace spaces and underscores with hyphens
        text = re.sub(r"[\s_]+", "-", text)
        # Remove leading/trailing hyphens
        return text.strip("-")

    def _get_file_anchors(self, file_path: Path) -> set:
        """Extracts all heading anchors and HTML anchor names from a Markdown file."""
        anchors = set()
        if not file_path.exists() or file_path.is_dir():
            return anchors

        content = file_path.read_text(encoding="utf-8")
        # Extract markdown headings: # Heading
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("#"):
                heading_text = line.lstrip("#").strip().lower()
                # GitHub GFM slug algorithm: remove punctuation (keep word chars, spaces, hyphens)
                cleaned = re.sub(r"[^\w\s-]", "", heading_text)
                # Form 1: collapsed spaces
                slug1 = re.sub(r"\s+", "-", cleaned).strip("-")
                # Form 2: literal spaces replaced with hyphens (e.g. "foo & bar" -> "foo  bar" -> "foo--bar")
                slug2 = cleaned.replace(" ", "-").strip("-")

                for s in (slug1, slug2):
                    if s:
                        anchors.add(s)
                        # Also without emojis if any
                        s_no_emoji = re.sub(r"[^\w\-]", "", s).strip("-")
                        if s_no_emoji:
                            anchors.add(s_no_emoji)

        # Extract HTML <a name="..."> or <a id="...">
        for match in re.finditer(r'<a\s+(?:name|id)=["\']([^"\']+)["\']', content, re.IGNORECASE):
            anchors.add(match.group(1).lower())

        return anchors

    def test_readmes_exist(self):
        """Ensure all 3 primary README files exist."""
        for readme in self.readme_files:
            self.assertTrue(readme.exists(), f"README file missing: {readme}")

    def test_readme_links_and_anchors(self):
        """Ensure all links, relative paths, and anchors in the 3 READMEs resolve."""
        link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

        total_links_checked = 0
        broken_links = []

        for readme in self.readme_files:
            content = readme.read_text(encoding="utf-8")
            file_anchors = self._get_file_anchors(readme)

            for match in link_pattern.finditer(content):
                link_text, link_target = match.group(1), match.group(2).strip()

                # Skip web links, badges, mailto
                if (
                    link_target.startswith("http://")
                    or link_target.startswith("https://")
                    or link_target.startswith("mailto:")
                    or link_target.startswith("img.shields.io")
                ):
                    continue

                total_links_checked += 1

                # 1. Same-file anchor link: #some-anchor
                if link_target.startswith("#"):
                    anchor = link_target.lstrip("#").lower()
                    # Allow variations
                    slug_cleaned = re.sub(r"[^\w\-]", "", anchor).strip("-")
                    if (
                        anchor not in file_anchors
                        and slug_cleaned not in file_anchors
                    ):
                        broken_links.append(
                            f"{readme.name}: Anchor '{link_target}' not found in file."
                        )
                    continue

                # 2. Relative file link: path/to/file or path/to/file#anchor
                target_parts = link_target.split("#", 1)
                rel_path = target_parts[0]
                target_anchor = target_parts[1].lower() if len(target_parts) > 1 else None

                target_file = (readme.parent / rel_path).resolve()

                # If relative link targets a directory, check if it has README.md
                if target_file.is_dir():
                    if (target_file / "README.md").exists():
                        target_file = target_file / "README.md"

                if not target_file.exists():
                    broken_links.append(
                        f"{readme.name}: Target path '{rel_path}' does not exist (resolved to {target_file})."
                    )
                elif target_anchor:
                    target_file_anchors = self._get_file_anchors(target_file)
                    slug_cleaned = re.sub(r"[^\w\-]", "", target_anchor).strip("-")
                    if (
                        target_anchor not in target_file_anchors
                        and slug_cleaned not in target_file_anchors
                    ):
                        broken_links.append(
                            f"{readme.name}: Anchor '{target_anchor}' not found in target '{rel_path}'."
                        )

        self.assertEqual(
            broken_links,
            [],
            f"Found broken Markdown links ({len(broken_links)} broken / {total_links_checked} checked):\n"
            + "\n".join(broken_links),
        )


if __name__ == "__main__":
    unittest.main()
