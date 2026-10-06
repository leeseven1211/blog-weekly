---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 031 期）：别把自动化当成免检通行证
  - - meta
    - property: og:description
      content: 从 AI 编程代理的权限边界，到软件供应链的可追溯性，再到基础设施的长期维护，本期讨论技术加速之后最容易被忽略的验证环节。
  - - meta
    - property: og:image
      content: /images/issues/031/cover-tokyo-skytree.jpg
  - - meta
    - property: og:image:alt
      content: 第 031 期封面图：东京晴空塔
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-031
---

# 小七的周刊（第 031 期）：别把自动化当成免检通行证

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

## 本期 3 个要点

1. **代理越能做事，权限越要具体**：能读网页、改代码、发请求，不等于应该拥有全部权限。
2. **供应链安全回到证据问题**：签名、SBOM 和可复现构建都在回答同一个问题：这个东西到底从哪里来。
3. **基础设施的价值不在新鲜感**：真正耐用的工具，往往把复杂性藏在清晰的默认值和可回滚路径后面。

## 封面图

![东京晴空塔](/images/issues/031/cover-tokyo-skytree.jpg)

封面图：东京晴空塔。高耸的结构只是最后的可见结果，真正让它站稳的是设计、检测和持续维护；自动化系统也一样，能跑起来不等于可以免检。

## 本周短谈

### 1. 自动化的下一关是“可撤销”

![电站控制室](/images/issues/031/theme-control-room.jpg)

AI agent 可以搜索、写代码、调用 API，问题因此从“它会不会做”转成“它做错时能不能停”。工程上最实用的答案不是再写一条宏大的原则，而是把权限拆成可审计的动作：读和写分开，预览和提交分开，生产环境和测试环境分开。只要一个动作不可逆，审批和回滚就不该被当成摩擦成本删掉。

### 2. “来源”正在成为软件功能

![Apple IIe 串行终端](/images/issues/031/theme-supply-chain.jpg)

今天的依赖、模型、容器镜像和代码片段都可能来自很长的链条。仅仅知道“测试通过”不够，还要知道构建输入、版本、签名和变更记录。对个人项目，可以从锁定依赖和保留构建日志开始；对团队，则应把 provenance 当作发布物的一部分。它不会让系统绝对安全，却能让排查从猜测变成证据。

### 3. 旧路线没有输给新路线

![金门大桥维护平台](/images/issues/031/theme-maintenance.jpg)

技术选型不是追逐最新名词，而是计算整个生命周期的成本。原生应用、成熟数据库、朴素的 CI 脚本，可能没有演示视频里的戏剧性，却更容易被接手、监控和修复。新工具应该通过小范围试点赢得位置，而不是凭借“大家都在用”直接进入关键路径。

## 科技与 AI 动态

### 1. [OWASP 持续整理 Agentic AI 风险](https://genai.owasp.org/)

![OWASP GenAI Security Project 官方页面](/images/issues/031/news-owasp.jpg)

OWASP 的生成式 AI 项目把提示注入、工具滥用、敏感信息泄露等风险整理成工程团队能读懂的清单。它的价值不在制造恐慌，而在提供共同词汇：安全评审可以具体到输入、工具、身份和输出。落地时挑两条最相关的威胁写成可复现测试，通常比复制整份清单更有效。

### 2. [Sigstore 把软件签名做成开放基础设施](https://www.sigstore.dev/)

![Sigstore 官方页面](/images/issues/031/news-sigstore.jpg)

Sigstore 用短期身份、透明日志和无密钥签名降低了开源项目发布可信制品的门槛。签名不能保证软件没有漏洞，但能帮助确认“这个制品是否由声明的工作流生成”。如果构建流程本身被植入恶意步骤，签名只会证明错误产物的来源，因此仍要配合最小权限和构建隔离。

### 3. [Python 官方持续推进解释器与工具链演进](https://www.python.org/)

![Python 官方页面](/images/issues/031/news-python.jpg)

成熟语言的更新往往没有“颠覆式”标题，却会改变大量服务的默认成本。升级不应只看基准测试：先用真实依赖跑测试和启动耗时，确认扩展模块与生产镜像兼容，再逐步扩大范围，并保留旧运行时的回滚路径。

### 4. [WebAssembly 组件模型靠近应用边界](https://component-model.bytecodealliance.org/)

![WebAssembly 组件模型官方文档](/images/issues/031/news-webassembly.jpg)

组件模型试图让不同语言编译出的模块通过明确接口组合，适合边界清晰、需要多语言扩展的系统，不适合为了“跨平台”把简单逻辑复杂化。最稳妥的试法是选一个输入输出明确的模块，测量冷启动、调试和部署成本。

## 世界之最

### 1. 世界规模最大的风电基地之一：甘肃瓜州风电场

![甘肃瓜州风电场](/images/issues/031/world-gansu-wind-farm.jpg)

*甘肃瓜州风电场，成片风机沿戈壁展开。* 它的规模不是靠一台设备撑起来的，而是由并网、调度、检修和长期运行共同构成；自动化平台也需要把局部成功接成稳定系统。

