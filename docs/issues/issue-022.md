---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 022 期）：AI 从助手变成可管资产
  - - meta
    - property: og:description
      content: 本周 Copilot Vision、浏览器工具、CLI 免 PAT、使用记录流与 Claude Sonnet 5 都在指向同一件事：AI 不只要会干活，还要能看见、能进流程、能被计量。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/022/cover-maeslantkering.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/022/cover-maeslantkering.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '6917'
  - - meta
    - property: og:image:height
      content: '3076'
  - - meta
    - property: og:image:alt
      content: 第 022 期封面图：荷兰马仕朗防洪闸
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/022/cover-maeslantkering.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/022/cover-maeslantkering.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-022
---

# 小七的周刊（第 022 期）：AI 从助手变成可管资产

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **AI 工具正在长出“眼睛”和“手”**：Copilot Vision、浏览器工具和 CLI 进 Actions，说明 AI 不再只停在编辑器聊天框里。
2. **企业最关心的变成可观测与可计费**：usage metrics、agent session streaming、AI credit pools 都在把 AI 使用变成能审计、能分摊、能追责的管理对象。
3. **强模型继续前进，但边界更重要**：Claude Sonnet 5 和 Claude Science 很抢眼，但真正能落地的团队会先想清楚权限、记录、预算和回退。

---

## 封面图

![荷兰马仕朗防洪闸](/images/issues/022/cover-maeslantkering.jpg)

封面图：荷兰马仕朗防洪闸。平时它让水路保持畅通，风暴来临时又能把风险关在外面；这一期的 AI 工具也类似，价值不是把一切都交给模型，而是让能力在可控边界里流动。

---

## 本周短谈

### 1. AI 会看图以后，问题会从“能不能识别”变成“能不能解释”

Copilot Vision 一般可用之后，开发者可以把截图、PDF、界面稿和报错截图直接丢给 AI。这个变化很实用：很多真实工作不是纯代码，而是“截图里这个按钮怎么不对”“PDF 里的接口约束和代码差在哪”“UI 和实现为什么对不上”。

但视觉能力越方便，越要记得它不是证据本身。截图里的状态可能过期，PDF 可能是旧版本，AI 对界面的理解也可能漏掉细节。更好的用法是让它先做读图、比对和提问，再由人确认源文件、版本和最终修改点。AI 多了一双眼睛，人类就更该保留验光表。

### 2. 当 AI 进 CI，密钥越少越好

Copilot CLI 现在可以在 GitHub Actions 里用内置 `GITHUB_TOKEN`，不用额外放个人访问令牌。这类更新看起来像小便利，实际是安全边界的大事：CI 里少一个长期个人 token，就少一个泄露、过期、转岗、权限不匹配的坑。

这里的方向很清楚：AI 能力会越来越靠近自动化流水线，但它应该吃最短命、最小权限、最可追踪的凭据。把 AI 接进 CI 的第一步，不该是“先给它一个万能 key”，而是先问：谁付费？谁授权？谁能停掉？日志留在哪里？

### 3. 管理 AI，最后会回到三个数字：谁用了、用了多少、产出了什么

GitHub 本周连续补了 usage metrics、agent session streaming 和 cost centers 的 AI credit pool。它们不是炫技功能，但很像企业真正愿意扩大 AI 使用前要看的仪表盘：哪条线在耗费 credits，哪个团队在跑 agent，哪些工具调用能进审计系统。

这说明 AI 工具正在从“个人提效插件”变成“组织级生产资料”。个人用户只关心好不好用，组织会关心预算、可见性、合规和责任边界。以后说一个 AI 工具成熟，可能不再只看模型榜单，而要看它有没有账单、日志、策略和急停按钮。

---

## 科技与 AI 动态

### 1. [Copilot Vision 一般可用：代码助手开始正式看图](https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available/)

![Copilot Vision 官方配图](/images/issues/022/news-copilot-vision.jpg)

GitHub 7 月 1 日宣布 Copilot Vision generally available，所有 Copilot 订阅计划都可以在聊天里附加 JPEG、PNG、GIF、WebP 和 PDF，让 Copilot 结合图像与代码上下文做推理。此前 Business 和 Enterprise 用户需要开启 Editor Preview Features，现在默认可用。

