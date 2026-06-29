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
- Current continuity prompt: `AGENTS.md를 먼저 읽고, HOUSE.md, MCP.md, DEVICES.md, OPERATIONS.md, HOUSE_LOG.md를 읽은 다음 우리 집 운영 비서 역할을 이어가.`
- `SETUP_NEW_PC.md` should treat macOS and Windows as full working environments, and smartphones as light access terminals for review, urgent operation, and continuity prompts.
- Removed stale Home Assistant automation entity `automation.decode_base64_sensor_value_2` (`Decode Base64 Sensor Value`) after confirming Node-RED directly receives and transforms the value. The automation config delete API reported the resource was not found, so the stale entity registry entry was removed instead. Automation count changed from 25 to 24.
- Windows Codex setup was completed on this machine: Git for Windows was installed, the repository was cloned from `https://github.com/CrazyFunky/home-assistant.git`, and `main` is tracking `origin/main`.
- Replaced the corrupted Korean continuity prompt in `SETUP_NEW_PC.md` with readable Korean text for future Windows/macOS/smartphone sessions.
- Home Assistant MCP connectivity was verified from this Windows machine. The local project MCP configuration is stored in ignored `.codex/config.toml`, and local environment hints are stored in ignored `.env`.
