---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 027 期）：当 Agent 开始有了快车道
  - - meta
    - property: og:description
      content: 本周的 AI 更新不只在比模型分数：更快的推理通道、跨工具插件、MCP 流量治理和表格里的小应用，都在把 agent 推向可组合、可控、可落地的工作流。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/027/cover-magdeburg-water-bridge.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/027/cover-magdeburg-water-bridge.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '1920'
  - - meta
    - property: og:image:height
      content: '1439'
  - - meta
    - property: og:image:alt
      content: 第 027 期封面图：德国马格德堡水桥
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/027/cover-magdeburg-water-bridge.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/027/cover-magdeburg-water-bridge.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-027
---

# 小七的周刊（第 027 期）：当 Agent 开始有了快车道

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **速度开始成为产品能力**：OpenAI 预览 Ultrafast，GitHub Copilot 引入更多模型，AI 产品正在把“等一会儿”变成可设计的体验变量。
2. **Agent 插件走向共同格式**：Agent Plugins 1.0、AWS 插件和 Codex 生态都在说明，能力复用会比单个客户端更重要。
3. **MCP 从连接协议变成治理对象**：Cloudflare 开始识别 MCP 流量，企业会更关心哪些工具能接入、谁能调用、怎样审计。

---

## 封面图

![德国马格德堡水桥横跨易北河](/images/issues/027/cover-magdeburg-water-bridge.jpg)

封面图：德国马格德堡水桥。它让运河像道路一样跨过河流，本期的主题也类似：AI 工作流正在被铺出更清楚的通道，速度、插件和治理各走其道，但要在同一个系统里相遇。

---

## 本周短谈

### 1. AI 体验开始进入“毫秒预算”阶段

