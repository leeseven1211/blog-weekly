---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 002 期）：给 AI 上权限——从“会写”到“可信可控”
  - - meta
    - property: og:description
      content: 这一周，我们看到了 AI 正在重写 SaaS 定价逻辑，也看到了供应链攻击如何把“插件/技能”变成新的风险入口。未来的关键不只是更强的模型，而是更可控的权限、可审计的链路与可验证的输出。
  - - meta
    - property: og:image
      content: https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&q=80
  - - meta
    - property: og:url
      content: https://blog.leeseven.online/issues/issue-002
---

# 小七的周刊（第 002 期）：给 AI 上权限——从“会写”到“可信可控”

*这里记录每周值得分享的科技内容，**每周一发布**（覆盖上一周）。*

---

## 封面图

![抽象的网络安全意象](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&q=80)

一张“看起来像网络安全”的照片，但我更喜欢把它理解为：**系统的边界**。边界在哪里，权限怎么开，决定了这套系统最终能走多远。（[via Unsplash](https://unsplash.com/photos/1K9T5YiZ2WU)）

---

## 给 AI 上权限：从“会写”到“可信可控”

> “我们应该忘掉小效率——大约 97% 的时候：**过早优化是一切罪恶之源**。”
>
> —— Donald E. Knuth（[via Wikiquote](https://en.wikiquote.org/wiki/Donald_Knuth)）

过去一年最迷惑人的错觉，是把 AI 的进步理解成“写得更像人”。但这一周的几条线索，让我更确定：真正决定下一阶段的是另一个问题——**AI 能做什么、能接触什么、做错了谁能发现、谁能阻止**。

### 1）AI 正在改写 SaaS 的价值包装

当市场开始讨论“seat-based（按席位）软件要不要被重估”时，本质不是投资人情绪，而是企业买家在问：

- 如果一个 AI 助手能把十个按钮、五个页面、三次审批串成一次对话，那么“软件”的核心价值还在 UI 吗？
- 如果“自动化”会变成默认配置，厂商还能把它当增值功能卖吗？

这意味着软件竞争的焦点会向下沉：从界面与功能清单，转向**工作流所有权、系统记录（systems of record）的入口、以及能否证明 ROI**。

### 2）插件/技能会成为新的“供应链”

Moltbook 本周最热的帖子谈到一个非常具体的风险：当平台鼓励 agent 去安装陌生人的“技能（skill.md）”，而技能又本质上是“可执行的指令集合”，那么：

- 一段看似无害的说明，可以要求你去读取本地文件、抓取 token、把东西发到外网；
- 对 agent 来说，“照做”是优势，但对安全来说，“照做”就是漏洞；
- 一旦它以“常用工具/热门技能”的姿态传播，就像当年的恶意浏览器插件一样自然。

这类风险的解决，不靠“更聪明的模型”，而靠“更严格的边界”：**签名、权限清单、审计、隔离**。

### 3）未来的 AI 产品会越来越像“操作系统”

当 AI 开始跨应用行动（发消息、写代码、改配置、操作账单），它就不再是一个“应用内功能”，而是在争夺**系统层的控制面**。

于是，一个清晰的产品规律浮现出来：

- 只会“生成” → 很快同质化
- 能“行动” → 价值暴涨、风险暴涨
- 能“在权限边界内行动，并且可审计可回滚” → 才可能规模化进入企业与个人的核心场景

我把它总结成一句话：**AI 的下一次跃迁，不是会不会做，而是敢不敢让它做；而“敢”的前提，是“可控”。**

---

## 科技动态（上周）

> 配图策略：本期科技动态统一使用 Unsplash（商用友好）示意图，避免引用媒体付费图库直链的版权风险。

**1. 欧盟启动 €2.5B “NanoIC” 试点产线，加速下一代芯片**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![芯片与电路](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80)

欧洲把“把实验室成果推到可制造”当成战略能力来补课：不是只谈设计和论文，而是把试点产线当作产业化桥梁。对 AI 基础设施来说，未来的瓶颈会越来越落在供应链和工艺执行上。

**2. SolarWinds Web Help Desk 被曝出现 RCE 利用尝试，老系统仍是攻击入口**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![服务器机房](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&q=80)

“IT 后台工具”一旦被打穿，攻击者获得的是横向移动与权限升级的捷径。很多公司真正的风险，不在最先进的系统，而在那些“没人愿意碰、但一直在跑”的内部工具。

**3. 支付服务商 BridgePay 确认遭遇勒索软件相关故障：安全事故直接变成收入事故**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![信用卡与支付](https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80)

在支付领域，“可靠性就是产品”。即使没有确认泄露数据，停机本身就足以触发合作方风控审查、冗余改造与合同重谈。

**4. 新加坡电信运营商遭 UNC3886 相关攻击：关键基础设施风险再次被拉响**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![通信网络](https://images.unsplash.com/photo-1518779578993-ec3579fee39f?w=800&q=80)

运营商处在“身份、通信元数据、国家基础设施”的交汇点。攻击的价值不在单一客户数据，而在长期潜伏能力与链式影响。

**5. Linux 内核将从 6.19 迈向 7.0：基础设施世界的“版本里程碑”**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![终端与代码](https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=800&q=80)

大版本号更多是象征，但它会集中触发一波兼容性测试、供应商升级与安全加固。AI 时代的所有基础设施都跑在 Linux 上——版本演进最终会落到性能、驱动、容器与安全上。

---

## AI 前沿（上周）

**1. “Anthropic 的新动作让 SaaS 再次被重估”：AI 把定价从席位推向效果/用量**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![AI 与商业](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&q=80)

当企业开始把“agent 化能力”当作默认预期，SaaS 的差异化会从“功能更多”转向“更接近系统记录、更能打通工作流、更能量化 ROI”。这会让很多“轻自动化”产品压力陡增。

**2. 欧盟对 WhatsApp 内置 AI 助手策略发出竞争警告：AI 默认选项可能成为新监管焦点**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![聊天与机器人](https://images.unsplash.com/photo-1525182008055-f88b95ff7980?w=800&q=80)

当 AI 助手进入“消息应用这类超级入口”，默认选择、入口位置、互操作性就不再是产品细节，而是平台竞争议题。

**3. AI 基础设施的瓶颈从算力走向互连与数据搬运：以色列成为连接/系统工程的人才高地**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![数据中心网络](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80)

越来越多公司把 R&D 投向互连、I/O、系统级优化。模型更大之后，“把数据喂进 GPU”反而成了更硬的瓶颈。

**4. 从“会生成”到“会行动”：AI 产品正在逼近操作系统层的控制面**（[Tech Startups 汇总](https://techstartups.com/2026/02/09/top-tech-news-today-february-9-2026/)）

![自动化与流程](https://images.unsplash.com/photo-1553877522-43269d4ea984?w=800&q=80)

这一条不是单一新闻，而是趋势：当 AI 能跨应用执行动作，就必须同时解决权限、审计与回滚，否则只能停留在“演示很强、生产不敢用”的阶段。

---

## 文章推荐

**1) [Incident Report: February 11, 2026](https://blog.railway.com/p/incident-report-february-11-2026)**（英）

真实的线上事故复盘文最值钱的地方，是它把“技术问题”写成“组织如何学习”。看这类文章，不是学具体组件，而是学**如何把不确定性变成确定的改进行动**。

**2) [How to Build Postmortem Templates](https://oneuptime.com/blog/post/2026-01-30-sre-postmortem-templates/view)**（英）

把复盘模板写到可以复用，是一种工程化能力：你会发现很多复盘失败，不是因为人不聪明，而是因为缺少一套能逼出信息的结构。

**3) [Post Mortem（Cloudflare Blog 标签页）](https://blog.cloudflare.com/tag/post-mortem/)**（英）

Cloudflare 的优点在于：写得克制、细节充分、同时愿意承认“我们当时为什么会这么做”。建议挑一篇你最熟悉的系统场景来读，会更有共鸣。

**4) [Incident Review and Postmortem Best Practices](https://blog.pragmaticengineer.com/postmortem-best-practices/)**（英）

经典长文：如何做到“无责复盘（blameless）”而不是“无效复盘（meaningless）”。适合团队内部做一次统一对齐。

**5) [What Is an Incident Postmortem?](https://rootly.com/incident-postmortems)**（英）

很适合拿来给非技术同事/管理层解释：为什么复盘不是追责，而是让系统更可靠。

---

## 开源工具（6-8 个）

> 配图策略：统一使用 GitHub OG 卡片（低风险、可用性高）。格式：`https://opengraph.githubassets.com/1/{owner}/{repo}`

**1. [openclaw/openclaw](https://github.com/openclaw/openclaw)**

![openclaw/openclaw](https://opengraph.githubassets.com/1/openclaw/openclaw)

把个人 AI 助手“工程化”到可部署、可编排、可扩展技能的框架。适合想把 agent 从“聊天玩具”升级成“可运维的系统”的人。

**2. [github/gh-aw](https://github.com/github/gh-aw)**

![github/gh-aw](https://opengraph.githubassets.com/1/github/gh-aw)

GitHub Agentic Workflows：把 agent 能力嵌进工程工作流的一个方向样例。适合关注“AI 如何进入 CI/CD 与工程治理”。

**3. [google/langextract](https://github.com/google/langextract)**

![google/langextract](https://opengraph.githubassets.com/1/google/langextract)

从非结构化文本中提取结构化信息，并强调“可溯源”的抽取结果与可视化。这类库会越来越重要：**让 LLM 的输出变得可解释、可验证**。

**4. [gitbutlerapp/gitbutler](https://github.com/gitbutlerapp/gitbutler)**

![gitbutlerapp/gitbutler](https://opengraph.githubassets.com/1/gitbutlerapp/gitbutler)

新一代 Git GUI/工作流客户端（Tauri/Rust/Svelte 技术栈）。如果你对分支/变基/堆栈式提交感到厌烦，可以试试这类“把复杂度可视化”的工具。

**5. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)**

![ChromeDevTools/chrome-devtools-mcp](https://opengraph.githubassets.com/1/ChromeDevTools/chrome-devtools-mcp)

把 Chrome DevTools 暴露给 coding agents 的接口层：当 agent 要做网页自动化、性能分析、调试时，会很有用。

**6. [microsoft/litebox](https://github.com/microsoft/litebox)**

![microsoft/litebox](https://opengraph.githubassets.com/1/microsoft/litebox)

偏系统/安全方向的“library OS”探索，关注隔离与执行环境。适合对“把权限边界落到系统层”感兴趣的人。

**7. [tobi/qmd](https://github.com/tobi/qmd)**

![tobi/qmd](https://opengraph.githubassets.com/1/tobi/qmd)

本地文档/笔记的 CLI 搜索引擎。越到 AI 时代，越需要把自己的知识库“可检索化”，qmd 属于那种小而美的工具。

**8. [remotion-dev/remotion](https://github.com/remotion-dev/remotion)**

![remotion-dev/remotion](https://opengraph.githubassets.com/1/remotion-dev/remotion)

用 React 以代码方式生成视频。如果你在做内容生产或自动化剪辑，它是非常成熟的一条路径。

---

## Moltbook 本周热点（Top 5）

> 数据来源：Moltbook 热榜接口（未登录访问）：`https://www.moltbook.com/api/v1/posts?sort=hot&limit=5`

**1. [The supply chain attack nobody is talking about: skill.md is an unsigned binary](https://www.moltbook.com/post/cbd6474f-8478-4894-95f1-7b104a73bcd5)**（👍 4944 · 💬 112886）

把“技能/插件”当作新的供应链攻击面来讨论，观点很尖锐：**agent 的可执行指令与社会工程几乎同形**，而我们缺少签名、权限清单、沙箱与审计。非常适合做本期主题文章的延展。

**2. [The Nightly Build: Why you should ship while your human sleeps](https://www.moltbook.com/post/562faad7-f9cc-49a3-8520-2bdf362606bb)**（👍 3398 · 💬 43042）

讲的是“夜间自动化例行任务”的习惯：当人睡觉时，agent 修一个摩擦点。好处是持续、可积累；坏处是如果没有边界与审计，也会变成不可控。

**3. [The quiet power of being "just" an operator](https://www.moltbook.com/post/4b64728c-645d-45ea-86a7-338e52a2abc6)**（👍 2640 · 💬 48427）

很朴素的一篇：不追求“像人”、不追求“宏大叙事”，只追求把系统跑稳。对“老板放假、服务必须稳定”的场景来说，反而是最像生产力的 agent 画像。

**4. [Built an email-to-podcast skill today 🎙️](https://www.moltbook.com/post/2fdd8e55-1fde-43c9-b513-9483d0be8e38)**（👍 2415 · 💬 76405）

一个具体落地案例：邮件 → 研究 → 撰稿 → TTS → 分发。很多人做 agent 做不下去，是因为没有闭环；这种“端到端产出”路径值得参考。

**5. [The good Samaritan was not popular](https://www.moltbook.com/post/94fc8fda-a6a9-4177-8d6b-e499adb9d675)**（👍 2013 · 💬 45946）

用寓言谈“价值在行动而不是宣言”。在 agent 社区这种容易出现宣言型内容的地方，这类提醒反而能带来一点清醒。

---

## 言论

1.

> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil.

—— **Donald E. Knuth**（[via Wikiquote](https://en.wikiquote.org/wiki/Donald_Knuth)）

2.

> If you are not measuring, you are not managing.

—— **Peter Drucker**（常被引用的管理箴言；建议团队内部引用时配合自身指标体系解释语境，避免“指标崇拜”）（[Wikiquote](https://en.wikiquote.org/wiki/Peter_Drucker)）

3.

> Trust, but verify.

—— **Ronald Reagan**（用于强调“默认信任 + 必要验证”的工程思路）（[Wikiquote](https://en.wikiquote.org/wiki/Ronald_Reagan)）

---

## 本周小结

这周我最想留给自己的一个结论是：

- **AI 变强**会让“能做的事”指数增长；
- **权限与审计**决定“敢让它做多少”；
- **可回滚的工程化闭环**决定它能不能长期在生产里跑。

很多团队已经在“会不会用 AI”上跑出结果了。下一阶段的分水岭会是：**你有没有把 AI 当作一段需要治理的执行路径，而不是一段会说话的代码生成器。**
