"""
Reads all non-index blog files (*.html and *.md) in the blog/ directory,
extracts their title, and rewrites the "Current posts:" section of llms.txt.

Run manually or via GitHub Actions whenever a new blog post is published.
"""

import re
from pathlib import Path

BLOG_DIR = Path("blog")
LLMS_FILE = Path("llms.txt")
BASE_URL = "https://bynorthlight.ca"

TITLE_SUFFIXES = re.compile(
    r"\s*[|—–-]+\s*(Northlight Advisory Services|Northlight)\s*$"
)


def get_title_from_html(content: str) -> str | None:
    match = re.search(r"<title>([^<]+)</title>", content, re.IGNORECASE)
    if not match:
        return None
    return TITLE_SUFFIXES.sub("", match.group(1).strip()).strip()


def get_title_from_md(content: str) -> str | None:
    match = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", content, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip().strip('"').strip("'")


def get_permalink_from_md(content: str, slug: str) -> str:
    match = re.search(r"^permalink:\s*(.+?)\s*$", content, re.MULTILINE)
    if match:
        path = match.group(1).strip()
        return f"{BASE_URL}{path}"
    return f"{BASE_URL}/blog/{slug}.html"


def get_blog_entries() -> list[str]:
    entries = {}

    # HTML posts
    for f in sorted(BLOG_DIR.glob("*.html")):
        if f.name == "index.html":
            continue
        content = f.read_text(encoding="utf-8")
        title = get_title_from_html(content)
        if title:
            url = f"{BASE_URL}/blog/{f.name}"
            entries[f.stem] = f"- {title} — {url}"

    # Markdown posts (override HTML if same slug exists — md = migrated canonical)
    for f in sorted(BLOG_DIR.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        # Skip redirect-only files
        if "redirect_to:" in content and "layout: redirect" in content:
            continue
        title = get_title_from_md(content)
        if title:
            url = get_permalink_from_md(content, f.stem)
            entries[f.stem] = f"- {title} — {url}"

    return [entries[k] for k in sorted(entries)]


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
