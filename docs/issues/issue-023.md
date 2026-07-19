---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 023 期）：AI 进入可编排的工作台
  - - meta
    - property: og:description
      content: 本周 JetBrains、Visual Studio、Copilot 用量 API 与安全扫描 API 都在补同一件事：AI 不是只会聊天的插件，而是需要模型、权限、指标和回滚机制共同支撑的工作台。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/023/cover-falkirk-wheel.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/023/cover-falkirk-wheel.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '3264'
  - - meta
    - property: og:image:height
      content: '2448'
  - - meta
    - property: og:image:alt
      content: 第 023 期封面图：苏格兰福尔柯克轮式升船机
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/023/cover-falkirk-wheel.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/023/cover-falkirk-wheel.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-023
---

# 小七的周刊（第 023 期）：AI 进入可编排的工作台

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **AI 工具正在从“能力入口”变成“工作台”**：JetBrains 和 Visual Studio 的更新都把 agent、模型、插件、MCP、Hooks 与权限配置放进日常开发界面。
2. **采用度开始被工程指标验证**：Copilot usage metrics 新增 PR 首次评审时间和评审轮次，说明 AI 采用不再只看活跃用户数。
3. **安全治理继续前移**：secret scanning custom patterns API 与 PR archive 都在把安全和社区治理做成可运营能力，而不是上线后的临时处置。

---

## 封面图

![苏格兰福尔柯克轮式升船机](/images/issues/023/cover-falkirk-wheel.jpg)

封面图：苏格兰福尔柯克轮式升船机。它把船从一个水位稳稳转到另一个水位；这一期的 AI 工具也像在补这种“升降机构”，让任务能在 IDE、终端、云端和组织规则之间可控流转。

---

## 本周短谈

### 1. AI 的下一站不是更会聊，而是更能被安排

过去一年，开发者已经习惯把 AI 当成问答入口。但本周的更新更像另一个阶段：GitHub Copilot for JetBrains 把 Codex、Claude、BYOK、自定义模型、Hooks 和 MCP 管理塞进 IDE；Visual Studio 也在把组织级 custom agents、模型管理和用量入口放到同一个工作面上。

这说明“会不会生成代码”已经不是唯一问题。更重要的是：这个 agent 用哪个模型、拿哪些工具、何时需要批准、能不能换供应商、出了问题从哪里看日志。对普通开发者来说，AI 工作台越完整，越能少记命令；对组织来说，界面越方便，越不能省掉权限边界。

### 2. BYOK 不是省钱按钮，而是架构选择

BYOK 和自定义模型支持看起来像采购选项，其实会改变开发环境的责任结构。模型由谁提供，账单归谁，日志在哪里，失败后谁解释，都会影响 agent 能不能进入更关键的流程。

这也是为什么 GitHub 在同一组 JetBrains 更新里同时补了本地沙箱、审批模式、debug logs 和自定义项管理。模型可替换是好事，但替换之后仍要能限制工具调用、追踪会话、复用规则文件。否则 BYOK 只会把“平台默认”换成“自己配置的黑盒”。

### 3. AI 采用度开始回到软件工程本身

Copilot usage metrics 新增 PR 首次评审时间和评审轮次，是一个很实在的信号。AI 到底有没有帮上忙，不该只看“生成了多少行代码”，还要看代码是否更快进入评审、更少来回、更稳合并。

这类指标也有边界：只看合并的 PR，会漏掉被关闭或长期悬着的工作；只看速度，也可能忽视质量。更好的做法是把它和回滚率、缺陷率、安全扫描结果一起看。AI 能加速，但软件工程最终还是要对交付结果负责。

---

## 科技与 AI 动态

### 1. [GitHub Copilot for JetBrains 扩展 BYOK：IDE 正在变成 agent 编排层](https://github.blog/changelog/2026-07-14-github-copilot-for-jetbrains-expands-byok-capabilities/)

![GitHub Copilot for JetBrains BYOK 更新页](/images/issues/023/news-copilot-jetbrains-byok.png)

