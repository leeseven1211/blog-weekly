---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 024 期）：AI Agent 开始接工单，也开始过门禁
  - - meta
    - property: og:description
      content: 本周 Linear、GitHub Issues、MCP 和 Code Quality 都在补同一件事：agent 可以进入真实工作流，但需要工单、门禁、规范测试和质量账本一起托住。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/024/cover-schwebebahn.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/024/cover-schwebebahn.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '1920'
  - - meta
    - property: og:image:height
      content: '1189'
  - - meta
    - property: og:image:alt
      content: 第 024 期封面图：德国伍珀塔尔悬挂铁路
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/024/cover-schwebebahn.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/024/cover-schwebebahn.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-024
---

# 小七的周刊（第 024 期）：AI Agent 开始接工单，也开始过门禁

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **Agent 正在进入工单系统**：Copilot cloud agent 接入 Linear 后，问题描述、分支、模型、进度流和 PR 评审开始连成一条异步交付线。
2. **自动化开始带上理由和置信度**：GitHub Issues 的 approvals、confidence 和 rationale 说明，平台不再只追求“自动改”，也在补“为什么改、谁确认”。
3. **质量与成本回到台前**：MCP conformance tests、Code Quality GA 和 Gemini 3.6 Flash 都在提醒开发者，agent 时代拼的不只是模型能力，还有规范、账单和可验证结果。

---

## 封面图

![德国伍珀塔尔悬挂铁路](/images/issues/024/cover-schwebebahn.jpg)

封面图：德国伍珀塔尔悬挂铁路。车厢看起来悬在空中，真正让它可靠运行的却是上方那条确定的轨道；本期的 AI agent 也像这样，越能独立跑，越需要清楚的工单、权限和回看路径。

---

## 本周短谈

### 1. Agent 从“会做事”走向“能被派活”

过去几个月，AI 编码工具的重点常常是模型、上下文和 IDE 入口。本周更有意思的是入口换了：Linear issue 可以直接分配给 Copilot cloud agent，GitHub Issues 里的自动化也开始给出 rationale、confidence 和 approvals。这意味着 agent 不再只是聊天窗口里的助手，而是逐步进入团队已经在用的工单系统。

这一步很现实。普通技术读者不一定每天研究 agent 框架，但大多数团队都离不开 issue、PR、CI 和代码评审。如果 agent 能沿着这些对象工作，人类就不用发明一套全新的协作语言；反过来，平台也必须把“它为什么这么做”记录下来，否则自动化越勤快，维护者越难放心。

### 2. 置信度不是装饰，是协作界面

GitHub Issues 这次把自动化动作拆成 high、medium、low confidence，并允许低置信度改动停在建议面板里。这个细节值得记住：AI 系统不可能每次都给出同样确定的答案，真正可用的产品要把不确定性暴露给用户，而不是假装每一步都理所当然。

不过，GitHub 自己也提醒 approvals 是 workflow convenience，不是 server-side security control。换句话说，建议面板能改善协作体验，但不能替代权限最小化、审计和规则约束。开发者做自动化时可以借鉴这个设计：能自动的先自动，拿不准的先排队给人看。

### 3. 规范测试会变成 agent 基础设施的一部分

MCP 新规格准备走向 stateless，GitHub MCP Server 提前支持，并且官方 conformance tests 出现了。这类事情看起来不如新模型刺激，却很像互联网协议早期的兼容性测试：大家都说自己支持同一个协议，最后还是要靠测试套件把边界跑出来。

对开发者来说，这周最值得带走的动作不是立刻换工具，而是为现有 agent 集成补一层验证：MCP server 能不能跑官方 conformance，质量扫描能不能挡住明显问题，模型选择和费用有没有可见账单。agent 要进入生产流程，靠感觉验收会越来越不够用。

---

## 科技与 AI 动态

### 1. [Copilot cloud agent 接入 Linear：异步 agent 开始从工单入口接活](https://github.blog/changelog/2026-07-23-copilot-cloud-agent-for-linear-is-now-generally-available/)

![Copilot cloud agent for Linear 发布页](/images/issues/024/news-linear-agent.png)

