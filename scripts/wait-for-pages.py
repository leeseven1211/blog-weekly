#!/usr/bin/env python3
"""Wait for the GitHub Pages deployment of a pushed commit, then verify the live page.

The old publish check curled the public URL immediately after push. GitHub Pages
usually needs 40-90 seconds after the workflow starts, so that check produced
false 404s. This script waits for the actual deploy runs and then polls the
public endpoints with cache busting.

Usage:
  python3 scripts/wait-for-pages.py --issue 036
  python3 scripts/wait-for-pages.py --issue 036 --sha <commit>
  python3 scripts/wait-for-pages.py --issue 036 --skip-ci   # only HTTP wait
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

DEPLOY_WORKFLOW = "Deploy VitePress to GitHub Pages"
PAGES_WORKFLOW = "pages build and deployment"
DEFAULT_BASE = "https://blog.leeseven.com"


def log(message: str) -> None:
    print(message, flush=True)


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def git_head() -> str:
    result = run(["git", "rev-parse", "HEAD"])
    if result.returncode != 0:
        raise SystemExit(f"git rev-parse failed: {result.stderr.strip()}")
    return result.stdout.strip()


def gh_json(args: list[str]) -> list[dict]:
    result = run(["gh", *args])
    if result.returncode != 0:
        raise SystemExit(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return json.loads(result.stdout or "[]")


def list_runs() -> list[dict]:
    fields = "databaseId,workflowName,status,conclusion,headSha,headBranch,createdAt,url"
    return gh_json(["run", "list", "--limit", "40", "--json", fields])


def run_status(run_id: int) -> dict:
    fields = "databaseId,workflowName,status,conclusion,createdAt,url"
    rows = gh_json(["run", "view", str(run_id), "--json", fields])
    return rows[0] if isinstance(rows, list) and rows else rows


def wait_run(run: dict, timeout: float, label: str) -> dict:
    deadline = time.monotonic() + timeout
    started = time.monotonic()
    last = None
    while time.monotonic() < deadline:
        current = run_status(run["databaseId"])
        state = f"{current.get('status')}/{current.get('conclusion') or '-'}"
        if state != last:
            log(f"  {label}: {state}")
            last = state
        if current.get("status") == "completed":
            elapsed = time.monotonic() - started
            log(f"  {label}: {current.get('conclusion')} in {elapsed:.0f}s ({current.get('url')})")
            return current
        time.sleep(5)
    raise SystemExit(f"TIMEOUT: {label} did not finish within {timeout:.0f}s")


def http_get(url: str) -> tuple[int, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "blog-weekly-deploy-check/1.0",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return response.status, response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as error:
        return error.code, ""
    except Exception:
        return 0, ""


def wait_http(url: str, marker: str, timeout: float, label: str) -> str:
    deadline = time.monotonic() + timeout
    attempt = 0
    last_code = None
    while time.monotonic() < deadline:
        attempt += 1
        bust = f"{url}{'&' if '?' in url else '?'}deploy-check={int(time.time())}"
        code, body = http_get(bust)
        ok = code == 200 and marker in body
        if code != last_code or ok:
            suffix = "ok" if ok else f"{code}, marker={marker in body}"
            log(f"  {label}: attempt {attempt} -> {suffix}")
            last_code = code
        if ok:
            log(f"  {label}: LIVE")
            return body
        time.sleep(5)
    raise SystemExit(f"TIMEOUT: {label} did not return 200 + expected content within {timeout:.0f}s")


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue", required=True, help="Issue number, e.g. 036")
    parser.add_argument("--base-url", default=DEFAULT_BASE)
    parser.add_argument("--sha", help="Commit SHA to verify (default: HEAD)")
    parser.add_argument("--skip-ci", action="store_true", help="Skip workflow waiting")
    parser.add_argument("--ci-timeout", type=float, default=600)
    parser.add_argument("--http-timeout", type=float, default=300)
    args = parser.parse_args()

    issue = args.issue.strip().lstrip("0") or "0"
    padded = f"{int(issue):03d}"
    sha = args.sha or git_head()
    started = time.monotonic()

    log(f"verify issue {padded} for {sha[:9]} ({args.base_url})")

    if not args.skip_ci:
        runs = list_runs()
        deploy = next(
            (row for row in runs if row.get("workflowName") == DEPLOY_WORKFLOW and row.get("headSha") == sha),
            None,
        )
        if not deploy:
            raise SystemExit(f"no '{DEPLOY_WORKFLOW}' run found for {sha}")

        log(f"deploy run {deploy['databaseId']}: {deploy.get('status')}/{deploy.get('conclusion') or '-'}")
        deploy_done = wait_run(deploy, args.ci_timeout, "deploy workflow")
        if deploy_done.get("conclusion") != "success":
            raise SystemExit(f"deploy workflow failed: {deploy_done.get('url')}")

        deploy_at = parse_time(deploy["createdAt"])
        pages = next(
            (
                row
                for row in runs
                if row.get("workflowName") == PAGES_WORKFLOW
                and parse_time(row["createdAt"]) >= deploy_at
            ),
            None,
        )
        if pages:
            log(f"pages run {pages['databaseId']}: {pages.get('status')}/{pages.get('conclusion') or '-'}")
            pages_done = wait_run(pages, args.ci_timeout, "pages deployment")
            if pages_done.get("conclusion") != "success":
                log("  pages deployment did not succeed; continuing with HTTP polling")
        else:
            log("  pages deployment run not listed yet; relying on HTTP polling")

    page_url = f"{args.base_url}/issues/issue-{padded}"
    html = wait_http(page_url, f"第 {padded} 期", args.http_timeout, "issue page")

    title = re.search(r"<title>(.*?)</title>", html, re.S)
    if title:
        log(f"  title: {title.group(1).strip()}")

    wait_http(f"{args.base_url}/feed.xml", f"issue-{padded}", args.http_timeout, "rss feed")

    cover = re.search(r'property="og:image"[^>]*content="([^"]+)"', html)
    if cover:
        image_url = cover.group(1)
        if image_url.startswith("/"):
            image_url = args.base_url + image_url
        code, _ = http_get(f"{image_url}?deploy-check={int(time.time())}")
        log(f"  cover image: {code} {image_url}")
        if code != 200:
            raise SystemExit("cover image is not 200")

    log(f"ALL GOOD in {time.monotonic() - started:.0f}s")


if __name__ == "__main__":
    main()
