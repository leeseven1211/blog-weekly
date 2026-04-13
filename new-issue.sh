#!/bin/bash
# new-issue.sh - 一键创建新一期周刊
# 用法: ./new-issue.sh [期号]
# 例如: ./new-issue.sh 003

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ISSUES_DIR="$SCRIPT_DIR/docs/issues"
TEMPLATE_FILE="$ISSUES_DIR/_TEMPLATE.md.tpl"
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

# 创建 Markdown 模板（统一使用详细模板，默认带配图占位与发布结构）
if [ ! -f "$TEMPLATE_FILE" ]; then
  echo "❌ 模板不存在：$TEMPLATE_FILE"
  exit 1
fi

python3 - "$TEMPLATE_FILE" "$ISSUE_FILE" "$ISSUE_NUM" <<'PY'
from pathlib import Path
import sys

template_file = Path(sys.argv[1])
issue_file = Path(sys.argv[2])
issue_num = sys.argv[3]

content = template_file.read_text(encoding='utf-8').replace('XXX', issue_num)
issue_file.write_text(content, encoding='utf-8')
PY

echo "✅ 已创建：$ISSUE_FILE"

# 用统一脚本更新侧边栏和归档（防重复、按 H1 自动取标题）
python3 "$SCRIPT_DIR/scripts/sync-issues-meta.py" --issue "$ISSUE_NUM" --date "$TODAY"
echo "✅ 已更新侧边栏和归档"

echo ""
echo "🎉 第 $ISSUE_NUM 期创建完毕！"
echo "   编辑：$ISSUE_FILE"
echo "   本地预览：npm run docs:dev"
echo "   发布：git add . && git commit -m 'feat: 第 $ISSUE_NUM 期' && git push"
