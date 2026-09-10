# CCBio 官方发布

衍波摩尔 CCBio 的安装包、版本说明与使用文档入口。

CCBio 面向生命科学与材料研究，提供分子结构查看与编辑、蛋白建模、晶胞构建，以及 CCAgent 辅助工作流。

## 下载

访问 [Releases](https://github.com/yanbo-mol/ccbiomol_release/releases) 获取已公开的安装包。下载具体版本 Assets 中的 Windows `.exe` 文件；GitHub 自动生成的 `Source code` 压缩包不是安装程序。

当前仓库尚未公开安装包，首个版本正在准备。需要内测安装包，请通过下方联系方式联系团队。

正式版与标记为 **Pre-release** 的测试版分开管理。测试版的适用范围及已知问题以对应版本说明为准。

## 安装与使用

- [官网](https://ccbiomol.com/)
- [文档中心](https://ccbiomol.com/docs/)
- [安装与激活指南](https://ccbiomol.com/manuals/CCBio-Installation-Guide.html)
- [手动建模与操作手册](https://ccbiomol.com/manuals/CCBio-Help-Manual.html)
- [通用使用指南](https://ccbiomol.com/manuals/CCBio-User-Guide.html)
- [离线手册下载](https://ccbiomol.com/manuals/CCBio-HTML-Manuals.zip)

安装指南可能对应指定候选构建。安装包名称、校验值和适用范围请以你下载的 Release 为准。下载客户端后仍需按指南完成设备激活。

## 校验安装包

每个发布版本附带 `SHA256SUMS`。在 PowerShell 中运行以下命令，将输出与该版本的校验文件比对：

```powershell
Get-FileHash -Algorithm SHA256 "C:\Downloads\实际安装包文件名.exe"
```

## 联系我们

- 邮箱：zhaoyanbo@ccbiomol.com、zhangshuai@ccbiomol.com
- 电话 / 微信：18506280715
- [产品演示与内测申请](https://ccbiomol.com/contact/)

本仓库用于软件分发，公开范围为本仓库文件及已公开的 Release 附件；不包含核心产品源码。软件使用与授权以安装包附带的条款及设备授权为准。
