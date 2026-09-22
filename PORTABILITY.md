# Portability

这些资产来自三台实际工作机，因此少数原始 Skill / reference 中保留了来源机器的绝对路径。它们用于记录当时真实运行环境，不代表目标机器必须使用相同目录。

迁移时按以下规则处理：

1. **行为规则保持不变**：Claim、Invariant、触发条件、ownership、frontier 等语义不因路径变化而改变。
2. **Skill 路径重新绑定**：把来源机器的 `/home/ad/.agents/skills`、`C:/Users/.../.agents/skills` 映射到目标机器真实 Skill root。若宿主工具要求绝对路径，使用目标机器的绝对路径。
3. **本地 repository catalog 只是示例**：例如 robotics-upstream 中的本机 Unitree 路径只证明来源机曾存在这些 checkout，不证明新机器也有相同路径或版本。
4. **verification 文件保留 provenance**：其中出现的来源路径属于历史验证记录，不应直接作为新机器运行配置。
5. **浏览器插件分两类**：本仓自研 Conversation Sidecar extension 可以从源码恢复；外部 `chrome:control-chrome` 等依赖只按对应 BROWSER_DEPENDENCY.md 安装/提供，不从本仓伪造替代品。
