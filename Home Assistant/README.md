# Home Assistant Live Config Backup

This folder mirrors the safe, file-based parts of the live Home Assistant
configuration from `/config`.

Included:

- Root YAML configuration files such as `configuration.yaml`, `automations.yaml`,
  `scripts.yaml`, `scenes.yaml`, `known_devices.yaml`, and `ui-lovelace.yaml`.
- User-managed include files from `include/`.
- YAML dashboard support files from `dashboards/`.
- Local Lovelace assets from `www/lovelace/`.

Excluded:

- `secrets.yaml`
- `/config/secrets/`
- `.storage/`
- Home Assistant database, logs, backup archives, tokens, certificates, and keys
- Temporary `*.bak_codex_*` files

Treat this as a Git history and review backup, not as a blind restore source.
Before copying these files back to Home Assistant, validate the configuration
and check for local-only changes on the live server.
