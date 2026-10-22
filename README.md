<p align="right"><strong>English</strong> | <a href="README_zh-CN.md">简体中文</a></p>

# YB_Mol

**An agent-integrated visual editing platform for molecular and materials design.**

YB_Mol brings molecular visualization and editing, project files, versioned states, domain Skills, and computational tools into one workspace. Researchers and YB_Agent work with the same molecular objects, so structures, tool results, and design changes remain inspectable.

[![Paper](https://img.shields.io/badge/Paper-ChemRxiv-0f766e)](https://doi.org/10.26434/chemrxiv.15010106/v1)
[![Windows](https://img.shields.io/badge/Windows-x64%20Preview-2563eb)](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.656a16e02897)
[![Website](https://img.shields.io/badge/Website-ccbiomol.com-102f31)](https://ccbiomol.com/)

[Download for Windows](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.656a16e02897/YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe) · [Read the Paper](https://doi.org/10.26434/chemrxiv.15010106/v1) · [Documentation](https://ccbiomol.com/docs/) · [Contact Us](https://ccbiomol.com/contact/)

## What YB_Mol provides

| Component | Role |
| --- | --- |
| **YB_Mol Workspace** | Manages projects, molecular structures, files, versions, and computational results with interactive 3D visualization and editing. |
| **YB_Agent** | Interprets research goals, reads project context, and uses configured Skills, models, and tools to assist with research tasks. |

Researchers can work manually or ask YB_Agent for assistance while reviewing the resulting structures, files, tool calls, logs, and conclusions.

## Download and install

The current public build is **YB_Mol 0.1.0 for Windows x64 (Preview)**, build `656a16e02897`, published on October 22, 2026.

1. [Download `YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe`](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.656a16e02897/YB_Mol-0.1.0-win-64-UNSIGNED-656a16e02897.exe).
2. Double-click the downloaded `.exe` and follow the Windows installer.

This preview installer is unsigned, so Windows may display an “Unknown publisher” warning. The automatically generated `Source code.zip` and `Source code.tar.gz` files on the Release page are not installers.

## Core capabilities

- Organize small molecules, proteins, complexes, crystals, surfaces, polymers, and related project files.
- Inspect and edit molecular structures from systems and chains down to residues, atoms, and bonds.
- Preserve baselines and versions, compare candidates, and export results.
- Let YB_Agent use configured models, scripts, scientific tools, and local or remote computing environments.
- Review plans, tool calls, logs, structural changes, and output files in the same project context.

## Typical workflow

```text
Import a structure → inspect and save a baseline
                   → edit manually or ask YB_Agent for assistance
                   → review structures, tool results, logs, and files
                   → compare candidates → export the selected result
```

YB_Mol supports research in protein and antibody design, small-molecule drug design, materials modeling, and polymer structure design. Available capabilities depend on the installed release and the models, tools, and computing environments configured by the user.

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

The manuscript is a preprint and has not undergone peer review.

## Safety and support

YB_Agent may access project files, network services, model providers, external programs, and remote computing environments according to user configuration. Review important structures, files, commands, results, and warnings before using them in research decisions. Do not use the preview as an unvalidated clinical, production, or safety-critical decision system.

- [Documentation](https://ccbiomol.com/docs/)
- [Contact](https://ccbiomol.com/contact/)
- zhaoyanbo@ccbiomol.com
- zhangshuai@ccbiomol.com

Report security issues privately as described in [`SECURITY.md`](SECURITY.md). Reproducible software issues without sensitive information may be reported through GitHub Issues.

## Repository scope

This public repository distributes YB_Mol installers and release information. It does not contain the core product source code, and its public visibility does not make the core software an open-source release.