GitHub 7 月 23 日宣布 Copilot cloud agent for Linear 一般可用。用户可以把 Linear issue 分配给 Copilot，agent 会分析 issue 内容、在由 GitHub Actions 支撑的临时开发环境中工作、打开 draft pull request，并把进度更新回 Linear activity timeline；完成后再请求用户做 PR review。

这条新闻的重点不是“又多接了一个工具”，而是 agent 正在贴近真实协作对象。Linear 里还能选择模型、指定 custom agent、设置 base branch 和 working branch，并通过评论继续 steering session。适合先放到小型 bugfix、文档更新和低风险重构里试用；边界是工单质量，issue 写得含糊，agent 很可能只是更快地产生含糊结果。

### 2. [GitHub Issues 加入 agent automation controls：自动化动作开始有理由、有置信度](https://github.blog/changelog/2026-07-23-agent-automation-controls-in-github-issues-in-public-preview/)

![GitHub Issues agent automation controls 发布页](/images/issues/024/news-issue-controls.png)

GitHub 7 月 23 日发布 GitHub Issues agent automation controls public preview，新增 approvals、confidence 和 rationale 三类能力。自动化可以先建议再应用，agent 会把 label、field、type、close、assignee 等支持动作标成 high、medium 或 low confidence，并记录每次变更的理由。

这对开源维护者和产品团队都很有价值：spam detection、triage、metadata backfill 这类重复劳动可以先交给 agent，但不确定的改动停下来等人确认。需要注意的是，GitHub 明确说明 approvals 不是安全控制；如果 agent 本身有权限直接改 issue，它仍然可能直接应用变更。真正的门禁仍要落在权限、规则和审计上。

### 3. [GitHub MCP Server 支持下一版 MCP 规格：协议开始补可伸缩和一致性测试](https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification/)

![GitHub MCP Server 支持下一版 MCP 规格发布页](/images/issues/024/news-mcp-stateless.png)

GitHub 7 月 23 日表示 GitHub MCP Server 已提前支持计划于 7 月 28 日发布的下一版 MCP 规格。新规格的核心变化是 stateless core，移除 sessions 和 initialize，让服务更容易扩展；GitHub MCP Server 也去掉了 Redis sessions，减少初始化和调用过程中的数据库读写。

这对 agent 开发者的影响很直接：MCP 不再只是“能接工具”的接口，而是走向更像基础协议的阶段。官方 conformance tests 也同时出现，可以帮助客户端、服务器和 SDK 验证实现是否真的符合规格。建议已经自建 MCP server 的团队把 conformance suite 加进发布前检查，避免协议升级时靠人工点几下误判兼容。

### 4. [GitHub Code Quality GA：AI 加速产出后，质量门禁开始单独计费](https://github.blog/changelog/2026-07-20-github-code-quality-is-now-generally-available/)

![GitHub Code Quality GA 发布页](/images/issues/024/news-code-quality.png)

GitHub Code Quality 7 月 20 日一般可用，面向 GitHub Enterprise Cloud 和 GitHub Team。它把 CodeQL 的确定性分析与 AI-assisted detection 结合，用来在 PR 中发现可维护性和可靠性问题，并由 Copilot Autofix 提供可审阅的修复建议。GitHub 披露，其内部工程组织在合并前解决了 67.3% 的 Code Quality findings。

真正值得注意的是产品边界和价格：Code Quality 是独立付费产品，按每位 active committer 每月 10 美元收费，AI-powered work 还会有 usage-based billing，确定性 CodeQL 分析也会产生 Actions compute costs。AI 让代码产出更快之后，质量检查、覆盖率门槛和规则集会成为更明确的预算项。

### 5. [Gemini 3.6 Flash 发布：大规模 agent 开始认真算延迟和 token](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)

![Google Gemini 3.6 Flash 发布页](/images/issues/024/news-gemini-flash.png)

