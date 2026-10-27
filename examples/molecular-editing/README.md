# Small-molecule editing / 小分子局部编辑

[All examples / 案例目录](../README.md)

![Actual app view / 实际界面](../../assets/screenshots/molecular-editing.png)

[Watch the actual app demo / 观看实际录像](../../assets/demos/molecular-editing.mp4)

## Input / 输入

Create anisole from SMILES `COc1ccccc1`. / 以 SMILES `COc1ccccc1` 创建苯甲醚。

To ask the Agent to repeat the workflow, install and activate the app as required and [configure an Agent model](../../docs/model-configuration.md). Manual viewing does not need an LLM. / 使用 Agent 重做需完成相应安装激活并配置模型；手动查看不需要大模型。

## Task / 任务

> 以当前原始 anisole 为基线，保留原件，复制新候选并立即 view。用 yb_mol 和原生 Entry 编辑将苯环对位的氢替换为氟，立即显示新 Revision。原件与候选错开放置，导出 SDF。只做结构建模，不做药效预测。

以苯甲醚为基线，把苯环对位的氢替换为氟。展示的是已有小分子的局部编辑，不是药效优化。

## Recorded outcome / 历史记录结果

The recording record reports para-fluoroanisole, `COc1ccc(F)cc1`, C7H7FO, one connected molecule.

SDF 复核得到 COc1ccc(F)cc1，分子式 C7H7FO，只有一个连通分子。

## What to inspect / 检查重点

Keep the baseline, inspect the selected site in 3D, and check the exported atom identities and connectivity. A natural-language completion message alone is insufficient. / 保留基线，查看三维位点，检查导出文件中的原子、残基和连接关系。

Entry 和 SDF 名称字段仍为 anisole，以导出文件名及结构区分候选。画面中的晶胞虚线保留；选择状态有高亮叠影，成片尾段已按 Escape 清除。

## Provenance / 记录说明

From the demonstration package prepared on 2026-10-05. The installed build was not recorded in its manifest. Outcomes above are attributed to that record; this repository update has not rerun the Agent task, and the original exported structure is not bundled here. Screenshots retain their original UI and captions. See [asset notes](../../assets/README.md).

来自 2026-10-05 整理的演示资料，清单未记录当时安装包的构建编号。以上结果注明为该次记录，不表示本次重新执行了 Agent；本仓库未附这次演示的原始结构导出。截图保留当时界面和字幕。
