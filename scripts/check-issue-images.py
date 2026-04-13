#!/usr/bin/env python3
"""检查周刊最新一期的配图完整性。

目标：在发布前直接拦住“封面/本周一图/科技与 AI 动态/开源工具”缺图的情况。
默认检查 docs/issues 下最新一期，也支持 --file 指定文件。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
ISSUES_DIR = ROOT / "docs" / "issues"


def latest_issue_file() -> Path:
    candidates = sorted(ISSUES_DIR.glob("issue-*.md"))
    if not candidates:
        raise FileNotFoundError(f"未找到 issue 文件：{ISSUES_DIR}")
    return candidates[-1]


def extract_section(text: str, title: str) -> str | None:
    pattern = re.compile(rf"^##\s+{re.escape(title)}\s*$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return None

    start = match.end()
    next_match = re.search(r"^##\s+", text[start:], re.MULTILINE)
    end = start + next_match.start() if next_match else len(text)
    return text[start:end].strip()


def split_blocks(section_text: str, start_patterns: Iterable[re.Pattern[str]]) -> list[str]:
    blocks: list[list[str]] = []
    current: list[str] | None = None

    for line in section_text.splitlines():
        if any(pattern.match(line) for pattern in start_patterns):
            if current:
                blocks.append(current)
            current = [line]
            continue

        if current is not None:
            current.append(line)

    if current:
        blocks.append(current)

    return ["\n".join(block).strip() for block in blocks]


def summarize_title(block: str) -> str:
    return block.splitlines()[0].strip()


def has_image(markdown: str) -> bool:
    return "![" in markdown


def extract_image_urls(markdown: str) -> list[str]:
    return re.findall(r"!\[[^\]]*\]\(([^)\s]+)", markdown)


def is_generic_stock_url(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return host in {"images.unsplash.com", "source.unsplash.com"}


def validate_single_image_section(text: str, section_title: str) -> list[str]:
    section = extract_section(text, section_title)
    if section is None:
        return [f"缺少章节：{section_title}"]
    if not has_image(section):
        return [f"{section_title} 缺少图片"]
    return []


def validate_repeat_blocks(
    text: str,
    section_title: str,
    start_patterns: Iterable[re.Pattern[str]],
) -> list[str]:
    section = extract_section(text, section_title)
    if section is None:
        return [f"缺少章节：{section_title}"]

    blocks = split_blocks(section, start_patterns)
    if not blocks:
        return [f"{section_title} 未识别出条目，检查格式是否变更"]

    missing = [summarize_title(block) for block in blocks if not has_image(block)]
    if not missing:
        return []

    errors = [f"{section_title} 有 {len(missing)}/{len(blocks)} 条缺图："]
    errors.extend([f"- {title}" for title in missing])
    return errors


def validate_no_generic_stock(
    text: str,
    section_title: str,
    start_patterns: Iterable[re.Pattern[str]],
) -> list[str]:
    section = extract_section(text, section_title)
    if section is None:
        return []

    blocks = split_blocks(section, start_patterns)
    if not blocks:
        return []

    offenders: list[str] = []
    for block in blocks:
        urls = extract_image_urls(block)
        if any(is_generic_stock_url(url) for url in urls):
            offenders.append(summarize_title(block))

    if not offenders:
        return []

    errors = [f"{section_title} 不应使用通用 stock 图（如 Unsplash），请改为事件相关图 / 官方素材 / 自制观点图："]
    errors.extend([f"- {title}" for title in offenders])
    return errors


def validate_issue_stock_budget(text: str, max_allowed: int = 1) -> list[str]:
    urls = extract_image_urls(text)
    generic_count = sum(1 for url in urls if is_generic_stock_url(url))
    if generic_count <= max_allowed:
        return []
    return [f"整期通用 stock 图过多：发现 {generic_count} 张，最多允许 {max_allowed} 张"]


def main() -> int:
    parser = argparse.ArgumentParser(description="检查最新一期周刊的配图完整性")
    parser.add_argument("--file", type=Path, help="指定要检查的 issue 文件")
    parser.add_argument("--latest", action="store_true", help="显式检查最新一期（默认行为）")
    args = parser.parse_args()

    issue_file = args.file or latest_issue_file()
    text = issue_file.read_text(encoding="utf-8")

    errors: list[str] = []
    errors.extend(validate_single_image_section(text, "封面图"))
    news_patterns = [re.compile(r"^\*\*\d+\.\s"), re.compile(r"^###\s*\d+[\).]\s")]
    tool_patterns = [re.compile(r"^\*\*\["), re.compile(r"^###\s*\d+[\).]\s")]

    errors.extend(validate_repeat_blocks(text, "科技与 AI 动态", news_patterns))
    errors.extend(validate_repeat_blocks(text, "开源工具", tool_patterns))
    errors.extend(validate_single_image_section(text, "本周一图"))
    errors.extend(validate_no_generic_stock(text, "科技与 AI 动态", news_patterns))
    errors.extend(validate_no_generic_stock(text, "开源工具", tool_patterns))
    errors.extend(validate_issue_stock_budget(text, max_allowed=1))

    if errors:
        print(f"❌ 配图检查未通过：{issue_file}")
        for err in errors:
            print(err)
        return 1

    print(f"✅ 配图检查通过：{issue_file}")
    print("已确认：封面图 / 科技与 AI 动态 / 开源工具 / 本周一图 均有配图，且科技动态/工具区未使用通用 stock 图。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
