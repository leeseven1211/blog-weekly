#!/usr/bin/env python3
"""Check that markdown image URLs resolve to usable image responses."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
ISSUES_DIR = ROOT / "docs" / "issues"


def latest_issue_file() -> Path:
    candidates = sorted(ISSUES_DIR.glob("issue-*.md"))
    if not candidates:
        raise FileNotFoundError(f"未找到 issue 文件：{ISSUES_DIR}")
    return candidates[-1]


def extract_image_urls(markdown: str) -> list[str]:
    return re.findall(r"!\[[^\]]*\]\(([^)\s]+)", markdown)


def check_remote_image(url: str, timeout: float) -> str | None:
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; blog-weekly-publish-check/1.0)",
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        },
        method="GET",
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            status = getattr(resp, "status", 200)
            ctype = (resp.headers.get("content-type") or "").lower()
            # Read a little to catch empty/HTML placeholder responses behind 200.
            sample = resp.read(256)
    except HTTPError as exc:
        return f"HTTP {exc.code}"
    except URLError as exc:
        return f"请求失败：{exc.reason}"
    except TimeoutError:
        return "请求超时"
    except Exception as exc:
        return f"请求异常：{exc}"

    if status >= 400:
        return f"HTTP {status}"
    if ctype and not (ctype.startswith("image/") or "octet-stream" in ctype):
        return f"Content-Type 不是图片：{ctype}"
    if not sample:
        return "响应为空"
    if sample.lstrip().lower().startswith((b"<!doctype html", b"<html")) and "image/svg" not in ctype:
        return "返回 HTML，不是图片资源"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="检查周刊图片 URL 是否能实际加载")
    parser.add_argument("--file", type=Path, help="指定 issue 文件")
    parser.add_argument("--latest", action="store_true", help="显式检查最新一期（默认行为）")
    parser.add_argument("--timeout", type=float, default=8.0, help="单张远程图片超时秒数")
    args = parser.parse_args()

    issue_file = args.file or latest_issue_file()
    text = issue_file.read_text(encoding="utf-8")
    errors: list[str] = []

    for url in extract_image_urls(text):
        parsed = urlparse(url)
        if parsed.scheme in {"http", "https"}:
            err = check_remote_image(url, args.timeout)
            if err:
                errors.append(f"远程图片不可用：{url}（{err}）")
            continue

        if url.startswith("/"):
            local = ROOT / "docs" / "public" / url.lstrip("/")
            if not local.exists():
                errors.append(f"本地图片不存在：{url}")

    if errors:
        print(f"❌ 图片 URL 检查未通过：{issue_file}")
        for err in errors:
            print(err)
        return 1

    print(f"✅ 图片 URL 检查通过：{issue_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
