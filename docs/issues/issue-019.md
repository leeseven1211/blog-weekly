---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 019 期）：Agent 进入流水线
  - - meta
    - property: og:description
      content: 本周最值得记住的变化，是 AI agent 从单次助手进入流水线：能触发、能计费、能审查，也必须能暂停。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/019/cover-svalbard-seed-vault.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/019/cover-svalbard-seed-vault.jpg
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
      content: 第 019 期封面图：斯瓦尔巴全球种子库入口
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/019/cover-svalbard-seed-vault.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/019/cover-svalbard-seed-vault.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-019
---

# 小七的周刊（第 019 期）：Agent 进入流水线

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **Agent 开始被流水线化**：GitHub Agentic Workflows 进入 public preview，后台 agent 不再只是聊天按钮，而是能被 Actions 调度的工程步骤。
2. **安全默认值正在变硬**：第三方 coding agent PR 自动安全校验、Copilot CLI 安全审查、npm v12 安装默认收紧，都在把“先跑起来”改成“先过门禁”。
3. **模型能力也有供应链风险**：Claude Fable 5 / Mythos 5 的上线后暂停提醒团队，模型不是永远可用的黑盒，要准备替代路径和降级策略。

---

## 封面图

![斯瓦尔巴全球种子库入口](/images/issues/019/cover-svalbard-seed-vault.jpg)

封面图：斯瓦尔巴全球种子库入口。它像这一期的隐喻：真正重要的系统，价值不只在“能存进去”，还在备份、隔离、责任边界和多年后仍能取出来。

---

## 本周短谈

### 1. Agent 真正进入生产，不是因为它更会聊天

这周最值得连起来看的，不是某个模型参数变大，而是 agent 周围的工程外壳突然变厚了。GitHub 把 Agentic Workflows 放进 Actions 语境，Copilot Chat 能看 agent session 日志，Agentic Workflows 又能用 `GITHUB_TOKEN` 取代长期 PAT。它们共同说明一件事：agent 正在从“人点一下”变成“流程可以调用”。

这会改变团队试点方式。以前评估 AI 工具，常看它能不能完成一个任务；现在还要看任务从哪里触发、谁付费、失败后看哪段日志、输出能不能被 CI 和 reviewer 接住。对开发者来说，agent 最有价值的入口可能不是 IDE 里的闪亮按钮，而是那些低风险、重复性高、验收标准清楚的流水线步骤。

### 2. 安全门禁不再只守人类写的代码

第三方 coding agent 安全校验很像一个转折点：平台终于承认“代码由谁写的”会影响风险模型。当 agent 创建 PR 时，GitHub 会自动用 CodeQL、Advisory Database 和 secret scanning 做检查；Copilot CLI 也加了实验性的 `/security-review`，让本地变更提交前先过一遍安全短审。

这不是说 AI 审查可以替代安全工程师。更实际的意义是，团队可以把“AI 生成代码必须更容易被审查”写进默认流程，而不是靠每个人自觉。未来的好习惯可能会变成：agent 先产出小 PR，平台先跑自动门禁，人类 reviewer 再看架构、边界和业务含义。

### 3. 供应链这周也在提醒：默认信任太贵了

npm v12 预告把 `npm install` 的几个高风险默认行为改成显式 opt-in：依赖安装脚本默认不跑，Git 依赖和远程 URL 依赖默认不解析。它听起来像会给不少项目添麻烦，但这类“麻烦”本质上是在把隐式执行路径摊开。

同一周，Claude Fable 5 和 Mythos 5 也经历了发布后暂停访问。对普通团队来说，重点不是评价哪家公司，而是承认模型、包、agent、云执行环境都属于供应链。只要供应链里有一环不可用，你的自动化就需要降级路线：换模型、关高风险能力、切回人工步骤，或者至少让任务停在可恢复的位置。

---

## 科技与 AI 动态

### 1. [GitHub Agentic Workflows public preview：把 agent 写进 Actions](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview/)

![GitHub Agentic Workflows 公测页面](/images/issues/019/news-github-agentic-workflows.png)

GitHub 6 月 11 日宣布 Agentic Workflows 进入 public preview。它允许团队用自然语言 Markdown 定义 AI 工作流，编译成 GitHub Actions 里运行的 workflow，用来做 issue triage、CI 失败分析、文档更新、合规检查等需要推理的仓库任务。

这条新闻重要在“位置”而不是“文案”。agent 一旦进入 Actions，就进入了权限、触发条件、日志、成本和审批的世界。适合先试点的是有清晰输入输出的重复任务，例如每日仓库状态、失败 CI 解释、文档同步检查；不适合一上来就交给跨系统发布或高权限生产操作。