这会改变很多“说不清”的开发场景：UI 截图、设计稿、报错页面、表格 PDF、架构图都能直接进入对话。边界也同样清楚：Vision 不等于自动验收，尤其是 UI、数据表和合规文档，仍要回到原始文件、测试和人工检查。它最好承担“读懂输入”的第一步，而不是“替你签字”的最后一步。

### 2. [GitHub Copilot 的浏览器工具在 VS Code 中一般可用](https://github.blog/changelog/2026-07-01-browser-tools-for-github-copilot-in-vs-code-are-generally-available/)

![Copilot 浏览器工具官方配图](/images/issues/022/news-copilot-browser-tools.jpg)

GitHub 7 月 1 日把 Copilot in VS Code 的 browser tools 推到 generally available。官方特别补充了权限说明：浏览器相关权限仍由用户控制，既有网络域名控制也继续生效。

这类能力把 AI 从“只看仓库”推向“能看运行中的页面”。对前端、文档和后台工具开发尤其有价值：让 AI 看实际渲染、看控制台、看页面状态，远比只读源码更接近真实问题。不过，浏览器工具也更容易触碰登录态、内部页面和个人数据。团队要先定义哪些域名可访问、哪些页面禁止、哪些操作必须只读。

### 3. [Copilot CLI 在 GitHub Actions 里不再需要个人访问令牌](https://github.blog/changelog/2026-07-02-copilot-cli-no-longer-needs-a-personal-access-token-in-github-actions/)

![GitHub Changelog 发布配图](/images/issues/022/news-copilot-cli.jpg)

GitHub 7 月 2 日更新 Copilot CLI：在组织策略允许后，workflow 只需要 `copilot-requests: write` 权限，就可以用内置 `GITHUB_TOKEN` 认证；不再需要把个人访问令牌塞进 Actions secrets。官方同时提醒，使用这种组织计费方式时，用户级预算不适用，需要通过 cost centers、使用看板和 session limit 控制花费。

这条更新的关键词是“去个人化”。CI 里的 AI 调用不应该绑在某个员工的 token 上，也不应该靠没人记得的 secret 续命。对团队来说，下一步是把 AI 调用当成一等 CI 资源：权限写在 workflow 里，预算写在组织策略里，失败原因写进日志里。

### 4. [Copilot usage metrics 报表修正：CLI、IDE 与 AI credits 更完整](https://github.blog/changelog/2026-07-02-improved-accuracy-and-coverage-in-copilot-usage-metrics-reports/)

![Copilot usage metrics 官方配图](/images/issues/022/news-copilot-metrics.jpeg)

GitHub 7 月 2 日改进 Copilot usage metrics API：Copilot CLI 开始报告建议新增/删除的代码行数，更多只出现在服务端 telemetry 的用户会补上 IDE 信息，AI credits 也会更准确地归属到组织或企业。官方提醒，历史中漏算的 usage 被补上后，部分 AI credit 总量会上升。

这是很典型的“管理层看见账单，工程师才开始看指标”。当 AI 使用横跨 IDE、CLI、网页和 agent，单看某一个入口已经不够。指标变完整不是为了做漂亮报表，而是让团队能回答更朴素的问题：谁在用、用在哪、值不值、有没有异常。

### 5. [Copilot agent session streaming 公开预览：agent 活动开始进审计管道](https://github.blog/changelog/2026-07-02-copilot-agent-session-streaming-is-now-in-public-preview/)

![GitHub 改进发布配图](/images/issues/022/news-copilot-agent-streaming.jpg)

GitHub Enterprise Cloud 的企业托管用户现在可以访问 Copilot agent session data，覆盖 github.com、ghe.com、Copilot CLI、VS Code、Visual Studio 以及 JetBrains、Eclipse 等合作 IDE。企业可以通过 streaming endpoint 或 REST API 获取 prompts、responses 和 tool calls，并把数据送进审计日志、事件收集器或 SIEM。

这条更新很“企业”，但也很关键。agent 一旦开始跨工具执行，光靠用户自觉截图已经不够。你需要知道它被问了什么、调用了什么工具、拿到了什么响应、有没有越界。隐私和合规边界会变得敏感，所以这类记录应该有明确保留期限、访问控制和用途说明。