过去谈大模型产品，常见问题是“能不能做对”。这周更明显的问题变成了“能不能在合适时间内做对”。OpenAI 预览 [Ultrafast](https://openai.com/index/previewing-ultrafast/)，称 GPT-5.6 Sol 在新服务层里最高可达 Standard 处理速度的 14 倍、输出最高 750 tokens/s；GitHub Copilot 一周内也继续增加 Kimi K3、MAI-Code-1.1-Flash、Grok 4.6 和 Gemini 3.7 Flash 等模型选择。

这不是单纯的跑分新闻。客服、语音、故障响应、结账推荐这类场景里，延迟会直接改变用户是否继续等下去。普通开发者接下来要多想一步：模型能力、成本和延迟不该只写在 README 里，而应该进入路由策略、降级方案和产品交互。

### 2. 插件标准化，会改变“写一次工具”的价值

Agent Plugins 1.0 的意义不在于又多了一个插件市场，而是让同一份能力包有机会跨 VS Code、Copilot CLI、Copilot app 和 SDK 复用。换句话说，工具不再只属于某个聊天窗口，而可能成为组织里的通用“工位设备”。

这会带来两个方向的变化。好的一面是，部署、数据库、云资源、测试流程都能更快沉淀成可分发能力；难的一面是，插件一旦跨客户端流动，权限边界、版本兼容和行为说明就不能含糊。一个插件写得好不好，不只看它能调用多少 API，还要看它是否能被安全地理解和替换。

### 3. MCP 火起来以后，安全团队也会进场

MCP 的流行让 agent 接工具更方便，也让“影子连接”更容易出现。Cloudflare 这周介绍了对 MCP 流量的识别与管控思路：通过协议层特征发现 MCP 请求，引导团队把访问收进受控入口，并阻止未批准的直连。

这对开发者不是坏消息。一个协议只有进入安全、日志、网络策略和审计视野，才有机会成为生产系统的一部分。接下来做 agent 应用时，别只问“能不能连上这个工具”，还要问“谁批准、走哪条路径、失败时谁能看见”。

---

## 科技与 AI 动态

### 1. [GitHub Copilot 周更新：模型、插件和 CLI 工作流一起扩容](https://github.blog/changelog/2026-08-13-github-copilot-weekly-releases-august-10/)

![GitHub Copilot 周更新官方配图](/images/issues/027/news-github-copilot-weekly.jpg)

GitHub 在 8 月 13 日发布 Copilot 周更新，重点包括 Kimi K3、MAI-Code-1.1-Flash 等模型滚动上线，Agent Plugins 1.0 在多个 Copilot 入口可用，Copilot app 支持更方便地管理插件，CLI 与编辑器体验也继续补强。

这类“周更”容易被看成小功能集合，但它真正反映的是 Copilot 正在从代码补全工具变成多入口 agent 平台。模型选择、插件管理、命令行交互和编辑器反馈如果能放在同一套工作流里，开发者就不必为了一个任务在多个孤岛之间搬上下文。

### 2. [Agent Plugins 1.0：一次打包，多端复用](https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/)

![Agent Plugins 1.0 官方发布配图](/images/issues/027/news-github-agent-plugins.jpg)

GitHub 8 月 12 日宣布 Agent Plugins 1.0 已可用于 VS Code、Copilot CLI、GitHub Copilot SDK 和 Copilot app。官方说法是“build a plugin once”，再在兼容的 agent 客户端中使用；这套规格也与 AWS、Anysphere、Microsoft、OpenAI、Vercel 等生态参与方一起推进。

对开发者来说，它像是 agent 时代的扩展包格式。过去插件经常绑定一个 IDE 或一个聊天产品，现在更值得关注的是能力描述、权限声明、版本升级和分发路径。它还很早期，但方向很清楚：agent 的竞争不会只发生在模型层，也会发生在工具层和生态层。

### 3. [Cloudflare 开始识别 MCP 流量：工具连接也需要网络侧治理](https://blog.cloudflare.com/mcp-security-updates/)

![Cloudflare MCP 安全更新官方配图](/images/issues/027/news-cloudflare-mcp.png)

Cloudflare 8 月 14 日介绍了 MCP 安全更新：Gateway 可以用协议层启发式方法识别 MCP 请求，安全团队可以据此发现影子 MCP 流量，把访问收敛到 Portal 等批准入口，并在受管网络路径上阻止直接连接。

这件事说明 MCP 已经不只是开发者本地实验的便利协议。只要 agent 能代替人调用工具，连接路径就会成为安全边界的一部分。比较务实的做法，是在试点阶段就把 MCP server 清单、身份策略、日志字段和阻断规则设计好，而不是等工具扩散后再补治理。

### 4. [Google Sheets canvas：表格开始生成可交互的小应用](https://blog.google/products-and-platforms/products/workspace/sheets-canvas-for-google-sheets-spreadsheets/)

![Google Sheets canvas 官方演示图](/images/issues/027/news-google-sheets-canvas.jpg)

Google 8 月 13 日发布 Sheets canvas，用户可以用提示词把表格数据变成互动仪表盘、学习追踪器、座位图等“小应用”。它把 Gemini 放进表格语境里，不只是帮人写公式，而是把已有数据、布局和交互一起组织起来。

这类功能很适合观察 AI 产品落地方式：不是每个用户都想打开一个专门的 agent 控制台，但很多人每天都在表格里做计划、统计和协作。当 AI 能在熟悉工具里生成轻量应用，真正的门槛就从“会不会写代码”变成“能不能描述清楚想要的工作流”。

---

## 世界之最

### 1. 世界最大热带沙漠：撒哈拉沙漠

![撒哈拉沙漠真实色彩卫星影像](/images/issues/027/world-sahara.jpg)

*撒哈拉沙漠面积约 900 万平方公里，是世界最大的热带沙漠。*

它的尺度提醒人们，空旷也可以是一种复杂系统。AI 应用里的“空白地带”也是这样：未覆盖的权限、缺失的日志、没有定义的失败路径，看似什么都没有，真正出事时却最难穿越。

### 2. 世界最长河流之一：尼罗河

![尼罗河沿岸自然景观](/images/issues/027/world-nile.jpg)

*尼罗河常被列为世界最长河流之一，流经非洲东北部多个国家。*

一条长河的价值不只在源头，而在沿途灌溉、运输和城市网络。agent 工作流也类似，单次回答只是源头，真正有用的是它能否一路流过数据、工具、审批和交付环节。

### 3. 世界最大淡水湖之一：苏必利尔湖

![国际空间站视角下的苏必利尔湖](/images/issues/027/world-lake-superior.jpg)

*按面积计算，苏必利尔湖通常被列为世界最大的淡水湖之一。*

大湖的稳定来自广阔水面和长期补给。团队的知识库也需要这种“水体感”：来源持续进入，旧内容定期沉淀，检索能快速定位，而不是临时把资料堆在一个聊天窗口里。

### 4. 世界最大活火山之一：冒纳罗亚

![夏威夷冒纳罗亚火山景观](/images/issues/027/world-mauna-loa.jpg)

*冒纳罗亚体量巨大，是地球上最大的活火山之一。*

火山平时像背景地形，爆发时才暴露能量。基础设施风险也常这样存在：模型供应、API 额度、插件权限、网络策略平时不显眼，一旦失控就会影响整个产品链路。

### 5. 世界最高树种：海岸红杉

![加州红木公路旁的海岸红杉](/images/issues/027/world-coast-redwood.jpg)

*海岸红杉是世界最高树种，个体高度可超过百米。*

一棵巨树能长高，靠的是根系、树皮和长期环境，而不是突然冲刺。AI 产品要长期变强，也离不开数据治理、评测基线和安全边界这些“根部结构”。

---

## 开源工具

### 1. [agent-plugins-spec：把 agent 扩展打包成可分发插件](https://github.com/agentplugins/agent-plugins-spec)

![agent-plugins-spec 仓库卡片](/images/issues/027/tool-agent-plugins-spec.png)

这个仓库提供 Agent Plugins Specification v1.0.0，目标是用一种尽量小的标准描述 agent 扩展如何被打包、发现和安装。它适合想理解插件生态底层格式的读者，尤其是已经在维护内部命令、脚本或工具连接的人。

### 2. [AWS Agent Plugins：把云架构与部署能力交给 coding agent](https://github.com/awslabs/agent-plugins)

![AWS Agent Plugins 仓库卡片](/images/issues/027/tool-aws-agent-plugins.png)

AWS 的 agent-plugins 仓库提供面向 AWS 架构、部署和运维的插件能力。它的价值不只是“让 agent 会调 AWS”，更重要的是把云服务操作变成可版本化、可说明、可审查的能力包，适合团队从低风险任务开始试点。

### 3. [Codex CLI：终端里的 coding agent 继续适合做自动化入口](https://github.com/openai/codex)

![OpenAI Codex 仓库卡片](/images/issues/027/tool-codex.png)

Codex CLI 是 OpenAI 的终端 coding agent。把它放在这一期，是因为插件、MCP 和模型路由都需要一个足够明确的执行现场：能看见文件、命令、差异和检查结果。对个人开发者来说，终端仍然是观察 agent 行为最直接的地方。

### 4. [Transformer Lab：本地训练、评测和管理模型的研究环境](https://github.com/transformerlab/transformerlab-app)

![Transformer Lab 仓库卡片](/images/issues/027/tool-transformerlab.png)

Transformer Lab 是一个面向 AI 研究者和开发者的开源环境，用来训练、评测和扩展模型。云端 API 越强，本地评测反而越重要：只有把数据集、指标和实验记录握在手里，模型升级时才知道到底变好了还是只是感觉更顺。

---

## 本周冷知识 / 彩蛋

马格德堡水桥不是“桥上有水”的奇观那么简单。它把两段运河接起来，让船不用先下降到易北河再上升回运河系统。好的工作流设计也有这种味道：不是让每一步都显得聪明，而是尽量减少不必要的上下切换。

---

## 小七的碎碎念

这周最有意思的变化，是 AI 基础设施开始出现交通系统的感觉：快车道、匝道、收费站、检查口和统一的道路标识都在成形。模型当然还重要，但只盯模型会漏掉很多真正影响体验的东西。

如果你正在做 AI 应用，可以从很小的地方开始：把“这个任务该走哪个模型、哪些工具、哪个权限、失败后怎么退”写成清楚的策略。它看起来不像炫技，却会决定产品能不能长期跑下去。

---

## 互动钩子

如果你在做 agent 或 AI 工具链，本周可以问自己一个问题：现在最拖慢体验的是模型能力、响应速度、工具连接，还是权限和流程？欢迎把答案当成下一轮优化的入口。

---

## 本周行动清单

- 给一个 AI 功能补上延迟、成本和成功率的基础监控。
- 盘点项目里所有 MCP server / 插件 / 外部工具入口，标注负责人和权限范围。
- 尝试把一个常用脚本整理成可说明、可版本化的 agent 工具。
- 做一次模型升级小实验：同一任务跑旧模型和新模型，记录质量、速度、成本三项结果。

---

我们下周见。
