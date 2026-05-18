# 周刊运作说明

这份文件说明《小七的周刊》当前到底怎么运作。只保留稳定流程，不放临时复盘、草稿和 agent 记忆。

## 1. 当前定位

- 仓库：`leeseven1211/blog-weekly`
- 本地路径：`/home/ubuntu/projects/blog-weekly`
- 线上站点：<https://blog.leeseven.com>
- 技术栈：VitePress + GitHub Pages + GitHub Actions
- 发布分支：`main` 触发构建，产物发布到 `gh-pages`

## 2. 仓库里哪些东西是核心

```text
blog-weekly/
├── docs/
│   ├── .vitepress/config.ts      # VitePress 配置、导航、侧边栏、RSS 钩子
│   ├── .vitepress/rss.ts         # build 时生成 feed.xml
│   ├── issues/                   # 每期周刊正文
│   │   ├── _TEMPLATE.md.tpl      # 新一期模板
│   │   └── issue-013.md          # 每期内容
│   ├── articles/                 # 独立专题文章
│   ├── public/                   # 站内图片、favicon、验证文件等静态资源
│   ├── index.md                  # 首页，自动同步最新一期/往期
│   ├── archive.md                # 归档页，自动同步
│   ├── about.md                  # 关于页
│   └── latest.md                 # 最新一期跳转页
├── scripts/
│   ├── sync-issues-meta.py       # 同步侧边栏、归档、首页最新期
│   └── check-issue-images.py     # 发布前检查最新一期关键配图
├── new-issue.sh                  # 创建新一期
├── EDITORIAL.md                  # 编辑规范与图片规则
├── OPERATIONS.md                 # 当前文件：运作说明
├── package.json                  # npm 脚本
└── .github/workflows/deploy.yml  # GitHub Pages 部署
```

## 3. 一期周刊的生命周期

### 3.1 创建新一期

```bash
cd /home/ubuntu/projects/blog-weekly
./new-issue.sh
```

它会做三件事：

1. 自动推算下一期期号，例如 `014`
2. 用 `docs/issues/_TEMPLATE.md.tpl` 生成 `docs/issues/issue-014.md`
3. 调用 `scripts/sync-issues-meta.py` 更新侧边栏、归档和首页

也可以手动指定期号：

```bash
./new-issue.sh 014
```

### 3.2 写稿与配图

正文写在：

```text
docs/issues/issue-XXX.md
```

图片放在：

```text
docs/public/images/issues/XXX/
```

公开稿的长期标准以 `EDITORIAL.md` 为准。当前最重要的几条：

- 周刊要像“可滑动、愿意收藏/转发的图文流”，不是行业报告
- 封面优先真实世界奇观 / 建筑 / 工程 / 场景图，少字、轻图注
- 科技动态优先官方图、产品界面、发布现场、原文截图、架构图
- 工具区优先 GitHub 仓库页、真实 UI、终端、README 截图
- 不再用本地脚本 / PIL / SVG / HTML / CSS 模板批量生成栏目图
- 发布前必须做成品审美复检，不能只看构建通过

临时图片计划、复盘、采集记录不要再长期堆在本仓库；需要留痕时写到 OpenClaw 工作区记忆或当天日志，稳定结论再沉淀进 `EDITORIAL.md` / `OPERATIONS.md`。

### 3.3 本地验证

基础构建检查：

```bash
npm run docs:build
```

这个命令会自动执行：

1. `npm run docs:sync`：同步首页、归档、侧边栏
2. `npm run docs:check-latest`：检查最新一期关键配图
3. `vitepress build docs`：构建站点
4. VitePress `buildEnd` 钩子调用 `docs/.vitepress/rss.ts` 生成 RSS

发布前最终门禁必须使用：

```bash
npm run docs:publish-check
```

它会在 `docs:build` 之外额外检查：

