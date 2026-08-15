# Blog Weekly 架构说明

> 更新：2026-08-15（按 docs/engineering-standards/architecture.md 模板补写）

## 1. 概述
小七的周刊：每周一期，记录有趣的技术与世界；内容用 Markdown 维护，vitepress 构建发布。

## 2. 技术栈
- 站点：VitePress 1.6（docs/），Node ESM
- 脚本：Python 3（sync-issues-meta.py、check-issue-images.py 等）
- 内容：Markdown + 图片（docs/ 与 notes/）

## 3. 模块划分
| 路径 | 职责 |
|---|---|
| docs/ | 周刊内容与站点（vitepress） |
| scripts/ | 元数据同步/图片校验/发布检查 |
| notes/ | 素材笔记 |
| new-issue.sh | 新一期脚手架 |

## 4. 数据流
new-issue.sh 建新期 → 写 Markdown → docs:sync 同步元数据 → docs:build 构建 → 发布检查 → 上线。

## 5. 部署拓扑
静态站点部署（部署细节见 docs/projects/blog-weekly/ 与 OPERATIONS.md）。

## 6. 已知限制与演进
- 发布前必须跑 docs:publish-check（构建+图片 URL+发布检查）；
- 编辑规范见 EDITORIAL.md，运营规范见 OPERATIONS.md。

