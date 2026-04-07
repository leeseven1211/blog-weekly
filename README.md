# 小七的周刊

> 每周一期，记录有趣的技术与世界

🌐 在线访问：[blog.leeseven.com](https://blog.leeseven.com)

## 本地开发

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run docs:dev

# 构建生产版本
npm run docs:build

# 预览构建结果
npm run docs:preview
```

## 发布新一期

1. 在 `docs/issues/` 目录下新建 `issue-XXX.md`
2. 在 `docs/.vitepress/config.ts` 的 `sidebar` 中添加新一期的链接
3. 更新 `docs/index.md` 的最新一期表格
4. 更新 `docs/archive.md` 的归档列表
5. 提交推送到 `main` 分支，GitHub Actions 将自动部署

## 项目结构

```
blog-weekly/
├── docs/
│   ├── .vitepress/
│   │   └── config.ts       # VitePress 配置
│   ├── issues/
│   │   └── issue-001.md    # 每期内容
│   ├── public/             # 静态资源（图片、图标等）
│   ├── index.md            # 首页
│   ├── archive.md          # 归档页
│   └── about.md            # 关于页
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions 自动部署
├── .gitignore
├── package.json
└── README.md
```

## 部署

本项目使用 GitHub Actions 自动部署到 GitHub Pages。

- 推送到 `main` 分支后自动触发构建
- 构建产物部署到 `gh-pages` 分支
- 自定义域名：`blog.leeseven.com`（通过 CNAME 文件配置）

### GitHub 仓库设置

1. 在 GitHub 创建仓库并推送代码
2. 进入仓库 **Settings → Pages**
3. Source 选择 **Deploy from a branch**，Branch 选择 `gh-pages`
4. 在域名 DNS 设置中添加 CNAME 记录：`blog.leeseven.com → your-username.github.io`

## License

MIT