1. `npm run docs:check-image-urls`：确认本地/远程图片资源实际能加载，避免破图上线。
2. `scripts/check-publish-review.py`：确认已在 OpenClaw 工作区留下发布前视觉评审记录。

视觉评审记录默认放在：

```text
/home/ubuntu/.openclaw/workspace/notes/blog-weekly/publish-reviews/issue-XXX.md
```

记录中必须明确包含：`publish: approved`、`visual-review: pass`、`image-display: pass`、`image-semantics: pass`、`image-duplicates: pass`、`image-quality: pass`，并附至少 3 张本地预览截图路径。缺任何一项都不能发布。

如果只想检查图片：

```bash
npm run docs:check-latest
npm run docs:check-image-urls
```

如果只想同步首页/归档/侧边栏：

```bash
npm run docs:sync
```

### 3.3.1 发布前视觉审核硬门槛

发布前必须先启动本地预览，从读者视角截图并评审，不能只看 markdown 或 `docs:build` 结果：

```bash
npm run docs:build
npm run docs:preview -- --host 127.0.0.1 --port 4173
```

然后用浏览器打开 `http://127.0.0.1:4173/issues/issue-XXX.html`，至少保存顶部/中段/底部 3 张截图；长文建议按栏目补充截图。评审必须逐栏确认：

- 图片是否真实显示，没有破图、空白、加载失败、跨域占位或缓存旧图；
- 图片是否贴合正文语义，不把无关网页、OG 卡片、泛风景、纯 Logo 当新闻/工具证据；
- 图片是否清晰、有编辑感，没有明显 AI 乱码、错别字、错误 logo、虚构 UI、低清硬放大；
- 同一期没有重复图片，封面图没有在正文原样复用；
- 整页滑读节奏像正式周刊，而不是素材堆叠。

任一项不通过，最终摘要必须写“失败”，不得 commit / push。

### 3.4 发布

发布前最后一步必须先跑：

```bash
npm run docs:publish-check
```

只有通过后才能：

```bash
git status
git add .
git commit -m "feat: publish issue XXX"
git push origin main
```

推送到 `main` 后，GitHub Actions 会：

1. `npm ci`
2. `npm run docs:build`
3. 写入 CNAME：`blog.leeseven.com`
4. 部署 `docs/.vitepress/dist` 到 `gh-pages`

### 3.5 上线验收

发布后不要只看 workflow 成功，必须确认用户入口真实更新：

- 正文页：`https://blog.leeseven.com/issues/issue-XXX.html`
- 首页“最新一期”
- `/latest` 跳转
- RSS 首条：`https://blog.leeseven.com/feed.xml`
- 关键图片实际渲染正确；若缓存仍回旧图，换新文件名并更新引用

## 4. 自动化边界

仓库内部的 GitHub Actions 定时任务是：

```yaml
schedule:
  - cron: '0 23 * * 0'
```

这等于北京时间每周一 07:00 自动构建/部署一次。

注意：这个 GitHub Actions 只会构建并部署仓库里已经存在的内容，不会自动采写新一期、不会自动改稿、不会自动找图。真正的选题、写稿、配图、审稿仍然需要在本地仓库里完成，然后 push。

## 5. 清理规则

以后这个仓库只保留三类东西：

1. **公开站点内容**：`docs/**/*.md`、站点图片、RSS、配置
2. **生产工具**：`new-issue.sh`、`scripts/`、`package.json`、GitHub Actions
3. **稳定规范**：`README.md`、`EDITORIAL.md`、`OPERATIONS.md`

不再放这些东西：

- agent 身份/记忆文件：`AGENTS.md`、`SOUL.md`、`USER.md` 等
- 一次性 review 请求、临时复盘、图片草案分析
- 未引用的旧图片、旧 SVG、旧 v2 中间稿
- 构建产物、缓存、Python `__pycache__`

如果某次复盘真的有长期价值，先提炼到 `EDITORIAL.md` 或本文件；不要把整份过程笔记塞进仓库。