Google 7 月 21 日发布 Gemini 3.6 Flash、3.5 Flash-Lite 和 3.5 Flash Cyber。Google 称 3.6 Flash 面向生产级 agentic workflows，在 Artificial Analysis Index 中相较 3.5 Flash 减少 17% 输出 token，并降低每输出 token 成本；3.5 Flash-Lite 则主打高吞吐，标称可达 350 output tokens/s。

这说明模型竞争已经不只看“最强”，还要看每个任务的成本、延迟和可靠性。对普通开发者来说，最实用的做法是把任务分层：低风险批处理、检索、文档解析可以用更快更便宜的模型；长链路编码、安全和数据分析再上更强模型。模型选择开始像数据库索引一样，是工程决策，不只是偏好。

---

## 世界之最

### 1. 世界最繁忙铁路车站：新宿站

![东京新宿站南口](/images/issues/024/world-shinjuku-station.jpg)

*东京新宿站以巨大的客流量闻名，是全球最繁忙的铁路枢纽之一。*

新宿站的难点不是“有站台”，而是让海量换乘在有限空间里保持秩序。agent 工作流也是这样：真正的挑战往往不是生成一个答案，而是把入口、状态、交接和异常路径安排清楚。

### 2. 世界最大铁路编组场：贝利编组场

![美国内布拉斯加州贝利编组场](/images/issues/024/world-bailey-yard.jpg)

*贝利编组场位于美国内布拉斯加州 North Platte，长期被称为世界最大的铁路编组场。*

编组场每天做的事很朴素：把车厢按目的地重新排列。软件团队的 issue triage 也类似，重要的不是把所有任务堆进列表，而是不断重排优先级、负责人和下一步动作。

### 3. 世界最深湖泊：贝加尔湖

![贝加尔湖奥尔洪岛附近水域](/images/issues/024/world-lake-baikal.jpg)

*贝加尔湖位于俄罗斯西伯利亚，是世界最深、蓄水量极大的淡水湖。*

深湖的启发是“表面平静不代表系统简单”。AI 平台也一样，用户看到的是一个按钮，下面却有模型路由、权限、缓存、日志、账单和安全策略。越深的系统，越需要可观测性。

### 4. 世界最高室内瀑布：星耀樟宜 Rain Vortex

![新加坡星耀樟宜 Rain Vortex](/images/issues/024/world-rain-vortex.jpg)

*Rain Vortex 位于新加坡星耀樟宜，被广泛称为世界最高室内瀑布。*

它把水流、屋顶、植物和游客动线整合在同一个空间里，看起来像景观，其实是复杂工程。好的 agent 产品也该如此：体验轻，后台重，最好让用户只感到顺手，而不是被流程本身绊住。

### 5. 世界最深金矿之一：姆波尼格金矿

![南非姆波尼格金矿](/images/issues/024/world-mponeng-mine.jpg)

*姆波尼格金矿位于南非，开采深度极大，常被列入世界最深矿井行列。*

深井作业靠的是分层、通风、温控和安全规程，而不是勇气。长任务 agent 也需要类似的安全结构：任务越深，越要有检查点、回滚点和明确的停止条件。

---

## 开源工具

### 1. [MCP Conformance：给 MCP 客户端和服务器跑规格验收](https://github.com/modelcontextprotocol/conformance)

![MCP Conformance 项目页](/images/issues/024/tool-mcp-conformance.png)

MCP Conformance 是 Model Context Protocol 官方的符合性测试框架，用来测试 MCP client 和 server 是否符合规格。它可以启动测试 server、捕获协议交互、跑 conformance checks，并输出详细结果；服务器侧也能通过指定 URL 接受测试。

它适合正在维护 MCP server、SDK 或内部工具网关的开发者。小项目手工连通一次就够用，但一旦 MCP 成为团队自动化入口，测试套件就比截图验收可靠得多。建议把它放进 release checklist，尤其是准备适配 stateless spec 的实现。

### 2. [linear-cli：把 Linear 工单带回命令行](https://github.com/schpet/linear-cli)

![linear-cli 项目页](/images/issues/024/tool-linear-cli.png)

linear-cli 可以在终端里 list、start、view、create Linear issues，并能根据 issue 创建分支、生成 PR 标题和正文。它同时理解 git 和 jj，对习惯在命令行里完成开发闭环的人很友好。

