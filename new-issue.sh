#!/bin/bash
# new-issue.sh - 一键创建新一期周刊
# 用法: ./new-issue.sh [期号]
# 例如: ./new-issue.sh 002

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ISSUES_DIR="$SCRIPT_DIR/docs/issues"
CONFIG_FILE="$SCRIPT_DIR/docs/.vitepress/config.ts"

# 自动推算下一期期号
if [ -n "$1" ]; then
  ISSUE_NUM=$(printf "%03d" "$1")
else
  LAST=$(ls "$ISSUES_DIR"/issue-*.md 2>/dev/null | sort | tail -1)
  if [ -z "$LAST" ]; then
    ISSUE_NUM="001"
  else
    LAST_NUM=$(basename "$LAST" | sed 's/issue-\([0-9]*\)\.md/\1/')
    ISSUE_NUM=$(printf "%03d" $((10#$LAST_NUM + 1)))
  fi
fi

ISSUE_FILE="$ISSUES_DIR/issue-$ISSUE_NUM.md"
TODAY=$(date +%Y-%m-%d)
YEAR=$(date +%Y)

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

# 更新 config.ts 侧边栏
SIDEBAR_ENTRY="          { text: '第 $ISSUE_NUM 期 - $TODAY', link: '/issues/issue-$ISSUE_NUM' },"

# 在侧边栏 items 数组第一行插入（最新期显示在最上面）
sed -i "s|          { text: '第 001 期|          { text: '第 $ISSUE_NUM 期 - $TODAY', link: '/issues/issue-$ISSUE_NUM' },\n          { text: '第 001 期|" "$CONFIG_FILE" 2>/dev/null || true

# 如果是 001 期之后的，用通用方式插入
if [ "$ISSUE_NUM" != "001" ]; then
  # 找到 items: [ 行，在其后插入新条目
  python3 - "$CONFIG_FILE" "$ISSUE_NUM" "$TODAY" << 'PYEOF'
import sys, re

config_file = sys.argv[1]
issue_num = sys.argv[2]
today = sys.argv[3]

with open(config_file, 'r') as f:
    content = f.read()

new_entry = f"          {{ text: '第 {issue_num} 期 - {today}', link: '/issues/issue-{issue_num}' }},\n"

# 在 items: [ 后面插入
content = re.sub(
    r'(items:\s*\[\n)',
    r'\1' + new_entry,
    content,
    count=1
)

with open(config_file, 'w') as f:
    f.write(content)

print(f"✅ 已更新侧边栏：第 {issue_num} 期")
PYEOF
fi

# 更新 archive.md
ARCHIVE_FILE="$SCRIPT_DIR/docs/archive.md"
if [ -f "$ARCHIVE_FILE" ]; then
  # 在文件末尾追加
  echo "" >> "$ARCHIVE_FILE"
  echo "- [第 $ISSUE_NUM 期](/issues/issue-$ISSUE_NUM)（$TODAY）" >> "$ARCHIVE_FILE"
  echo "✅ 已更新归档页"
fi

echo ""
echo "🎉 第 $ISSUE_NUM 期创建完毕！"
echo "   编辑：$ISSUE_FILE"
echo "   本地预览：npm run docs:dev"
echo "   发布：git add . && git commit -m 'feat: 第 $ISSUE_NUM 期' && git push"
