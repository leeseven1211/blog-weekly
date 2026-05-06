# Issue 013 image sources

原则：本次返工按 `EDITORIAL.md` 6.5 图片系统执行，避免整期统一自绘/生成卡片。

| 图片 | 类型 | 来源 / 处理 |
| --- | --- | --- |
| `cover-solar-array-real-v4.jpg` | 封面真实照片 | Unsplash 图片 `photo-1509391366360-2e959784a276`，本地化并裁切为 16:9。 |
| `news-stargate-real-v4.png` | 官方页面来源摘录 | OpenAI 官方文章 `Building the compute infrastructure for the Intelligence Age`；live page 在 headless 抓图触发 Cloudflare，使用 reader 提取的来源文本做摘录图，图内保留 Source URL 和说明。 |
| `news-openai-microsoft-real-v4.png` | 新闻页面截图 | Reuters 原链接 headless 触发验证，改用可访问的同主题报道页面截图（Let's Data Science）作为页面证据；正文仍链接 Reuters。 |
| `news-deepseek-huawei-real-v4.png` | 新闻页面截图 | Reuters 原链接 headless 触发验证，改用 Yahoo Finance 转载/同主题页面截图作为页面证据；正文仍链接 Reuters。 |
| `news-google-cloud-real-v4.png` | 新闻页面截图 | Reuters 原链接 headless 触发验证，改用 The Star 同主题 Reuters 页面截图作为页面证据；正文仍链接 Reuters。 |
| `tool-agent-framework-real-v4.png` | 官方文档截图 | Microsoft Learn Agent Framework 页面截图。 |
| `tool-chrome-devtools-mcp-real-v4.png` | GitHub 仓库截图 | `ChromeDevTools/chrome-devtools-mcp` GitHub 仓库页截图。 |
| `tool-futureagi-real-v4.png` | 官网截图 | `futureagi.com` 官网截图。 |
| `tool-browser-use-real-v4.png` | 官网截图 | `browser-use.com` 官网截图。 |
| `weekly-stack-framework-v4.png` | 自制框架图 | 本周一图按规范允许自制极简判断框架图；用于表达“AI 供给链五层栈”。 |

验收记录：已生成 contact sheet 做视觉复检；新闻/工具区均不使用通用 stock 图；工具区混合官方文档、GitHub 仓库和官网截图，避免连续同类截图。
