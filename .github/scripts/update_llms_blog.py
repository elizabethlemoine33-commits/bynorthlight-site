"""
Reads all non-index HTML files in the blog/ directory, extracts their <title>
tags, and rewrites the "Current posts:" section of llms.txt.

Run manually or via GitHub Actions whenever a new blog post is published.
"""

import re
from pathlib import Path

BLOG_DIR = Path("blog")
LLMS_FILE = Path("llms.txt")
BASE_URL = "https://bynorthlight.ca"

TITLE_SUFFIXES = re.compile(
    r"\s*[—–-]+\s*(Northlight Advisory Services|Northlight)\s*$"
)


def get_title(filepath: Path) -> str | None:
    content = filepath.read_text(encoding="utf-8")
    match = re.search(r"<title>([^<]+)</title>", content, re.IGNORECASE)
    if not match:
        return None
    return TITLE_SUFFIXES.sub("", match.group(1).strip()).strip()


def get_blog_entries() -> list[str]:
    entries = []
    for f in sorted(BLOG_DIR.glob("*.html")):
        if f.name == "index.html":
            continue
        title = get_title(f)
        if title:
            entries.append(f"- {title} — {BASE_URL}/blog/{f.name}")
    return entries


def update_llms(entries: list[str]) -> None:
    content = LLMS_FILE.read_text(encoding="utf-8")
    new_block = "Current posts:\n" + "\n".join(entries) + "\n"
    updated = re.sub(
        r"Current posts:\n(?:- .+\n?)+",
        new_block,
        content,
    )
    if updated == content:
        print("No changes to llms.txt — blog list already up to date.")
        return
    LLMS_FILE.write_text(updated, encoding="utf-8")
    print(f"Updated llms.txt with {len(entries)} blog post(s).")


if __name__ == "__main__":
    entries = get_blog_entries()
    if not entries:
        print("No blog posts found — llms.txt unchanged.")
    else:
        update_llms(entries)
