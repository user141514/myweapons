# Agent Runtime Package

## 目标
保存我们围绕长期 ChatGPT 子对话、监督、恢复与长任务执行形成的运行时能力。

## 主要资产
- `chatgpt-subagents`：通过 Sidecar/WorkController 创建和复用受控 ChatGPT child conversation。
- `watchdog-mount`：把精确 conversation 与 Watchdog 控制面绑定并验证。
- `reanchor`：跨会话/上下文恢复时保持用户授权与正确 frontier。
- `lifetime`：让可长时间运行的本地命令/agent 具备可恢复生命周期。
- `browser-plugins/conversation-sidecar-extension`：上述 conversation transport 的浏览器扩展源码。

## 触发原则
这些是运行时能力，不是所有任务都加载。只有任务确实涉及长生命周期、子对话、Watchdog 或跨上下文恢复时才触发。
