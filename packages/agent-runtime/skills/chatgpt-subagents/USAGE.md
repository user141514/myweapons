# 使用说明

## 用途
创建、复用和管理长期存活的 ChatGPT child conversation，并通过 Sidecar/WorkController 管理其工作状态。

## 触发
出现 ChatGPT 子对话、conversation worker、Sidecar child、长期复用 child conversation 等行为时。

## 依赖
需要 `conversation-sidecar-extension` 浏览器扩展以及对应 Sidecar Runtime Home。

## 最小使用
先确认 Runtime Home 与固定扩展 identity 已就绪；通过 managed conversation worker 创建/复用 child；`send` 只代表提交，不代表完成；最终读取同一 conversation/work 的真实完成状态。
