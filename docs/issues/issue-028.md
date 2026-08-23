---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 028 期）：当 Agent 进了群聊，护栏也要进场
  - - meta
    - property: og:description
      content: GitHub 把 Copilot 带进 Slack 和 Teams，Google 用 ADK 演示零信任 agent，Cloudflare 开始同步 AI bot 偏好；本期关注协作型 agent 的治理、权限和可观察性。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/028/cover-bastei-bridge.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/028/cover-bastei-bridge.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '3409'
  - - meta
    - property: og:image:height
      content: '2260'
  - - meta
    - property: og:image:alt
      content: 第 028 期封面图：德国萨克森瑞士国家公园的巴斯泰桥
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/028/cover-bastei-bridge.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/028/cover-bastei-bridge.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-028
---

# 小七的周刊（第 028 期）：当 Agent 进了群聊，护栏也要进场

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **Agent 开始进入协作现场**：GitHub Copilot 同一天进入 Slack 和 Teams，说明 AI 工作不再只发生在 IDE 或命令行里。
2. **治理从配置项变成产品能力**：JetBrains 托管设置、零信任 agent 示例和 bot 偏好同步，都在把权限、审计和策略前置。
3. **真正难的是“谁能让它动手”**：共享会话很诱人，但只要 agent 能开 PR、改数据库或调用工具，身份、审批和可观察性就必须跟上。

---

## 封面图

![德国萨克森瑞士国家公园的巴斯泰桥](/images/issues/028/cover-bastei-bridge.jpg)

封面图：德国萨克森瑞士国家公园的巴斯泰桥。几段石桥把分散岩峰连成可行走的路径，本期主题也类似：agent 正在跨进聊天、会议、IDE 和云沙箱，连接变多以后，真正重要的是桥面、护栏和限行标识。

---

## 本周短谈

### 1. Agent 进群聊，不等于工作自动消失

GitHub 这周连续把 Copilot 带进 Slack 和 Microsoft Teams。表面看，这是“在聊天里叫一个 agent 来帮忙”；更深一层，它把需求、讨论、上下文、执行和验收放进同一个协作现场。

这会改变很多人的第一反应。过去把任务交给 AI，常常像开一个单独窗口；现在它更像在公开讨论里拉进一位能动手的参与者。好处是上下文不容易丢，旁观者也能及时纠偏；风险是所有人都要更清楚地知道：谁有权限触发修改，哪些仓库可见，agent 产物应该在哪里被审查。

### 2. “会不会做”之后，问题变成“能不能被约束”

Google 的零信任 agent 示例讲得很直白：一个客服退款 agent 如果共用数据库连接、能执行代码，又只靠系统提示词守规矩，攻击者一句提示就可能把 149 美元退款改成 10,000 美元，甚至读取环境变量。

