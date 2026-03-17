#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Sync sidebar + archive from docs/issues")
    parser.add_argument("--issue", help="Issue number like 006 to force date in archive")
    parser.add_argument("--date", help="Date like 2026-03-17 used with --issue")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    config_path = root / "docs/.vitepress/config.ts"
    archive_path = root / "docs/archive.md"
    issues_dir = root / "docs/issues"

    config = config_path.read_text(encoding="utf-8")
    archive = archive_path.read_text(encoding="utf-8") if archive_path.exists() else "# 归档\n\n"

    issue_files = sorted(issues_dir.glob("issue-*.md"))
    entries = []

    for fp in issue_files:
        mnum = re.search(r"issue-(\d{3})\.md$", fp.name)
        if not mnum:
            continue
        num = mnum.group(1)
        body = fp.read_text(encoding="utf-8", errors="ignore")

        mh1 = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        mtitle = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', body, re.MULTILINE)
        raw_title = mh1.group(1).strip() if mh1 else (mtitle.group(1).strip() if mtitle else f"第 {num} 期")
        text = raw_title.replace("'", "\\'")

        entries.append((num, text))

    sorted_entries = sorted(entries, key=lambda x: int(x[0]), reverse=True)
    new_items_block = "\n".join(
        [f"          {{ text: '{text}', link: '/issues/issue-{num}' }}," for num, text in sorted_entries]
    )

    config_new, changed = re.subn(
        r"(items:\s*\[\n)([\s\S]*?)(\n\s*\],)",
        lambda m: m.group(1) + new_items_block + m.group(3),
        config,
        count=1,
    )
    if changed == 0:
        raise SystemExit("❌ 未找到 sidebar items 区块，无法更新 config.ts")

    config_path.write_text(config_new, encoding="utf-8")

    line_pattern = re.compile(
        r"- \[第\s*(\d{3})\s*期(?:[^\]]*)\]\(/issues/issue-(\d{3})\)（(\d{4}-\d{2}-\d{2})）"
    )
    records = {}
    for m in line_pattern.finditer(archive):
        n1, n2, date = m.groups()
        if n1 == n2:
            records[n1] = date

    # Ensure every issue has a date entry; keep existing dates if present
    for num, _ in sorted_entries:
        if num not in records:
            records[num] = "1970-01-01"

    if args.issue and args.date:
        records[args.issue] = args.date

    sorted_records = sorted(records.items(), key=lambda x: int(x[0]), reverse=True)
    header = "# 归档\n\n这里是「小七的周刊」所有期数的归档。\n\n## 2026 年\n\n"
    lines = [f"- [第 {num} 期](/issues/issue-{num})（{date}）" for num, date in sorted_records]
    archive_new = header + "\n".join(lines) + "\n"
    archive_path.write_text(archive_new, encoding="utf-8")

    print("✅ Sidebar & archive synced")


if __name__ == "__main__":
    main()
