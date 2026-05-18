#!/usr/bin/env python3
"""Require an explicit visual publish review before pushing a weekly issue."""
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUES_DIR = ROOT / "docs" / "issues"
DEFAULT_REVIEW_DIR = Path(os.environ.get(
    "BLOG_WEEKLY_REVIEW_DIR",
    "/home/ubuntu/.openclaw/workspace/notes/blog-weekly/publish-reviews",
))


def latest_issue_file() -> Path:
    candidates = sorted(ISSUES_DIR.glob("issue-*.md"))
    if not candidates:
        raise FileNotFoundError(f"未找到 issue 文件：{ISSUES_DIR}")
    return candidates[-1]


def issue_number(issue_file: Path) -> str:
    match = re.search(r"issue-(\d+)", issue_file.name)
    if not match:
        raise ValueError(f"无法识别期号：{issue_file}")
    return match.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description="检查发布前视觉评审记录")
    parser.add_argument("--file", type=Path, help="指定 issue 文件")
    parser.add_argument("--latest", action="store_true", help="显式检查最新一期（默认行为）")
    parser.add_argument("--review-dir", type=Path, default=DEFAULT_REVIEW_DIR, help="评审记录目录")
    args = parser.parse_args()

    issue_file = args.file or latest_issue_file()
    number = issue_number(issue_file)
    review_file = args.review_dir / f"issue-{number}.md"

    if not review_file.exists():
        print(f"❌ 缺少发布前视觉评审记录：{review_file}")
        print("必须先本地预览并保存截图，逐栏确认图片显示/语义/质量/重复问题，再写评审记录。")
        return 1

    text = review_file.read_text(encoding="utf-8")
    required_patterns = {
        "publish: approved": r"(?im)^publish:\s*approved\s*$",
        "visual-review: pass": r"(?im)^visual-review:\s*pass\s*$",
        "image-display: pass": r"(?im)^image-display:\s*pass\s*$",
        "image-semantics: pass": r"(?im)^image-semantics:\s*pass\s*$",
        "image-duplicates: pass": r"(?im)^image-duplicates:\s*pass\s*$",
        "image-quality: pass": r"(?im)^image-quality:\s*pass\s*$",
    }
    missing = [label for label, pattern in required_patterns.items() if not re.search(pattern, text)]

    screenshot_lines = re.findall(r"(?im)^\s*-\s+.+\.(?:png|jpg|jpeg|webp)\s*$", text)
    if len(screenshot_lines) < 3:
        missing.append("至少 3 张预览截图路径（顶部/中段/底部或等效分段）")

    if missing:
        print(f"❌ 发布前视觉评审未通过：{review_file}")
        for item in missing:
            print(f"- 缺少或未通过：{item}")
        return 1

    print(f"✅ 发布前视觉评审通过：{review_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
