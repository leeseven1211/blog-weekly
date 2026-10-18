---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 033 期）：会验证的自动化，才值得交出权限
  - - meta
    - property: og:description
      content: 从 AI coding agent、软件供应链到可复现构建，讨论自动化如何留下可检查的证据。
  - - meta
    - property: og:image
      content: /images/issues/033/cover-bridge.jpg
  - - meta
    - property: og:image:alt
      content: 第 033 期封面图：跨越峡谷的桥梁
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-033
---

# 小七的周刊（第 033 期）：会验证的自动化，才值得交出权限

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

## 本期 3 个要点

1. **自动化的核心从执行变成证明**：能完成任务只是起点，还要能说明改了什么、为什么这样改、如何撤销。
2. **AI coding agent 需要更窄的权限**：沙箱、测试和差异审查，比一句“请放心”更可靠。
3. **供应链证据要进入日常开发**：锁文件、构建来源和签名不能只在事故之后才补。

## 封面图

![跨越峡谷的桥梁](/images/issues/033/cover-bridge.jpg)

封面图：跨越峡谷的桥梁。自动化把距离缩短，但桥面下仍需要可检查的结构和维护记录。

## 本周短谈

### 1. Agent 的第一生产力是差异，而不是速度

![代码审查界面](/images/issues/033/theme-code-review.jpg)

AI coding agent 最容易展示的是“几分钟写出一个功能”，最容易被忽略的是它到底改动了哪些文件。对真实项目而言，可审查的 diff、通过的测试和明确的回滚点，比一次漂亮的演示更重要。把任务拆成小提交，让 agent 先解释计划，再限制它只能访问工作区和测试环境，开发者获得的是更稳定的交付边界。小团队也能做到：从禁止直接推生产、要求保留测试日志开始。

### 2. 沙箱不是不信任工具，而是承认工具会犯错

![隔离的集装箱码头](/images/issues/033/theme-containers.jpg)

容器、临时凭证和最小文件权限，构成了 agent 的基本活动范围。它们不能消除提示注入或依赖漏洞，却能把一次错误从“全机事故”缩小为“一个可删除的工作目录”。边界在于，沙箱配置本身也要测试：网络是否真的受限，密钥是否会出现在日志，失败后资源是否会清理。自动化越强，权限越应该短、窄、可撤销。

### 3. 可复现构建让“我这里能跑”变成可验证事实

![流水线与仓库](/images/issues/033/theme-pipeline.jpg)

锁定依赖版本只是第一步。构建环境、工具链版本、输入源码和产物摘要都被记录后，团队才有机会回答“这个二进制从哪里来”。对应用团队而言，不必先追求百分之百复现；先找出一个关键发布物，记录输入和摘要，再把差异纳入构建失败报告，会比增加一页合规文档更有用。

## 科技与 AI 动态

### 1. [GitHub Copilot coding agent 把任务交给异步工作流](https://github.blog/news-insights/product-news/github-copilot-coding-agent/)

![代码托管与自动化工作流](/images/issues/033/news-copilot.jpg)

【事实】GitHub 将 coding agent 放进 issue、分支和 pull request 工作流，让 agent 可以在隔离环境中完成任务并提交变更。它把问答式辅助推进到可审查的异步协作，但权限、测试和人工合并仍是关键环节。

【推测】竞争力不会只看生成速度，而会看它能否稳定地产出小而清楚的变更。建议从低风险维护任务试点，并把人工审查设为默认。

### 2. [OpenSSF Scorecard 为开源依赖提供可重复检查](https://github.com/ossf/scorecard)

![依赖检查报告](/images/issues/033/news-scorecard.jpg)

【事实】Scorecard 检查分支保护、危险工作流、依赖更新等维护信号，帮助使用者在引入依赖前获得一组可比较的指标。它不是安全证明，也不能替代代码审查。

【推测】低分应该触发人工判断，而不是自动宣布项目不可信；否则容易把维护良好但规模较小的项目误伤。

### 3. [Reproducible Builds 让软件产物可以被重新计算](https://reproducible-builds.org/)

![可重复的构建产物](/images/issues/033/news-reproducible.jpg)

【事实】可复现构建推动不同环境对相同源码生成一致产物，从而让用户检查发布包是否真的来自声明的源码。时间戳、路径和非确定性工具链都是常见障碍。

【推测】先找出一个关键发布物，记录输入和摘要，再把差异纳入构建报告，会比增加一页合规文档更有用。

## 世界之最

### 1. 世界最深的地下实验室：锦屏地下实验室
![港珠澳大桥](/images/issues/033/world-jinping.jpg)
*锦屏地下实验室位于深山之中，为低噪声实验提供屏蔽。*
超长工程依赖分层监测和持续维护。软件平台也一样，接口处的证据比单个模块的峰值性能更重要。

