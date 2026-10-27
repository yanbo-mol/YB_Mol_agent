# First structure, first edit / 第一个结构与编辑任务

[English home](../README.md) · [中文首页](../README_zh-CN.md)

## 1. Open a test project / 打开测试项目

Install and, if requested, activate the app using the [installation guide](installation.md). Create a project in a writable folder. Keep your first test separate from unpublished research.

按[安装说明](installation.md)安装并完成所需激活，在可写文件夹新建项目，第一次体验使用简单练习结构。

## 2. Inspect a structure manually / 先手动查看结构

For a ready-made file, download [the Co₃O₄ bulk crystal](../examples/materials/files/Co3O4_COD_9005887.cif), import it through the structure file-opening workflow and display the resulting Entry. Rotate and zoom the view, select an atom and inspect the cell. This first inspection does not require an LLM connection.

可以先下载 [Co₃O₄ 体相晶体](../examples/materials/files/Co3O4_COD_9005887.cif)，通过结构文件导入入口打开并显示对应 Entry。旋转、缩放、选择原子并查看晶胞。此步骤不需要配置大模型。

Expected structure: 56 atoms (24 Co + 32 O), cubic cell with a = b = c = 8.0821 Å. The exported file lists all positions explicitly and uses P1 symmetry metadata.

应看到 56 个原子（24 Co + 32 O），晶胞 a = b = c = 8.0821 Å。该导出文件显式列出全部原子位置，使用 P1 对称性元数据。

## 3. Connect YB_Agent / 配置智能体

Use [Settings → Agent Models](model-configuration.md) to select a configured provider and model. Model selection and credentials are shared settings in the current design; this is not a separate API key per project. Running tasks may retain their starting model.

在 [Settings → Agent Models](model-configuration.md) 中配置并选择模型。当前设计采用全局模型设置和连接信息，不需要每个项目单独填一份密钥；正在执行的任务可能继续使用启动时的模型。

## 4. Try a precise edit / 尝试精确编辑

For the [small-molecule example](../examples/molecular-editing/README.md), use the molecular drawing/SMILES input workflow to create anisole from `COc1ccccc1`, display it, then ask:

通过分子绘制或 SMILES 导入入口，以 `COc1ccccc1` 创建并显示苯甲醚，然后向 Agent 输入：

> 保留当前苯甲醚原件，在独立副本中把苯环对位的氢替换为氟。显示新候选，让原件和候选错开放置，并导出 SDF。只做结构编辑。

> Keep the current anisole unchanged. In an independent copy, replace the para hydrogen on the phenyl ring with fluorine. Show the new candidate next to the original and export an SDF. Perform structural editing only.

Inspect the actual candidate and export. The intended connectivity is `COc1ccc(F)cc1` (C₇H₇FO). Ask for a correction or make a manual edit before continuing if the selected site differs.

检查实际候选和导出文件，目标连接关系为 `COc1ccc(F)cc1`（C₇H₇FO）。位点不对时可让 Agent 修改，也可以手动调整后继续。

## 5. Continue from the result / 继续迭代

Keep the original, compare the candidate, select the part you want to change and describe the next operation. Scientific calculations may need additional tools and compute resources; start with a task whose output you can inspect directly.

保留原件、比较候选、选中目标区域并提出下一步操作。科学计算可能需要另外配置工具与计算资源，首次体验建议从能直接检查结果的局部编辑开始。
