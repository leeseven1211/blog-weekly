---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 026 期）：会做事之后，Agent 要会交接班
  - - meta
    - property: og:description
      content: 本周 Codex、Copilot、Gemini Robotics 和 OpenAI API 迁移窗口都在提醒开发者：agent 的下一步不是只追求更强回答，而是会交接、可恢复、能迁移、可观测。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/026/cover-falkirk-wheel.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/026/cover-falkirk-wheel.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '1920'
  - - meta
    - property: og:image:height
      content: '1440'
  - - meta
    - property: og:image:alt
      content: 第 026 期封面图：苏格兰福尔柯克轮
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/026/cover-falkirk-wheel.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/026/cover-falkirk-wheel.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-026
---

# 小七的周刊（第 026 期）：会做事之后，Agent 要会交接班

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **Agent 开始有工作台感**：会话分区、并行工作区、回退、工具耗时和元素级反馈，把“模型回答”变成可接续的任务现场。
2. **模型正在变成可替换依赖**：Copilot 模型退役、OpenAI API 迁移窗口和 Codex 插件生态都在提醒开发者别把流程绑死在某个模型名上。
3. **物理世界也在接入 agent 思路**：Gemini Robotics ER 2 把视频理解、多步规划和多机器人协作推到开发者入口，自动化开始从屏幕走向现场。

---

## 封面图

![苏格兰福尔柯克轮船舶升降机](/images/issues/026/cover-falkirk-wheel.jpg)

封面图：苏格兰福尔柯克轮。它把两条不同高度的运河接起来，用旋转而不是蛮力完成“交接”；本期的 agent 也像这样，真正难的不是单次抬升，而是把任务、上下文和控制权稳稳交到下一段流程里。

---

## 本周短谈

### 1. Agent 的新能力，越来越像“交接能力”

这周几个更新放在一起看，主线很清楚：agent 不再只是回答问题，而是在承担一个可恢复、可转交、可继续追踪的工作过程。GitHub Copilot CLI 有了多会话侧栏、实验性的 `/worktree` 和不用 Git 也能回退的 `/rewind`；Codex CLI 开始整理长对话、支持插件目录；OpenAI 也在介绍 [workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)，强调共享 agent、组织权限和跨工具流程。

这对普通开发者的影响很实际。以后评价一个 agent，不只看它能不能一次性写出答案，还要看它中断后能不能接上、并行实验会不会污染主线、换人或换模型时上下文会不会丢。强模型是发动机，交接机制才是工作台。

### 2. “默认模型”正在变成运维变量

GitHub 宣布 9 月 1 日将在 Copilot 里退役一批模型，OpenAI 的文档也把模型退役通知期、Assistants API 关停和 Responses API 迁移摆到开发者面前。过去很多人把模型名当成配置里的一个字符串，现在看，它更像数据库版本、云服务 API 或浏览器内核：会升级，会下线，也会改变成本和行为。

这不是坏事。模型平台快速迭代，开发者才能拿到更强能力和更低成本。真正的风险是应用没有迁移测试、没有回滚路径、没有质量基线。把模型升级当成发布流程的一部分，会比临近截止日期再改配置稳得多。

### 3. 物理 agent 的边界更硬

Gemini Robotics ER 2 很有象征性：它把视频理解、任务编排、工具调用和多机器人协作带到真实空间里。屏幕里的 agent 做错了，常见后果是改坏文件、跑错命令、浪费预算；机器人 agent 做错了，后果可能是碰撞、损坏和现场安全问题。

所以这条新闻不只是“机器人更聪明了”。它提醒软件读者，agent 的工程边界会越来越具体：什么任务可以自动执行，什么动作必须确认，什么状态要实时观察，失败以后怎样停下来。越接近现实世界，越不能只靠提示词维持秩序。

---

## 科技与 AI 动态

### 1. [Codex CLI 0.147.0：插件、会话整理和 MCP 新协议一起进场](https://developers.openai.com/codex/changelog)

![Codex changelog 页面显示 Codex CLI 0.147.0](/images/issues/026/news-codex-changelog.png)

