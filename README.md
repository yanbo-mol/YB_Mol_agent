# YB Mol Agent

**面向计算化学、结构生物学与分子设计研究者的桌面工作台。**

YB Mol Agent 当前公开版本由 CCBio 桌面工作台与 CCAgent 科研智能体组成。CCBio 将三维分子结构查看与编辑、项目文件管理和 CCAgent 自然语言辅助放在同一界面中。研究者可以检查结构，从原子、残基到整个体系进行修改，调用已配置的建模与计算工具，并保存、比较或恢复修改结果。

[下载 Windows 预览版](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.c6e4ba4788af/CCBio-0.1.0-win-64-UNSIGNED-c6e4ba4788af.exe) · [查看版本说明](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.c6e4ba4788af) · [阅读使用手册](https://ccbiomol.com/manuals/CCBio-Help-Manual.html) · [申请产品演示](https://ccbiomol.com/contact/)

[![CCBio 工作台：蛋白三维结构、结构列表与 CCAgent 分析面板](https://ccbiomol.com/images/products/ccbio-workbench-4o9h.png)](https://ccbiomol.com/images/products/ccbio-workbench-4o9h.png)

## CCBio 能做什么

- **查看与检查结构**：在三维视图和结构树之间定位分子、链、残基与原子。
- **精细编辑结构**：选择目标后进行原子、残基或体系级修改，并检查修改结果。
- **管理设计过程**：在同一项目中组织输入、输出和导出文件，保留原始结构以及不同设计版本。
- **辅助建模**：支持从已有结构开展蛋白编辑、分子组装和晶胞构建等工作。
- **使用科研智能体**：用自然语言描述任务，让 CCAgent 读取当前项目上下文，调用已配置的模型、建模与计算工具，并在会话中返回执行过程和结果。
- **连接远程计算环境**：将结构和任务发送到已配置的服务器，检查任务状态与输出，再将结果导回当前项目。

常用结构文件包括蛋白和复合物使用的 PDB/mmCIF，以及小分子使用的 SDF。不同格式对链标识、键级等信息的保留能力不同，正式计算前应按照手册检查导入和导出结果。

## 一个典型工作流

```text
导入结构 → 检查链、残基、原子与键 → 复制基线版本
        → 手动编辑或向 CCAgent 描述任务
        → 检查生成的结构、日志与警告
        → 对比结果 → 导出并重新加载复核
```

例如，可以导入一个蛋白—配体复合物，保留 WT 基线，在副本中完成残基替换或组分调整，再比较修改前后的结构并导出候选结果。CCBio 负责可视化、交互编辑和版本管理；需要真实能量评价或专门模拟时，应调用合适的计算工具并核对参数与输出，不能把手动摆放直接视为有效构象。

## CCBio 与 CCAgent

| 组件 | 主要作用 |
| --- | --- |
| **CCBio** | 提供三维结构视图、交互式编辑、项目文件和版本管理。 |
| **CCAgent** | 理解自然语言任务，读取当前结构与项目文件，并调用已配置的模型和工具。 |

两者使用同一个项目上下文：你可以手动选择和修改，也可以让 Agent 辅助执行；结果仍需由研究者检查、保存或恢复。

## 适用方向

CCBio 的产品方向覆盖：

- 抗体、蛋白与酶设计
- 小分子药物设计
- 晶体、表面、界面及其他凝聚态材料建模
- 聚合物结构设计

这些是产品覆盖方向，不代表当前预览版已经包含每个方向的完整计算流程。实际可用能力取决于具体版本以及已配置的模型和工具，请以对应 Release 说明为准。

## 下载与快速开始

当前提供 **CCBio 0.1.0 Windows x64 公开预览版**（构建 `c6e4ba4788af`）：

- [下载 Windows 安装包（EXE，约 734 MB）](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.c6e4ba4788af/CCBio-0.1.0-win-64-UNSIGNED-c6e4ba4788af.exe)
- [版本说明与已知限制](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.c6e4ba4788af)
- [下载 SHA256SUMS 校验文件](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.c6e4ba4788af/SHA256SUMS)

1. 下载具体 Release 的 Windows `.exe` 文件。GitHub 自动生成的 `Source code` 压缩包不是安装程序。
2. 按下方方法校验安装包的 SHA-256。
3. 安装并按照[安装与激活指南](https://ccbiomol.com/manuals/CCBio-Installation-Guide.html)完成设备激活。
4. 创建项目并导入结构。初次使用建议跟随[完整操作手册](https://ccbiomol.com/manuals/CCBio-Help-Manual.html#walkthrough)完成一次从导入、编辑到导出的练习。

正式版与标记为 **Pre-release** 的测试版分开管理。安装包名称、校验值、适用范围和限制均以你下载的 Release 为准。

## 当前预览版须知

这是未签名的 CI 候选构建，尚非客户正式版：

- Windows 可能显示“未知发布者”提示。
- 尚未通过交互取消验收。
- Quick Select 与右键编辑的目标衔接尚不一致，编辑前请核对目标。
- 不包含完整 GAFF 参数化、Vina、Meeko，也不包含 PDBFixer。
- 发布前的验证包括 OpenMM CPU 最小化和安装后的分子编辑 smoke；这不代表额外的功能、兼容性或计算精度认证。

请勿仅根据 Agent 的自然语言结论判断任务已经完成。应检查实际 Entry、版本、输出文件、退出状态、日志以及结构警告。处理未公开或敏感研究数据前，请确认所配置模型、远程服务器和计算工具的数据边界。

## 校验安装包

每个发布版本附带 `SHA256SUMS`。在 PowerShell 中运行以下命令，将输出与该版本的校验文件比对：

```powershell
Get-FileHash -Algorithm SHA256 "C:\Downloads\实际安装包文件名.exe"
```

## 文档与支持

- [CCBio 官网](https://ccbiomol.com/)
- [文档中心](https://ccbiomol.com/docs/)
- [安装与激活指南](https://ccbiomol.com/manuals/CCBio-Installation-Guide.html)
- [手动建模与操作手册](https://ccbiomol.com/manuals/CCBio-Help-Manual.html)
- [通用使用指南](https://ccbiomol.com/manuals/CCBio-User-Guide.html)
- [离线手册下载](https://ccbiomol.com/manuals/CCBio-HTML-Manuals.zip)
- [官网隐私说明](https://ccbiomol.com/privacy/)

需要设备激活、使用咨询、产品演示或科研合作，可通过以下方式联系：

- 邮箱：zhaoyanbo@ccbiomol.com、zhangshuai@ccbiomol.com
- 电话 / 微信：18506280715
- [产品演示与内测申请](https://ccbiomol.com/contact/)

## 关于本仓库

本仓库用于 CCBio 安装包分发、版本说明和文档导航，不包含核心产品源码。软件使用与授权以安装包附带的条款及设备授权为准。
