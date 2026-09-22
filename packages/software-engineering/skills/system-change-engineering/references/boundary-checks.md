# 按发生变化的边读取，不全量执行

本页是 `system-change-engineering` 的可选展开，不是每次任务必读，也不取代现有工程技能。

## 表示转换与身份

先写 `语义值 → producer表示 → wire → consumer重建`，再从真实 schema 推导测试空间。对空/缺省/null、枚举、单位、坐标系、时钟域、消息身份分别建模，不用字段同名推断语义相同。

序列化涉及签名、hash或兼容性时，用当前依赖的真实参考实现做 differential test；固定向量只是回归快路，不等于参考实现对照已做过。至少考虑空集合、重复元素、空元素、多字节UTF-8、嵌入零字节和长度编码边界。Protobuf repeated string 的 `[]` 与 `[""]` 不同：前者没有字段，后者仍有 field tag 和零长度。单个标量默认值的省略规则不能直接套到 repeated 元素。

响应记录原始 owner/设备/帧身份、request关联及选择策略；聚合结构被投影为单对象时，明确唯一性/选择条件和丢弃信息。未知枚举、非法数值、截断payload不能靠字符串转换“成功解析”。合法旧新表示分别测试。

## 权限与失败

分开业务 payload、来源身份、授权证明、错误返回、deadline/取消。遵循已确认协议；增加 header、metadata 或 adapter 都需验证旧消费者是否仍成立。不能为了接通而关闭生产鉴权，也不能把另一个owner的权限检查复制成第二个权威。

每个拒绝负例配同一实例/版本/路径的有效正例，然后只改变要攻击的条件：未签名、非法domain、payload与metadata冲突、paired身份与声明冲突、重放、过期、错误hash。测试接收到错误并确认业务handler没有执行；连接拒绝或服务死亡不是鉴权PASS。

拒绝响应必须真正能表达失败：检查字段的类型与基数，不只看名字。没有合适业务错误结构则返回明确非成功transport status。区分“业务已执行但失败”“鉴权未执行”“请求超时且远端效果未知”。

注入测试state只覆盖该state之后的路径；不能据此宣称真实配对/凭证发放已验收。使用本机非loopback地址可以覆盖相关filter分支，但不等于验证另一台机器的路由、防火墙、时钟偏差和交付环境。

## 资源与运行生命周期

看到新owned fd/socket/thread/device/CURL/crypto/CUDA/DDS handle，立即确定创建、所有权转移、拷贝/移动、初始化失败、close/析构、重入和并发行为。优先使用库的RAII/生命周期设施；必要时禁止拷贝或明确定义移动。单实例close幂等不能排除浅拷贝double-free。

构建环境、安装产物和实际加载进程是三个证据对象。镜像标签不是不可变版本；缓存路径、underlay、动态库、挂载、UID/GID和插件加载位置须匹配。用容器格式化/构建时避免把宿主源码写成root owner。

## 组合测试和交付

从最便宜的区分性证据开始：局部测试 → 受影响边集成 → 必要端到端；物理效果声明才增加物理证据。这不是每次强跑所有层的线性清单。

至少给出一个与变化相关的“局部都PASS，组合仍错”反例；为安全/序列化/生命周期等独立风险分别补测试。记录反例当前公共入口是否可达、违反的下层契约、影响范围；不能靠更换验收定义把缺陷降为成功。

保留行为契约和混合版本矩阵：producer旧/consumer新、producer新/consumer旧、必要的同时迁移/功能开关、回滚后的持久状态。只有版本组合实际相关才展开。

最终记录精确测试版本及未覆盖项。单元测试通过、模拟场景通过、人工真实集成通过、已自动化长期回归，必须分别报告。

## 本机入口的来源与边界

本次接入复用本机 Graft 的两种真实机制：`~/.agents/skills/graft/SKILL.md` 的行为描述用于发现，以及安装包 `dist/hosts/sections.js` 的标记区块用于保留AGENTS其余内容。本机 DevSpace `open_workspace` 暴露 skill 的 name/description/path；已打开会话的发现缓存不等于自动刷新。

公开说明的交叉核对来源：`https://www.npmjs.com/package/@nanonets/graft` 的 Agent integration。不同客户端可能另有hooks；本机此次只接可验证的 Skill + AGENTS + 原技能路由，不声称新增PreToolUse硬拦截，不修改Graft、DevSpace核心或业务仓库。
