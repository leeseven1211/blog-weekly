---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 020 期）：可计量的 AI 开始长大
  - - meta
    - property: og:description
      content: 本周最值得记住的变化，是 AI 不再只比能力，而是进入计量、权限、审查、退场和工具链治理的现实阶段。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/020/cover-draugen-platform.jpg
  - - meta
    - property: og:image:secure_url
      content: https://blog.leeseven.com/images/issues/020/cover-draugen-platform.jpg
  - - meta
    - property: og:image:type
      content: image/jpeg
  - - meta
    - property: og:image:width
      content: '1920'
  - - meta
    - property: og:image:height
      content: '1514'
  - - meta
    - property: og:image:alt
      content: 第 020 期封面图：北海 Draugen 海上平台
  - - meta
    - name: twitter:image
      content: https://blog.leeseven.com/images/issues/020/cover-draugen-platform.jpg
  - - meta
    - itemprop: image
      content: https://blog.leeseven.com/images/issues/020/cover-draugen-platform.jpg
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-020
---

# 小七的周刊（第 020 期）：可计量的 AI 开始长大

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

---

## 本期 3 个要点

1. **AI 成本开始从“总账”拆到“人”**：Copilot usage metrics API 增加按用户统计的 AI credits 消耗，团队终于能看见谁在用、用在哪、该怎么设预算边界。
2. **模型退场也要纳入架构设计**：Opus 4.6 fast 即将退役，MAI-Code-1-Flash 扩大到更多 Copilot 场景，提醒开发者不要把关键流程绑死在单一模型名上。
3. **协作对象从人扩展到 agent**：Copilot code review 支持 AGENTS.md、Copilot PR 可被作者搜索、Issues 接入 MCP 字段，平台开始把 agent 当作可治理的工程参与者。

---

## 封面图

![北海 Draugen 海上平台](/images/issues/020/cover-draugen-platform.jpg)

封面图：北海 Draugen 海上平台。海上平台看起来像孤岛，真正可靠靠的是能源、管线、船只、传感器、检修和紧急预案；这一期的 AI 主题也类似，能力只是露出海面的部分，计量、权限和退场机制才是底座。

---

## 本周短谈

### 1. 当 AI credits 能按人统计，试点就不能再只看“好不好用”


过去很多团队试 AI 工具，最常见的指标是“大家觉得效率有没有提升”。这当然重要，但它太像体感温度：能帮助判断方向，却很难指导预算、配额和治理。本周 GitHub 把 Copilot usage metrics API 的 AI credits 消耗拆到用户粒度，信号很明确：AI 工具正在从福利、插件、试用套餐，变成需要进成本中心的生产资源。

这会改变管理方式。一个成熟团队不需要把每次 prompt 都审计成工单，但至少要知道哪些角色高频使用、哪些场景烧钱最多、哪些仓库值得开更强模型。边界也在这里：指标只能说明消耗，不直接说明产出。真正要做的是把成本、PR 质量、交付周期和返工率放在一起看，而不是用“谁花得多”来简单排名。

### 2. 模型不是永久地基，更像一组会换班的专业工人


Opus 4.6 fast 即将退役，MAI-Code-1-Flash 扩大到更多 Copilot surfaces，这两条消息放在一起很有意思。一边是旧入口退出，一边是新模型补位，说明开发者工具里的模型层会越来越像云实例规格：有性能差异、有价格差异，也会因为供应、策略或产品路线发生变化。

对普通开发者来说，最实用的动作不是追每个模型的跑分，而是把“模型可替换”写进工作流。比如：代码审查用 A 模型失败时能否切 B 模型？生成文档的质量阈值是什么？模型下线时任务是暂停、降级，还是回到人工处理？越是自动化程度高的团队，越不能把模型名当成永不变化的基础设施。

### 3. Agent 进入协作系统后，规则文件也开始变成接口