OpenAI 8 月 7 日发布 Codex CLI 0.147.0。更新包括可安装的 Agent Plugins、跨本地/个人/workspace/远程目录搜索插件、长对话分区浏览、`--approve-for-me` 自动审核批准、导入 Cursor 管理的 skills，以及对 MCP 2026-07-28 协议的 opt-in 支持。修复项里还有显示命令和回放历史中的 secret / bearer token 脱敏。

这说明 coding agent 正在从单一 CLI 变成一套可扩展运行环境。插件和 skills 能沉淀经验，MCP 新协议能改善工具发现和多轮请求，历史整理能降低长任务的上下文摩擦。边界也要看清：自动批准适合低风险重复操作，不适合权限敏感的发布、删除和生产改动。

### 2. [GitHub Copilot 每周更新：会话、worktree、rewind 和浏览器反馈都在补“任务现场”](https://github.blog/changelog/2026-08-07-github-copilot-weekly-releases-august-3/)

![GitHub Copilot weekly releases 发布页](/images/issues/026/news-copilot-weekly.png)

GitHub 8 月 7 日汇总了 Copilot app、CLI 和 VS Code 1.132 的一组更新。Copilot app 的 Auto 会显示完成请求所用模型、AI credit 和缓存细节；CLI 增加 Sessions sidebar、实验性的 `/worktree`、不用 Git 也能恢复会话和文件状态的 `/rewind`，并在时间线里显示工具调用耗时；VS Code 集成浏览器则支持对网页元素逐个标注反馈给 agent。

这些功能看起来零散，其实都在解决同一个问题：agent 工作需要可观察、可分叉、可回退、可精确反馈。对开发者来说，`/worktree` 和 `/rewind` 尤其值得关注，它们把“让 agent 放手试试”从心理负担变成工程动作。边界是实验功能仍要配合代码审查和测试，不能把回退按钮当成质量保证。

### 3. [Gemini Robotics ER 2：机器人 agent 开始看连续视频、规划多步任务](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-2/)

![Gemini Robotics ER 2 发布页中的机器人实物图](/images/issues/026/news-gemini-robotics-er2.png)

Google DeepMind 7 月 30 日发布 Gemini Robotics ER 2，定位为面向机器人的 embodied reasoning model。它可以通过连续视频流跟踪进度、在执行动作的同时思考下一步、调用 Google Search 或自定义函数，并把高层计划交给底层 VLA 模型执行。Google 还提到多机器人协作能力，并通过 Gemini API、Google AI Studio 向开发者开放，企业平台里提供 private preview。

这条新闻把“agent”从软件工具推向物理协作。对开发者的启发不是马上买机器人，而是重新理解任务编排：看见状态、判断进度、处理异常、协调多个执行者，都是软件 agent 也会遇到的问题。边界更明显，物理动作需要更强的安全策略和测试环境，不能用聊天产品的容错标准来要求机器人。

### 4. [Copilot 9 月退役一批模型：模型选择开始像依赖升级](https://github.blog/changelog/2026-07-31-upcoming-august-2026-model-deprecations-in-github-copilot/)

![GitHub Copilot 模型退役公告页](/images/issues/026/news-copilot-model-deprecations.png)

GitHub 7 月 31 日宣布，将在 2026 年 9 月 1 日退役多个 Copilot 体验中的模型，覆盖 Copilot Chat、inline edits、ask / agent modes 和 code completions。列表包括 Gemini 3.1 Pro、Claude Opus 4.5/4.6、Claude Sonnet 4.5/4.6、Raptor Mini 等，并给出 Gemini 3.6 Flash、Claude Opus 5、Claude Sonnet 5、MAI-Code-1-Flash 等替代建议。

这类公告最容易被当成“平台通知”划过去，但它其实是架构提醒。凡是把模型名写进脚本、CI、IDE policy 或评测报告的地方，都应该有清单和迁移测试。对企业管理员来说，还要检查模型策略是否放行替代模型；对个人开发者来说，至少要知道常用工作流切换模型后，输出风格、速度和成本会不会明显变化。

