# RSS + 订阅功能 Code Review 请求

## 变更概要

为「小七的周刊」VitePress 博客实现了 RSS feed + 邮件订阅引导功能。

## 变更文件

### 新增文件
1. **`docs/.vitepress/rss.ts`** - RSS feed 生成器，在 buildEnd 钩子中调用
2. **`docs/issues/_TEMPLATE.md.tpl`** - 模板文件（从 .md 改名为 .tpl 避免 Vue 编译 `{{}}` 占位符）

### 修改文件
3. **`docs/.vitepress/config.ts`** - 添加 RSS `<link>` head 标签、buildEnd 钩子、导航栏 RSS 链接、footer RSS 链接
4. **`docs/.vitepress/theme/custom.css`** - 新增订阅区域样式（subscribe-section、issue-subscribe-cta）
5. **`docs/index.md`** - 首页改造：增加订阅按钮、RSS 引导、最新期刊展示
6. **`docs/issues/issue-001.md`** - 文末添加订阅 CTA
7. **`docs/issues/issue-002.md`** - 文末添加订阅 CTA

## 技术方案

- **RSS 生成**：零外部依赖，纯 Node.js 字符串拼接，通过 VitePress buildEnd 钩子自动生成 `feed.xml`
- **日期提取**：从 `archive.md` 解析期号→日期映射，fallback 到默认日期
- **邮件订阅**：采用"订阅引导"方案，引导用户通过 RSS 阅读器（Feedly/Inoreader）的邮件通知功能实现
- **订阅 CTA**：首页有独立订阅区域（带 RSS 指南），每篇文章底部有 RSS + Twitter 转发按钮

## 构建验证
- `npm run docs:build` 无报错
- `feed.xml` 正确生成在 dist 目录
- RSS discovery `<link>` 出现在所有页面 `<head>` 中

## 请 Review 的要点
1. RSS 生成器的健壮性（日期解析、XML 转义、边界情况）
2. 首页改造的 UX/文案
3. CSS 样式的兼容性和可维护性
4. 订阅引导方案是否足够清晰
5. 是否有安全问题（XSS、信息泄露等）
6. 代码风格和可维护性
