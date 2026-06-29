# House Log

This file records important decisions, setup history, and operating context.

## 2026-06-29

- The assistant is intended to manage the whole household, not only Home Assistant.
- Home Assistant, MCP servers, and IoT integrations currently run on the home mini PC.
- Codex may be used from different computers and with different models.
- The durable operating memory should live in this repository, not only inside one Codex app installation or chat thread.
- Other computers should act as terminals that open this repository and connect securely to the mini PC.
- Required base documents were created so future Codex sessions can restore the operating context.
- The repository was connected to GitHub at `https://github.com/CrazyFunky/home-assistant.git`.
- The first commit, `064b904 Initialize home operations docs`, was pushed to GitHub on the `main` branch.
- GitHub access should use per-computer local credentials. Codex should not store or receive GitHub Personal Access Tokens.
- For HTTPS Git access, GitHub requires a Personal Access Token instead of the website password.
- On a new computer, install Codex and Git, clone this repository, configure local credentials and MCP access, then ask Codex to read `AGENTS.md` and the supporting house documents.
- Current continuity prompt: `AGENTS.md를 먼저 읽고, HOUSE.md, MCP.md, DEVICES.md, OPERATIONS.md, HOUSE_LOG.md를 읽은 다음 우리집 운영 비서 역할을 이어가.`
