# Release maintenance / 发布维护

The public product name is **YB_MOL Studio**. Keep internal package names, published paper titles and existing installer filenames unchanged when they identify a specific artifact.

## Public contents / 对外内容

This repository contains product documentation, approved screenshots, small demonstration files and feedback forms. Upload installers to Release assets, not Git history. Do not publish application source, private logs, project databases, credentials or licensing tools.

## Before publishing / 发布前

- Choose the exact build and label it Preview, Release Candidate or Stable according to actual acceptance status. Internal builds remain drafts.
- Preserve the original installer bytes and filename. Compute SHA-256 from the exact file; verify it against the source artifact and GitHub asset digest when available. Attach `SHA256SUMS`.
- Include platform, date, build, user-facing changes, activation requirements, signing state and known limitations. Distinguish build checks from clean installation and real GUI validation.
- Check installer download without authentication, documentation links, bilingual README parity, citation version and issue forms.
- Publish only visuals reviewed for private information. State recording date/build when known and label speed changes. Do not imply that old recordings validate a new build.

## After publishing / 发布后

Update both READMEs, installation links and CITATION.cff. Pin downloads to the chosen public tag; `/releases/latest` does not identify preview-only releases reliably. Preserve older releases for traceability. If installer bytes change, create a new release instead of silently replacing the existing package.

Sync the website separately when its deployment is available. A repository documentation change does not itself update the installed app or website.

公开产品名称统一为 **YB_MOL Studio**。发布前核对安装包、校验值、签名与激活状态、真实验收范围、中英文入口、案例隐私及链接；发布后同步仓库版本说明。官网、应用界面与历史安装包是独立发布对象，不要将仓库文档更新描述为全部产品已更新。
