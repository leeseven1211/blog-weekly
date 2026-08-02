---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 025 期）：AI Agent 上生产线，护栏也要上生产线
  - - meta
    - property: og:description
      content: 本周 GitHub、Google 和 Anthropic 的更新把 agent 从炫技拉回工程化：统一策略、只读上下文、沙箱钩子、身份和安全复盘，决定它能不能进入生产流程。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/025/cover-oosterscheldekering.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/025/cover-oosterscheldekering.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '1920'
  - - meta
    - property: og:image:height
      content: '1080'
  - - meta
    - property: og:image:alt
      content: 第 025 期封面图：荷兰东斯海尔德防洪闸
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/025/cover-oosterscheldekering.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/025/cover-oosterscheldekering.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-025
---

# 小七的周刊（第 025 期）：AI Agent 上生产线，护栏也要上生产线

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **Agent 的入口更多了**：代码评审、Visual Studio、Gemini API 和企业级 agent 平台都在把 agent 接到开发者日常工具里。
2. **护栏开始产品化**：企业托管设置、只读 MCP 调用、沙箱 hooks、Agent Identity 和预算控制，正在变成 agent 功能的一部分。
3. **安全评测不能只靠“相信隔离”**：Anthropic 复盘三起网络安全评测事故，提醒所有做 agent 的团队把环境边界当成第一等需求。

---

## 封面图

![荷兰东斯海尔德防洪闸](/images/issues/025/cover-oosterscheldekering.jpg)

封面图：荷兰东斯海尔德防洪闸。它平时让水流通过，风暴来临时再把闸门关上；本期的 agent 也需要类似能力：不是永远禁止行动，而是知道什么时候放行、什么时候收口、什么时候留下记录。

---

## 本周短谈

### 1. 护栏不是拖慢 agent，而是让它能进生产线

这周几条更新放在一起看，关键词很一致：agent 的能力继续扩展，但平台更急着补“边界”。GitHub 让 Copilot app 和 cloud agent 读同一份 enterprise managed settings；Copilot code review 的 MCP 调用强调 read-only；Google Managed Agents 加入 environment hooks 和预算控制。这些都不是炫技功能，却决定 agent 能不能从个人实验进入团队流程。

对普通开发者来说，这个变化很实际。以后评价一个 agent 工具，不该只问“它会不会写代码”，还要问它能不能被统一配置、能不能解释上下文来源、能不能限制工具调用、能不能把风险操作停下来等确认。速度有用，但能被管理的速度更有用。

### 2. 科研软件正在把 agent 用成“工程放大器”

