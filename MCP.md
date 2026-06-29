# MCP And Live Home Access

This document describes how Codex should access live home systems.

## Source Of Truth

The mini PC is the source of truth for live home control.

Expected services on or near the mini PC:

- Home Assistant
- MCP server or servers for Home Assistant and household tools
- IoT bridges and integrations
- Any supporting services needed for home operations

## Access Model

Other computers should not become separate home-control authorities.

They should act as terminals:

```text
Codex on another PC
-> opens this repository
-> connects securely to the mini PC
-> uses MCP/Home Assistant for live state and actions
```

## Secure Remote Access

Use a secure private access method for remote connections, such as:

- Tailscale
- ZeroTier
- WireGuard
- Another trusted VPN

Avoid exposing Home Assistant or MCP servers directly to the public internet unless there is a deliberate, reviewed security design.

## Secrets

Do not commit:

- Access tokens
- API keys
- Passwords
- Private tunnel keys
- Exact sensitive addresses

Use local-only files such as:

- `.env`
- `secrets.yaml`
- Codex local configuration
- Operating-system keychain or password manager

Keep examples in tracked files only when they contain placeholders.

## Connection Checklist

When setting up a new computer:

1. Connect to the trusted home network or VPN.
2. Confirm the mini PC is reachable.
3. Confirm Home Assistant is reachable.
4. Confirm MCP server endpoints are reachable.
5. Configure local secrets or tokens.
6. Start Codex from this repository.
7. Ask Codex to read `AGENTS.md`.

## Local Codex MCP Configuration

This repository may use a local project-scoped Codex MCP configuration at `.codex/config.toml`.

That file can contain private Home Assistant MCP endpoint details and must stay local-only. It is ignored by Git and should not be committed.

Local environment hints may also be stored in `.env`, which is also ignored by Git.

## Open Items

- Document the mini PC hostname or private VPN name.
- Document MCP server names and purposes.
- Document local setup commands once confirmed.
- Document health-check commands once confirmed.

