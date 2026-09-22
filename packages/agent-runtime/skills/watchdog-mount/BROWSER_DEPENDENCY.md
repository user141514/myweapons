# Browser dependency

- Required for end-to-end message path: yes
- Bundled source: `../../browser-plugins/conversation-sidecar-extension`
- Role: Watchdog/Sidecar 与精确 ChatGPT conversation 的浏览器消息通道。
- Control-plane mount verification 与实际消息发送是两条不同链路；注册成功不能替代 relay/页面通道验证。
