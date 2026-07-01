# Setup A New Device

Use this checklist to continue the same home assistant environment from another device.

## Goal

After setup, a new device should be able to:

- Open this repository.
- Understand the home operating rules.
- Connect securely to the mini PC.
- Use MCP/Home Assistant for live state and actions.
- Continue work without depending on the original Mac.

The exact setup differs by platform:

- macOS and Windows are full working environments.
- Smartphones are light access terminals for review, urgent edits, Home Assistant control, and continuity prompts.

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

Each device should store its own GitHub credentials locally through the operating system credential manager, Git Credential Manager, or a trusted password manager.

For HTTPS Git access, GitHub account passwords are not accepted. Use a Personal Access Token instead.

Recommended token rule:

- Scope the token only to this repository when possible.
- Grant `Contents: Read and write`.
- Store the token locally on that device.
- Never paste the token into chat.
- Rotate or revoke the token if a device is lost or no longer trusted.

## macOS Setup

1. Install Codex.
2. Install Git. Xcode Command Line Tools or Homebrew Git are both acceptable.
3. Connect to the home VPN or trusted network.
4. Clone this repository:

```bash
git clone https://github.com/CrazyFunky/home-assistant.git
cd home-assistant
```

5. Open the repository in Codex.
6. Configure local secrets and tokens in Keychain, a password manager, `.env`, or other local-only files.
7. Configure MCP connections to the mini PC.
8. Confirm Home Assistant is reachable.
9. Ask Codex to read `AGENTS.md`.
10. Ask Codex to summarize current status from `HOUSE_LOG.md`.

## Windows Setup

1. Install Codex.
2. Install Git for Windows.
3. Make sure Git Credential Manager is enabled during Git installation.
4. Connect to the home VPN or trusted network.
5. Open PowerShell or Windows Terminal.
6. Clone this repository:

```powershell
git clone https://github.com/CrazyFunky/home-assistant.git
cd home-assistant
```

7. Open the repository in Codex.
8. Configure local secrets and tokens in Windows Credential Manager, a password manager, `.env`, or other local-only files.
9. Configure MCP connections to the mini PC.
10. Confirm Home Assistant is reachable.
11. Ask Codex to read `AGENTS.md`.
12. Ask Codex to summarize current status from `HOUSE_LOG.md`.

### Windows Notes

- If Git was installed while Codex or PowerShell was already open, restart the terminal or Codex so the updated `PATH` is loaded.
- If `git` is not found in the current session immediately after installation, Git can usually still be verified at `C:\Program Files\Git\cmd\git.exe`.
- Keep GitHub credentials in Git Credential Manager or Windows Credential Manager. Do not paste tokens into Codex chat or commit them to the repository.
- Use this repository as the durable context store, and use the mini PC for live Home Assistant and MCP state.

## Smartphone Setup

Smartphones should be treated as light access terminals, not the primary working environment for large Home Assistant or repository edits.

Use a smartphone for:

- Reading the repository.
- Checking `HOUSE_LOG.md`.
- Asking for household status or next actions.
- Reviewing or approving small changes.
- Accessing Home Assistant.
- Emergency or away-from-desk operation.

### Android

1. Install the Home Assistant app.
2. Install the VPN app used for home access, such as Tailscale, ZeroTier, or WireGuard.
3. Install GitHub Mobile or use GitHub in a browser.
4. Sign in to GitHub as `CrazyFunky`.
5. Open `https://github.com/CrazyFunky/home-assistant`.
6. Verify that `AGENTS.md`, `SETUP_NEW_PC.md`, and `HOUSE_LOG.md` are readable.
7. If using a mobile Codex or ChatGPT surface that can access the repository, start with the continuity prompt below.

### iOS

1. Install the Home Assistant app.
2. Install the VPN app used for home access, such as Tailscale, ZeroTier, or WireGuard.
3. Install GitHub Mobile or use GitHub in Safari.
4. Sign in to GitHub as `CrazyFunky`.
5. Open `https://github.com/CrazyFunky/home-assistant`.
6. Verify that `AGENTS.md`, `SETUP_NEW_PC.md`, and `HOUSE_LOG.md` are readable.
7. If using a mobile Codex or ChatGPT surface that can access the repository, start with the continuity prompt below.

### Smartphone Limits

- Do not store broad GitHub tokens in plain text notes.
- Prefer read/review on mobile and commit/push from macOS or Windows.
- If a mobile token is needed, make it repository-scoped and revoke it when no longer needed.
- For urgent live control, use the Home Assistant app through VPN rather than editing automation files on the phone.

## First Prompt For Codex

Use this prompt when opening the repository from a new device:

```text
AGENTS.md를 먼저 읽고, HOUSE.md, MCP.md, DEVICES.md, OPERATIONS.md, HOUSE_LOG.md를 읽은 다음 우리 집 운영 비서 역할을 이어가.
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
- Home Assistant is reachable by private IP when inside the home network.
- Home Assistant is reachable by external DNS when outside the home network.
- MCP tools are available.
- No secrets were committed into Git.
- `git pull` works.
- `git push` works after local authentication.

For smartphones, confirm at minimum:

- The Home Assistant app works through the secure network path.
- The GitHub repository is readable.
- `HOUSE_LOG.md` can be checked before asking the assistant to continue context.

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
7. Platform-specific credential manager behavior.
