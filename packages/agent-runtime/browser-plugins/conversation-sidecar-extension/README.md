# Conversation Sidecar Browser Extension

## 用途
这是 `chatgpt-subagents` / conversation worker 与 Watchdog 消息链路使用的自研 Chrome unpacked extension 源码快照。

## 使用场景
需要让本地 Sidecar Runtime Home 与真实 ChatGPT 页面建立受控通信时使用。

## 安装/触发
1. 先部署对应 Sidecar Runtime Home。
2. 在 Chrome 扩展管理页开启开发者模式。
3. 仅在 Runtime Home 要求人工建立信任时，加载该 release 对应的 unpacked extension 目录。
4. 之后由运行时验证固定 extension identity 与重连状态；不要把“扩展已显示”当作 conversation transport 已验证。

## 边界
这里只归档扩展源码，不包含浏览器 profile、登录状态或本机运行数据。
