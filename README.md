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