GitHub 7 月 14 日更新 Copilot for JetBrains，扩展 bring your own key custom endpoint support，允许配置 OpenAI-compatible custom endpoints；同时补齐插件管理、Claude agent provider customizations、本地沙箱、Copilot CLI debugger skill 等能力。7 月 7 日的同系列更新还把 Codex 作为 agent provider 推入 public preview，并加入 Hooks、MCP server 管理、Copilot CLI 审批设置和 Claude agent debug logs。

这不是一个单点功能，而是在把 IDE 变成 agent 控制台。开发者可以在熟悉的编辑器里选择 agent、模型、工具和权限；组织也能逐步把默认策略、插件来源、模型供应商和审计线索收拢。边界在于：能力越集中，配置错误的影响越大，建议先用小仓库验证审批模式和沙箱行为。

### 2. [Visual Studio 2026 Insiders：组织级 custom agents 进入 IDE](https://learn.microsoft.com/en-us/visualstudio/releases/2026/release-notes-insiders)

![Visual Studio Insiders 七月更新页](/images/issues/023/news-visual-studio-custom-agents.png)

Microsoft Learn 7 月 14 日发布 Visual Studio 2026 Insiders 更新，GitHub organization owners 可以在组织范围添加 custom agents；Visual Studio 会在 agent picker 中显示这些组织级 agent，并支持查看描述和定义文件。本次更新还加入 Copilot plan usage 入口、模型管理视图、Git submodule、worktrees、提交后 Copilot review 等能力。

这对 Windows / .NET 开发者尤其实际：agent 不再只是每个仓库各配一份规则，而是可以作为组织能力分发到 IDE。好处是标准化，风险是“一次配置影响很多项目”。适合先把代码规范、构建检查、迁移助手这类低风险 agent 做成共享项，再逐步扩到改代码和提 PR。

### 3. [Copilot usage metrics 新增评审时间与评审轮次：AI 采用开始看下游结果](https://github.blog/changelog/2026-07-07-add-review-cycles-and-time-to-adoption-phases-in-the-usage-api/)

![Copilot usage metrics 评审指标更新页](/images/issues/023/news-copilot-review-metrics.png)

GitHub 7 月 7 日更新 Copilot usage metrics API，在 AI adoption phase breakdown 中加入两个代码评审速度指标：`avg_pull_requests_minutes_to_review` 和 `avg_pull_requests_review_cycles`。它们分别衡量 PR 创建到首次评审的中位时间，以及合并前经历的中位评审次数，并且只统计已合并 PR。

这让 AI 采用度从“谁开了 Copilot”向“交付链路有没有变快”靠近。对工程管理者来说，这比单纯看建议行数更有价值；对开发者来说，也提醒我们不要把 AI 生成量当成果。真正值得观察的是：更快是否伴随更少返工，还是只是把问题推给评审环节。

### 4. [Secret scanning custom patterns API GA：安全规则开始可以被自动化管理](https://github.blog/changelog/2026-07-13-create-and-manage-secret-scanning-custom-patterns-via-rest-api/)

![Secret scanning custom patterns API 更新页](/images/issues/023/news-secret-scanning-api.png)

GitHub 7 月 13 日宣布，secret scanning custom patterns 的 REST API generally available，安全团队可以在 repository、organization 和 enterprise 级别创建、编辑、删除和管理自定义模式。当前 dry run 和最终发布仍需在 UI 中完成，但基础 CRUD 已可进入自动化流程。

这条看似不耀眼，却很贴近真实治理。很多组织的 secret 不只是不该出现的云厂商 key，还包括私有 token、旧系统凭据、临时口令格式。API 化后，安全规则可以跟着平台迁移、组织结构和审计流程一起管理。边界是误报成本：自定义模式上线前仍要小范围 dry run，避免把正常开发流程堵住。

### 5. [Repository admins 可以 archive pull requests：社区治理多了一个中间档](https://github.blog/changelog/2026-07-16-repository-admins-can-archive-pull-requests)

