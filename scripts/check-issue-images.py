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


def main() -> int:
    parser = argparse.ArgumentParser(description="检查最新一期周刊的配图完整性")
    parser.add_argument("--file", type=Path, help="指定要检查的 issue 文件")
    parser.add_argument("--latest", action="store_true", help="显式检查最新一期（默认行为）")
    args = parser.parse_args()

    issue_file = args.file or latest_issue_file()
    text = issue_file.read_text(encoding="utf-8")

    errors: list[str] = []
    errors.extend(validate_single_image_section(text, "封面图"))
    errors.extend(validate_repeat_blocks(
        text,
        "科技与 AI 动态",
        [re.compile(r"^\*\*\d+\.\s"), re.compile(r"^###\s*\d+[\).]\s")],
    ))
    errors.extend(validate_repeat_blocks(
        text,
        "开源工具",
        [re.compile(r"^\*\*\["), re.compile(r"^###\s*\d+[\).]\s")],
    ))
    errors.extend(validate_single_image_section(text, "本周一图"))

    if errors:
        print(f"❌ 配图检查未通过：{issue_file}")
        for err in errors:
            print(err)
        return 1

    print(f"✅ 配图检查通过：{issue_file}")
    print("已确认：封面图 / 科技与 AI 动态 / 开源工具 / 本周一图 均有配图。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