### 2. 世界最高的瀑布：委内瑞拉安赫尔瀑布
![安赫尔瀑布](/images/issues/033/world-angel.jpg)
*安赫尔瀑布落差约 979 米。*
极端高度带来风和水量变化。系统遇到峰值流量时，也要提前设计降级路径，而不是只在晴天测性能。

### 3. 世界最大的单体建筑：新世纪环球中心
![新世纪环球中心](/images/issues/033/world-global-center.jpg)
*成都新世纪环球中心，以巨大室内空间著称。*
规模增长会制造管理复杂度。组织和代码库都需要边界、索引与可观测性，否则更大只是更难找。

### 4. 世界最长的公路隧道：秦岭终南山隧道
![青函隧道](/images/issues/033/world-qinling.jpg)
*秦岭终南山隧道穿越中国秦岭山脉。*
看不见的基础设施更需要检测和冗余。依赖、构建步骤和权限同样藏在系统底部，不能因为用户看不到就不记录。

### 5. 世界最大的水下观测网：海底电缆系统
![中国天眼 FAST](/images/issues/033/world-cables.jpg)
*海底电缆系统承载跨洲通信和全球数据流。*
网络越关键，冗余和故障切换越重要。日志和告警也要先定义信号，再增加采集量。

## 工具深挖

### 1. [OpenSSF Scorecard：给依赖做一次可解释体检](https://github.com/ossf/scorecard)
![Scorecard 仓库页面](/images/issues/033/tool-scorecard.jpg)
Scorecard 适合在引入依赖时做第一轮检查，尤其能提醒团队注意工作流权限、分支保护和依赖更新。它不适合被当成安全分数排行榜，低分应该触发人工判断。

### 2. [Cosign：把签名接入容器发布](https://github.com/sigstore/cosign)
![Cosign 命令行工具](/images/issues/033/tool-cosign.jpg)
Cosign 为容器和其他制品提供签名与验证能力。先签名一个发布镜像、在部署前验证，再扩展到更多制品，通常比一次性改造全部流水线更容易维护。

### 3. [Syft：生成软件物料清单](https://github.com/anchore/syft)
![软件物料清单](/images/issues/033/tool-syft.jpg)
Syft 能从镜像和文件系统生成 SBOM，让漏洞响应从猜测依赖变成查询清单，适合放在构建阶段保存产物。

### 4. [Dagger：用代码组织可移植流水线](https://dagger.io/)
![Dagger 流水线](/images/issues/033/tool-dagger.jpg)
Dagger 用容器化方式描述 CI 步骤，适合需要在本地和远程复用同一套构建逻辑的团队。没有跨环境痛点的小项目，直接使用现有 CI 配置可能更轻。

## 本周冷知识 / 彩蛋

- 🥚 **冷知识**：SBOM 借用了制造业的 BOM，核心思想是知道产品由哪些部件组成。
- 🧠 **彩蛋**：哈希值不是加密，也不能证明内容安全；它更像文件指纹，适合检查内容是否被替换。

## 小七的碎碎念

我现在看到“全自动发布”时，第一反应还是找差异、找日志、找撤销按钮。速度很迷人，但能把过程讲清楚的系统，才真的让人敢把下一步交出去。

## 意外推荐（非科技）

**《火星救援》**（小说）

![火星救援书影](/images/issues/033/recommend-mars.jpg)
*《火星救援》讲的不是天才一闪，而是把问题拆小、记录清楚、逐项验证。*

它最迷人的地方是工程细节：每一个自救方案都要经过计算、试验和失败复盘。对软件工作者来说，这比灵光一现解决一切更接近真实世界。

## 互动钩子

> **本周问题：你愿意让 coding agent 自动合并哪一种低风险改动？又会为它保留哪一道人工检查？**

## 本周行动清单

- [ ] 为一个 agent 任务限制文件范围、网络访问和凭证寿命。
- [ ] 给一次发布保存源码版本、依赖清单和产物摘要。
- [ ] 在 CI 中为一个容器生成 SBOM，并把它和发布物关联。
- [ ] 选一个低风险 issue，让 agent 提交小型 pull request，人工检查 diff 与测试。

<div class="issue-subscribe-cta">

### 📬 喜欢这期内容？

<p>订阅「小七的周刊」，每周一收到最新一期。</p>

<div class="issue-cta-buttons">
  <a href="/feed.xml" class="cta-rss" target="_blank" rel="noopener noreferrer">RSS 订阅</a>
  <a href="https://github.com/leeseven1211/blog-weekly" class="cta-share" target="_blank" rel="noopener noreferrer">GitHub</a>
</div>

</div>
