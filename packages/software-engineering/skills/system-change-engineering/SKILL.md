---
name: system-change-engineering
description: Use when adding a capability or vertical module, integrating or migrating a real system, or fixing a boundary failure while requirements, ownership, consumers, repositories, deployment dependencies, or acceptance are unclear. Also use when a local change reveals another owner or cross-boundary contract, even inside one repository. Triggers include 新增能力、纵向模块、模糊需求、归属未知、跨层接入. Not for conceptual questions or proven isolated edits.
---

# System Change Engineering

从用户结果推导最小系统变更面，再绑定仓库和文件。仓库数量不是触发条件；仓库名也不是必须由用户提供的输入。

这是既有工程流程的**条件入口**，不另建调度器、审批链或全系统模型。复用 `software-engineering-review` 的 Claim → Model → Invariant → Counterexample → Decision → Evidence，以及现有 router 的 TARGET / REFERENCE / DELTA / FRONTIER / PROBE。只补一项 SURFACE，不重复写计划。

当全局 `TEAM_WORK_MODE=ON` 时，团队职责边界高于系统发现结果。SURFACE 可以扩大**阅读/理解范围**，但不能自动扩大 mutation authority；发现另一 owner、共享基础设施或跨仓依赖时，先判断它是当前 Claim 的显式/必要 owned change，还是 `OBSERVED-UNOWNED`。后者记录证据并 handoff/block，不因“系统上相关”直接接管。`dependency closure != ownership closure`。

## 何时进入、何时跳过

在选择修改位置或开始局部设计前，出现任一信号就读本 skill：新增用户可见能力/纵向模块；职责或消费方未知；共享接口、权限、状态归属或部署边界可能改变；局部修补反复跨越边界。一个 monorepo 同样触发。

任务确实只有一个已知 owner、无接口/共享状态影响时走局部快路；纯概念讨论、拼写/格式修正不启动系统发现。恢复任务先复用已验证的 SURFACE，只更新变更或失效的边，不因换对话重扫。

同一边界若已经出现连续修补、补丁补丁、fallback/reconcile 增殖或 mutation surface 持续扩大，先暂停新变更并回看任务起点/最近正确基线以来的历史 diff。把“历史改动是否越界或基于错误假设”作为当前 FRONTIER；没有证据证明继续前向 patch 是当前 owner 的最小正确动作时，不以赶进度为理由继续堆补丁。

## 1. 分开意图未知与实现未知

用现有需求写出 `谁使用 → 可观察结果 → 成功/失败判据 → 允许修改范围`，并标注非目标。区分用户明确要求、证据确认、待验证假设。

源码、配置和历史能回答的 owner/路径/依赖问题自己查；本机还是远程、仅显示还是标定测量、授权和验收取舍等真正改变方案的意图问题，先检索已给出的约定，仍无答案才集中问必要问题。不用实验替用户选择目的，也不把“新增模块”当成必须创建新组件的命令。

## 2. 继承基线，沿证据发现必要切片

先恢复当前任务和最近可执行的相邻能力，冻结 KEEP，只追 CHANGE / UNKNOWN。按对象选证据，不用一条固定扫描顺序覆盖所有问题：

- **当前部署事实**：进程/服务/容器、设备实例、实际 topic/service、加载配置与二进制身份；只读观察，不擅自启动设备、重启服务或改变权限。
- **声明及潜在依赖**：launch/manifest、package/CMake/import、CI、Docker、schema、测试和部署文档。设备离线或模块未启动不意味着该依赖不存在；区分已部署图、声明图、目标图。
- **代码来源**：从入口/契约追 source path、remote、submodule 固定版本、包来源及镜像构建 provenance，定位真正 owner 所在仓库。不要按目录名猜 owner，也不要把定义复制到方便修改的仓库。

