<p align="right"><a href="README.md">English</a> | <strong>简体中文</strong></p>

# YB_MOL Studio

**与 AI 智能体一起查看、编辑和持续完善分子结构。**

YB_MOL Studio 是面向分子与材料设计的桌面工作平台。用户与 YB_Agent 围绕同一份可编辑分子对象协作：在三维界面中查看结构，通过手动操作或自然语言精确修改，比较候选方案，并连接科学工具继续研究。

**[下载 Windows 预览版](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.656a16e02897/YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe) · [快速上手](docs/quickstart.md) · [查看案例](examples/README.md) · [反馈问题](https://github.com/yanbo-mol/YB_Mol_agent/issues/new/choose)**

[Windows x64 预览版](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.656a16e02897) · [ChemRxiv 预印本](https://doi.org/10.26434/chemrxiv.15010106/v1) · [官网](https://ccbiomol.com/)

[![真实工作界面：保留苯甲醚原件，并检查氟代候选结构](assets/screenshots/molecular-editing.png)](assets/demos/molecular-editing.mp4)

**[观看约 64 秒的实际编辑演示](assets/demos/molecular-editing.mp4)**：保留苯甲醚，在候选副本中将苯环对位的氢替换为氟。录像整理于 2026-10-05，其中执行片段为 8 倍速。[录像说明](assets/README.md)。

## 核心价值

- **结构可以直接编辑。** 从体系、链和残基定位到原子与化学键，在三维界面中检查和修改。适合不以编程为主要工作方式的研究者，也支持专家手动设计与精细调整。
- **用户与 Agent 协作。** 让 YB_Agent 完成局部修改，查看产生的分子对象，再继续手动操作或提出下一步要求。
- **设计可以持续迭代。** 在同一项目中保留基线、创建候选、比较版本，最后导出选定结构。
- **连接科学计算。** 使用已配置的科学工具、模型服务及本地或远程计算环境，在项目中检查输出文件和计算结果。

`yb_mol` 是分子对象核心，YB_Agent 通过平台工具执行操作。实际可用任务取决于安装版本、模型连接和科学计算环境。

## 看实际案例

| 案例 | 可以看到什么 |
| --- | --- |
| [小分子局部编辑](examples/molecular-editing/README.md) | 苯甲醚 → 对氟苯甲醚；原件与候选并排查看，附实际操作录像。 |
| [蛋白局部编辑](examples/protein-editing/README.md) | 1UBQ 的 A 链第 11 位 Lys → Ala，在三维界面中检查侧链变化。 |
| [Co₃O₄ 晶体与表面建模](examples/materials/README.md) | 体相晶体 → (112) 表面超胞 → 甲苯放置，附可下载结构文件。 |
| [RNA 化学修饰](examples/rna-editing/README.md) | 短 RNA 片段腺苷 N6 位添加甲基，说明结构结果及导出限制。 |

这些案例展示结构建模能力，不代表已经验证活性、稳定性或催化性能的提升。录像和晶体文件分别标注日期，不等同于对当前安装包重新完成验收。

## 安装与首次使用

当前公开版本为 **0.1.0 Windows x64 预览版**，`v0.1.0-preview.656a16e02897`，发布于 **2026-10-22**。

1. 从[发布页](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.656a16e02897)[下载安装程序](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.656a16e02897/YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe)。`Source code` 压缩包不是安装程序。
2. 安装并启动；如出现激活界面，按[安装与激活说明](docs/installation.md)操作。
3. 导入结构，先尝试手动查看；使用 YB_Agent 时，在 **Settings → Agent Models** 配置模型服务，再完成[第一个编辑任务](docs/quickstart.md)。

安装包尚未签名。下载安装包、设备授权，以及第三方模型和计算服务费用是不同事项，详见[安装说明](docs/installation.md)与[模型配置](docs/model-configuration.md)。

## 文档、反馈与合作

[快速上手](docs/quickstart.md) · [模型配置](docs/model-configuration.md) · [常见问题](docs/faq.md) · [官网文档](https://ccbiomol.com/docs/)

可复现的问题和功能建议请提交到 [GitHub Issues](https://github.com/yanbo-mol/YB_Mol_agent/issues/new/choose)。激活与科研合作可联系 [zhaoyanbo@ccbiomol.com](mailto:zhaoyanbo@ccbiomol.com) 或 [zhangshuai@ccbiomol.com](mailto:zhangshuai@ccbiomol.com)。安全问题请按 [SECURITY.md](SECURITY.md) 私下反馈。

## 论文与引用

**YB_Mol Studio: an agent-integrated visual editing platform for molecular and materials design**<br />
Yanbo Zhao, Shuai Zhang, Shenggang Li, Zezhong Miao, Haijiao Fu, Miaomiao Wang. ChemRxiv, 2026。[阅读预印本](https://doi.org/10.26434/chemrxiv.15010106/v1)。

论文标题保留发表时的原名；预印本尚未经同行评审。

```bibtex
@article{zhao2026ybmol,
  title   = {YB_Mol Studio: an agent-integrated visual editing platform for molecular and materials design},
  author  = {Zhao, Yanbo and Zhang, Shuai and Li, Shenggang and Miao, Zezhong and Fu, Haijiao and Wang, Miaomiao},
  journal = {ChemRxiv},
  year    = {2026},
  doi     = {10.26434/chemrxiv.15010106/v1}
}
```

## 仓库范围

这里是 **YB_MOL Studio** 的公开下载、文档与反馈仓库，不包含核心应用源码，也不代表核心代码开源。软件使用以适用的产品许可证为准，第三方数据遵循各自条款。欢迎按[贡献说明](CONTRIBUTING.md)完善文档和反馈问题。