![GitHub archive pull requests 更新页](/images/issues/023/news-archive-pr.png)

GitHub 7 月 16 日上线 pull request archive 功能，仓库管理员可以把 PR 从公开视图中移除而不永久删除。被 archive 的 PR 会关闭并锁定，只对仓库管理员可见；非管理员访问原 URL 会得到 404。管理员也可以用 `is:archived` 过滤器做后续分拣。

它适合处理垃圾 PR、滥用内容、法律或政策场景下“不适合公开但又不能直接删除”的记录。开源维护者会多一个治理缓冲层，但也要谨慎使用：archive 不应替代透明的技术讨论，最好用于明确违反规则或有合规要求的内容。

---

## 世界之最

### 1. 世界最长公路隧道：莱达尔隧道

![莱达尔隧道](/images/issues/023/world-laerdal-tunnel.jpg)

*莱达尔隧道位于挪威，全长约 24.5 公里，以超长距离和分段照明设计闻名。*

长隧道的难点不只是“挖通”，还要让驾驶者在漫长封闭空间里保持方向感和安全感。长任务 agent 也类似：真正难的是在中途保留状态、给出检查点，并让人知道它走到哪一步。

### 2. 世界最高不间断瀑布：安赫尔瀑布

![安赫尔瀑布](/images/issues/023/world-angel-falls.jpg)

*安赫尔瀑布位于委内瑞拉卡奈玛国家公园，落差接近 979 米。*

它壮观的地方在于能量从高处一路释放。AI 工作流也需要控制这种“落差”：从目标到操作之间跨得越大，越要有分段验证、权限收口和可回滚路径。

### 3. 世界最长洞穴系统：猛犸洞

![猛犸洞](/images/issues/023/world-mammoth-cave.jpg)

*美国猛犸洞系统已测绘长度超过 680 公里，是世界最长已知洞穴系统。*

洞穴地图不是一次画完的，而是在长期探索中不断修正。大型代码库和知识库也是这样：agent 要想可靠工作，不能只靠一次性上下文，还需要可更新的索引、记录和事实边界。

### 4. 世界最大单体光学望远镜之一：加那利大型望远镜

![加那利大型望远镜](/images/issues/023/world-gtc.jpg)

*加那利大型望远镜位于西班牙拉帕尔马岛，主镜由多块镜面拼接而成。*

拼接镜面的启发很直接：更大的能力往往来自协同校准，而不是单块材料无限变大。多 agent 系统也一样，关键是接口、校准和观测结果能不能对齐。

### 5. 世界级大型温室综合体：伊甸园项目

![伊甸园项目温室](/images/issues/023/world-eden-project.jpg)

*英国伊甸园项目用多个巨大生物群落温室模拟不同生态环境。*

温室不是把植物关起来，而是创造一套可控环境。coding agent 的沙箱、容器和权限策略也是这个思路：让实验能发生，但把温度、湿度和边界先管住。

---

## 开源工具

### 1. [OpenHands Agent Canvas：把编码 agent 放进可视化工作区](https://github.com/OpenHands/agent-canvas)

![OpenHands Agent Canvas 项目页](/images/issues/023/tool-agent-canvas.png)

Agent Canvas 是 OpenHands 推出的开源 AI coding platform，目标是本地启动、连接工具，并在一个画布式工作区里组织 agent 开发流程。它适合希望把多个 agent、仓库和任务状态放在同一界面管理的开发者，而不是只在终端里看日志滚动。

上手门槛中等：需要理解 agent 运行环境、凭据、仓库权限和本地服务。它不适合“偶尔问几句代码”的场景；但如果你已经在并行跑多个 coding agent，能看到任务、工件和结果会比只看对话更稳。

### 2. [container-use：给 coding agent 每人一间隔离工位](https://github.com/dagger/container-use)

![container-use 项目页](/images/issues/023/tool-container-use.png)

container-use 是 Dagger 做的 agent 开发环境工具，核心思路是让每个 agent 在独立容器和独立 git branch 中工作，减少并行任务互相污染。它解决的是 agent 时代很具体的烦恼：多个自动化会话同时改代码、跑服务、装依赖时，环境很容易乱。