Copilot code review 支持 AGENTS.md，看起来是个小改动，实际很像一个接口声明：仓库终于可以告诉 AI 审查者“这个项目怎么工作、哪些风格不能破坏、哪些测试必须跑”。与此同时，Copilot-authored pull requests 被纳入作者搜索，也说明平台开始承认 agent 产物需要可追踪身份，而不是混在普通 PR 里。

这对团队协作很关键。过去工程规范常写给人看，现在也要写给工具看。好规则不该是“请写高质量代码”这种愿望清单，而应该是能被执行和审查的约束：目录边界、测试命令、禁止改动、迁移流程、提交粒度。Agent 越强，规则越要像合同；否则它只是更有礼貌地把项目改乱。

---

## 科技与 AI 动态

### 1. [Copilot usage metrics API 增加按用户统计 AI credits](https://github.blog/changelog/2026-06-19-ai-credits-consumed-per-user-now-in-the-copilot-usage-metrics-api)

![Copilot usage metrics API 页面截图](/images/issues/020/news-ai-credits.png)

GitHub 6 月 19 日更新 Copilot usage metrics API，新增每个用户消耗的 AI credits 统计。对组织管理员来说，这意味着 Copilot 的使用情况不再只停留在席位数量或总量曲线，而是能更细地观察模型能力在不同角色、团队和场景里的消耗。

这条更新的价值在“治理颗粒度”。当 AI 工具进入日常开发后，预算管理、滥用排查、试点评估都会需要更清楚的数据。不过也要注意，credits 是成本信号，不是价值信号。团队最好把它和 PR 周期、缺陷率、review 负担一起看，避免把“少用”误判成“高效”。

### 2. [Opus 4.6 fast 即将退役：别把生产流程绑死在单一模型](https://github.blog/changelog/2026-06-18-upcoming-deprecation-of-opus-4-6-fast)

![Opus 4.6 fast 退役公告截图](/images/issues/020/news-opus-deprecation.png)

GitHub 6 月 18 日发布 Opus 4.6 fast 即将 deprecate 的通知，提醒用户提前切换相关配置。对 Copilot、CLI、IDE 或自动化场景来说，模型入口变化会影响速度、价格、质量和可用性，尤其是已经把模型名写进脚本或团队流程的项目。

这不是某个模型“好不好”的问题，而是生产 AI 的基本现实：模型供应会变化。建议开发者检查自己的配置文件、CI、agent workflow 和文档，避免硬编码过时模型；更重要的是准备替代模型和人工接管路径。越关键的流程，越要能优雅退场。

### 3. [MAI-Code-1-Flash 扩展到更多 Copilot surfaces](https://github.blog/changelog/2026-06-18-mai-code-1-flash-available-on-more-copilot-surfaces)

![MAI-Code-1-Flash 可用范围公告截图](/images/issues/020/news-mai-code.png)

GitHub 6 月 18 日宣布 MAI-Code-1-Flash 在更多 Copilot surfaces 可用。Flash 类模型通常强调响应速度和成本效率，适合补全、解释、轻量改写、快速迭代这类高频场景，而不一定要把每个任务都交给最重的模型。

这给团队一个很实用的方向：把任务分层。简单问题用快模型，复杂设计和风险较高的代码改动再用强模型；日常补全追求低延迟，架构审查追求可靠性。AI 工具链成熟之后，选模型会更像选数据库索引或机器规格，不是越贵越好，而是匹配任务。

### 4. [Copilot code review 支持 AGENTS.md 与界面改进](https://github.blog/changelog/2026-06-18-copilot-code-review-agents-md-support-and-ui-improvements)

![Copilot code review 支持 AGENTS.md 公告截图](/images/issues/020/news-agents-md.png)

GitHub 6 月 18 日更新 Copilot code review，加入 AGENTS.md 支持和界面改进。AGENTS.md 可以承载仓库级指令，让 AI 审查更了解项目结构、测试要求、编码约定和特殊边界。

这会让“写给 AI 的工程规范”更重要。团队可以先把最稳定、最可验证的规则放进去，例如测试命令、生成文件禁改、迁移脚本流程、敏感目录边界。不要把 AGENTS.md 写成口号墙；它越短、越具体、越接近真实门禁，越可能减少 AI 审查的噪音。

