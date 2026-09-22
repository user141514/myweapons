# 使用说明

## 用途
跨会话、compaction、worker handoff 或故障恢复时重新锚定当前任务，而不是把旧摘要当新授权。

## 触发
上下文/执行主体变化后，需要确认“现在应该从哪里继续”。

## 最小使用
重读原始用户要求与后续修订；验证当前 task/target/host/root/revision；比较旧 checkpoint 与新事实；只恢复真正未解决的 blocker。
