# 使用说明

## 用途
为精确 ChatGPT conversation 注册、移动、验证或移除 Watchdog 监督。

## 触发
出现“挂 watchdog”“验证是否真的挂载”“切换 watchdog 到当前/指定对话”等行为时。

## 依赖
需要运行中的 Watchdog/Sidecar，并依赖 `conversation-sidecar-extension` 提供浏览器消息通道。

## 最小使用
先发现 live runtime 与 listener owner；再解析 exact conversation identity；完成 register/read-back/post-poll。不能把注册 ACK、UI badge、标题或 active tab 当作成功证明。
