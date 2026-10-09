# YB_Mol

**An agent-integrated visual editing platform for molecular and materials design.**

YB_Mol 是面向分子与材料设计的专业科研 Agent 平台。它将三维结构查看与编辑、项目文件、版本状态、领域 Skills 和计算工具组织在同一个可检查的研究工作区中，让研究者与 YB_Agent 围绕同一份分子对象协作。

[![Paper](https://img.shields.io/badge/Paper-ChemRxiv-0f766e)](https://doi.org/10.26434/chemrxiv.15010106/v1)
[![Windows](https://img.shields.io/badge/Windows-x64%20Preview-2563eb)](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.d87497e61870)
[![Website](https://img.shields.io/badge/Website-ccbiomol.com-102f31)](https://ccbiomol.com/)

[Website](https://ccbiomol.com/) · [Download](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.d87497e61870/YB_Mol-0.1.0-win-64-UNSIGNED-d87497e61870.exe) · [Read the Paper](https://doi.org/10.26434/chemrxiv.15010106/v1) · [Documentation](https://ccbiomol.com/docs/) · [Contact Us](https://ccbiomol.com/contact/)

[![YB_Mol 工作台：蛋白三维结构、项目文件与 YB_Agent 分析面板](https://ccbiomol.com/images/products/ccbio-workbench-4o9h.png)](https://ccbiomol.com/images/products/ccbio-workbench-4o9h.png)

> 截图来自历史版本，因此界面中仍可能出现 CCBio / CCAgent 名称。当前产品名称为 **YB_Mol**，科研智能体名称为 **YB_Agent**。

## Overview

通用对话模型可以解释问题，科研 Agent 还需要面对真实研究对象、选择专业工具、执行计算并交付可检查的结果。YB_Mol 围绕这一过程提供两层能力：

| 组件 | 作用 |
| --- | --- |
| **YB_Mol Workspace** | 管理项目、结构、文件、版本与计算结果，提供分子可视化和交互编辑。 |
| **YB_Agent** | 理解研究目标、规划步骤、读取项目上下文，并调用已配置的 Skills、模型与工具。 |

两者共享同一项目上下文。研究者可以手动选择和修改，也可以让 Agent 辅助执行；关键结构、输出与结论仍由研究者检查和确认。

## Quick Start

当前公开版本为 **YB_Mol 0.1.0 Windows x64 预览版**，构建 `d87497e61870`，发布于 2026-10-05。

1. 从 [GitHub Release](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.d87497e61870) 下载：

   ```text
   YB_Mol-0.1.0-win-64-UNSIGNED-d87497e61870.exe
   ```

2. 使用同一 Release 中的 `SHA256SUMS` 核对安装包：

   ```powershell
   Get-FileHash -Algorithm SHA256 "C:\Downloads\YB_Mol-0.1.0-win-64-UNSIGNED-d87497e61870.exe"
   ```

   预期 SHA-256：

   ```text
   5e15d97342f905ba607de1817d41d69893e8f6c8875a045763ab2af0c84e2b2b
   ```

3. 按照[安装与激活指南](https://ccbiomol.com/manuals/CCBio-Installation-Guide.html)完成安装和设备激活。
4. 创建项目并导入结构。首次使用建议跟随[完整操作手册](https://ccbiomol.com/manuals/CCBio-Help-Manual.html#walkthrough)完成一次导入、编辑、检查与导出。

GitHub 自动生成的 `Source code.zip` / `Source code.tar.gz` 不是安装程序。普通用户应下载 Release Assets 中的 Windows `.exe` 文件。

## Core Capabilities

- **统一分子工作区**：围绕小分子、蛋白质、复合物、晶体、表面和聚合物组织结构与项目文件。
- **三维查看与精细编辑**：从体系、链和残基定位到原子与化学键，并检查每次修改的实际结果。
- **任务规划与工具执行**：让 YB_Agent 读取当前项目上下文，调用已配置的模型、脚本和科学计算工具。
- **可检查的执行过程**：保留计划、工具调用、日志、结构变化、输出文件和版本状态。
- **本地与远程计算**：连接已配置的计算环境，跟踪任务状态，并把结果带回当前项目。
- **版本化设计过程**：保留基线结构，对比候选方案，在需要时恢复到已知状态。

## A Typical Workflow

```text
导入结构 → 检查链、残基、原子与键 → 保存基线版本
        → 手动编辑或向 YB_Agent 描述任务
        → 检查工具调用、日志、结构与输出文件
        → 对比候选结果 → 导出并重新加载复核
```

例如，可以导入蛋白—配体复合物，保留 WT 基线，在副本中完成残基替换或组分调整，再比较修改前后的结构并导出候选结果。需要真实能量评价或专门模拟时，应调用适合的计算工具并核对参数与输出；手动摆放本身不能视为已经获得有效构象或科学结论。

## Research Areas

- 抗体、蛋白与酶设计
- 小分子药物设计
- 晶体、表面、界面及其他凝聚态材料建模
- 聚合物结构设计

这些是平台覆盖方向，不代表当前预览版已经包含每个方向的完整计算流程。实际能力取决于所安装版本以及用户配置的模型、工具和计算环境。

## Paper

**YB_Mol Studio: an agent-integrated visual editing platform for molecular and materials design**<br />
Yanbo Zhao, Shuai Zhang, Shenggang Li, Zezhong Miao, Haijiao Fu, Miaomiao Wang<br />
ChemRxiv, Version 1, 2026. [https://doi.org/10.26434/chemrxiv.15010106/v1](https://doi.org/10.26434/chemrxiv.15010106/v1)

```bibtex
@article{zhao2026ybmol,
  title   = {YB_Mol Studio: an agent-integrated visual editing platform for molecular and materials design},
  author  = {Zhao, Yanbo and Zhang, Shuai and Li, Shenggang and Miao, Zezhong and Fu, Haijiao and Wang, Miaomiao},
  journal = {ChemRxiv},
  year    = {2026},
  doi     = {10.26434/chemrxiv.15010106/v1}
}
```

该文稿为预印本，尚未经过同行评审。GitHub 也会从本仓库的 [`CITATION.cff`](CITATION.cff) 生成引用信息。

## Preview Status and Known Limitations

当前安装包是未签名的 Windows x64 测试候选，不是已签名的客户正式版：

- Windows 可能显示“未知发布者”提示，请先核对来源、文件名和 SHA-256。
- 尚未完成交互式安装取消验收。
- 构建验证不等于完整 GUI 回归或真实远程 SSH 登录验收。
- OpenSSH 是可选系统客户端，不随安装包捆绑。
- 不包含完整 GAFF 参数化、Vina、Meeko 或 PDBFixer。
- 具体功能、修复和限制以所下载版本的 Release Notes 为准。

## Safety and Data Boundaries

YB_Agent 可以根据配置访问项目文件、网络、模型服务、外部程序和远程计算环境。使用时请注意：

- 不要仅根据自然语言回复判断任务已经完成；应检查实际结构、版本、输出文件、退出状态、日志与警告。
- 处理未公开或敏感研究数据前，确认所配置模型、数据库、远程服务器和计算工具的数据边界。
- 对外部程序执行、远程操作和可能改变文件的步骤保留人工检查与审批。
- 预览版不应用作未经验证的临床、生产或安全关键决策系统。

安全问题请按照 [`SECURITY.md`](SECURITY.md) 中的方式私下报告，不要在公开 Issue 中提交密钥、许可证文件、未公开结构或其他敏感数据。

## Documentation and Support

- [文档中心](https://ccbiomol.com/docs/)
- [安装与激活指南](https://ccbiomol.com/manuals/CCBio-Installation-Guide.html)
- [手动建模与操作手册](https://ccbiomol.com/manuals/CCBio-Help-Manual.html)
- [通用使用指南](https://ccbiomol.com/manuals/CCBio-User-Guide.html)
- [离线手册下载](https://ccbiomol.com/manuals/CCBio-HTML-Manuals.zip)
- [FAQ 与 Contact Us](https://ccbiomol.com/#faq)

可复现、且不包含敏感信息的软件问题可以通过 GitHub Issues 反馈。设备激活、产品演示和科研合作请使用[官网联系页面](https://ccbiomol.com/contact/)或邮件联系：

- zhaoyanbo@ccbiomol.com
- zhangshuai@ccbiomol.com

## Repository Scope

本仓库用于发布 YB_Mol 安装包、版本说明、校验文件和文档入口，**不包含核心产品源码**。软件使用与授权以安装包附带的条款及设备授权为准。欢迎提交可复现的问题报告、文档建议和科研工作流需求；请勿把本仓库的公开可见性误解为核心软件已经按开源许可证发布。