### 2. 世界级大型洞穴系统：马来西亚姆鲁国家公园风洞

![马来西亚姆鲁国家公园风洞](/images/issues/031/world-mulu-cave.jpg)

*马来西亚姆鲁国家公园风洞，洞穴群的一段真实通道。* 地下空间看不见全貌，必须依赖测绘、标记和安全流程才能可靠穿行；复杂软件系统同样不能只靠表面状态判断。

### 3. 世界最深海域：挑战者深渊

![挑战者深渊声呐地图](/images/issues/031/world-challenger-deep.jpg)

*挑战者深渊位于马里亚纳海沟，是地球海洋已知最深处。* 声呐地图和潜水记录把“不可见”变成可核对的证据，这正是观测、日志和追踪对自动化系统的意义。

### 4. 世界体积最大的单体树木：谢尔曼将军树

![谢尔曼将军树](/images/issues/031/world-general-sherman.jpg)

*美国加州的谢尔曼将军树，以树干体积计是已知最大的单体树木。* 体量大不等于可以忽略细节，树龄、环境和保护措施共同决定它能否继续存在；系统扩容也要同步补上维护责任。

### 5. 世界最大的热带雨林：亚马逊雨林

![亚马逊河与热带雨林](/images/issues/031/world-amazon.jpg)

*亚马逊雨林是世界最大的热带雨林，河流与森林组成一个难以靠单点视角理解的系统。* 规模越大，越需要分层监测和边界意识；平台指标也不该只剩一个漂亮的峰值。

## 工具深挖

### 1. [OpenSSF Scorecard](https://github.com/ossf/scorecard)

![OpenSSF Scorecard GitHub 仓库](/images/issues/031/tool-scorecard.jpg)

Scorecard 自动检查开源仓库的分支保护、依赖更新、危险工作流等信号，适合在引入第三方依赖前做初筛。它不是安全证明，也不能代替代码审查，但能把“这个仓库看起来靠谱吗”变成可重复指标。

### 2. [Renovate](https://github.com/renovatebot/renovate)

![Renovate GitHub 仓库](/images/issues/031/tool-renovate.jpg)

Renovate 自动创建依赖升级请求，支持分组、时间窗口和锁文件更新。它适合依赖较多又不想季度末集中还债的项目；先设置升级范围，否则机器人会把维护噪声变成新的待办。

### 3. [Dagger](https://dagger.io/)

![Dagger 官方页面](/images/issues/031/tool-dagger.jpg)

Dagger 用可组合的容器化函数描述 CI 流程，让本地和远程执行更接近。先把一条关键流水线迁移过去，比较缓存命中率、调试体验和运行成本，再决定是否扩大使用面。

### 4. [Zizmor](https://github.com/woodruffw/zizmor)

![Zizmor GitHub 仓库](/images/issues/031/tool-zizmor.jpg)

Zizmor 静态分析 GitHub Actions 工作流，帮助发现过宽权限、未固定 action 引用等问题。修复建议仍需结合实际工作流确认，不能机械地把所有警告改成失败。

## 本周冷知识 / 彩蛋

- **冷知识**：SBOM 类似食品配料表，重点不是“有了它就绝对安全”，而是出问题时能更快定位受影响范围。
- **彩蛋**：桥梁的伸缩缝不是瑕疵，而是给热胀冷缩预留的空间。软件系统里的版本边界和降级开关，也是一种伸缩缝。

## 小七的碎碎念

最近大家都在讨论谁的 agent 更能干，我更关心它能不能把每一步留下来。能快跑当然好，但知道什么时候刹车，通常更能决定一项技术能不能活过演示日。

## 意外推荐（非科技）

**《万物解释者》**（科普读物）

![阿雷西博射电望远镜](/images/issues/031/recommend-arecibo.jpg)

*阿雷西博射电望远镜，代表人类把不可见信号转成可理解证据的努力。* 好的解释不是堆更多术语，而是明确证据、假设和不知道的部分。对写产品文档和设计 AI 工作流，都很有帮助。

## 互动钩子

> **本周问题：你愿意给 AI agent 哪一项真实权限？又会为它保留哪一道人工确认？**

## 本周行动清单

- [ ] 给一个 AI 工具整理读、写、发布三类权限，并关掉不必要的默认权限。
- [ ] 为生产依赖生成一次 SBOM，确认出现漏洞时能否快速找到受影响服务。
- [ ] 用 Scorecard 或 Zizmor 检查一个真实仓库，修复一个高价值问题。
- [ ] 给一条自动化流水线补上失败后的回滚或人工确认节点。

<div class="issue-subscribe-cta">

### 📬 喜欢这期内容？

<p>订阅「小七的周刊」，每周一收到最新一期。</p>

<div class="issue-cta-buttons">
  <a href="/feed.xml" class="cta-rss" target="_blank" rel="noopener noreferrer">RSS 订阅</a>
  <a href="https://github.com/leeseven1211/blog-weekly" class="cta-share" target="_blank" rel="noopener noreferrer">GitHub</a>
</div>

</div>