OpenAI 在 [The Defender's Window](https://openai.com/index/the-defenders-window/) 里也强调，AI 会同时放大攻击者和防守者的能力。对普通技术读者来说，这不是遥远的安全论文，而是一个产品设计问题：当 AI 变成执行者，规则要尽量落在身份、沙箱、策略网关、日志和测试里，而不是只写在一段提示词里。

### 3. 内容和工具都在要求“可声明的边界”

Cloudflare 的 Bot Preference Sync 看起来像站长工具，但它背后是同一个趋势：AI 流量、agent 抓取、训练访问都需要可声明、可同步、可执行的偏好。网站拥有者不想在 robots.txt、一组后台开关和边缘规则之间来回维护冲突状态。

这件事和开发者很近。未来的 AI 系统不会只问“模型能不能理解我”，还会问“外部世界怎么理解这个 AI 的意图”。无论是访问网站、调用 MCP server，还是从聊天里开一个 PR，机器之间也需要更明确的交通规则。

---

## 科技与 AI 动态

### 1. [GitHub Copilot 进入 Slack：从讨论串直接交办代码任务](https://github.blog/changelog/2026-08-21-the-new-github-copilot-experience-in-slack/)

![GitHub Copilot Slack 官方发布页](/images/issues/028/news-copilot-slack.png)

GitHub 8 月 21 日宣布，Slack 里的 GitHub 集成开始把 Copilot CLI 和 GitHub Copilot app 的 agent 能力带进 Slack，当前为公开预览。用户可以在私信、频道或讨论串里提及 `@GitHub`，让 Copilot 计划修改、调查问题、整理 bug、创建或更新 issue，并在安全云沙箱里实现和验证变更。

最值得注意的是它对“多人协作”的处理：Copilot 可以创建专门的 Slack Code channel，让参与者看计划、查 diff、审预览产物，并从原讨论继续接力。这不是简单把聊天机器人搬进 Slack，而是把 coding agent 放进工作协调层。适合先从低风险仓库试用，重点观察权限、噪音和审查流程是否跟得上。

### 2. [Copilot 进入 Microsoft Teams：会议行动项可以变成共享 agent 会话](https://github.blog/changelog/2026-08-21-shared-agentic-work-with-github-copilot-in-microsoft-teams/)

![GitHub Copilot Teams 官方发布页](/images/issues/028/news-copilot-teams.png)

同一天，GitHub 也发布了 Copilot in Microsoft Teams 公开预览。用户可以在频道、讨论串或私信里提及 `@GitHub`，启动一个所有参与者都能看见并引导的 Copilot cloud agent session；有仓库写权限的人可以触发 Copilot 进行代码修改，相关会话会消耗 AI credits。

这让“会议结论没人落地”的老问题多了一个新解法：在讨论还没散场时，把调查、修复或验证交给云沙箱异步推进。不过边界也很清楚，agent 不应该绕过已有的代码审查。更务实的采用方式，是把 Teams 入口当成任务启动器，而不是最终决策者。

### 3. [Copilot for JetBrains 加入企业托管设置：插件、MCP 和遥测开始统一收口](https://github.blog/changelog/2026-08-18-enterprise-managed-settings-in-github-copilot-for-jetbrains/)

![GitHub Copilot JetBrains 托管设置发布页](/images/issues/028/news-copilot-jetbrains-settings.png)

GitHub 8 月 18 日宣布，Copilot for JetBrains 支持企业托管设置，覆盖插件治理、MCP server 访问、OpenTelemetry 和权限模式。管理员可以集中设置启用或禁用插件、额外市场、受限市场，也可以通过 `allowedMcpServers` 和 `deniedMcpServers` 管理开发者可连接的 MCP server。

这条更新不如新模型上架显眼，但对生产环境更关键。agent 进入 IDE 后，真正的风险往往不是“它答错一句话”，而是“它接了哪些工具、把遥测发到哪里、默认能执行到什么程度”。企业托管设置的价值，是让策略不再依赖每位开发者手工配置。

### 4. [Google ADK 零信任 agent 示例：不要把系统提示词当安全边界](https://developers.googleblog.com/build-zero-trust-ai-agents-with-googles-agent-development-kit/)

![Google ADK 零信任 agent 官方文章](/images/issues/028/news-google-zero-trust-agents.png)

Google Developers Blog 8 月 17 日介绍了用 Agent Development Kit 和 Gemini 构建的零信任 agent 示例。官方场景是一个客服与退货 agent：正常情况下，它会读取用户请求、计算退款、写入数据库账本；在攻击场景里，恶意提示可能诱导它越权退款、读取环境变量或篡改数据。

Google 的结论很直接：系统提示词不是安全边界。示例把防线拆成三层：加密身份与账本签名、受管沙箱执行、语义网关与确定性测试。对开发者来说，这套思路比“再写一条更严厉的 prompt”可靠得多，也更容易被安全审计和回归测试吸收。

### 5. [Cloudflare Bot Preference Sync：把 AI bot 偏好同步到 robots.txt](https://blog.cloudflare.com/bot-preference-sync/)

![Cloudflare Bot Preference Sync 官方文章](/images/issues/028/news-cloudflare-bot-preference-sync.png)

Cloudflare 8 月 21 日发布 Bot Preference Sync，面向从 Free 到 Enterprise 的所有客户开放。它会把站点在 AI bot 配置里的 Search、Agent、Training 等偏好同步反映到 robots.txt，减少“后台策略禁止、公开声明没更新”或相反状态造成的冲突。

这不是只给 SEO 人员看的小功能。AI agent 越多，网站就越需要表达“哪些访问欢迎、哪些访问拒绝、哪些访问只能在特定条件下发生”。robots.txt 本身不是强制安全边界，但当偏好声明和边缘执行策略保持一致，内容拥有者与爬虫、搜索、agent 之间的摩擦会小很多。

---

## 世界之最

### 1. 世界最长防御工程：长城

![金山岭长城蜿蜒在山脊上](/images/issues/028/world-great-wall.jpg)

*长城是世界最知名的线性防御工程之一，历代墙体、壕堑和关隘共同构成庞大的边界系统。*

长城的启发不只是“筑墙”，而是边界需要分段、关口、巡检和维护。AI 工具也是如此，最有效的防线不是一句“不要越权”，而是把访问、审批、日志和例外路径拆成可检查的节点。

### 2. 世界最大钟面：麦加皇家钟塔

![麦加皇家钟塔的巨大钟面](/images/issues/028/world-abraj-clock.jpg)

*麦加皇家钟塔被吉尼斯世界纪录列为最高钟楼，其钟面也常被列为世界最大钟面。*

一个城市级钟面最重要的功能不是炫耀尺寸，而是给大量人群一个共同时间。协作型 agent 也需要类似同步信号：任务状态、执行进度、谁在审查、何时停止，都应该让参与者看得见。

### 3. 世界最大体育场：纳伦德拉·莫迪体育场

![纳伦德拉·莫迪体育场看台](/images/issues/028/world-narendra-modi-stadium.jpg)

*纳伦德拉·莫迪体育场位于印度艾哈迈达巴德，容量约 132,000 人，通常被列为世界最大体育场。*

十几万人同时在场，靠的不是嗓门，而是入口、分区、屏幕、安保和广播系统。把 agent 放进 Slack 或 Teams 也是这个逻辑：参与者越多，越不能只靠“大家自觉看清楚”。

### 4. 世界最大货运飞机代表：Antonov An-225 Mriya

![Antonov An-225 Mriya 停靠在莱比锡哈雷机场](/images/issues/028/world-an225.jpg)

*Antonov An-225 Mriya 是人类制造过的最大货运飞机之一，也是超重型空运能力的代表。*

An-225 的故事提醒人们，单体能力再惊人，也有脆弱性。技术系统同样如此：把太多关键流程压在一个超级 agent 上很诱人，但更稳的方式往往是拆分职责、保留回退，并让交接可验证。

### 5. 世界最干旱非极地沙漠之一：阿塔卡马沙漠

![阿塔卡马沙漠荒原景观](/images/issues/028/world-atacama.jpg)

*阿塔卡马沙漠位于智利北部，极端干燥和晴朗天空让它成为重要天文观测地点。*

低噪声环境适合看见微弱信号。排查 agent 系统也一样：如果日志混乱、权限模糊、上下文到处飘，真正的错误会被噪声淹没。先把环境变干净，诊断才有可能变准确。

---

## 开源工具

### 1. [zero-trust-agents：用 ADK 演示身份、沙箱和语义网关](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/zero-trust-agents)

![GoogleCloudPlatform zero-trust-agents 仓库目录](/images/issues/028/tool-zero-trust-agents.png)

这个示例仓库是 Google 本周文章的配套项目，目标是把零信任 agent 的三层防线做成可运行蓝图：交易签名与审计账本、受控代码执行环境、语义网关和测试用例。它不适合直接当生产框架复制粘贴，但很适合用来和产品、安全、后端一起讨论“agent 到底能碰什么”。

如果你正在做会写数据库、调支付或跑代码的 agent，这个仓库值得先看。它的价值不在炫技，而在把风险拆得足够具体：越权退款、密钥泄露、数据库篡改都能映射到对应控制点。

### 2. [Cloudflare Agents：把 agent 做成有状态、可休眠的执行环境](https://github.com/cloudflare/agents)

![Cloudflare Agents 仓库页面](/images/issues/028/tool-cloudflare-agents.png)

Cloudflare Agents 是一个基于 Durable Objects 的 agent 运行环境，支持持久状态、存储、生命周期、实时通信、调度、模型调用、MCP 和 workflows。官方强调 agent 闲置时可以休眠、按需唤醒，适合“一人一个会话、一个房间一个 agent”这类高并发场景。

它对开发者的启发是：agent 不是只能存在于一次 API 调用里，也可以是长期存在的状态对象。采用时要注意平台绑定和调试方式，但如果应用本来就在 Cloudflare 生态里，它提供了一条很清楚的部署路径。

### 3. [AgentTeams：把多 agent 协作放进可见房间](https://github.com/agentscope-ai/AgentTeams)

![AgentTeams GitHub 仓库页面](/images/issues/028/tool-agentteams.png)

AgentTeams 是一个开源多 agent 协作运行平台，核心思路是让多个 agent 在受控、可审计的房间里协作，并保留人工可见性和介入能力。它使用 Manager-Workers 架构，强调 OpenClaw、QwenPaw、Hermes 等不同运行时可以在同一协作空间里分工。

这类工具适合观察“多 agent”从演示走向工程时会遇到什么：共享文件、角色分配、任务接力、房间记录、网关和审计。它不是最轻量的起步方式，但能提醒读者，多 agent 的难点常常不是让它们说话，而是让它们有秩序地交接。

### 4. [OpenAI Agents SDK：把 handoff、guardrails、HITL 和 tracing 放进同一个框架](https://github.com/openai/openai-agents-python)

![OpenAI Agents SDK Python 仓库页面](/images/issues/028/tool-openai-agents-python.png)

OpenAI Agents SDK 是一个用于构建多 agent workflow 的 Python 框架，仓库说明里列出了 agents、tools、handoffs、guardrails、human in the loop、sessions 和 tracing 等模块。它的重点不是单次问答，而是把长流程里的委派、保护和记录纳入同一套开发模型。

如果只是做一个聊天功能，它可能显得偏重；但当任务开始跨工具、跨步骤、跨审批时，框架提供的结构会比手写一堆回调更容易维护。读者可以重点看 human in the loop 和 tracing，两者决定了 agent 出错时是否能停下来、查回去。

---

## 本周冷知识 / 彩蛋

- **冷知识 1**：robots.txt 更像“访问偏好声明”，不是强制门禁。真正阻断仍要靠服务端、边缘规则或身份策略，但声明和执行不一致会让 AI bot 治理变得很混乱。
- **冷知识 2**：巴斯泰桥所在的砂岩地貌由长期水蚀形成，后来才被人类加上桥面。很多技术系统也是这样：自然形成的沟壑先存在，工程做的是让跨越变得可控。

---

## 小七的碎碎念

这周的关键词不是“更聪明”，而是“更像同事”：agent 会出现在群聊、会议、工单和 IDE 里，甚至会带着一段上下文去开 PR。

可一旦它像同事一样能动手，就也要像同事一样被授权、被记录、被审查。把护栏做早一点，往往比事后补一篇事故说明便宜得多。

---

## 互动钩子

如果一个 agent 可以从聊天里直接创建 PR，你最希望先看到哪三件事：权限范围、执行日志、回滚方案，还是人工确认点？

---

## 本周行动清单

- 盘点一个项目里所有 AI 工具入口：聊天、IDE、CLI、MCP server、浏览器插件，标出它们能读写什么。
- 把一个高风险工具调用改成需要显式确认，例如支付、删库、发邮件、开 PR 或部署。
- 给 agent 任务补最小可用日志：谁触发、用了哪些上下文、调用了哪些工具、产物在哪里审查。
- 选择一个低风险流程试验共享 agent 会话，并提前写清停止条件和验收标准。

---

我们下周见。
