#!/usr/bin/env python3
"""检查周刊最新一期的配图完整性。

目标：在发布前直接拦住“封面/科技与 AI 动态/开源工具/世界之最”缺图的情况。
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


def issue_number(issue_file: Path) -> int | None:
    match = re.search(r"issue-(\d+)", issue_file.name)
    if not match:
        return None
    return int(match.group(1))


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


def extract_images(markdown: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[([^\]]*)\]\(([^)\s]+)", markdown)


def is_generic_stock_url(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return host in {"images.unsplash.com", "source.unsplash.com"}



def validate_optional_image_section(text: str, section_title: str) -> list[str]:
    section = extract_section(text, section_title)
    if section is None:
        return []
    if has_image(section):
        return []
    return [f"{section_title} 出现时必须配图"]

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




def extract_section_by_heading_prefix(text: str, heading_prefix: str) -> tuple[str, str] | None:
    pattern = re.compile(rf"^##\s+({re.escape(heading_prefix)}[^\n]*)$", re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return None

    title = match.group(1).strip()
    start = match.end()
    next_match = re.search(r"^##\s+", text[start:], re.MULTILINE)
    end = start + next_match.start() if next_match else len(text)
    return title, text[start:end].strip()


def validate_section_prefix_min_images(text: str, heading_prefix: str, min_count: int) -> list[str]:
    result = extract_section_by_heading_prefix(text, heading_prefix)
    if result is None:
        return [f"缺少章节：{heading_prefix}"]

    section_title, section = result
    urls = extract_image_urls(section)
    if len(urls) >= min_count:
        return []

    return [f"{section_title} 至少需要 {min_count} 张与文字匹配的配图，当前只有 {len(urls)} 张"]

def validate_no_duplicate_images(text: str) -> list[str]:
    urls = extract_image_urls(text)
    seen: dict[str, int] = {}
    duplicates: list[str] = []

    for url in urls:
        seen[url] = seen.get(url, 0) + 1
        if seen[url] == 2:
            duplicates.append(url)

    if not duplicates:
        return []

    errors = ["同一期不允许重复使用同一张图片："]
    errors.extend([f"- {url}（出现 {seen[url]} 次）" for url in duplicates])
    return errors


def validate_banned_sections(text: str) -> list[str]:
    """Block sections that have been retired from the public weekly format."""
    banned_patterns = [
        (re.compile(r"^##\s+.*Moltbook.*$", re.MULTILINE), "Moltbook 独立栏目已停用；相关内容只能自然融入正文，不允许单独成栏"),
    ]
    return [message for pattern, message in banned_patterns if pattern.search(text)]


def validate_issue_scoped_local_images(issue_file: Path, text: str) -> list[str]:
    """For new issues, prevent silently reusing old issue images as placeholders."""
    number = issue_number(issue_file)
    if number is None:
        return []

    current_prefix = f"/images/issues/{number:03d}/"
    errors: list[str] = []
    for url in extract_image_urls(text):
        if not url.startswith("/images/issues/"):
            continue
        if not url.startswith(current_prefix):
            errors.append(f"新一期不得复用旧期栏目图片：{url}（应使用 {current_prefix} 下的图片）")
        if url.lower().endswith(".svg"):
            errors.append(f"新一期正文图片不得使用 SVG 模板图：{url}，请改用真实素材截图/照片或必要的 PNG 解释图")
    return errors


def validate_issue_assets_are_referenced(issue_file: Path, text: str) -> list[str]:
    """Catch cases where new assets are generated but not wired into the issue."""
    number = issue_number(issue_file)
    if number is None:
        return []

    issue_image_dir = ROOT / "docs" / "public" / "images" / "issues" / f"{number:03d}"
    if not issue_image_dir.exists():
        return []

    referenced = {
        (ROOT / "docs" / "public" / url.lstrip("/")).resolve()
        for url in extract_image_urls(text)
        if url.startswith(f"/images/issues/{number:03d}/")
    }
    image_files = {
        path.resolve()
        for path in issue_image_dir.iterdir()
        if path.is_file() and path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}
    }
    unreferenced = sorted(path for path in image_files if path not in referenced)
    if not unreferenced:
        return []

    errors = ["本期图片目录存在未被正文引用的图片，可能是生成/组装链路断开："]
    errors.extend([f"- {path.relative_to(ROOT / 'docs' / 'public')}" for path in unreferenced])
    return errors


def heading_position(text: str, heading_options: Iterable[str]) -> int | None:
    positions: list[int] = []
    for title in heading_options:
        match = re.search(rf"^##\s+{re.escape(title)}\s*$", text, re.MULTILINE)
        if match:
            positions.append(match.start())
    return min(positions) if positions else None


def validate_section_order(text: str) -> list[str]:
    """Keep the public reading order aligned with the editorial spec."""
    news = heading_position(text, ["科技与 AI 动态", "科技与 AI 动态（上周）"])
    world = heading_position(text, ["世界之最"])
    tools = heading_position(text, ["开源工具", "工具深挖", "工具深挖（4-5 个）"])

    if news is None or world is None or tools is None:
        return []
    if news < world < tools:
        return []
    return ["栏目顺序错误：世界之最必须放在「科技与 AI 动态」后、「开源工具/工具深挖」前"]


def read_image_size(image_path: Path) -> tuple[int, int]:
    data = image_path.read_bytes()

    # PNG: 8-byte signature + IHDR width/height.
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        width = int.from_bytes(data[16:20], "big")
        height = int.from_bytes(data[20:24], "big")
        return width, height

    # JPEG: scan SOF markers.
    if data.startswith(b"\xff\xd8"):
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            while i < len(data) and data[i] == 0xFF:
                i += 1
            if i >= len(data):
                break
            marker = data[i]
            i += 1
            if marker in {0xD8, 0xD9, 0x01} or 0xD0 <= marker <= 0xD7:
                continue
            if i + 2 > len(data):
                break
            segment_length = int.from_bytes(data[i:i + 2], "big")
            if segment_length < 2 or i + segment_length > len(data):
                break
            if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
                if segment_length >= 7:
                    height = int.from_bytes(data[i + 3:i + 5], "big")
                    width = int.from_bytes(data[i + 5:i + 7], "big")
                    return width, height
            i += segment_length

    raise ValueError("unsupported or unreadable image format")

def validate_local_image_dimensions(issue_file: Path, text: str, min_width: int = 500, min_height: int = 250) -> list[str]:
    errors: list[str] = []

    for url in extract_image_urls(text):
        if not url.startswith("/images/"):
            continue

        image_path = ROOT / "docs" / "public" / url.lstrip("/")
        if not image_path.exists():
            errors.append(f"本地图片不存在：{url}")
            continue

        try:
            width, height = read_image_size(image_path)
        except Exception as exc:
            errors.append(f"无法读取图片尺寸：{url} ({exc})")
            continue

        if width < min_width or height < min_height:
            errors.append(f"图片尺寸过小：{url} ({width}x{height})，最低要求 {min_width}x{min_height}")

    return errors

def validate_world_records_section(text: str, issue_file: Path, min_count: int = 5) -> list[str]:
    number = issue_number(issue_file)
    # 第 014 期起强制；历史期数不因新增栏目规则而 retroactively 失败。
    if number is not None and number < 14:
        return []

    section = extract_section(text, "世界之最")
    if section is None:
        return ["第 014 期起必须包含栏目：世界之最"]

    item_patterns = [re.compile(r"^###\s*\d+[\).、.]?\s"), re.compile(r"^\*\*\d+[\).、.]?\s")]
    blocks = split_blocks(section, item_patterns)
    if len(blocks) < min_count:
        return [f"世界之最至少需要 {min_count} 个条目，当前只有 {len(blocks)} 个"]

    missing = [summarize_title(block) for block in blocks if not has_image(block)]
    if not missing:
        return []

    errors = [f"世界之最有 {len(missing)}/{len(blocks)} 条缺图："]
    errors.extend([f"- {title}" for title in missing])
    return errors


def validate_no_page_screenshot_labels(text: str) -> list[str]:
    """Catch page-screenshot labels in sections that must use real photos."""
    forbidden = re.compile(r"(截图|页面|资料页|网页)")
    errors: list[str] = []

    cover = extract_section(text, "封面图")
    if cover:
        offenders = [alt for alt, _url in extract_images(cover) if forbidden.search(alt)]
        if offenders:
            errors.append("封面图不得使用网页/资料页截图，请换成真实照片或高质量编辑图：")
            errors.extend([f"- {alt}" for alt in offenders])

    world = extract_section(text, "世界之最")
    if world:
        offenders = [alt for alt, _url in extract_images(world) if forbidden.search(alt)]
        if offenders:
            errors.append("世界之最不得使用百科/资料页截图，请换成每个对象的真实照片或官方图：")
            errors.extend([f"- {alt}" for alt in offenders])

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
    errors.extend(validate_world_records_section(text, issue_file, min_count=5))
    errors.extend(validate_optional_image_section(text, "意外推荐（非科技）"))
    errors.extend(validate_banned_sections(text))
    errors.extend(validate_no_generic_stock(text, "科技与 AI 动态", news_patterns))
    errors.extend(validate_no_generic_stock(text, "开源工具", tool_patterns))
    errors.extend(validate_issue_stock_budget(text, max_allowed=1))
    errors.extend(validate_no_duplicate_images(text))
    errors.extend(validate_issue_scoped_local_images(issue_file, text))
    errors.extend(validate_issue_assets_are_referenced(issue_file, text))
    errors.extend(validate_section_order(text))
    errors.extend(validate_local_image_dimensions(issue_file, text, min_width=500, min_height=250))
    errors.extend(validate_no_page_screenshot_labels(text))

    if errors:
        print(f"❌ 配图检查未通过：{issue_file}")
        for err in errors:
            print(err)
        return 1

    print(f"✅ 配图检查通过：{issue_file}")
    print("已确认：封面图 / 科技与 AI 动态 / 开源工具均有配图；第014期起世界之最至少5条且逐条配图；意外推荐出现时也有配图；无 Moltbook 独立栏目；新一期未复用旧期栏目图、未引用 SVG 模板图、无未接入的新期图片；世界之最位于科技动态后、工具区前；科技动态/工具区未使用通用 stock 图；同一期没有重复图片；本地图片尺寸不低于 500x250；封面图/世界之最未用文字标注为网页或资料页截图。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
