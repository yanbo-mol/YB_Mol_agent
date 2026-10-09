<p align="right"><strong>English</strong> | <a href="README_zh-CN.md">简体中文</a></p>

# YB_Mol

**An agent-integrated visual editing platform for molecular and materials design.**

YB_Mol is a research agent platform for molecular and materials design. It brings 3D structure visualization and editing, project files, versioned states, domain Skills, and computational tools into one inspectable workspace, enabling researchers and YB_Agent to work on the same molecular objects.

[![Paper](https://img.shields.io/badge/Paper-ChemRxiv-0f766e)](https://doi.org/10.26434/chemrxiv.15010106/v1)
[![Windows](https://img.shields.io/badge/Windows-x64%20Preview-2563eb)](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.d87497e61870)
[![Website](https://img.shields.io/badge/Website-ccbiomol.com-102f31)](https://ccbiomol.com/)

[Website](https://ccbiomol.com/) · [Download](https://github.com/yanbo-mol/YB_Mol_agent/releases/download/v0.1.0-preview.d87497e61870/YB_Mol-0.1.0-win-64-UNSIGNED-d87497e61870.exe) · [Read the Paper](https://doi.org/10.26434/chemrxiv.15010106/v1) · [Documentation](https://ccbiomol.com/docs/) · [Contact Us](https://ccbiomol.com/contact/)

[![YB_Mol workspace showing a protein structure, project files, and the YB_Agent analysis panel](https://ccbiomol.com/images/products/ccbio-workbench-4o9h.png)](https://ccbiomol.com/images/products/ccbio-workbench-4o9h.png)

> The screenshot is from an earlier build and may still display the legacy names CCBio and CCAgent. The current product name is **YB_Mol**, and the research agent is **YB_Agent**.

## Overview

A general-purpose conversational model can explain a problem. A research agent must additionally operate on real scientific objects, select specialized tools, run computations, and return results that researchers can inspect. YB_Mol supports this process through two connected layers:

| Component | Role |
| --- | --- |
| **YB_Mol Workspace** | Manages projects, structures, files, versions, and computational results while providing molecular visualization and interactive editing. |
| **YB_Agent** | Interprets research goals, plans steps, reads project context, and invokes configured Skills, models, and tools. |

Both layers share the same project context. Researchers can edit structures manually or ask the agent to assist, while retaining responsibility for reviewing key structures, outputs, and conclusions.

## Quick Start

The current public build is **YB_Mol 0.1.0 for Windows x64 (Preview)**, build `d87497e61870`, published on October 5, 2026.

1. Download the installer from the [GitHub Release](https://github.com/yanbo-mol/YB_Mol_agent/releases/tag/v0.1.0-preview.d87497e61870):

   ```text
   YB_Mol-0.1.0-win-64-UNSIGNED-d87497e61870.exe
   ```

2. Verify the installer against `SHA256SUMS` from the same release:

   ```powershell
   Get-FileHash -Algorithm SHA256 "C:\Downloads\YB_Mol-0.1.0-win-64-UNSIGNED-d87497e61870.exe"
   ```

   Expected SHA-256:

   ```text
   5e15d97342f905ba607de1817d41d69893e8f6c8875a045763ab2af0c84e2b2b
   ```

3. Follow the [installation and activation guide](https://ccbiomol.com/manuals/CCBio-Installation-Guide.html).
4. Create a project and import a structure. For a first run, follow the [complete walkthrough](https://ccbiomol.com/manuals/CCBio-Help-Manual.html#walkthrough) from import and editing through validation and export.

The automatically generated `Source code.zip` and `Source code.tar.gz` files are not installers. End users should download the Windows `.exe` file under Release Assets.

## Core Capabilities

- **Unified molecular workspace:** organize structures and project files for small molecules, proteins, complexes, crystals, surfaces, and polymers.
- **3D inspection and precise editing:** navigate from systems, chains, and residues down to atoms and bonds, and inspect the actual result of each modification.
- **Task planning and tool execution:** let YB_Agent read project context and invoke configured models, scripts, and scientific computing tools.
- **Inspectable execution:** retain plans, tool calls, logs, structural changes, output files, and version states.
- **Local and remote computation:** connect configured computing environments, track jobs, and return results to the active project.
- **Versioned design process:** preserve baselines, compare candidates, and restore known states when needed.

## A Typical Workflow

```text
Import a structure → inspect chains, residues, atoms, and bonds → save a baseline
                   → edit manually or describe a task to YB_Agent
                   → inspect tool calls, logs, structures, and output files
                   → compare candidates → export and reload for verification
```

For example, a researcher can import a protein–ligand complex, preserve a wild-type baseline, modify residues or components in a copy, compare the resulting structures, and export candidate designs. When an actual energy evaluation or specialized simulation is required, use an appropriate computational method and inspect its parameters and outputs. Manual placement alone is not evidence of a valid conformation or scientific conclusion.

## Research Areas

- Antibody, protein, and enzyme design
- Small-molecule drug design
- Crystals, surfaces, interfaces, and other condensed-matter systems
- Polymer structure design

These are platform directions, not a claim that the current preview contains complete computational workflows for every area. Available capabilities depend on the installed release and the models, tools, and computing environments configured by the user.

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

This manuscript is a preprint and has not undergone peer review. GitHub also generates citation metadata from [`CITATION.cff`](CITATION.cff).

## Preview Status and Known Limitations

The current installer is an unsigned Windows x64 preview candidate, not a signed production release:

- Windows may display an “Unknown publisher” warning. Verify the source, exact filename, and SHA-256 before installation.
- Interactive installation-cancellation acceptance testing has not been completed.
- Build validation is not equivalent to a complete GUI regression or a real remote SSH login test.
- OpenSSH is an optional system client and is not bundled with the installer.
- Complete GAFF parameterization, Vina, Meeko, and PDBFixer are not included.
- Consult the selected release notes for the exact features, fixes, and limitations of that build.

## Safety and Data Boundaries

Depending on its configuration, YB_Agent may access project files, network services, model providers, external programs, and remote computing environments.

- Do not treat a natural-language response alone as evidence that a task is complete. Inspect the actual structures, versions, files, exit status, logs, and warnings.
- Before processing unpublished or sensitive research data, review the data boundaries of every configured model, database, remote server, and computational tool.
- Retain human review and approval for external program execution, remote operations, and file-changing steps.
- Do not use the preview as an unvalidated clinical, production, or safety-critical decision system.

Report security issues privately as described in [`SECURITY.md`](SECURITY.md). Do not place credentials, license files, unpublished structures, or other sensitive data in a public issue.

## Documentation and Support

- [Documentation center](https://ccbiomol.com/docs/)
- [Installation and activation guide](https://ccbiomol.com/manuals/CCBio-Installation-Guide.html)
- [Molecular modeling and operations manual](https://ccbiomol.com/manuals/CCBio-Help-Manual.html)
- [General user guide](https://ccbiomol.com/manuals/CCBio-User-Guide.html)
- [Offline manuals](https://ccbiomol.com/manuals/CCBio-HTML-Manuals.zip)
- [FAQ and Contact Us](https://ccbiomol.com/#faq)

Reproducible software issues that contain no sensitive information may be reported through GitHub Issues. For device activation, product demonstrations, or research collaborations, use the [contact page](https://ccbiomol.com/contact/) or email:

- zhaoyanbo@ccbiomol.com
- zhangshuai@ccbiomol.com

## Repository Scope

This repository distributes YB_Mol installers, release notes, checksums, and documentation links. It **does not contain the core product source code**. Software use and licensing are governed by the terms bundled with the installer and the device-license agreement. Reproducible bug reports, documentation suggestions, and research workflow requests are welcome, but the public visibility of this repository must not be interpreted as an open-source release of the core software.