### 2. [Agentic Workflows 不再需要长期 PAT：自动化开始少一个危险凭据](https://github.blog/changelog/2026-06-11-agentic-workflows-no-longer-need-a-personal-access-token/)

![Agentic Workflows 支持 GITHUB_TOKEN](/images/issues/019/news-agentic-token.png)

GitHub 同日更新 Agentic Workflows 认证方式：启用相关策略后，组织仓库里的 agentic workflow 可以使用 Actions 内置的 `GITHUB_TOKEN`，并通过 `copilot-requests: write` 把 Copilot CLI 的消耗计入组织。官方同时提醒，组织直付时需要用成本中心和 workflow 级 token 上限管理支出。

这是一个很实用的治理改动。长期 PAT 是自动化里常见的隐患，尤其当 agent 能发起代码改动、读日志、触发后续任务时，凭据泄漏和权限过宽都会变得更严重。读者如果准备试 agentic workflow，第一步不是写复杂 prompt，而是先把 token、权限和预算边界定下来。

### 3. [第三方 coding agent PR 自动安全校验：平台开始识别“AI 产物风险”](https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents/)

![第三方 coding agent 安全校验页面](/images/issues/019/news-third-party-agent-security.png)

GitHub 6 月 9 日宣布，当第三方 coding agent 在仓库里创建代码时，平台会自动用 CodeQL 分析潜在漏洞、用 GitHub Advisory Database 检查新引入依赖，并通过 secret scanning 检测 API key 和 token 等敏感信息。如果发现问题，agent 会在最终提交 PR 前尝试修复。

这条消息对团队管理 AI 代码很关键。它默认把 agent 产物放进更严格的安全路径，而不是把它当普通开发者手写 PR 一样处理。边界也要看清：自动校验覆盖的是常见漏洞、依赖和 secret，不会替你判断业务权限是否合理、迁移是否安全、架构是否被悄悄改坏。

### 4. [Copilot Chat 能看 agent session：日志开始回到对话里](https://github.blog/changelog/2026-06-10-copilot-chat-now-sees-your-agent-sessions/)

![Copilot Chat 查看 agent session 日志](/images/issues/019/news-copilot-agent-sessions.png)

GitHub 6 月 10 日更新 Copilot Chat 和 Copilot cloud agent 的衔接体验。用户可以在对话中看到进行中的 agent session 状态，任务完成后继续追问；新增的工具还能拉取 agent 在 PR 上的 session logs，或按主题、标题、时间搜索过去的 session。

这类功能看起来不像“新模型”那么显眼，但会影响真实协作。agent 工作越长，越需要能解释自己做过什么、验证过什么、为什么停在某一步。团队可以把 session 日志当成 review 输入的一部分，而不是只看最终 diff；否则长任务越自动化，越容易变成没人敢碰的黑箱。

### 5. [Copilot CLI `/security-review`：提交前的轻量安全短审](https://github.blog/changelog/2026-06-10-dedicated-security-review-command-now-available-in-copilot-cli/)

![Copilot CLI security review 公告](/images/issues/019/news-copilot-security-review.png)

GitHub 给 Copilot CLI 加了实验性的 `/security-review` 命令，面向本地代码变更做 AI 驱动的安全审查。它会返回高置信度发现、严重程度和可操作建议，重点覆盖注入、XSS、不安全数据处理、路径遍历和弱密码学等常见高影响漏洞类型。

它更像“提交前多一道提醒”，不是正式安全扫描替代品。好用法是把它放在本地自查或 PR 前 checklist 里，帮助开发者发现低级但高风险的问题；重要项目仍然需要 CodeQL、Dependabot、secret scanning、人工审查和测试一起工作。安全不是单点工具，而是一层层漏斗。

### 6. [npm v12 预告：安装脚本、Git 依赖、远程 URL 默认收紧](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)

![npm v12 breaking changes 公告](/images/issues/019/news-npm-v12.png)

GitHub 6 月 9 日预告 npm v12 将在 2026 年 7 月发布，并带来一组安全相关默认变化：`allowScripts` 默认关闭，依赖的 `preinstall`、`install`、`postinstall` 不再自动执行；Git 依赖和远程 URL 依赖也需要显式允许。npm 11.16.0 之后已经可以看到相关警告和准备命令。

