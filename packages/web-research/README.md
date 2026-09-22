# Web Research Package

## 目标
把“搜索发现、已知内容归档、私人收藏导出、音视频转写、跨阶段深度研究、ChatGPT 官网研究”拆成边界清晰的自研路由。

## 路由
- `yichen-web-research`：跨平台、跨阶段总入口。
- `yichen-unified-search`：关键词驱动的公共内容发现与候选核验。
- `yichen-content-archive`：处理用户已给 URL、URL 文件或已确认候选。
- `yichen-bookmarks-export`：当轮授权后的私人收藏/书签只读导出。
- `yichen-asr`：本地音视频转写后端路由。
- `yichen-chatgpt-web-research`：使用用户已登录的 ChatGPT 官方网页做研究。

## 不变量
发现、归档、私人读取和转写是不同权限/操作面，不能因为前一步有权限就自动扩展到下一步。
