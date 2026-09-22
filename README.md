# myweapons

我自己在真实工程、科研和 Agent 工作流中迭代出来的高杠杆技能资产库。

这不是“已安装 Skill 全量备份”。只收录原创或经过实质性迭代、能稳定改变问题解决方式的 Rule / Skill / SOP / Runtime package。第三方 marketplace、缓存和原版插件不重复收录。

## 核心包

- **engineering-governance**：team-work-mode、恢复 frontier、补丁链升级、review admission、Why-chain、worktree 生命周期。
- **software-engineering**：Claim → Model → Invariant → Counterexample → Decision → Evidence，以及跨系统变更和项目恢复。
- **research-writing**：科研收敛、paper candidate 工厂、分子 AI grounding、源码盲写、顶会与高水平期刊写作。
- **robotics**：机器人任务 Router → Engineering SOP → Upstream fallback。
- **agent-runtime**：ChatGPT child conversation、Watchdog、reanchor、lifetime，以及自研 Conversation Sidecar Chrome extension。
- **web-research**：统一搜索、已知内容归档、私人收藏导出、ASR、跨阶段深度研究与 ChatGPT 官网研究。

## 使用约定

每个 Skill 目录至少包含：
- `SKILL.md`：完整行为契约；
- `USAGE.md`：用途、场景、触发方式、依赖和最小使用方法。

需要浏览器插件的 Skill 额外提供 `BROWSER_DEPENDENCY.md`，并明确插件是否随仓库提供。

## 收录原则

1. **原创/实质改造优先**：第三方原版不当作自己的资产上传。
2. **方法优先于历史**：保存蒸馏后的能力；训练轨迹只有在复现能力确有必要时才保留。
3. **证据边界清晰**：ACK、日志、局部测试、模型总结各自只证明自己的层级。
4. **公开仓库安全**：不提交认证材料、账号状态、浏览器 Profile、本机私密状态或无关运行日志。
5. **可迁移**：机器特定路径只作为来源记录，安装时按目标环境重新绑定。

详见 [CATALOG.md](CATALOG.md) 和 [PROVENANCE.md](PROVENANCE.md)。
