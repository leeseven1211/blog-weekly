#!/usr/bin/env python3
"""List world-record subjects already used and suggest unused ones.

Run this before writing the 世界之最 section:

    python3 scripts/list-world-records.py

The checker `check-issue-images.py` rejects a new issue that repeats an earlier
subject. This helper makes the constraint visible before writing, instead of
discovering it at build time.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ISSUES_DIR = ROOT / "docs" / "issues"

POOL = [
    ("世界最大的水族馆之一：乔治亚水族馆", "Georgia Aquarium"),
    ("世界最大的天文馆之一：上海天文馆", "Shanghai Astronomy Museum"),
    ("世界最大的风洞之一：NASA Ames 80x120 风洞", "NASA Ames 80 by 120 Foot Wind Tunnel"),
    ("世界最大的室内滑雪场之一：迪拜滑雪场", "Ski Dubai"),
    ("世界最大的隧道掘进机之一：Bertha", "Bertha tunnel boring machine Seattle"),
    ("世界面积最大的机场之一：法赫德国王国际机场", "King Fahd International Airport"),
    ("世界最大的火车站之一：纽约大中央车站", "Grand Central Terminal"),
    ("世界参观人数最多的博物馆：卢浮宫", "Louvre pyramid"),
    ("世界最高的酒店之一：Gevora Hotel", "Gevora Hotel"),
    ("世界最大的球形建筑：拉斯维加斯 Sphere", "Sphere Las Vegas"),
    ("世界最大的海水淡化厂之一：Ras Al Khair", "Ras Al Khair desalination plant"),
    ("世界最大的室内卡丁车场之一", "indoor karting track"),
]


def section(text: str) -> str | None:
    match = re.search(r"^##\s+世界之最\s*$", text, re.MULTILINE)
    if not match:
        return None
    start = match.end()
    nxt = re.search(r"^##\s+", text[start:], re.MULTILINE)
    return text[start:start + nxt.start()] if nxt else text[start:]


def headings(text: str) -> list[str]:
    body = section(text)
    if not body:
        return []
    return [h.strip() for h in re.findall(r"^###\s+(.+)$", body, re.MULTILINE)]


def norm(title: str) -> str:
    title = re.sub(r"^\d+[\).、.]?\s*", "", title)
    title = title.split("：", 1)[-1]
    title = re.sub(r"[\s\[\]【】()（）,，、:：;；/／\-—_·.。]+", "", title).lower()
    for term in ("世界", "全球", "之一", "工程", "项目", "系统", "建筑", "设施"):
        title = title.replace(term, "")
    return title


def main() -> None:
    used: dict[str, str] = {}
    for path in sorted(ISSUES_DIR.glob("issue-*.md")):
        for heading in headings(path.read_text(encoding="utf-8")):
            used.setdefault(norm(heading), f"{path.name}: {heading}")

    print("已用过的世界之最对象：")
    for key in sorted(used):
        print(f"  - {used[key]}")

    print("\n可用的新选题（未被往期使用）：")
    for title, query in POOL:
        if norm(title) in used:
            continue
        print(f"  - {title}\n    commons 查询：{query}")


if __name__ == "__main__":
    main()
