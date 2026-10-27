# Model connections / 模型配置

[Quick start / 快速上手](quickstart.md) · [FAQ](faq.md)

## Agent Models

1. Open **Settings → Agent Models**. / 打开设置中的 Agent Models。
2. In **Provider connections**, expand an available provider or use **Add model service** for your own service. / 展开常用服务商，或通过 Add model service 添加自定义服务。
3. Enter the API key, the endpoint required by that service and an available model ID. A connection's display name is not the API model ID. / 填入服务对应的 API Key、接口地址和账号可用的模型 ID；连接显示名称不等于模型 ID。
4. Select the provider and model in **Current model**, then **Apply**. / 在 Current model 选择服务和模型，并点击 Apply。
5. Try a small text request before a larger task. / 先测试一个简单文字请求，再执行复杂任务。

Connections and the default Agent model are shared across projects and Brain in the current settings design. Changes apply to the next Agent turn; an ongoing task keeps its active configuration. Historical screenshots can show older wording.

当前设置中，连接和默认 Agent 模型由各项目及 Brain 共用；修改用于后续 Agent 轮次，正在执行的任务保留其配置。历史截图可能显示旧版提示语。

## Image, audio and video / 图片、音频与视频

Use the corresponding **Image Models**, **Audio Models** or **Video Models** section for that capability. An Agent text-model key does not by itself enable image, speech or video generation. Configure the appropriate model and service endpoint; access and billing depend on the provider and your account.

对应能力分别在 Image Models、Audio Models、Video Models 中配置。Agent 文本模型密钥不自动代表具有图片、语音或视频生成权限；模型和地址应与服务商、账号权限对应，费用以服务商为准。

For example, a provider's coding-plan key can have different permissions from its general API key. Regional or workspace endpoints must match the key's issuing service. Use the provider's current documentation for exact URLs and model IDs; this guide intentionally does not freeze a model catalog.

例如，编程套餐专用密钥与通用 API 密钥的权限可能不同，地域和业务空间地址也需要与密钥所属服务匹配。具体地址与模型 ID 按服务商当前文档填写。

## If a request fails / 请求失败时

Record the provider, model ID, HTTP status, error text and whether images were involved. Check the exact error rather than inferring that every failure means a depleted balance. Never include the API key in a screenshot or public issue.

记录服务商、模型 ID、HTTP 状态码、完整报错及是否包含图片，根据实际错误定位；不要把所有失败都归因于欠费。截图和公开 Issue 中不要包含 API Key。
