<p align="right"><a href="README.md">English</a> | <strong>简体中文</strong></p>

# YB_Mol

**面向分子与材料设计的智能体集成可视化编辑平台。**

YB_Mol 将分子可视化与编辑、项目文件、版本状态、领域 Skills 和计算工具组织在同一个工作区中。研究者与 YB_Agent 围绕同一份分子对象协作，结构、工具结果和设计修改都可以直接检查。

[![论文](https://img.shields.io/badge/Paper-ChemRxiv-0f766e)](https://doi.org/10.26434/chemrxiv.15010106/v1)
[![Windows](https://img.shields.io/badge/Windows-x64%20Preview-2563eb)](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.656a16e02897)
[![官网](https://img.shields.io/badge/Website-ccbiomol.com-102f31)](https://ccbiomol.com/)

[下载 Windows 版](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.656a16e02897/YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe) · [阅读论文](https://doi.org/10.26434/chemrxiv.15010106/v1) · [使用文档](https://ccbiomol.com/docs/) · [联系我们](https://ccbiomol.com/contact/)

## YB_Mol 提供什么

| 组件 | 作用 |
| --- | --- |
| **YB_Mol Workspace** | 管理项目、分子结构、文件、版本和计算结果，并提供交互式三维查看与编辑。 |
| **YB_Agent** | 理解研究目标、读取项目上下文，并使用已配置的 Skills、模型和工具协助科研任务。 |

研究者既可以手动操作，也可以让 YB_Agent 协助，同时检查产生的结构、文件、工具调用、日志与结论。

## 下载与安装

当前公开版本是 **YB_Mol 0.1.0 Windows x64 预览版**，构建 `656a16e02897`，发布于 2026-10-22。

1. [下载 `YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe`](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.656a16e02897/YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe)。
2. 双击下载的 `.exe`，按照 Windows 安装程序完成安装。

该预览版安装包尚未签名，因此 Windows 可能显示“未知发布者”提示。Release 页面自动生成的 `Source code.zip` 和 `Source code.tar.gz` 不是安装程序。

## 核心能力

- 管理小分子、蛋白质、复合物、晶体、表面、聚合物及相关项目文件。
- 从体系和链定位到残基、原子与化学键，查看并编辑分子结构。
- 保存基线和版本、比较候选结果并导出所需结构。
- 让 YB_Agent 使用已配置的模型、脚本、科学工具以及本地或远程计算环境。
- 在同一项目上下文中检查计划、工具调用、日志、结构变化和输出文件。

## 典型工作流

```text
导入结构 → 检查并保存基线
        → 手动编辑或让 YB_Agent 协助
        → 检查结构、工具结果、日志与文件
        → 比较候选结果 → 导出选定结果
```

YB_Mol 可用于蛋白与抗体设计、小分子药物设计、材料建模和聚合物结构设计。实际能力取决于所安装版本以及用户配置的模型、工具和计算环境。

## 论文

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

该文稿为预印本，尚未经过同行评审。

## 安全与支持

YB_Agent 可以根据用户配置访问项目文件、网络服务、模型服务、外部程序和远程计算环境。将结果用于科研决策前，应检查重要结构、文件、命令、结果与警告。请勿将预览版用于未经验证的临床、生产或安全关键决策。

- [使用文档](https://ccbiomol.com/docs/)
- [联系我们](https://ccbiomol.com/contact/)
- zhaoyanbo@ccbiomol.com
- zhangshuai@ccbiomol.com

安全问题请按照 [`SECURITY.md`](SECURITY.md) 私下报告。不包含敏感信息、且可复现的软件问题可以通过 GitHub Issues 反馈。

## 仓库范围

本公开仓库用于发布 YB_Mol 安装包和版本信息，不包含核心产品源码。仓库公开可见不代表核心软件已经作为开源项目发布。