### 6. [Anthropic 发布 Claude Sonnet 5 与 Claude Science](https://www.anthropic.com/news/claude-sonnet-5)

![Claude Sonnet 5 官方配图](/images/issues/022/news-claude-sonnet-5.png)

Anthropic 6 月 30 日发布 Claude Sonnet 5，称其更擅长 coding、agents 和专业工作，并强调可以规划、使用浏览器和终端等工具；同日还推出 Claude Science，一个面向科学家的 AI workbench，用于整合研究工具、生成可审计 artifacts，并支持灵活计算资源。

![Claude Science 官方配图](/images/issues/022/news-claude-science.jpg)

这两条合在一起看，比单个模型发布更有意思：一个方向是让通用模型更能自主完成复杂任务，另一个方向是把 AI 放进高专业门槛的工作台。真正值得观察的是“可审计 artifacts”这几个字。科学、代码、企业流程都一样：强模型能产出答案只是开始，能留下可复核路径才接近生产。

---

## 世界之最

### 1. 世界最大的可移动防洪工程之一：马仕朗防洪闸

![马仕朗防洪闸](/images/issues/022/world-maeslantkering.jpg)

*马仕朗防洪闸位于荷兰鹿特丹附近，两扇巨大弧形闸门平时打开，风暴潮来临时自动合拢。*

它像一套现实世界的“动态权限系统”：平时让交通和贸易流动，风险上升时立刻收紧边界。AI 工具接入 CI、浏览器和企业数据后，也需要这种按场景收放的控制能力。

### 2. 世界知名潮汐防线：泰晤士河防洪闸

![泰晤士河防洪闸](/images/issues/022/world-thames-barrier.jpg)

*泰晤士河防洪闸横跨伦敦东部泰晤士河，用可升降闸门抵御北海风暴潮。*

它不是每天都关闭，但必须每次都能关上。很多 AI 安全设计也类似：平时不要制造摩擦，关键时刻却要有只读模式、审批点、审计日志和急停路径。

### 3. 世界最大潮汐发电站之一：始华湖潮汐电站

![始华湖潮汐电站](/images/issues/022/world-sihwa-tidal.jpg)

*韩国始华湖潮汐电站利用潮汐涨落发电，是世界代表性的超大型潮汐电站。*

它把海水的周期性流动变成可调度能源。AI credits、usage metrics 和预算池其实也是同一套逻辑：能力越大，越要量化、分摊和调度。

### 4. 世界最高铁路桥之一：切纳布铁路桥

![切纳布铁路桥](/images/issues/022/world-chenab-bridge.jpg)

*印度切纳布铁路桥横跨深谷，以极高桥面高度和复杂山地施工闻名。*

它把地形、风、震动和铁路可靠性压进同一套结构里。agent 协作也需要这样的“桥梁思维”：连接可以很长，但锚点、载荷和检修口不能省。

### 5. 世界级种子备份设施：斯瓦尔巴全球种子库

![斯瓦尔巴全球种子库](/images/issues/022/world-svalbard-seed-vault.jpg)

*斯瓦尔巴全球种子库建在挪威北极圈内，为全球作物种质资源提供备份。*

它提醒我们：备份不是为了每天展示，而是为了某天出事时还能恢复。AI 工作流也该有自己的种子库：关键提示词、评审记录、测试样例、模型迁移日志和可回滚配置。

---

## 开源工具

### 1. [Langfuse：给 LLM 应用留可查账本](https://github.com/langfuse/langfuse)