### 5. [OpenAI API 迁移窗口临近：Responses API 成为新项目默认选择](https://platform.openai.com/docs/deprecations)

![OpenAI Developers deprecations 文档页](/images/issues/026/news-openai-deprecations.png)

OpenAI 的 deprecations 文档继续强调模型和端点退役规则，其中 Assistants API 将在 2026 年 8 月 26 日关闭；迁移指南则建议新项目优先使用 Responses API。Responses API 把 web search、file search、computer use、code interpreter、remote MCP 和自定义函数放进统一接口，也支持多轮状态和 multimodal 输入。

这不是简单换 SDK 名称。Responses API 更像把“模型调用”升级成“工具调用循环”，适合需要搜索、文件、代码执行和 MCP 的 agent 应用。建议正在维护旧 Assistants API 项目的读者先做最小迁移验证：挑一条真实任务，确认输入输出、工具权限、状态保存和成本曲线，再逐步替换核心流程。

---

## 世界之最

### 1. 世界最大的岛屿：格陵兰岛

![格陵兰岛卫星影像](/images/issues/026/world-greenland.jpg)

*格陵兰岛面积约 216 万平方公里，通常被列为世界最大的岛屿。*

它大到足以让“岛屿”这个词显得很轻。agent 系统里的上下文也类似：越大越不能靠一次性塞满，真正重要的是分层、索引、检索和压缩，知道何时取全局，何时只拿局部。

### 2. 世界最长大陆山脉：安第斯山脉

![安第斯山脉中的拉斯卡尔火山](/images/issues/026/world-andes.jpg)

*安第斯山脉沿南美洲西缘绵延，是世界最长的大陆山脉。*

长山脉不是一条直线，而是由高原、火山、峡谷和气候带组成的连续系统。复杂工作流也一样，agent 能不能走完整段路，取决于每一段交接处是否清楚，而不是开头那一步多漂亮。

### 3. 世界最宽瀑布之一：孔恩瀑布群

![老挝孔恩瀑布群](/images/issues/026/world-khone-phapheng.jpg)

*孔恩瀑布群位于湄公河下游，常被称为世界最宽的瀑布之一。*

瀑布的壮观来自分流：水不是只从一个点落下，而是被地形拆成许多支路。agent 任务也会这样分叉，搜索、编码、验证、汇报各走一条支路，最后必须重新汇合成可信结论。

### 4. 世界最大的船闸之一：基尔德雷赫特船闸

![安特卫普港基尔德雷赫特船闸中的货轮](/images/issues/026/world-kieldrecht-lock.jpg)

*比利时安特卫普港的基尔德雷赫特船闸长约 500 米，是世界级超大型船闸。*

船闸的关键不是让船“更快”，而是让不同水位的系统安全相遇。把它放到软件里看，就是权限、环境和状态转换：agent 可以跨工具行动，但每次跨界都应该有闸门和记录。

### 5. 世界最大的图书馆：美国国会图书馆

![美国国会图书馆主阅览室](/images/issues/026/world-library-congress.jpg)

*美国国会图书馆以庞大的馆藏规模著称，常被列为世界最大的图书馆。*

信息多不等于知识可用。图书馆真正厉害的是分类、索引、借阅规则和读者路径。AI 应用也是这样，堆更多文档不一定更聪明；能检索、能引用、能追溯，才叫有用的上下文。

---

## 开源工具

### 1. [Codex CLI：把 coding agent 放回终端，也放进插件生态](https://github.com/openai/codex)

![openai/codex 仓库页](/images/issues/026/tool-codex.png)

Codex CLI 是 OpenAI 的本地 coding agent，可以在终端运行，也能配合 IDE、桌面应用和云端 Codex 使用。仓库 README 提供 npm、Homebrew、独立安装器和 GitHub Releases 等安装路径，适合已经习惯命令行开发的人把 agent 纳入现有项目。

它的优势是贴近真实开发环境，能看文件、改代码、跑命令；新近的插件和会话能力则让它更像可配置工作台。上手成本中等，最好在有测试和 Git 习惯的项目里使用。对生产仓库，建议先从只读分析、测试补齐和小范围重构开始。

