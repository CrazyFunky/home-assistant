# MCP And Live Home Access

This document describes how Codex should access live home systems.

## Source Of Truth

The mini PC is the source of truth for live home control.

Expected services on or near the mini PC:

- Home Assistant
- MCP server or servers for Home Assistant and household tools
- IoT bridges and integrations
- Matterbridge for exposing selected Home Assistant devices to Google Home
- Any supporting services needed for home operations

## Home Network Topology

The current home network is organized as:

```text
Public internet
-> wired/wireless router
-> wired and wireless home devices
   -> Home Assistant server
      -> Zigbee antenna
      -> Zigbee2MQTT server
      -> Nginx Proxy Manager
      -> Matterbridge
      -> MCP access layer
   -> NAS server
   -> other wired/wireless devices
```

The router is the boundary between the public internet and the home LAN. Home Assistant, NAS, and other household devices are connected behind the router by wired or wireless networking.

Home Assistant has the Zigbee antenna attached and runs Zigbee2MQTT. Zigbee devices should be treated as part of the Home Assistant-controlled device layer, even when the physical radio path is through Zigbee2MQTT.

Nginx Proxy Manager is installed in the Home Assistant environment. External DNS-based access reaches Nginx Proxy Manager first, and Nginx Proxy Manager routes the request to the configured internal service.

## Current Remote MCP Access

The current Codex-to-Home-Assistant MCP access path is:

```text
Codex on an external computer
-> external DNS name
-> Nginx Proxy Manager reverse proxy
-> Home Assistant MCP server
-> Home Assistant
```

This is the live remote access model in use today. Treat it as an intentionally exposed HTTPS reverse-proxy path for MCP, not as a general-purpose LAN access method.

Security rules for this path:

- Do not expose Samba, SSH, NAS, router admin, or arbitrary LAN services through this same path.
- Keep the exact DNS name, MCP secret path, bearer tokens, and Home Assistant tokens in local-only ignored files.
- Prefer narrow MCP endpoints and least-privilege Home Assistant tokens where possible.
- If a future VPN or AI gateway is added, document whether it replaces or supplements this NPM reverse-proxy path.

## Voice Control Path

The current voice-control path is:

```text
Home Assistant devices
-> Matterbridge
-> Google Home
-> Google speakers
-> spoken household commands
```

Home Assistant remains the source of truth for device state and automation behavior. Matterbridge is the bridge that makes selected Home Assistant devices available in Google Home so household members can control them by voice through Google speakers.

When troubleshooting voice control, check the path in this order:

1. Confirm the device works directly in Home Assistant.
2. Confirm the device is exposed through Matterbridge.
3. Confirm the device appears correctly in Google Home.
4. Confirm the target Google speaker or voice command path is working.

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

## Access Profiles

Each computer should choose the access profile that matches its network location.

- `local`: Use the private LAN Home Assistant IP address and private LAN MCP endpoint when inside the home network.
- `remote`: Use the external DNS/HTTPS Home Assistant address and remote MCP endpoint when away from the home network.

Home Assistant is currently reachable in two ways:

- Inside the home network: by private IP address.
- Outside the home network: by external DNS name.

Prefer the local IP path when physically at home because it avoids unnecessary external routing. Use the DNS path when away from home or on a network that cannot reach the private LAN address.

The exact URLs, bearer tokens, and MCP secret path belong in ignored local files only:

- `.env` for local environment hints such as `HOME_ASSISTANT_URL`, `HOME_ASSISTANT_LOCAL_URL`, `HOME_ASSISTANT_REMOTE_URL`, `MCP_HOME_SERVER_URL`, `MCP_HOME_LOCAL_SERVER_URL`, and `MCP_HOME_REMOTE_SERVER_URL`.
- `.codex/config.toml` for project-scoped Codex MCP servers.

When configuring remote MCP access, include the required MCP secret path in the ignored local URL. Do not commit that path.

## Open Items

- Document the mini PC hostname or private VPN name.
- Document MCP server names and purposes.
- Document local setup commands once confirmed.
- Document health-check commands once confirmed.