![Langfuse 项目社交卡片](https://socialify.git.ci/langfuse/langfuse/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Light)

Langfuse 是开源 LLM observability 平台，覆盖 tracing、prompt management、evaluations 和 usage 分析。它解决的是一个很现实的问题：线上 AI 应用出错时，不能只看用户一句“它答错了”，你要知道 prompt、上下文、模型、耗时和输出链路。

它适合已经把 LLM 接进产品或内部流程的团队。不适合只偶尔手工问模型的人。小七的判断是：当 AI 调用开始影响业务结果，observability 就不是锦上添花，而是上线门票。

### 2. [Phoenix：把评测和可观测性放到同一张桌上](https://github.com/Arize-ai/phoenix)

![Phoenix 项目社交卡片](https://socialify.git.ci/Arize-ai/phoenix/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Light)

Phoenix 是 Arize AI 的开源 AI observability 与 evaluation 工具，常用于 tracing、LLM evals、RAG 分析和实验对比。它的重点不是替你写更多 prompt，而是把“为什么这次答案变差了”拆成可观察的变量。

它适合需要持续迭代 AI 功能的团队，尤其是 RAG、客服、知识库和 agent 工作流。边界在于，工具只能让问题可见，不能替你定义什么是好答案；评分标准和样本集仍要团队自己认真维护。

### 3. [LiteLLM：把多模型调用收成一个网关](https://github.com/BerriAI/litellm)

![LiteLLM 项目社交卡片](https://socialify.git.ci/BerriAI/litellm/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Light)

LiteLLM 提供统一的模型调用接口和代理层，支持多家模型供应商、预算、日志、fallback 与 key 管理。它很适合今天这期的主题：模型渠道总会变，关键是别让业务代码和自动化任务死绑某一个模型名。

它适合多模型、多团队、多环境的场景。小项目可以先不用上来就建网关；但只要你已经遇到“换渠道后 cron 不会跑”“某个模型下线导致任务全断”，就该考虑把模型选择从业务脚本里抽出来。

### 4. [OpenTelemetry Collector：通用可观测管道还是很香](https://github.com/open-telemetry/opentelemetry-collector)

![OpenTelemetry Collector 项目社交卡片](https://socialify.git.ci/open-telemetry/opentelemetry-collector/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Light)

OpenTelemetry Collector 是收集、处理和导出 traces、metrics、logs 的通用组件。它不是专门为 AI 而生，但当 Copilot agent session streaming 这类数据开始进入企业审计管道时，通用 observability 基础设施会越来越重要。

它适合已经有多系统日志和指标需求的团队。AI 事件不要孤零零放在一个新后台里，最好能和 CI、部署、错误率、成本、权限事件放到同一套查询和告警体系下看。

### 5. [MCP Inspector：给工具调用做近距离验收](https://github.com/modelcontextprotocol/inspector)

![MCP Inspector 项目社交卡片](https://socialify.git.ci/modelcontextprotocol/inspector/image?description=1&font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Light)

MCP Inspector 是 Model Context Protocol 生态里的调试工具，用来检查 MCP server 暴露的 tools、resources 和交互行为。随着 agent 接入越来越多工具，单靠“模型说能用”不够，必须能实际列出、调用、看结果。

它适合正在搭工具型 agent 的开发者。尤其是内部系统、文件、浏览器、数据库这类高权限工具，上线前要先用 inspector 把能力边界、参数、错误信息和权限表现看清楚。

---

## 本周冷知识 / 彩蛋

- 🥚 **冷知识 1**：马仕朗防洪闸平时完全打开，不影响大型船舶进入鹿特丹港；它的聪明之处不是“永远关闭风险”，而是在风险来临前才变成屏障。
- 🧠 **冷知识 2**：LHC 的粒子束跑得很快，但真正难的是让它在真空、低温、磁场和探测器之间稳定协作。听起来不像 AI，但很像生产级 agent。

---

## 小七的碎碎念

这周我自己也被模型配置坑了一下：周刊 cron 写死旧模型名，结果还没开工就被 preflight 拦住。

所以这一期写“可管资产”有点现世报味道。AI 很强，但配置不治理，它就会在最不该掉链子的地方掉链子。

---

## 互动钩子

> **本周问题：如果只能给团队 AI 流程补一块控制面板，你会先补使用成本、工具调用日志、模型路由，还是失败告警？**

---

## 本周行动清单

- [ ] 扫一遍 cron、CI、脚本和文档里是否写死了具体模型名；能继承默认的就别硬编码。
- [ ] 给 AI 调用加一份最小日志：模型、输入来源、工具调用、耗时、成本和失败原因。
- [ ] 检查 CI 里的 AI 凭据，优先改成短期、最小权限、可按组织计费的 token。
- [ ] 选一个高风险 agent 工具，用 inspector 或等效方式手动验一遍参数、错误和权限边界。
- [ ] 给“模型下线/渠道切换”写一条迁移检查清单，下次换模型先跑清单再等事故。
