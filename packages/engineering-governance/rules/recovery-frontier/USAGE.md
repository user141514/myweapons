# 使用说明

用途：跨会话、worker、daemon 或机器恢复时，从已证明边界继续，而不是重新调研。

触发：任务属于 continuation / handoff / retry / recovery。

最小使用：记录 Claim | Proven boundary | Invalidated evidence | First unknown frontier | Next discriminating action | Stop condition；只刷新易失状态。