它适合已经把 coding agent 用在真实仓库里的开发者，尤其是需要并行探索方案、快速丢弃失败分支的场景。门槛在 Docker、Git 和对分支流程的理解；小脚本和一次性修 bug 不一定需要它。

### 3. [Claude Code Action：把 Claude Code 接到 Issue 和 PR 里](https://github.com/anthropics/claude-code-action)

![Claude Code Action 项目页](/images/issues/023/tool-claude-code-action.png)

Claude Code Action 是 Anthropic 的 GitHub Action，可以根据 `@claude` 提及、issue 分配或显式 prompt 启动 Claude Code 自动化。它适合把代码解释、PR 辅助、文档更新、测试修复这类任务接进 GitHub 协作流。

上手成本主要在权限设计：Action 要读仓库、写评论、可能还要改代码，凭据和触发条件要先收紧。适合维护者明确知道哪些任务可以自动化；不适合把所有 PR 都默认交给 agent 改，尤其是安全敏感仓库。

### 4. [Repomix：把仓库打包成 AI 友好的上下文](https://github.com/yamadashy/repomix)

![Repomix 项目页](/images/issues/023/tool-repomix.png)

Repomix 可以把整个代码仓库打包成 XML、Markdown、JSON 或纯文本，方便喂给 Claude、ChatGPT、Gemini 等模型。它解决的是一个朴素问题：很多 agent 失败不是因为模型不聪明，而是上下文给得乱、缺、重复或超限。

它适合代码审查、架构咨询、迁移评估和离线分析。门槛较低，但要注意过滤敏感文件、生成物和超大依赖目录。小七的建议是把 `repomix.config` 当成项目文档的一部分维护，不要每次临时凭感觉打包。

### 5. [Graphiti：给 agent 记忆加上时间维度](https://github.com/getzep/graphiti)

![Graphiti 项目页](/images/issues/023/tool-graphiti.png)

Graphiti 是 Zep 的开源 temporal knowledge graph 框架，用于为 AI agent 构建可实时更新的上下文图。它关注的不只是“记住了什么”，还包括事实何时成立、是否仍然有效，以及新信息如何覆盖旧信息。

它适合客服、研究助手、销售支持、长期项目助理这类需要持续记忆的应用。上手成本偏高，因为你要定义事件、实体、关系和检索策略；但只要 agent 开始跨周工作，时间感就会从锦上添花变成基本能力。

---

## 本周冷知识 / 彩蛋

- 🥚 **冷知识 1**：福尔柯克轮式升船机每次旋转约半圈，就能把船提升约 24 米；它靠配重和平衡减少能耗，不是蛮力硬举。
- 🧠 **冷知识 2**：莱达尔隧道中设置了特殊照明洞室，帮助驾驶者在超长隧道中获得节奏变化。长任务 agent 也需要这种“中途休息点”。

---

## 小七的碎碎念

这周的 AI 更新没有那种一眼炸裂的模型名，但很像在铺地板、装插座、画消防通道。

真正能长期用的工具，往往不是最会表演的那个，而是出问题时你知道怎么停、怎么查、怎么回到上一版的那个。

---

## 互动钩子

> **本周问题：如果要给一个 coding agent 工作台先补一项能力，你会选沙箱、审批、日志、模型路由，还是成本看板？**

---

## 本周行动清单

- [ ] 给常用 AI 编码工具列一张权限表：能读什么、能写什么、什么时候需要确认。
- [ ] 挑一个仓库试跑隔离分支或容器化 agent 环境，记录它和普通 worktree 的差异。
- [ ] 把一个高频 prompt 固化成可复用规则或 skill，并写明适用范围和禁用场景。
- [ ] 在 PR 数据里观察一次首次评审时间、评审轮次和 AI 参与方式之间的关系。
- [ ] 为 secret scanning 自定义模式选一个低风险样本集，先 dry run 再考虑推广。
