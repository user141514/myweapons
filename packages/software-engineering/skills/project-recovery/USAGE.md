# 使用说明

用途：跨会话、机器、worker、worktree 或 runtime 恢复任务时定位正确执行 frontier。

触发：继续之前项目、从断点继续、对齐进度、恢复历史任务。

最小使用：先验证 identity/authority，再找 latest accepted transition + first unresolved transition；恢复只刷新易失状态，不重复已经证明的知识。
