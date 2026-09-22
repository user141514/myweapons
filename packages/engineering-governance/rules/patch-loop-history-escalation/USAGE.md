# 使用说明

用途：识别连续补丁正在补偿更早的错误决策。

触发：同一边界多次连续修复、fallback/reconcile 增殖、修改面持续扩大。

最小使用：回看 original assignment -> authorized diff -> later patches -> current failure；若撤回早期越界或错误假设即可消除后续补丁需求，优先回退而不是继续补偿。
