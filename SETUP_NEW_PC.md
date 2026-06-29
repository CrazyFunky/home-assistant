# Setup A New Computer

Use this checklist to continue the same home assistant environment from another computer.

## Goal

After setup, a new computer should be able to:

- Open this repository.
- Understand the home operating rules.
- Connect securely to the mini PC.
- Use MCP/Home Assistant for live state and actions.
- Continue work without depending on the original Mac.

## Prerequisites

- Codex installed.
- Git installed.
- Access to the repository remote.
- Access to the secure home network or VPN.
- Required secrets or tokens available from a password manager or trusted local source.

## GitHub Access

Repository:

```text
https://github.com/CrazyFunky/home-assistant.git
```

Do not give GitHub tokens to Codex and do not commit them to this repository.

Each computer should store its own GitHub credentials locally through the operating system credential manager, Git Credential Manager, or a trusted password manager.

For HTTPS Git access, GitHub account passwords are not accepted. Use a Personal Access Token instead.

Recommended token rule:

- Scope the token only to this repository when possible.
- Grant `Contents: Read and write`.
- Store the token locally on that computer.
- Never paste the token into chat.
- Rotate or revoke the token if a computer is lost or no longer trusted.

## Setup Steps

1. Install Codex.
2. Install Git.
3. Connect to the home VPN or trusted network.
4. Clone this repository:

```bash
git clone https://github.com/CrazyFunky/home-assistant.git
cd home-assistant
```

5. Open the repository in Codex.
6. Configure local secrets and tokens.
7. Configure MCP connections to the mini PC.
8. Confirm Home Assistant is reachable.
9. Ask Codex to read `AGENTS.md`.
10. Ask Codex to summarize current status from `HOUSE_LOG.md`.

## First Prompt For Codex

Use this prompt when opening the repository from a new computer:

```text
AGENTS.md를 먼저 읽고, HOUSE.md, MCP.md, DEVICES.md, OPERATIONS.md, HOUSE_LOG.md를 읽은 다음 우리집 운영 비서 역할을 이어가.
```

If the new session needs to continue from the latest documented context, add:

```text
HOUSE_LOG.md의 마지막 항목을 기준으로 현재 상태를 요약하고 다음에 해야 할 일을 제안해줘.
```

## Verification

Confirm:

- `AGENTS.md` is readable.
- `HOUSE.md` is readable.
- The mini PC is reachable.
- Home Assistant is reachable.
- MCP tools are available.
- No secrets were committed into Git.
- `git pull` works.
- `git push` works after local authentication.

## Local Files That May Be Needed

These files may exist locally but should not be committed with real secrets:

- `.env`
- `secrets.yaml`
- local Codex config files
- VPN configuration
- SSH keys
- GitHub Personal Access Token stored in the local credential manager or password manager

## If Something Does Not Work

Check in this order:

1. VPN or network connection.
2. Mini PC power and network status.
3. Home Assistant status.
4. MCP server status.
5. Local token or secret configuration.
6. Codex project configuration.
