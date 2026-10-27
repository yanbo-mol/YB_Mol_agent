# Security Policy

## Supported Release

YB_MOL Studio is currently distributed as a Windows x64 preview. Security fixes and support apply to the latest published preview release unless a release note states otherwise.

## Reporting a Vulnerability

Please report suspected vulnerabilities privately by email:

- zhaoyanbo@ccbiomol.com
- zhangshuai@ccbiomol.com

Include the affected version, operating system, reproduction steps, observed impact and any relevant logs with secrets and research data removed. Please do not open a public GitHub Issue for an unpatched vulnerability.

Do not send API keys, private keys, unpublished molecular structures, patient data or other sensitive research material. We will acknowledge the report and coordinate follow-up through email.

## Agent and Data Safety

Depending on user configuration, YB_Agent may access local project files, network services, external model providers, command-line programs and remote computing environments. Before using confidential data:

- review the data policies of every configured external service;
- keep credentials outside project files and screenshots;
- inspect proposed commands and file-changing operations;
- verify actual files, structures, logs and exit status instead of relying only on natural-language summaries;
- use an isolated test project when evaluating unfamiliar tools or workflows.

The public preview is not intended for unvalidated clinical, production or safety-critical decision-making.