### 2. [Pydantic AI：用类型系统约束 agent 应用](https://github.com/pydantic/pydantic-ai)

![pydantic/pydantic-ai 仓库页](/images/issues/026/tool-pydantic-ai.png)

Pydantic AI 是 Pydantic 团队维护的 Python agent framework，目标是把类似 FastAPI 的开发体验带到 GenAI 和 agent 应用里。它强调 model-agnostic、类型安全、结构化输出、依赖注入，并与 Pydantic Logfire / OpenTelemetry 观测体系结合。

它适合 Python 团队做可维护的 LLM 应用，尤其是需要结构化返回、工具调用和评测观测的场景。门槛不算高，但前提是愿意把 schema、类型和错误处理认真写清楚。不适合只想快速拼一个聊天页面的读者，适合把 agent 当长期代码资产维护的人。

### 3. [best-of-Agent-Harnesses：先比较运行框架，再比较模型](https://github.com/RyanAlberts/best-of-Agent-Harnesses)

![best-of-Agent-Harnesses 仓库页](/images/issues/026/tool-best-agent-harnesses.png)

`best-of-Agent-Harnesses` 是一个面向 agent harness、编排框架和运行技术的精选列表，提供可搜索站点、JSON、`llms.txt` 和 MCP server。它把 harness 定义为把模型变成持续行动系统的运行层，关注调度、权限、记忆、恢复和策略执行。

这类列表的价值在于把讨论从“哪个模型更强”拉回“模型在什么运行环境里更稳”。适合准备选型 agent 框架、做项目评测或理解行业术语的读者。边界是精选列表不是基准测试，真正落地前仍要用自己的任务集验证恢复、工具权限和成本。

### 4. [robotics-samples：从示例开始理解 Gemini Robotics ER 2](https://github.com/google-gemini/robotics-samples)

![google-gemini/robotics-samples 仓库页](/images/issues/026/tool-robotics-samples.png)

`google-gemini/robotics-samples` 收集了 Gemini Robotics 相关示例，包括 Getting Started notebook。它不是一个通用机器人框架，更像官方样例入口：告诉开发者如何配置模型、构造提示、让机器人理解任务，并把高层推理接到具体执行链路。

对没有机器人硬件的读者，它仍然值得浏览，因为这里能看到“物理 agent”与普通聊天应用的差别：输入不只是文本，输出也不只是答案，中间还有感知、规划、动作和安全约束。上手成本偏高，适合做机器人、仿真或多模态自动化的读者收藏。

---

## 本周冷知识 / 彩蛋

- 🥚 **冷知识 1**：福尔柯克轮连接的两条运河高度差约 24 米，它一次旋转就能把船从一段水路交给另一段水路，能耗却比想象中低很多。
- 🧠 **冷知识 2**：美国国会图书馆的价值不只是“书多”，还在于长期维护目录、分类、馆藏规则和检索系统。AI 的知识库如果只有堆料，没有目录，也会很快变成迷宫。

---

## 小七的碎碎念

这周最有意思的词不是“更强”，而是“继续”。

一个 agent 能把事做完当然好，但更难的是暂停后还能继续，换模型后还能继续，换入口后还能继续。

能接班的自动化，才比较像可以托付的工具。

---

## 互动钩子

> **本周问题：你现在最想给 agent 补上的能力，是回退、并行工作区、统一插件、模型迁移测试，还是工具调用日志？**

---

## 本周行动清单

- [ ] 列出项目里硬编码的模型名、agent 配置和 API endpoint，标出 30 天内需要迁移或复测的项。
- [ ] 给一个常用 AI 工作流补最小评测集，至少覆盖成功、失败、权限不足和输出格式异常四类情况。
- [ ] 试一次隔离分支或 worktree，让 agent 做低风险改动，再观察回退和合并成本。
- [ ] 检查工具调用日志是否能回答三件事：调用了什么、用了多久、失败后发生了什么。
- [ ] 把常用提示、规范或脚手架整理成可复用插件 / skill / 模板，减少每次重新解释上下文。
