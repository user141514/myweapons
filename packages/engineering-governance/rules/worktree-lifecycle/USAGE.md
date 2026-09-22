# 使用说明

用途：把 worktree 当作有 owner、purpose、exit condition 的有界执行面，而不是永久缓存。

触发：新工程任务需要选择/创建/保留 worktree，或任务结束需要收口。

最小使用：先查现有 worktree；优先复用兼容工作树；超过规则定义的新鲜度边界后进入 integrate / archive / discard。
