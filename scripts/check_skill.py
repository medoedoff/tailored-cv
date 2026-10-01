#!/usr/bin/env python3
"""Run dependency-free structural and portability checks for this skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
RUNTIME_FILES = [
    SKILL,
    *sorted((ROOT / "references").glob("*.md")),
    *sorted((ROOT / "assets").glob("*")),
]

BANNED_RUNTIME_PATTERNS = {
    "host-specific home path": r"/(?:home|Users)/[^/\s]+/",
    "provider-specific tool name": r"\b(?:WebFetch|AskUserQuestion|SendUserFile|remote-devices)\b",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        fail("SKILL.md frontmatter is not closed")

    values: dict[str, str] = {}
    for raw_line in block.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            fail(f"unsupported frontmatter line: {raw_line}")
        key, value = raw_line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def check_frontmatter(text: str) -> None:
    values = parse_frontmatter(text)
    name = values.get("name", "")
    description = values.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail("name must contain lowercase letters, digits, and internal hyphens only")
    if len(name) > 64:
        fail("name exceeds 64 characters")
    if not description or len(description) > 1024:
        fail("description must contain 1-1024 characters")


def check_links(text: str) -> None:
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        path = (ROOT / target.split("#", 1)[0]).resolve()
        if not path.is_relative_to(ROOT.resolve()) or not path.exists():
            fail(f"missing or unsafe local link: {target}")


def check_portability() -> None:
    for path in RUNTIME_FILES:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in BANNED_RUNTIME_PATTERNS.items():
            if re.search(pattern, text, flags=re.IGNORECASE):
                fail(f"{label} found in {path.relative_to(ROOT)}")


def main() -> None:
    if not SKILL.exists():
        fail("SKILL.md is missing")
    skill_files = [path for path in ROOT.rglob("*") if path.is_file() and path.name.lower() == "skill.md"]
    if skill_files != [SKILL]:
        fail("the bundle must contain exactly one root SKILL.md")

    text = SKILL.read_text(encoding="utf-8")
    check_frontmatter(text)
    check_links(text)
    check_portability()
    print("Skill structure and portability checks passed.")


if __name__ == "__main__":
    main()
