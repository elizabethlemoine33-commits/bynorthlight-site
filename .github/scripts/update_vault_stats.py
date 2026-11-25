#!/usr/bin/env python3
"""Refresh _data/vault.yml from the public GitHub release data for Northlight Vault.

Counts the downloads GitHub records for every installer attached to a published release
(drafts and pre-releases are ignored), finds the latest published version, and writes the
numbers the Vault case study page reads (case-studies/northlight-vault.html).

GitHub counts downloads, not people: repeat downloads, re-installs and scanners all add to
the number. The page says so. No secrets are needed: the release data is public. A token is
used only if GITHUB_TOKEN is set, to avoid anonymous rate limits.

Run from the repo root:  python3 .github/scripts/update_vault_stats.py
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

REPO = "elizabethlemoine33-commits/Northlight-Vault"
OUT = "_data/vault.yml"
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def fetch_releases():
    releases, page = [], 1
    while True:
        url = f"https://api.github.com/repos/{REPO}/releases?per_page=100&page={page}"
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "bynorthlight-site-vault-stats",
        })
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=30) as resp:
            batch = json.load(resp)
        releases.extend(batch)
        if len(batch) < 100:
            return releases
        page += 1


def month_year(iso):
    d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return f"{MONTHS[d.month - 1]} {d.year}"


def main():
    releases = [r for r in fetch_releases() if not r.get("draft") and not r.get("prerelease")]
    if not releases:
        sys.exit("No published releases found; refusing to write zeros.")

    releases.sort(key=lambda r: r["published_at"])
    total = sum(a.get("download_count", 0) for r in releases for a in r.get("assets", []))
    latest = releases[-1]
    now = datetime.now(timezone.utc)

    lines = [
        "# Written by .github/scripts/update_vault_stats.py (monthly workflow). Do not edit by hand:",
        "# the next run overwrites it. Read by case-studies/northlight-vault.html.",
        f"downloads: {total}",
        f'as_of: "{MONTHS[now.month - 1]} {now.year}"',
        f'latest_version: "{latest["tag_name"].lstrip("v")}"',
        f'latest_released: "{month_year(latest["published_at"])}"',
        f"updates_since_launch: {len(releases) - 1}",
        "per_release:",
    ]
    for r in releases:
        count = sum(a.get("download_count", 0) for a in r.get("assets", []))
        lines.append(f'  - {{ version: "{r["tag_name"].lstrip("v")}", released: "{r["published_at"][:10]}", downloads: {count} }}')

    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {OUT}: {total} downloads, latest {latest['tag_name']}")


if __name__ == "__main__":
    main()