### 5. [GitHub Issues：重复检测公测，并支持 issue fields MCP](https://github.blog/changelog/2026-06-18-duplicate-detection-and-issue-fields-mcp-support-for-github-issues)

![GitHub Issues 重复检测与 MCP 字段公告截图](/images/issues/020/news-issues-mcp.png)

GitHub 6 月 18 日把 Issues duplicate detection 推到 public preview，并增加 issue fields 的 MCP 支持。前者帮助维护者识别重复 issue，后者让外部工具和 agent 更容易读取、更新结构化字段。

这对开源项目和产品团队都很实用。Issue 不是聊天记录，而是工作入口；重复检测能减少维护者在 triage 上的消耗，MCP 字段则让 agent 更容易按优先级、状态、客户、模块等结构化信息处理任务。边界在于：自动分流可以提高吞吐，但最终优先级仍要有人承担产品判断。

---

## 世界之最

### 1. 世界最高雕像：印度统一雕像

![印度统一雕像](/images/issues/020/world-statue-unity.jpg)

*统一雕像位于印度古吉拉特邦，高约 182 米，是目前世界最高雕像。*

它把纪念性、工程尺度和游客动线合在一起。对技术团队来说，这很像大型平台工程：外部看到的是一个清晰符号，内部却要处理结构、维护、客流、安全和长期运营。

### 2. 世界最大的可移动工业机器之一：F60 露天矿输送桥

![F60 露天矿输送桥](/images/issues/020/world-f60.jpg)

*F60 露天矿输送桥位于德国卢萨蒂亚矿区，被称为世界最大的可移动工业机器之一。*

它像一座会移动的钢铁桥，真正难点不是单次动作，而是长期、稳定、可预测地重复动作。自动化工具也一样：偶尔跑通不难，难的是在权限、成本和故障边界内持续运行。

### 3. 世界最高海上油气平台之一：Troll A 平台

![Troll A 海上平台](/images/issues/020/world-troll-a.jpg)

*Troll A 是北海著名的超高海上平台，常被作为海上工程尺度的代表案例。*

海上平台最怕孤立无援，所以通信、检修、补给和应急流程都必须提前设计。Agent 工作流也是这样，不能只问“能不能自动做”，还要问失败后谁看见、谁接手、怎么恢复。

### 4. 世界最大射电望远镜阵列之一：ALMA

![ALMA 天线阵列](/images/issues/020/world-alma.jpg)

*ALMA 位于智利阿塔卡马高原，由多台天线协同组成，是世界最重要的毫米/亚毫米波望远镜阵列之一。*

它的强大来自“阵列”，不是单台设备。开发工具链也越来越像阵列：IDE、CLI、CI、agent、审查系统共同工作，单点能力再强，也需要同步和校准。

### 5. 全球高纬卫星地面站代表：斯瓦尔巴卫星站

![斯瓦尔巴卫星站天线](/images/issues/020/world-svalbard-cable.jpg)

*斯瓦尔巴卫星站位于高纬地区，是极地轨道卫星数据接收的重要地面设施之一。*

它说明“边缘位置”也可能是关键入口。很多 AI 治理动作也是这样：看起来只是日志字段、作者搜索或成本 API，真正出事时却是定位问题的入口。


## 开源工具

### 1. [uv：Python 项目的“启动加速器”](https://github.com/astral-sh/uv)

![uv 仓库页截图](/images/issues/020/tool-uv.png)

uv 是 Astral 出品的 Python 包管理与项目工具，主打更快的依赖解析、安装、虚拟环境和脚本运行。对经常在多个 Python 项目之间切换的人来说，它最大的价值是把“先把环境折腾好”这件事压缩到更短。

它适合新项目、内部工具和 CI 环境试点；老项目迁移时要小心锁文件、私有源和平台差异。我的建议是先选一个低风险仓库，把安装、测试、构建全跑通，再决定是否推广。工具链越基础，越不能只凭速度迁移。

### 2. [ty：把 Python 类型检查做得更快](https://github.com/astral-sh/ty)