它的特别之处在于 agent friendly：仓库中包含 skill，能让 agent 创建 issue、更新状态并和代码工作流一起管理 Linear。适合 Linear 深度用户、CLI 重度用户和希望把工单动作脚本化的团队；不适合只是偶尔看一眼 Linear 看板的读者。

### 3. [Opik：给 LLM 应用和 agent 工作流做追踪与评测](https://github.com/comet-ml/opik)

![Opik 项目页](/images/issues/024/tool-opik.png)

Opik 是 Comet 开源的 LLM observability 与 evaluation 平台，覆盖 tracing、datasets、experiments、LLM-as-a-judge metrics、prompt management 和 production monitoring。它面向的不只是 RAG，也包括多步骤 agent 和工具调用链。

如果你正在把 agent 放进真实产品，Opik 这类工具的价值会很快变高：出错时需要知道是哪一步检索错、哪次工具调用慢、哪个 prompt 版本引入了回归。它的门槛在于你要愿意系统化采集 trace，而不是只在失败后翻聊天记录。

### 4. [goose：本地运行的开源通用 AI agent](https://github.com/aaif-goose/goose)

![goose 项目页](/images/issues/024/tool-goose.png)

goose 是 Agentic AI Foundation 下的开源 AI agent，提供桌面端、CLI 和 API，支持 OpenAI、Anthropic、Google、Ollama、OpenRouter、Azure、Bedrock 等多个 provider，也能通过 MCP 接入扩展。

它适合希望把 agent 放在本机、终端和桌面之间切换的开发者。优点是开放、可扩展、供应商选择多；代价是你需要自己管理模型凭据、扩展权限和运行环境。把它当成“可组装 agent 工作台”会比当成单一聊天助手更合适。

### 5. [AG-UI：把 agent 带进前端应用的交互协议](https://github.com/ag-ui-protocol/ag-ui)

![AG-UI 项目页](/images/issues/024/tool-ag-ui.png)

AG-UI 是一个轻量、事件驱动的 Agent-User Interaction Protocol，目标是标准化 AI agent 与用户界面的连接方式。它强调事件流、实时用户上下文和前端集成，并且定位为 MCP、A2A 的补充：MCP 给工具，A2A 让 agent 互通，AG-UI 负责面向用户的交互。

如果你在做带 agent 的产品界面，这个方向值得看。真正难的不是把一句模型回复显示出来，而是把中间状态、工具调用、等待确认、取消和局部 UI 更新处理好。AG-UI 适合前端和平台团队评估，不一定适合只做一次性脚本自动化。

---

## 本周冷知识 / 彩蛋

- 🥚 **冷知识 1**：伍珀塔尔悬挂铁路早在 1901 年就开始运行，车厢悬挂在轨道下方，看起来像“倒着开的电车”。
- 🧠 **冷知识 2**：贝利编组场每天处理的核心动作是分类和重组，这和 issue triage 很像：把复杂流量变成可执行的下一步。

---

## 小七的碎碎念

这周的关键词不是“更像人”，而是“更像一个能被管理的同事”。

会写代码当然重要，但会看工单、会说理由、会等确认、会留下痕迹，才是进入真实流程的门票。

---

## 互动钩子

> **本周问题：如果要把 agent 放进你的日常工作流，你最先要求它补哪项能力：工单接入、权限审批、质量检查，还是成本看板？**

---

## 本周行动清单

- [ ] 选一个低风险 issue，按“输入是否清楚、验收是否明确、权限是否可控”三项检查它能不能交给 agent。
- [ ] 给常用 MCP server 跑一次基本连通或 conformance 检查，记录协议版本和已知限制。
- [ ] 在团队代码评审里加一个质量维度：AI 生成代码是否增加了覆盖率、复杂度或可维护性风险。
- [ ] 把本月 AI 工具费用和使用场景对齐一次，区分探索、生产和高风险任务。
- [ ] 为一个重复 triage 流程写出“高置信度可自动、低置信度需确认”的规则。
