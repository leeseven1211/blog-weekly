# 小七的周刊

> 每周一期，记录有趣的技术与世界

🌐 在线访问：[blog.leeseven.com](https://blog.leeseven.com)

## 当前怎么运作

详细流程见：[OPERATIONS.md](./OPERATIONS.md)

一句话版本：

1. `./new-issue.sh` 创建新一期
2. 编辑 `docs/issues/issue-XXX.md`
3. 图片放到 `docs/public/images/issues/XXX/`
4. `npm run docs:build` 本地同步、查图、构建、生成 RSS
5. push 到 `main`，GitHub Actions 自动部署到 GitHub Pages

注意：仓库里的 GitHub Actions 定时任务只负责按北京时间每周一 07:00 构建/部署现有内容，不负责自动采写新一期。

## 本地开发

```bash
npm install
npm run docs:dev
npm run docs:build
npm run docs:preview
```

## 发布新一期

```bash
cd /home/ubuntu/projects/blog-weekly
./new-issue.sh
npm run docs:build
git add .
git commit -m "feat: publish issue XXX"
git push origin main
```

发布后必须确认：

- 正文页已更新
- 首页“最新一期”已更新
- `/latest` 指向最新一期
- RSS 首条是最新一期
- 关键图片在线上实际渲染正确

## 项目结构

```text
blog-weekly/
├── docs/                         # VitePress 站点内容
│   ├── .vitepress/               # 配置与 RSS 生成器
│   ├── issues/                   # 每期周刊正文
│   ├── articles/                 # 独立专题文章
│   ├── public/                   # 图片、favicon、验证文件等静态资源
│   ├── index.md                  # 首页
│   ├── archive.md                # 归档页
│   ├── about.md                  # 关于页
│   └── latest.md                 # 最新一期跳转页
├── scripts/                      # 同步与检查脚本
├── new-issue.sh                  # 创建新一期
├── EDITORIAL.md                  # 编辑规范
├── OPERATIONS.md                 # 运作说明
├── package.json                  # npm 脚本
└── .github/workflows/deploy.yml  # GitHub Pages 部署
```

## 部署

- 推送 `main` 后触发 GitHub Actions
- 构建产物发布到 `gh-pages`
- 自定义域名：`blog.leeseven.com`

## License

MIT

## 编辑与发布规范（OpenClaw 归档）

> 归档自 OpenClaw 记忆（2026-08-14），已脱敏。

### 编辑定位
- 公开科技/AI/开源周刊，不写内部复盘口吻。
- 目标不是“生成一篇能 build 的文章”，而是发布一篇愿意滑完、愿意收藏/转发的图文流。
- 发布自动化必须服务质量，不得把“构建通过 / 图片存在 / push 成功”误报成“可发布”。

### 编辑硬规则
- 禁止固定「本周一图」栏目；如需信息图，只能自然放入对应主题、新闻、工具或世界之最条目。
- 禁止独立 “Moltbook 热点精选 / Moltbook 本周热点” 栏目；个别 Moltbook 内容只能作为普通素材进入合适栏目。
- 禁止整期使用本地脚本 / PIL / SVG / HTML / CSS 模板批量生成概念图。
- 图片优先级：真实来源图、官方图、产品界面、GitHub/README/文档截图、新闻页图；AI 图只在语义和视觉都贴合时谨慎使用。
- 禁止复用往期栏目图、错配图、低清硬放大、纯 logo 硬凑、明显 AI 乱码/错字/错误 logo。
- 封面/主题图不强制配图；只有真实、高质量、贴正文的证据图/场景图才放。

### 发布验收
- 必须本地预览，从头到尾滚读，并保存顶部/中段/底部截图。
- 必须有发布前视觉评审记录：notes/blog-weekly/publish-reviews/issue-XXX.md。
- npm run docs:build、图片 URL 检查、npm run docs:publish-check 都要通过。
- push 后要验证线上新一期可访问；若 Pages 未更新，只能报告“push 成功但线上验证未完成”。

### 历史教训索引
- 2026-04/05 多次图片质量失败：只保留硬规则，详细事故见归档原文。
- 2026-05-15 cron 误报：构建/push 成功但中途工具错误不应污染最终状态，状态机要看最终产物。
- 2026-05-18 第015期撤回：没有视觉审核就发布是失败；此后 publish-check 与视觉评审成为硬门禁。
