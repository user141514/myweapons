# Robotics Package

用途：把机器人任务从“模糊目标”推进到“可验证真实结果”。

链路：robotics-work-router -> robotics-engineering-sop -> robotics-upstream（仅当本地证据无法闭合且外部兼容性已建立时）。

核心不变量：先复用最近可执行基线；只追 first unknown frontier；真实机器人状态必须由当前 runtime/device 证据确认；source claim 与 physical claim 使用不同层级证据。