搜索从已知项目根/历史入口开始，沿一条有证据的边扩展；结合名称、数据类型、调用/订阅关系。未命中只说明已搜索范围未发现。Graft 已有且适配当前 checkout 时用它找代码关系；先核对根目录/覆盖范围，缓存失效或未索引配置才定向用 read/rg。Skill 可发现不代表当前目录已有 Graft 索引；尚未绑定仓库或只有交接文档时，直接读取声明材料，不为了遵守 Graft 先试 CLI 或建图。不要给整个 home 建图；外部开源只用来评估已定位缺口的兼容基线，不替代私有系统事实。

从用户入口向实际效果追、从事实生产者向消费者追，在必要边界汇合。SDK、Gateway、协议仓、UI、仿真并非必经层。配置接线已足够就不新增实现；相关但无需修改的 owner 也写 KEEP 及理由。

## 3. 收敛成一个 SURFACE

沿用现有计划/恢复记录，补一张小表即可：

`职责/transition | owner与证据 | 输入→输出契约 | 源码/仓库/worktree | build/test/runtime身份 | KEEP/CHANGE/UNKNOWN | 最便宜的判别检查`

每条关键边标 confirmed / hypothesized / unknown。build/install/startup/runtime/optional 依赖分开；记录网络、权限、挂载路径、设备、可混用版本等实际相关约束，不机械填表。

找到 owner 后才选工作树：先查其 Git/worktree/dirty 状态，复用已有兼容工作树；并行写入才建隔离面。未知 remote/缺访问权限保留 unresolved frontier，不猜 URL、分支或已安装版本。

**允许实施的门槛**：受影响路径的 owner、输入输出、不变量、执行环境、验收方式已足以决定最小改动；会改变该改动的关键未知已解决，或该边明确暂停。无关未知不阻止独立安全工作。

**停止发现的门槛**：最小切片已能解释结果且没有影响下一步决策的未知，就执行最小可逆验证。连续检索不改变 SURFACE/FRONTIER 时换证据源或询问真正决策，不扩大成全仓/全机理解。结论可以是“无需代码变更”。

## 4. 在既有工程流程内实施和证明

由 `software-engineering-review` 继续组合门和局部实现；真实机器人执行才接 `robotics-engineering-sop`。这些 skill 已有相同 SURFACE 时不互相重复调用发现流程。

新增或改动边界时，按需检查：[边界与证据清单](references/boundary-checks.md)。重点是同一事实/意图跨表示后仍保持身份、值、权限、失败和时间语义，以及资源从创建到销毁的所有权。业务 payload 与 auth/trace/deadline 等 metadata 归属按现有契约决定，不预设全塞 payload 或全移 header。

先用真实 schema/owner 实现产生反例与失败测试，再改动；参考序列化器对照、实际 filter 行为和真实消费结果优先于源码字符串断言。测试数量不等于覆盖，单仓 PASS 不推出组合 PASS。

审计只看固定 diff/版本和剩余高风险边：一名只读审计者可在主线开发下一独立步时复查前一步；记录真实 session/URL、完成状态，失败先读状态不重复派发。未审不能写已审；触发提示不是运行时强制保证。

审计意见只返回主对话作为候选证据，不直接扩大 SURFACE。主对话按 `Claim relevance | ownership | invariant necessity | evidence | marginal value | cost/risk | stop condition` 做 admission；只有被明确 ACCEPT 的意见才进入后续 mutation。已达到验收目标时，默认停止，不把“还能更稳/更漂亮/更完整”自动转成新工作。

## 5. 收口与版本一致性

验收必须对应用户声明的运行条件；localhost、旁路鉴权、注入测试配对状态都单独标记，不能替代真实远程/配对/部署全链结论。安全负例配相同环境下有效请求的正例，防止“服务没起来所以全拒绝”。

记录 `各仓 HEAD + dirty差异标识/补丁 | schema版本 | 镜像digest/二进制 | 启动配置/设备实例 | 测试与时间 | 未覆盖边界`。提交/推送/部署分别遵守授权；未提交时保存可重建差异，不强行 commit。存在独立发布消费者时检查旧新版本兼容、发布顺序、回滚及过渡状态，不能只测“三个本地最新版”。

输出只保留：改了哪个系统边界、证据证明到哪里、还剩什么。不把本地配置安装当成后续所有会话必然触发的保证。
