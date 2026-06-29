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

## Setup Steps

1. Install Codex.
2. Install Git.
3. Connect to the home VPN or trusted network.
4. Clone this repository.
5. Open the repository in Codex.
6. Configure local secrets and tokens.
7. Configure MCP connections to the mini PC.
8. Confirm Home Assistant is reachable.
9. Ask Codex to read `AGENTS.md`.
10. Ask Codex to summarize current status from `HOUSE_LOG.md`.

## Verification

Confirm:

- `AGENTS.md` is readable.
- `HOUSE.md` is readable.
- The mini PC is reachable.
- Home Assistant is reachable.
- MCP tools are available.
- No secrets were committed into Git.

## Local Files That May Be Needed

These files may exist locally but should not be committed with real secrets:

- `.env`
- `secrets.yaml`
- local Codex config files
- VPN configuration
- SSH keys

## If Something Does Not Work

Check in this order:

1. VPN or network connection.
2. Mini PC power and network status.
3. Home Assistant status.
4. MCP server status.
5. Local token or secret configuration.
6. Codex project configuration.