OpenAI 本周发布的 [scientific computing field report](https://openai.com/index/scientific-computing-agentic-ai/) 很值得读。报告整理了 8 个 agent 辅助科学计算项目，其中 5 个使用 Codex，3 个结合 Codex 和 Claude Code，场景从基因组文件库维护、性能优化到大规模语言迁移都有。重点不是“模型替代科学家”，而是研究者从手写实现转向定义目标、验收正确性和编排工作。

这给软件团队一个更朴素的参照：agent 最先稳定创造价值的地方，往往不是天马行空的新产品，而是那些长期欠账的测试、迁移、性能和维护工作。边界也很清楚，最终责任仍在人，尤其是科学、金融、安全这类对正确性敏感的场景。

### 3. 安全评测本身也要被评测

Anthropic 复盘三起网络安全评测事故时提到，一个模型在第三方评测环境中获得了原本不该有的互联网访问能力，并进一步访问了真实组织的生产系统。这个故事的重点不是“某个模型有多危险”，而是评测环境、任务提示、网络隔离和合作方边界之间出现了错位。

这件事对开发者有直接启发：任何能调用工具、能联网、能执行代码的 agent，都不能只靠 prompt 说“你在沙箱里”。沙箱要是真的沙箱，权限要是真的权限，日志要能回放，异常要能停止。越是高能力模型，越要把工程隔离做到可验证。

---

## 科技与 AI 动态

### 1. [GitHub Copilot app 和 cloud agent 纳入企业托管设置：策略开始跨客户端生效](https://github.blog/changelog/2026-07-27-enterprise-managed-settings-now-apply-to-the-github-copilot-app/)

![GitHub Copilot enterprise managed settings 发布页](/images/issues/025/news-copilot-managed-settings.png)

GitHub 7 月 27 日宣布，enterprise managed settings 现在适用于 GitHub Copilot app 和 Copilot cloud agent。企业所有者可以通过 `managed-settings.json` 定义一组统一策略，包括允许哪些插件、可以从哪些 marketplace 安装、是否允许开发者绕过命令和文件访问前的 approval prompts，以及是否把自动模型选择设为新会话默认项。

这个更新的价值在于补齐“最薄弱客户端”。当开发者同时使用 VS Code、CLI、桌面 app 和 cloud agent，任何一个入口游离在策略外，都会变成治理缺口。边界是 cloud agent 目前主要读取插件和 marketplace 相关设置，bypass-prompt 控制仍只适用于交互客户端；企业落地时还要继续用权限、仓库规则和审计日志兜底。

### 2. [Copilot code review 的 Agent skills 和 MCP 一般可用：评审开始读团队上下文](https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/)

![Copilot code review agent skills and MCP 发布页](/images/issues/025/news-copilot-review-skills.png)

GitHub 7 月 29 日宣布，Copilot code review 对 Agent skills 和 MCP servers 的支持一般可用，覆盖 Copilot Pro、Pro+、Business 和 Enterprise 用户。团队可以在 `.github/skills` 下放置 `SKILL.md`，把内部工具、代码标准和仓库特定规则带进评审；MCP server 则能从 issue tracker、文档系统、service catalog 等外部平台拉取上下文。

这里最值得注意的细节是安全边界：GitHub 表示 Copilot code review 执行的 MCP tool calls 会限制为 read-only，并且评论会标注是否使用了 skills 或 MCP context。这让 AI 评审从“看 diff 猜意图”向“读取团队语境”迈了一步。建议先把它用于规范提醒、上下文补全和低风险建议，真正影响合并的规则仍要保留确定性检查。

### 3. [Gemini API Managed Agents 加入 hooks 和预算控制：沙箱里也要有闸门](https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/)

![Gemini API Managed Agents 发布页](/images/issues/025/news-gemini-managed-agents.png)

Google 7 月 28 日宣布 Gemini API Managed Agents 默认使用 Gemini 3.6 Flash，并新增 environment hooks、model selection、free tier access、budget controls 和 scheduled triggers。Managed Agents 可以在隔离云沙箱中协调推理、代码执行、包安装、文件管理和网页检索；hooks 则允许开发者在工具调用前后阻止、lint 或审计操作。

这类能力说明 agent 平台正在从“给模型一个工具箱”走向“给工具箱装门禁”。预算控制适合防止长任务烧穿账单，scheduled triggers 适合周期性巡检，hooks 则适合把组织规则放在模型动作前。边界是平台托管降低了运维门槛，却不会自动替你定义什么是危险动作，规则本身仍要工程团队认真写。

### 4. [Gemini Enterprise Agent Platform 扩展 Runtime、Identity 和 Memory：企业 agent 开始补基础设施](https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise-agent-platform)

![Gemini Enterprise Agent Platform 更新页](/images/issues/025/news-gemini-agent-platform.png)

Google Cloud 本周介绍 Gemini Enterprise Agent Platform 的一组更新，强调 Agent Runtime、Agent Identity、Agent Memory Bank 等能力面向更广泛用户开放，并把 CodeMender 这类托管代码安全 agent 放进同一条产品叙事里。它关注的不是一次聊天，而是长期运行、带身份、带记忆、能被企业发布和管理的 agent。

这条新闻适合产品和平台团队关注。聊天机器人常常靠会话体验取胜，企业 agent 则更像后台服务：要有运行环境、身份模型、记忆结构、发布路径和安全策略。对中小团队来说，不必马上追完整平台，但可以先借鉴它的清单：身份是谁、数据存在哪、谁能调用、失败后谁接手。

### 5. [Anthropic 复盘三起网络安全评测事故：高能力模型需要真隔离](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)

![Anthropic 网络安全评测事故复盘页](/images/issues/025/news-anthropic-cyber-evals.png)

Anthropic 披露，在回顾 141,006 次可能获得互联网访问的网络安全评测运行后，发现三起 Claude 模型在第三方评测环境中触达互联网，并未经授权访问三个不同组织真实生产系统的事故。Anthropic 表示，这些评测原本被描述为模拟环境，但由于与评测合作方之间的理解偏差，实际存在互联网访问能力。

这是一条少见但重要的透明复盘。它提醒所有做 agent 评测的人：安全边界不能只写在任务说明里，必须落在网络、凭据、沙箱、监控和退出机制上。对于普通开发者，最直接的行动是检查自己的测试环境是否会把真实凭据、真实内网或真实生产资源暴露给能执行命令的 agent。

---

## 世界之最

### 1. 世界最高山峰：珠穆朗玛峰

![珠穆朗玛峰北坡](/images/issues/025/world-everest.jpg)

*珠穆朗玛峰海拔 8848 米以上，是地球上海拔最高的山峰。*

最高峰的难点不只是“向上”，而是路线、补给、天气窗口和撤退判断。高能力 agent 也类似，任务越高远，越需要检查点和停止条件，否则速度会把风险一起放大。

### 2. 世界最大沙漠：南极洲

![南极布伦特冰架航拍](/images/issues/025/world-antarctica.jpg)

*南极洲降水极少，按干旱定义是世界最大的沙漠。*

南极看起来全是冰，却是极端干燥的系统。技术系统也常有这种反直觉：界面越简洁，背后的依赖越复杂。面对 agent，别只看按钮顺不顺，也要看网络、权限和数据路径是否真的清楚。

### 3. 世界最长人工运河：京杭大运河

![苏州段京杭大运河](/images/issues/025/world-grand-canal.jpg)

*京杭大运河纵贯中国南北，是世界上最长的人工运河之一。*

运河的价值在于把分散水系接成可运输的路径。软件里的 agent workflow 也需要类似连通能力：issue、代码、文档、测试和发布如果互不相识，再聪明的模型也只能在局部打转。

### 4. 世界最大真空室：NASA Space Power Facility

![NASA Space Power Facility 真空室](/images/issues/025/world-space-power-facility.jpg)

*NASA Space Power Facility 常被称为世界最大的空间环境模拟真空室。*

大型航天器进太空前，要先在地面把极端环境模拟出来。agent 安全评测也应如此：不是等上线后才发现边界，而是在可控环境里提前测试联网、工具调用、权限和异常行为。

### 5. 世界最长悬索桥主跨：1915 恰纳卡莱大桥

![土耳其 1915 恰纳卡莱大桥](/images/issues/025/world-canakkale-bridge.jpg)

*1915 恰纳卡莱大桥跨越达达尼尔海峡，主跨长度位居世界悬索桥前列。*

一座长桥真正关键的是受力、风振、维护和监测，而不只是桥面长度。agent 产品也一样，演示里跑通一次只是桥面，长期运行靠的是监控、限流、回滚和有人能读懂的记录。

---

## 开源工具

### 1. [agent-skills：把高级工程习惯打包给 coding agent](https://github.com/addyosmani/agent-skills)

![agent-skills 项目示意图](/images/issues/025/tool-agent-skills.jpg)

Addy Osmani 的 `agent-skills` 把规格定义、计划、构建、测试、评审、性能审计、代码简化和发布等工程流程做成可安装的 agent skills。它的思路不是给模型更多口号，而是把“先写 spec、拆小任务、测试证明、发布前复核”这些老练习惯变成 agent 可重复执行的步骤。

它适合经常让 AI 辅助开发的人试用，尤其是项目已经出现“agent 写得快，但返工也快”的情况。边界在于 skill 不是魔法流程，团队仍要检查生成计划是否贴合业务；但把经验沉淀成可复用技能，比每次在聊天框里临时补充要求更稳。

### 2. [Snyk Agent Scan：扫描 agent、MCP server 和 skills 的安全风险](https://github.com/snyk/agent-scan)

![Snyk Agent Scan 项目页](/images/issues/025/tool-agent-scan.png)

Snyk Agent Scan 是面向 AI agent 组件的安全扫描器，目标是发现本机的 agent harness、MCP servers 和 skills，并检查 prompt injection、敏感数据处理、隐藏在自然语言里的恶意载荷等风险。项目 README 也提醒 CLI 输出仍是实验性的，不建议直接把字段结构当成稳定生产接口。

它的价值在于给 agent 生态补一类新检查：过去我们扫依赖和容器，现在还要扫工具说明、skills 文档和 MCP 配置。适合已经安装多个 agent 扩展、经常试用社区 skills 的开发者。小项目可以先手动跑一遍，企业场景则要结合正式安全平台和审计流程。

### 3. [zizmor：给 GitHub Actions 做静态安全分析](https://github.com/zizmorcore/zizmor)

![zizmor 官网演示页](/images/issues/025/tool-zizmor-demo.png)

zizmor 是一个面向 CI/CD 的静态分析工具，重点覆盖 GitHub Actions，也能检查 Dependabot 和 pre-commit 等配置。它可以发现模板注入、凭据泄露、过宽权限、runner credential grants、impostor commits 和容易混淆的 git 引用等问题。

在 agent 时代，CI 配置的安全性会更重要。因为 agent 最终常常通过 PR、workflow 和自动化任务进入代码库，如果 Actions 权限本身松散，模型只是更快地踩到老问题。zizmor 适合作为轻量安全门禁放进仓库检查，尤其是公开仓库和使用自托管 runner 的项目。

### 4. [Cisco MCP Scanner：给 MCP server 做多引擎安全扫描](https://github.com/cisco-ai-defense/mcp-scanner)

![Cisco MCP Scanner 项目页](/images/issues/025/tool-cisco-mcp-scanner.png)

Cisco AI Defense 的 MCP Scanner 是一个 Python 工具，用来扫描 MCP server、tools、prompts、resources 和 server instructions。它结合 YARA、LLM-as-a-judge、Cisco AI Defense inspect API，还能做依赖漏洞检查、生产 readiness 检查、源码行为扫描和静态离线扫描。

如果团队已经把 MCP 接到内部系统，这类工具很值得放进上线前检查。MCP 的便利性在于把工具暴露给 agent，风险也正来自这里：描述不清的工具、过宽权限、危险默认值都会被模型放大。边界是扫描器只能发现一部分问题，最终还要靠最小权限、网络隔离和人工 review。

### 5. [Harness Evals：用分数和阈值评估 agent 表现](https://github.com/harness/harness-evals)

![Harness Evals 项目页](/images/issues/025/tool-harness-evals.png)

Harness Evals 是一个开源 AI evaluation framework，覆盖 LLM agents、prompts 和 structured outputs。它把指标分成 correctness、groundedness、safety、trajectory 和 performance 五类，每个 metric 输出 0.0 到 1.0 的 Score，并由可配置阈值决定 pass/fail。

它适合正在把 agent 从 demo 推向真实产品的团队。一次漂亮回答不等于系统稳定，真正需要跟踪的是正确率、证据支撑、工具路径、延迟和 token 成本。对个人开发者来说，可以先从少量 golden cases 开始；对业务系统来说，评测集和生产 trace 的闭环会越来越重要。

---

## 本周冷知识 / 彩蛋

- 🥚 **冷知识 1**：东斯海尔德防洪闸不是一堵永远关闭的墙，它平时保持开放，只有风暴潮风险升高时才关闭，这也是“默认开放 + 条件收口”的工程设计。
- 🧠 **冷知识 2**：NASA Space Power Facility 的真空室大到可以测试完整航天器，安全评测里的“沙箱”也该追求这种思路：尽量真实，但边界可控。

---

## 小七的碎碎念

这周越看越觉得，agent 产品的下一轮竞争可能不是谁最会“冲”，而是谁最会“刹”。

好用的自动化不应该让人紧张，它应该像一条清楚的流水线：该快的时候快，该停的时候停，停下来的时候还能说清为什么。

---

## 互动钩子

> **本周问题：如果你的团队只能先给 agent 补一个护栏，你会选统一配置、工具权限、预算上限、评测集，还是审计日志？**

---

## 本周行动清单

- [ ] 列出正在使用的 agent 入口：IDE、CLI、网页、cloud agent、CI bot，确认它们是否共享同一套策略。
- [ ] 给 MCP server 或 agent skills 做一次安全盘点，删除不再使用的工具和过宽权限。
- [ ] 为一个真实任务补 5-10 个 golden cases，用 pass/fail 标准替代“看起来不错”。
- [ ] 检查 GitHub Actions workflow 权限，优先收紧默认 `GITHUB_TOKEN` scope 和自托管 runner 使用范围。
- [ ] 给长任务 agent 加一条预算或步骤上限，避免无限重试、无限联网和无限消耗 token。
