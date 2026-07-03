# Home Assistant GitOps Plan

This document records what can be synchronized into Git and what access path is needed.

## Current Finding

The current remote Codex access path is:

```text
Codex
-> external DNS
-> Nginx Proxy Manager
-> Home Assistant MCP server
-> Home Assistant APIs
```

This path can inspect and modify many Home Assistant configuration objects through APIs. After registering the HA MCP Tools integration, it can also perform guarded file/YAML operations through the MCP server's allowlisted file tools.

## Currently Reachable Through MCP/API

These can be inspected through the current MCP path:

| Surface | Current status | GitOps note |
| --- | --- | --- |
| Installed add-ons | Reachable | Useful for inventory, not full add-on data export |
| Storage-mode dashboards | Reachable | Can be fetched/edited through dashboard APIs |
| YAML-mode dashboard registration | Partially reachable | Dashboard metadata is visible; allowlisted file tools are needed for the YAML file body |
| Automations | Reachable as HA config objects | Can be exported object-by-object |
| Scripts | Reachable as HA config objects | Can be exported object-by-object |
| Scenes | Reachable; currently none found | Can be exported object-by-object if created |
| Blueprints | Reachable; currently none found | Can be exported if present |
| HACS installed metadata | Reachable | Useful for inventory and reinstall notes |
| Integrations metadata | Reachable | Useful for inventory; do not commit secrets/options |
| Themes | Reachable as theme list; currently none found | Theme YAML files are reachable through allowlisted file/YAML tools |
| Backups | Reachable as backup metadata | Full backup tarballs should not be committed |

Current counts observed:

- Installed add-ons: 12, all running.
- Automations: 24.
- Scripts: 24.
- Scenes: 0.
- Automation blueprints: 0.
- Script blueprints: 0.
- Installed HACS repositories: 13.
- Installed HACS Lovelace cards: 4.
- Themes: 0.

## Home Assistant Backup Feasibility

Home Assistant snapshot backups are reachable through MCP.

Current observed backup state:

- Snapshot backups found: 14.
- Backup cadence appears monthly.
- Most listed backups include Home Assistant configuration and the database.
- Backup sizes are roughly 500-700 MB.
- Restore capability exists through the MCP backup tool, but restore is a recovery operation and restarts Home Assistant.

Backups are useful for:

- Recovery before risky changes.
- Confirming that regular HA backups exist.
- Restoring the whole Home Assistant configuration after a bad change.

Backups are not a good primary GitOps deployment path because:

- The current MCP backup tool can list, create, and restore snapshots, but it does not expose a safe "extract one file" or "upload a modified backup tarball" workflow.
- Restoring a snapshot is broad and disruptive compared with changing one file such as `ui-lovelace.yaml`.
- Backups may include the database, secrets, add-on data, tokens, local keys, and other private material.
- A backup restore can overwrite unrelated runtime changes and may require a Home Assistant restart.

Do not use backup restore as the normal way to update dashboard YAML or configuration YAML. Use backups as the safety net around a GitOps or file-sync workflow.

Preferred pattern:

```text
1. Create or confirm a recent HA backup.
2. Sync/edit safe YAML files through Git, SSH, Samba, or a future file MCP gateway.
3. Run Home Assistant config validation.
4. Reload the affected integration/dashboard when possible.
5. Restart only when required.
6. Use backup restore only if recovery is needed.
```

## Confirmed Installed Add-ons Relevant To GitOps

| Add-on | Slug | Use |
| --- | --- | --- |
| File editor | `core_configurator` | Manual browser-based file editing |
| Samba share | `core_samba` | Internal LAN file access |
| Terminal & SSH | `core_ssh` | Internal LAN shell access |
| Node-RED | `a0d7b954_nodered` | Flow logic and possible data transformation |
| ESPHome Device Builder | `5c53de3b_esphome` | ESPHome YAML management |
| Zigbee2MQTT | `45df7312_zigbee2mqtt` | Zigbee device bridge |
| Nginx Proxy Manager | `a0d7b954_nginxproxymanager` | External DNS reverse proxy |
| Home Assistant MCP Server | `81f33d0f_ha_mcp` | Current Codex remote API path |

Do not read or commit add-on options blindly. Some add-ons can contain tokens, passwords, local keys, or private URLs.

## MCP Filesystem Access

HA MCP Tools is now registered as a Home Assistant integration, so the MCP path has guarded file access.

Currently available file operations include:

- `ha_read_file`
- `ha_list_files`
- `ha_write_file`
- `ha_delete_file`
- `ha_config_set_yaml`

This is not unrestricted shell/Samba access. It is an allowlisted, safety-checked file path intended for controlled edits.

Confirmed reachable or editable through the guarded file path:

| File or directory | Why it matters |
| --- | --- |
| `/config/ui-lovelace.yaml` | Main YAML-mode dashboard body |
| `/config/dashboards/button_card_templates.yaml` | Shared button-card design templates |
| `/config/configuration.yaml` | Core YAML configuration; top-level edits should use `ha_config_set_yaml` so validation and backups run |
| `/config/automations.yaml` | YAML automation file if used |
| `/config/scripts.yaml` | YAML script file if used |
| `/config/scenes.yaml` | YAML scene file if used |
| `/config/include/` | Package files loaded through `homeassistant.packages: !include_dir_named include`, including recorder configuration |
| `/config/dashboards/` | YAML dashboard files and dashboard-specific includes |
| `/config/www/` | Local dashboard assets and custom frontend files |
| `/config/themes/` | Theme YAML files |

Still treat these as cautious/manual review areas:

| File or directory | Why it matters |
| --- | --- |
| `/config/custom_components/` | Custom integrations; usually better tracked by HACS metadata, not committed wholesale |
| `/config/esphome/` | ESPHome device YAML files, if stored there |
| `/addon_configs/` | Add-on data such as Node-RED or Zigbee2MQTT config, depending on HAOS layout |

`secrets.yaml`, tokens, passwords, database files, and private keys must never be committed.

## Recommended GitOps Scope

Start with a conservative GitOps set:

```text
/config/ui-lovelace.yaml
/config/dashboards/
/config/configuration.yaml
/config/automations.yaml
/config/scripts.yaml
/config/scenes.yaml
/config/include/
/config/www/lovelace/
/config/themes/
/config/esphome/
```

Only add `/addon_configs/` after inspecting the actual directory layout and excluding secrets.

## Recommended Exclusions

Never commit:

```text
secrets.yaml
.storage/
home-assistant_v2.db*
*.log
*.key
*.pem
*.crt
*.token
*.db
*.sqlite
deps/
tts/
backups/
```

Be cautious with:

```text
custom_components/
www/
addon_configs/
esphome/
```

These may contain generated files, vendor downloads, or credentials depending on the integration.

## Next Step

Use the guarded MCP file tools for narrow remote edits, especially when Codex needs to update a known YAML file such as `ui-lovelace.yaml` or `configuration.yaml`.

For durable GitOps, still keep Git as the source of history and review:

1. Create or confirm a recent HA backup before risky file changes.
2. Use MCP file tools for small, targeted edits.
3. Mirror safe configuration files into this repository when they should become durable operating memory.
4. Use Git commits as weekly review points unless an immediate commit is explicitly requested.
5. For larger HA config sync, consider an HA-side pull script that runs validation before reload or restart.

The current MCP path is enough for live Home Assistant object management and controlled YAML edits. It should not replace Git history, backups, or cautious review for broad configuration changes.
