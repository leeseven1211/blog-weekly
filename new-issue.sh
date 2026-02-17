#!/bin/bash
# new-issue.sh - 一键创建新一期周刊
# 用法: ./new-issue.sh [期号]
# 例如: ./new-issue.sh 003

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ISSUES_DIR="$SCRIPT_DIR/docs/issues"
CONFIG_FILE="$SCRIPT_DIR/docs/.vitepress/config.ts"
ARCHIVE_FILE="$SCRIPT_DIR/docs/archive.md"

# 自动推算下一期期号
if [ -n "${1:-}" ]; then
  ISSUE_NUM=$(printf "%03d" "$1")
else
  LAST=$(ls "$ISSUES_DIR"/issue-*.md 2>/dev/null | sort | tail -1 || true)
  if [ -z "$LAST" ]; then
    ISSUE_NUM="001"
  else
    LAST_NUM=$(basename "$LAST" | sed 's/issue-\([0-9]*\)\.md/\1/')
    ISSUE_NUM=$(printf "%03d" $((10#$LAST_NUM + 1)))
  fi
fi

ISSUE_FILE="$ISSUES_DIR/issue-$ISSUE_NUM.md"
TODAY=$(date +%Y-%m-%d)

# 检查是否已存在
if [ -f "$ISSUE_FILE" ]; then
  echo "⚠️  第 $ISSUE_NUM 期已存在：$ISSUE_FILE"
  exit 1
fi

# 创建 Markdown 模板
cat > "$ISSUE_FILE" << EOF
# 第 $ISSUE_NUM 期（$TODAY）

> 每周一期，记录有趣的技术与世界。

---

## 封面图

<!-- 替换为本期封面图链接 -->
<!-- ![封面](https://your-image-url.jpg) -->

---

## 文章推荐

**标题一**（[链接](#)）：一两句介绍这篇文章讲了什么，为什么值得读。

**标题二**（[链接](#)）：一两句介绍这篇文章讲了什么，为什么值得读。

---

## 工具推荐

**工具名称**（[链接](#)）：这个工具解决什么问题，适合什么场景。

**工具名称**（[链接](#)）：这个工具解决什么问题，适合什么场景。

---

## 有趣的项目

**项目名称**（[GitHub](#)）：项目简介，star 数，为什么有意思。

**项目名称**（[GitHub](#)）：项目简介，star 数，为什么有意思。

---

## 本周图片 / 冷知识

<!-- 一张图或一句有意思的冷知识 -->

---

## 碎碎念

<!-- 本周的一点个人想法 -->
EOF

echo "✅ 已创建：$ISSUE_FILE"

# 用 Python 统一更新侧边栏和归档（防重复、排序稳定）
python3 - "$CONFIG_FILE" "$ARCHIVE_FILE" "$ISSUE_NUM" "$TODAY" << 'PYEOF'
import re
import sys
from pathlib import Path

config_path = Path(sys.argv[1])
archive_path = Path(sys.argv[2])
issue_num = sys.argv[3]
today = sys.argv[4]

# ------------------------------
# 更新 config.ts 侧边栏（按期号倒序、去重）
# ------------------------------
config = config_path.read_text(encoding='utf-8')

entry_pattern = re.compile(
    r"\{\s*text:\s*'([^']+)'\s*,\s*link:\s*'/issues/issue-(\d{3})'\s*\}"
)

entries = []
for m in entry_pattern.finditer(config):
    text, num = m.group(1), m.group(2)
    entries.append((num, text))

# 补入新一期（如果不存在）
if not any(num == issue_num for num, _ in entries):
    entries.append((issue_num, f"第 {issue_num} 期 - {today}"))

# 去重：同一期号只保留一条，优先保留“更有信息量”的 text
dedup = {}
for num, text in entries:
    if num not in dedup:
        dedup[num] = text
    else:
        # 优先保留更长描述（通常包含标题而非仅日期）
        if len(text) > len(dedup[num]):
            dedup[num] = text

sorted_entries = sorted(dedup.items(), key=lambda x: int(x[0]), reverse=True)
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

config_path.write_text(config_new, encoding='utf-8')

# ------------------------------
# 更新 archive.md（按期号倒序、去重）
# ------------------------------
archive = archive_path.read_text(encoding='utf-8') if archive_path.exists() else "# 归档\n\n"

line_pattern = re.compile(
    r"- \[第\s*(\d{3})\s*期(?:[^\]]*)\]\(/issues/issue-(\d{3})\)（(\d{4}-\d{2}-\d{2})）"
)

records = {}
for m in line_pattern.finditer(archive):
    n1, n2, date = m.groups()
    if n1 != n2:
        continue
    records[n1] = date

records[issue_num] = today

sorted_records = sorted(records.items(), key=lambda x: int(x[0]), reverse=True)

header = "# 归档\n\n这里是「小七的周刊」所有期数的归档。\n\n## 2026 年\n\n"
lines = [f"- [第 {num} 期](/issues/issue-{num})（{date}）" for num, date in sorted_records]
archive_new = header + "\n".join(lines) + "\n"
archive_path.write_text(archive_new, encoding='utf-8')

print(f"✅ 已更新侧边栏：第 {issue_num} 期（自动去重）")
print(f"✅ 已更新归档页：第 {issue_num} 期（按期号倒序）")
PYEOF

echo ""
echo "🎉 第 $ISSUE_NUM 期创建完毕！"
echo "   编辑：$ISSUE_FILE"
echo "   本地预览：npm run docs:dev"
echo "   发布：git add . && git commit -m 'feat: 第 $ISSUE_NUM 期' && git push"
