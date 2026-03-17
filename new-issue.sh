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

# 用统一脚本更新侧边栏和归档（防重复、按 H1 自动取标题）
python3 "$SCRIPT_DIR/scripts/sync-issues-meta.py" --issue "$ISSUE_NUM" --date "$TODAY"
echo "✅ 已更新侧边栏和归档"

echo ""
echo "🎉 第 $ISSUE_NUM 期创建完毕！"
echo "   编辑：$ISSUE_FILE"
echo "   本地预览：npm run docs:dev"
echo "   发布：git add . && git commit -m 'feat: 第 $ISSUE_NUM 期' && git push"