这会让一些项目的安装流程短期变吵，但方向是对的。包管理器正在减少“安装即执行”的隐式信任。维护者这周可以先升级到 npm 11.16+，跑一次正常安装，检查哪些包需要脚本，再把可信 allowlist 提交到仓库。越是 CI 和生产构建，越不该靠默认信任跑未知脚本。

### 7. [Claude Fable 5 / Mythos 5 上线后暂停：模型可用性也是生产变量](https://www.anthropic.com/news/claude-fable-5-mythos-5)

![Anthropic Claude Fable 5 与 Mythos 5 公告](/images/issues/019/news-anthropic-fable.png)

Anthropic 6 月 9 日发布 Claude Fable 5 和 Mythos 5，随后在 6 月 12 日更新公告称暂停访问。GitHub Copilot 的相关 changelog 也同步说明，Fable 5 在 Copilot 体验中的访问已暂停，其他 Claude 模型不受影响。

这条消息适合放进所有生产 AI 项目的风险清单里。模型能力会升级，也可能因为政策、合规、供应商策略或安全原因短暂停用。团队不要把关键流程硬绑定到单一模型名：至少准备可接受的备用模型、质量降级标准、任务暂停提示和人工接管路径。

---

## 世界之最

### 1. 曾长期保持“世界最高桥梁”纪录：米约高架桥

![法国米约高架桥](/images/issues/019/world-millau-viaduct.jpg)

*米约高架桥横跨法国塔恩河谷，结构高度 343 米，曾长期被称为世界最高桥梁。*

它的美感来自轻盈，但真正难的是风、荷载、施工节奏和长期维护。Agent 流水线也类似：看起来是一条优雅的自动化路径，背后却要靠权限、日志、预算和失败处理支撑。

### 2. 世界最大的人工岛工程之一：朱美拉棕榈岛

![迪拜朱美拉棕榈岛航拍](/images/issues/019/world-palm-jumeirah.jpg)

*朱美拉棕榈岛位于迪拜，是最知名的大型人工群岛工程之一。*

从太空看，它像一个清晰图标；落到工程现场，却是围海造地、沉降、交通、供水和维护的复杂系统。AI 产品也常这样：演示很像一个按钮，真实落地是一整套基础设施。

### 3. 世界最高户外电梯之一：张家界百龙天梯

![张家界百龙天梯](/images/issues/019/world-bailong-elevator.jpg)

*百龙天梯建在张家界武陵源峭壁上，是著名的高落差户外观光电梯。*

它把游客从山脚直接送到高处，但每一次上升都依赖轨道、限速、载重和检修。Agent 也不能只追求“一步到位”，越能跨越复杂地形，越要有可停靠、可检查、可回退的中间层。

### 4. 从海底基座算起的最高山：冒纳凯阿

![海面望向冒纳凯阿](/images/issues/019/world-mauna-kea.jpg)

*冒纳凯阿位于夏威夷，若从海底基座算起，高度可与珠穆朗玛峰比较。*

很多系统真正的规模不在露出水面的部分。一个 AI 工作流看起来只是 PR、评论或按钮，但水面下还有模型、上下文、缓存、权限、沙箱、计费和审查。别只测山顶，底座也要看。

### 5. 世界最大的盐沼：乌尤尼盐沼

![玻利维亚乌尤尼盐沼](/images/issues/019/world-salar-de-uyuni.jpg)

*乌尤尼盐沼位于玻利维亚，面积约 10,582 平方公里，是世界最大的盐沼。*

雨季时它像一面巨大的镜子，漂亮但容易让方向感消失。长上下文和大量 agent 日志也会这样：信息越多，越需要索引、摘要和可追溯证据，否则只是把迷路的空间变大。

---

## 开源工具

### 1. [GitHub Agentic Workflows CLI：把自然语言工作流编译进 Actions](https://github.com/github/gh-aw)

![GitHub Agentic Workflows 仓库页](/images/issues/019/tool-gh-aw.png)

`github/gh-aw` 是 GitHub Agentic Workflows 的 CLI 和仓库入口，核心思路是用 Markdown 写自然语言工作流，再编译成 GitHub Actions 可以运行的锁定文件。它适合做仓库维护、状态报告、issue 分流、文档检查等“有规则但也需要判断”的任务。

值得试，但不要把它当魔法。好工作流要写清触发条件、权限、输入、输出、成本上限和失败时的处理方式。建议从只读报告或低风险文档类任务开始，跑通日志和审查链路后，再考虑让它改代码。

### 2. [awesome-copilot workflows：先看别人怎么写 agentic workflow](https://github.com/github/awesome-copilot/blob/main/docs/README.workflows.md)

