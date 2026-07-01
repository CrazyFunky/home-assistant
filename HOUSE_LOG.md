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
- Git workflow preference changed: do not commit every small update. Accumulate routine changes and make one weekly summary commit unless an immediate commit is explicitly requested.
- Updated the old `Home Assistant 장비.xlsx` inventory into a new HA-current workbook at `outputs/ha_device_inventory_2026-06-29/Home Assistant 장비_HA기준_2026-06-29.xlsx`. The update keeps the original A:J column structure, clears sensitive `Local Key` values, and uses the current Home Assistant device registry as the baseline.
- Added Binance USDT price display for BTC, ETH, ONDO, and TRUMP to the `SweetHome` storage dashboard (`lovelace-sweetkitchen`) using `input_number` helpers and a read-only markdown card. The card now also shows Binance 24-hour percentage change for each symbol. This is a dashboard display layer only; automatic market-data refresh still needs a durable updater such as `cryptoinfo_advanced`, REST YAML sensors, or a Node-RED flow.
- Windows Codex setup was completed on this machine: Git for Windows was installed, the repository was cloned from `https://github.com/CrazyFunky/home-assistant.git`, and `main` is tracking `origin/main`.
- Replaced the corrupted Korean continuity prompt in `SETUP_NEW_PC.md` with readable Korean text for future Windows/macOS/smartphone sessions.
- Home Assistant MCP connectivity was verified from this Windows machine. The local project MCP configuration is stored in ignored `.codex/config.toml`, and local environment hints are stored in ignored `.env`.
- Local and remote Home Assistant access profiles were configured for this Windows project. The current PC uses the local LAN profile by default; remote HTTPS HA/MCP URLs are stored only in ignored local configuration files, with the MCP secret path kept out of tracked documentation.

## 2026-06-30

- The macOS repository was reconciled with the GitHub `main` branch after Windows Codex setup. The merge preserves both the Mac dashboard/device-inventory commit and the Windows local/remote access profile documentation.
- Current voice-control architecture: selected Home Assistant devices are exposed to Google Home through Matterbridge, and household members control them by spoken commands through Google speakers. Home Assistant remains the source of truth; Matterbridge and Google Home are the voice-control bridge.
- Home Assistant access model confirmed: inside the home network, Home Assistant is reachable by private IP address; outside the home network, it is reachable by external DNS name. Exact addresses remain local-only and should not be committed.
- Home network topology confirmed: public internet enters through the wired/wireless router; the Home Assistant server, NAS server, and other wired/wireless devices sit behind that router. The Home Assistant server has the Zigbee antenna attached, runs Zigbee2MQTT, and also runs Nginx Proxy Manager so external DNS access is routed to configured internal services.
- Current Codex remote MCP path confirmed: Codex reaches the Home Assistant MCP server through the external DNS name and Nginx Proxy Manager reverse proxy. This path is for MCP/Home Assistant access only and should not be generalized to Samba, SSH, NAS, router admin, or arbitrary LAN services.
- GitOps feasibility check completed. The current MCP path can read HA configuration objects such as storage dashboards, automations, scripts, add-on inventory, HACS metadata, and integration metadata, but it cannot directly list or read the HA `/config` filesystem. A new `GITOPS.md` document records safe candidate files and directories for a future HA configuration sync.
- Home Assistant backup feasibility checked through MCP. Fourteen snapshot backups are currently visible and restore capability exists, but backup restore is broad and disruptive, so it should be treated as a recovery/safety-net mechanism rather than the normal path for updating files such as `ui-lovelace.yaml`.

## 2026-07-01

- Converted the SweetHome Binance display path from direct `input_number.binance_*` dashboard references to `sensor.binance_*` template sensor helpers for BTCUSDT, ETHUSDT, ONDOUSDT, and TRUMPUSDT prices and 24-hour changes. The existing updater path still feeds the original input helpers, while the new sensor helpers expose the values as sensor entities with `state_class: measurement` so Home Assistant can begin tracking them as sensors from this point forward.
- Follow-up needed: the existing Binance input helpers did not show recent recorder history during verification, so the stronger long-term design is to replace the input-helper updater with native Binance REST sensors or another durable sensor-producing integration. REST sensors require YAML configuration and a Home Assistant restart.
- Completed the Binance sensor migration. HA MCP Tools was registered as a Home Assistant integration so safe file/YAML services became available, then `include/rest.yaml` received a `rest:` sensor block that polls Binance 24-hour ticker data for BTCUSDT, ETHUSDT, ONDOUSDT, and TRUMPUSDT every 60 seconds. The temporary template sensor helpers and the older `input_number.binance_*` helpers were removed. `sensor.binance_*` entities now update directly from Binance and keep `state_class: measurement`; recorder history should be rechecked after the next recorder/statistics cycle.
- Recorder configuration is loaded from `include/recorder.yaml` via `homeassistant.packages: !include_dir_named include`. The recorder include list did not originally match the new Binance sensors, so `sensor.binance_*` was added to `recorder.include.entity_globs`. HA MCP Tools extra allowed paths now include `include` so Codex can inspect and update these package files through the guarded file path.
- After moving the Binance REST sensor block out of `configuration.yaml` and into `include/rest.yaml`, Home Assistant was restarted and validated successfully. All eight `sensor.binance_*` entities came back with live values, no Binance-related system log entries were found, and recorder history began returning rows for `sensor.binance_btcusdt_price`.
- The older `cryptoinfo_advanced` Bitcoin sensors were removed from `include/sensors.yaml` after the Binance REST sensors replaced them. The `sensor.cryptoinfo_bitcoin_*` recorder include glob was also removed from `include/recorder.yaml`; a Home Assistant restart is needed for the old YAML sensor entities to disappear from the state machine.
- Home Assistant was restarted after removing the old crypto YAML sensors. The stale `sensor.cryptoinfo_bitcoin_price` and `sensor.cryptoinfo_bitcoin_price_us` registry entries were then removed, and `ui-lovelace.yaml` was updated so the former two-row Bitcoin card now shows four Binance price sensors: BTCUSDT, ETHUSDT, ONDOUSDT, and TRUMPUSDT.
- The default YAML Lovelace dashboard was updated again so the Binance card shows both price and 24-hour percentage change for all four tracked symbols. The card now references eight entities: `sensor.binance_btcusdt_price`, `sensor.binance_btcusdt_24h_change`, `sensor.binance_ethusdt_price`, `sensor.binance_ethusdt_24h_change`, `sensor.binance_ondousdt_price`, `sensor.binance_ondousdt_24h_change`, `sensor.binance_trumpusdt_price`, and `sensor.binance_trumpusdt_24h_change`.
- The default YAML Lovelace Binance card was compacted from eight separate entity rows into one markdown table with one row per symbol. Each row shows symbol, current USDT price, and 24-hour percentage change.
- `lovelace-multiple-entity-row` was installed through HACS and registered as a YAML-mode Lovelace resource in `configuration.yaml`. The default YAML Lovelace Binance card now uses four `custom:multiple-entity-row` rows so each symbol shows current price and 24-hour percentage change on one row.
- The Binance rows in the default YAML Lovelace dashboard were adjusted so the 24-hour percentage change appears before the current price on each row.
