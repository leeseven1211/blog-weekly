#!/usr/bin/env python3
"""Fetch and localize every image referenced by an issue.

Why this exists: the weekly generator used to write image paths first and only
download a few of them, so `npm run docs:build` failed the same way every week.
This script makes asset preparation deterministic:

  * every referenced local image must exist on disk afterwards;
  * the same file may not be referenced twice (later slots get a new filename);
  * images are downloaded from Wikimedia/Wikipedia or an explicit URL, verified
    with Pillow, and recorded in notes/issue-NNN-image-sources.md.

Usage:
  python3 scripts/fetch-issue-images.py --issue 034
  python3 scripts/fetch-issue-images.py --latest --dry-run
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ISSUES_DIR = ROOT / "docs" / "issues"
PUBLIC_DIR = ROOT / "docs" / "public"
NOTES_DIR = ROOT / "notes"
UA = "blog-weekly-image-bot/1.0 (https://blog.leeseven.com; contact: leeseven1211@gmail.com)"
MIN_WIDTH = 900
MIN_HEIGHT = 400
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\((/images/issues/\d+/[^)\s]+)\)")


def latest_issue() -> Path:
    return sorted(ISSUES_DIR.glob("issue-*.md"))[-1]


def issue_number(path: Path) -> str:
    return re.search(r"issue-(\d+)", path.name).group(1)


def api_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def commons_search(query: str, limit: int = 8) -> list[dict]:
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {query}",
        "gsrnamespace": "6",
        "gsrlimit": str(limit),
        "prop": "imageinfo",
        "iiprop": "url|size|mime",
        "iiurlwidth": "1600",
    }
    data = api_get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params))
    pages = (data.get("query") or {}).get("pages") or {}
    out = []
    for page in pages.values():
        info = (page.get("imageinfo") or [{}])[0]
        if info.get("mime") not in ("image/jpeg", "image/png"):
            continue
        if (info.get("width") or 0) < MIN_WIDTH:
            continue
        out.append({
            "url": info.get("thumburl") or info.get("url"),
            "width": info.get("width"),
            "height": info.get("height"),
            "title": page.get("title"),
            "index": page.get("index", 99),
        })
    out.sort(key=lambda x: x["index"])
    return out


def wiki_page_image(title: str, lang: str) -> dict | None:
    params = {
        "action": "query",
        "format": "json",
        "prop": "pageimages",
        "piprop": "original|thumbnail",
        "pithumbsize": "1600",
        "redirects": "1",
        "titles": title,
    }
    data = api_get(f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params))
    pages = (data.get("query") or {}).get("pages") or {}
    for page in pages.values():
        if page.get("missing"):
            continue
        thumb = (page.get("thumbnail") or {}).get("source")
        original = (page.get("original") or {}).get("source")
        url = thumb or original
        if url:
            return {"url": url, "title": page.get("title")}
    return None


def wiki_search_title(query: str, lang: str) -> str | None:
    params = {"action": "query", "format": "json", "list": "search", "srlimit": "1", "srsearch": query}
    data = api_get(f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params))
    hits = (data.get("query") or {}).get("search") or []
    return hits[0]["title"] if hits else None


def resolve(spec: str, alt: str) -> tuple[bytes, str, str]:
    """Return (bytes, source_url, method) for a mapping spec or fallback query."""
    kind, _, value = spec.partition(":") if ":" in spec else ("commons", "", spec)

    if kind == "url":
        return download(value), value, "direct URL"

    if kind == "wiki":
        for lang in ("zh", "en"):
            page = wiki_page_image(value, lang)
            if page:
                return download(page["url"]), page["url"], f"{lang}.wikipedia page image"

    query = value if kind == "commons" and value else spec
    candidates = commons_search(query)
    if not candidates and alt:
        candidates = commons_search(alt)
    if not candidates and query != alt:
        candidates = commons_search(f"{query} {alt}")
    if not candidates:
        raise RuntimeError(f"no image found for query: {query!r}")

    best = candidates[0]
    return download(best["url"]), best["url"], f"Wikimedia Commons: {best['title']}"


def normalize_image(data: bytes, target: Path) -> None:
    img = Image.open(io.BytesIO(data))
    img.load()
    if img.width < MIN_WIDTH or img.height < MIN_HEIGHT:
        raise RuntimeError(f"image too small: {img.width}x{img.height}")
    if target.suffix.lower() in (".jpg", ".jpeg"):
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")
        elif img.mode == "L":
            img = img.convert("RGB")
        img.save(target, "JPEG", quality=88, optimize=True)
    else:
        img.save(target)


def unique_name(path: Path, taken: set[str], counter: int) -> Path:
    candidate = path.with_name(f"{path.stem}-{counter}{path.suffix}")
    while candidate.name in taken or candidate.exists():
        counter += 1
        candidate = path.with_name(f"{path.stem}-{counter}{path.suffix}")
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue")
    parser.add_argument("--latest", action="store_true")
    parser.add_argument("--mapping")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    issue_file = latest_issue() if args.latest or not args.issue else ISSUES_DIR / f"issue-{args.issue.zfill(3)}.md"
    number = issue_number(issue_file)
    text = issue_file.read_text(encoding="utf-8")
    mapping: dict[str, str] = {}
    if args.mapping:
        mapping = json.loads(Path(args.mapping).read_text(encoding="utf-8"))

    matches = list(IMAGE_RE.finditer(text))
    seen: dict[str, int] = {}
    slots: list[dict] = []
    taken: set[str] = {m.group(2).rsplit("/", 1)[-1] for m in matches}

    for match in matches:
        alt, url = match.group(1), match.group(2)
        base = url.rsplit("/", 1)[-1]
        seen[base] = seen.get(base, 0) + 1
        if seen[base] > 1:
            new_path = unique_name(Path(url), taken, seen[base])
            taken.add(new_path.name)
            new_url = f"/images/issues/{number}/{new_path.name}"
            text = text[:match.start(2)] + new_url + text[match.end(2):]
            url = new_url
        slots.append({"alt": alt, "url": url, "file": url.rsplit("/", 1)[-1]})

    changed = text != issue_file.read_text(encoding="utf-8")
    if changed and not args.dry_run:
        issue_file.write_text(text, encoding="utf-8")

    sources: list[str] = []
    failures: list[str] = []
    for slot in slots:
        target = PUBLIC_DIR / slot["url"].lstrip("/")
        if target.exists() and target.stat().st_size > 20_000:
            continue
        spec = mapping.get(slot["file"]) or mapping.get(slot["alt"]) or f"commons:{slot['alt']}"
        if args.dry_run:
            print(f"[dry-run] {slot['file']} <- {spec}")
            continue
        try:
            data, source_url, method = resolve(spec, slot["alt"])
            target.parent.mkdir(parents=True, exist_ok=True)
            normalize_image(data, target)
            sources.append(f"- `{slot['file']}` — {method} — {source_url}")
            print(f"ok   {slot['file']}  ({method})")
        except Exception as exc:  # noqa: BLE001 - report and continue
            failures.append(f"{slot['file']}: {exc}")
            print(f"FAIL {slot['file']}: {exc}", file=sys.stderr)

    if sources and not args.dry_run:
        NOTES_DIR.mkdir(exist_ok=True)
        note = NOTES_DIR / f"issue-{number}-image-sources.md"
        existing = note.read_text(encoding="utf-8") if note.exists() else f"# 第 {number} 期图片来源\n\n"
        if existing and not existing.endswith("\n"):
            existing += "\n"
        note.write_text(existing + "\n".join(sources) + "\n", encoding="utf-8")

    if failures:
        print(f"\n{len(failures)} image(s) still missing:", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1
    print(f"\nall {len(slots)} image slots satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