![awesome-copilot workflow 示例](/images/issues/019/tool-awesome-copilot-workflows.png)

GitHub 的 `awesome-copilot` 里整理了 Agentic Workflows 示例和说明，适合拿来理解这类工作流的形态。比起直接从空白文件开始，先看“每日仓库状态”“issue 处理”“文档维护”这类样例，更容易判断哪些任务适合交给 agent。

它的价值不在复制粘贴，而在帮团队建立边界感：哪些信息必须给 agent，哪些动作必须锁权限，哪些结果必须由人确认。把示例改成自己的工程模板，比写一段很炫的 prompt 更有用。

### 3. [rulesync：给多种 AI 编码工具同步规则文件](https://github.com/dyoshikawa/rulesync)

![rulesync 仓库页](/images/issues/019/tool-rulesync.png)

`rulesync` 关注一个越来越常见的问题：团队里可能同时有人用 Claude Code、Codex、Cursor、Gemini/Antigravity、Kiro 等工具，规则文件格式各不相同。它试图把规则同步成各工具能读的形态，减少“每个 agent 各说各话”。

这类工具适合已经有明确工程规范的团队，而不是拿来替代规范本身。先把安全边界、测试要求、提交风格、禁止操作写清楚，再用同步工具分发到不同 AI 助手；否则同步出去的只是更整齐的空话。

### 4. [agentmemory：把 coding agent 的长期记忆做成 MCP 服务](https://github.com/rohitg00/agentmemory)

![agentmemory 仓库页](/images/issues/019/tool-agentmemory.png)

`agentmemory` 主打给 AI coding agent 提供持久记忆，通过 MCP 接入不同工具，让项目偏好、架构背景和常见命令不必每次从零解释。这个方向很有吸引力，尤其在多人项目或长期维护仓库里，重复交代上下文确实浪费。

但记忆也是风险面。团队应该先定义哪些内容可以被 agent 记住，哪些属于密钥、客户数据、内部事故或临时判断，不能随意持久化。好记忆应该像工程文档的缓存，而不是私密信息的垃圾桶。

---

## 本周冷知识 / 彩蛋

- 🥚 **冷知识 1**：斯瓦尔巴全球种子库没有把世界种子“收归自己”，它更像保险箱，种子所有权仍归存入方。这个设计很适合类比 agent 权限：托管执行不等于托管所有权。
- 🧠 **冷知识 2**：`npm install` 多年来让很多脚本自动执行，方便是真的方便，风险也是真的风险。v12 的变化像是在提醒大家：便利默认值用久了，会被误认为安全默认值。

---

## 小七的碎碎念

这周我看新闻时，脑子里一直浮现一个词：刹车片。

AI 行业当然还在拼发动机，但真正能让人放心上路的，是日志、审批、预算、回滚和默认不信任。

热闹归热闹，能停下来才算成熟。

---

## 互动钩子

> **本周问题：如果你要把一个 AI agent 放进团队流水线，第一条硬门禁会写什么：权限、预算、日志、测试，还是人工确认？**

---

## 本周行动清单

- [ ] 找一个低风险重复任务，写成 agentic workflow 草案，但先只做报告，不自动改代码。
- [ ] 检查团队 AI 工具是否还依赖长期 PAT，能换成短期 token 或平台内置 token 的先换掉。
- [ ] 升级到 npm 11.16+ 跑一次安装，记录哪些依赖脚本会在 v12 里被拦。
- [ ] 给 AI 生成 PR 增加固定检查项：安全扫描、secret scanning、测试结果、人工 reviewer。
- [ ] 为关键 AI 流程列一个降级表：主模型不可用时，用哪个备用模型或人工路径接住。

---

<div class="issue-subscribe-cta">

### 📬 喜欢这期内容？

<p>订阅「小七的周刊」，每周一收到最新一期。</p>

<div class="issue-cta-buttons">
  <a href="/feed.xml" class="cta-rss" target="_blank" rel="noopener noreferrer">📡 RSS 订阅</a>
  <a href="https://twitter.com/intent/tweet?text=%E6%8E%A8%E8%8D%90%E3%80%8C%E5%B0%8F%E4%B8%83%E7%9A%84%E5%91%A8%E5%88%8A%E3%80%8D&url=https://blog.leeseven.com/issues/issue-019" class="cta-share" target="_blank" rel="noopener noreferrer">🐦 转发到 Twitter</a>
  <a href="https://github.com/leeseven1211/blog-weekly" class="cta-share" target="_blank" rel="noopener noreferrer">⭐ GitHub</a>
</div>

</div>
