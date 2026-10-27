# Installation / 安装

[English home](../README.md) · [中文首页](../README_zh-CN.md) · [Quick start / 快速上手](quickstart.md)

## Windows x64 preview

- Build / 构建：`v0.1.0-preview.656a16e02897` (2026-10-22).
- [Installer / 安装程序](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.656a16e02897/YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe) · [Release notes / 发布说明](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.656a16e02897).
- Size / 文件大小：788,128,620 bytes (about 752 MiB).
- SHA-256：`b344f2abdc919d9792769a1b793d2c0d79e07df3c9be112c95383e7c7e2db1ed`.

The checksum above is the GitHub release asset's reported SHA-256, checked on 2026-10-28. It identifies the existing installer; this documentation update did not rebuild or reinstall it.

以上摘要来自 GitHub 对该 Release 附件提供的 SHA-256，核对日期为 2026-10-28。本次文档更新没有重新构建或安装该安装包。

```powershell
Get-FileHash -Algorithm SHA256 '.\YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe'
```

Compare the returned hash with the value above. / 核对输出摘要与上面一致。

## Install and activate / 安装与激活

1. Download the `.exe`; run the installer and choose an installation directory. The GitHub `Source code` ZIP/TAR files are not installers. / 下载并运行 `.exe` 安装程序，按向导完成安装；不要下载源码压缩包作为安装程序。
2. Launch YB_MOL Studio. This is an unsigned preview; Windows may show an unknown-publisher warning. Check the source and checksum before deciding to proceed. / 启动 YB_MOL Studio。预览版未签名，Windows 可能提示未知发布者；请先确认来源和摘要。
3. If activation is requested, generate the request information in the activation window and send it privately to the product team. Import the returned license file or paste the license, then activate. / 如提示激活，在激活窗口生成请求信息，私下联系产品团队，取得许可证后导入文件或粘贴并激活。
4. Open a new test project in a writable folder and follow the [quick start](quickstart.md). / 在可写文件夹创建测试项目，按[快速上手](quickstart.md)操作。

Activation and usage terms: [zhaoyanbo@ccbiomol.com](mailto:zhaoyanbo@ccbiomol.com), [zhangshuai@ccbiomol.com](mailto:zhangshuai@ccbiomol.com). Download availability does not imply unrestricted licensing. External model APIs and computing services can have separate charges.

授权范围、有效期和使用条件请联系产品团队确认。可下载安装包不代表无限制授权，外部模型 API 和计算资源可能单独收费。

## Updating / 更新

Back up important projects and exported structures before updating. Use the release notes for the selected build; keep the original installer filename when checking hashes. Older filenames and screenshots may retain historical branding.

更新前备份重要项目和导出结构，以选定版本的发布说明为准。核对摘要时保留安装包原文件名；历史文件名和截图可能保留旧品牌写法。
