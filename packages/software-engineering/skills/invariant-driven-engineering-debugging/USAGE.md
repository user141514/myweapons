# 使用说明

用途：处理“修了很多次仍失败”“测试绿但用户失败”“状态导致环境分叉”的故障。

触发：同一问题经过多轮修复仍未收敛，或 explanation 多于 reproducible root cause。

最小使用：Initial reality -> user action -> required final reality；寻找一个跨层 invariant，并用互相独立的证据域验证。