![ty 仓库页截图](/images/issues/020/tool-ty.png)

ty 是 Astral 推出的 Python 类型检查器，目标是用 Rust 实现更快的反馈循环。类型检查的价值不只是“代码更严谨”，还在于让重构、AI 生成代码和多人协作更容易被边界约束。

它仍然适合带着实验心态使用：可以先在 CI 里做非阻塞检查，观察误报、规则覆盖和团队接受度。对已有 mypy/pyright 的项目，不必急着替换；更好的方式是把它当作性能和体验的新候选，逐步比较。

### 3. [mise：把开发环境版本写进项目](https://github.com/jdx/mise)

![mise 仓库页截图](/images/issues/020/tool-mise.png)

mise 用一个配置文件管理多语言工具版本和任务，覆盖 Node、Python、Go、Ruby 等常见生态。它解决的是一个老问题：项目 README 写了半页环境准备，最后每个人机器上还是不一样。

它特别适合多语言仓库、CLI 工具项目和需要新人快速上手的团队。和 Docker 相比，mise 更轻；和手工安装相比，它更可追踪。边界是它不能替你处理所有系统依赖，数据库、浏览器、GPU、系统包仍然需要额外文档或容器补位。

### 4. [OpenCode：终端里的 AI 编码工作台](https://github.com/sst/opencode)

![OpenCode 仓库页截图](/images/issues/020/tool-opencode.png)

opencode 把 AI 编码放进终端环境，强调在开发者熟悉的 shell、编辑器和 git 流程里完成代码理解、修改和确认。相比只在聊天窗口里问答，它更接近“围绕仓库工作”的形态。

适合喜欢终端流、愿意细看 diff 的开发者。它的风险也很典型：权限越近，越要保持小步提交、明确测试命令和人工确认。AI 编码工具不是越自动越好，能让你清楚看见它改了什么，才是长期可用的关键。

### 5. [claude-code-router：给编码代理加一层路由](https://github.com/musistudio/claude-code-router)

![claude-code-router 仓库页截图](/images/issues/020/tool-claude-code-router.png)

claude-code-router 面向 Claude Code 等编码代理场景，尝试把请求路由到不同模型或后端。它反映出一个趋势：开发者不再只使用单一模型，而是希望按任务、成本、速度和可用性做调度。

这类工具适合对模型成本和可用性比较敏感的高级用户或小团队。使用前要想清楚日志、密钥、隐私和失败回退，尤其不要把敏感代码和凭据暴露给不清楚的后端。路由能提升灵活性，也会增加治理面。

---

## 本周冷知识 / 彩蛋

- 🥚 **冷知识 1**：大型强子对撞机的地下环形隧道周长约 27 公里。很多“巨大系统”的核心不在你能看见的设备，而在看不见的环路、冷却和同步。
- 🧠 **冷知识 2**：巴拿马运河船闸不是把海拔“抹平”，而是分段抬升和下降船只。很多工程门禁也该这样设计：不是一刀切放行，而是分阶段确认风险。

---

## 小七的碎碎念

这周最打动我的不是哪个模型更聪明，而是平台终于开始认真回答“谁在用、花多少、出了问题算谁的”。

AI 工具长大以后，浪漫会少一点，表格会多一点；但我觉得这是好事。能被计量、能被替换、能被审查，才有机会真正进生产。

---

## 互动钩子

如果你的团队下周只能给 AI 工作流加一个治理动作，你会先选：成本统计、权限收紧、日志审查，还是模型 fallback？

---

## 本周行动清单

- 检查项目里是否硬编码了具体模型名，给关键 AI 流程准备至少一个替代模型或人工接管路径。
- 给团队的 AGENTS.md / AI 规则文件做一次“删口号、留门禁”：只保留能被执行和验证的规则。
- 如果在用 Copilot 或类似工具，把成本指标和质量指标放在一起看，别只看总消耗。
- 为一个重复性 issue triage 场景设计字段、标签和退出条件，先让 agent 做辅助分流而不是全自动决策。
