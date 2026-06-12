import re
from pathlib import Path

BASE_URL = "https://bynorthlight.ca"

NOINDEX_PATTERN = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]*content=["\'][^"\']*noindex',
    re.IGNORECASE
)
CANONICAL_PATTERN = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
    re.IGNORECASE
)


def get_priority_and_freq(url_path):
    if url_path == "/":
        return "1.0", "weekly"
    if url_path in ("/about.html", "/vault.html"):
        return "0.9", "monthly"
    if url_path == "/blog/":
        return "0.8", "weekly"
    if url_path == "/case-studies/":
        return "0.8", "monthly"
    if url_path.startswith("/blog/"):
        return "0.7", "monthly"
    if url_path.startswith("/case-studies/"):
        return "0.7", "monthly"
    return "0.6", "monthly"


def collect_urls():
    urls = {}  # full_url -> (priority, changefreq)

    for html_file in sorted(Path(".").rglob("*.html")):
        if ".github" in html_file.parts:
            continue

        content = html_file.read_text(encoding="utf-8", errors="ignore")

        # Skip noindex pages
        if NOINDEX_PATTERN.search(content):
            continue

        # Get canonical URL
        canonical_match = CANONICAL_PATTERN.search(content)
        if canonical_match:
            canonical = canonical_match.group(1).rstrip("/")
            # Normalise trailing slash for index pages
            if canonical_match.group(1).endswith("/"):
                canonical += "/"
            if not canonical.startswith(BASE_URL):
                continue
            url_path = canonical[len(BASE_URL):] or "/"
        else:
            # Construct path from file location
            parts = html_file.parts
            if parts[0] == ".":
                parts = parts[1:]
            path = "/".join(parts)
            if path == "index.html":
                url_path = "/"
            elif path.endswith("/index.html"):
                url_path = "/" + path[: -len("index.html")]
            else:
                url_path = "/" + path

        full_url = BASE_URL + url_path

        # Deduplicate — canonical URL wins; skip if already seen
        if full_url not in urls:
            priority, changefreq = get_priority_and_freq(url_path)
            urls[full_url] = (priority, changefreq)

    return urls


def sort_key(url):
    path = url[len(BASE_URL):]
    fixed = {"/": 0, "/about.html": 1, "/vault.html": 2,
             "/case-studies/": 3, "/blog/": 4}
    if path in fixed:
        return (fixed[path], path)
    if path.startswith("/case-studies/"):
        return (5, path)
    if path.startswith("/blog/"):
        return (6, path)
    return (7, path)


def generate_sitemap(urls):
    sections = {"Core pages": [], "Case studies": [], "Blog": []}

    for url in sorted(urls, key=sort_key):
        path = url[len(BASE_URL):]
        priority, changefreq = urls[url]
        entry = (
            f"  <url>\n"
            f"    <loc>{url}</loc>\n"
            f"    <changefreq>{changefreq}</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            f"  </url>"
        )
        if path.startswith("/case-studies"):
            sections["Case studies"].append(entry)
        elif path.startswith("/blog"):
            sections["Blog"].append(entry)
        else:
            sections["Core pages"].append(entry)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        "",
    ]
    for section, entries in sections.items():
        if entries:
            lines.append(f"  <!-- {section} -->")
            lines.extend(entries)
            lines.append("")
    lines.append("</urlset>")
    lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    urls = collect_urls()
    sitemap = generate_sitemap(urls)

    with open("sitemap.xml", "w", encoding="utf-8", newline="\n") as f:
        f.write(sitemap)

    print(f"Generated sitemap.xml — {len(urls)} URLs:")
    for url in sorted(urls, key=sort_key):
        print(f"  {url}")
