# Browser dependency

- Required: yes
- Bundled source: `../../browser-plugins/conversation-sidecar-extension`
- Role: 与真实 ChatGPT 页面建立 conversation transport，并支持受控 extension reload / reattach。
- Success criterion: Runtime Home 验证正确 extension identity、instance/build 与页面 reattachment；仅在 Chrome 中看到扩展图标不算成功。
