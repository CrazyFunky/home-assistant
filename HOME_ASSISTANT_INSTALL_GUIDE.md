# Home Assistant Server Installation Guide

This document records the baseline choices for preparing a server to run Home Assistant.

Home Assistant is expected to run 24/7, so the host should be stable, low-power, easy to back up, and easy to recover. Prefer a dedicated machine when Home Assistant is the main home-control authority.

## Recommended Direction

For this household, the preferred production path is:

```text
Low-power mini server
-> Home Assistant Operating System
-> wired Ethernet
-> fixed LAN IP or DHCP reservation
-> regular Home Assistant backups
```

Home Assistant Operating System is preferred for the main system because it includes Home Assistant Core, Supervisor, backups, updates, and Apps. Container-based installs are useful, but they require more manual operation and do not include the full Home Assistant OS management layer.

## Option Summary

| Option | Best for | Strengths | Tradeoffs | Household recommendation |
| --- | --- | --- | --- | --- |
| Mini server | Main 24/7 home server | Good performance, SSD storage, low power, HA OS support | Requires dedicated hardware | Best production choice |
| Synology NAS | Reusing an always-on NAS | No extra box, easy storage access | Usually Home Assistant Container, no HA OS Apps/Supervisor, USB device passthrough can be awkward | Good secondary or simple install |
| Raspberry Pi | Low-cost starter system | Small, low power, official HA OS path | SD card wear if not using SSD, less headroom | Good starter or backup lab |

## Common Preparation Checklist

Before installing Home Assistant on any platform:

1. Decide whether this will be the production Home Assistant host or a test system.
2. Prefer wired Ethernet over Wi-Fi.
3. Reserve a fixed IP address in the router.
4. Prepare a stable power source; use a UPS if possible.
5. Decide where backups will be stored.
6. Decide how Zigbee, Bluetooth, Z-Wave, or other USB radios will connect.
7. Record the host, storage, IP address, and recovery notes in this repository.
8. Do not store passwords, tokens, exact private external URLs, or API keys in tracked files.

## 1. Mini Server Installation

Use this when Home Assistant should be the main home automation system.

Recommended hardware:

- Low-power x86-64 mini PC, such as an Intel NUC-class or similar machine.
- 8 GB RAM or more for comfortable long-term operation.
- SSD or NVMe storage; avoid USB flash storage for the main system.
- Wired Ethernet.
- Enough USB ports or a powered USB hub for Zigbee/Z-Wave/Bluetooth adapters.

Recommended installation type:

```text
Home Assistant Operating System on generic x86-64 hardware
```

Why this is the best default:

- Home Assistant OS is the recommended installation type for most users.
- Supervisor and Apps are available.
- Updates, backups, restores, and add-on management are simpler.
- It avoids Docker host maintenance for the main home-control system.
- It gives enough CPU and storage headroom for add-ons such as MQTT, Zigbee2MQTT, Matterbridge, Node-RED, MariaDB, Nginx Proxy Manager, or MCP services.

High-level install flow:

1. Back up anything on the target mini server; installing HA OS will overwrite the target disk.
2. Enable UEFI boot in BIOS.
3. Disable Secure Boot if required by the Home Assistant OS install guide.
4. Write the Home Assistant OS x86-64 image to the internal boot drive.
5. Boot the mini server from the HA OS drive.
6. Connect by browser at `http://homeassistant.local:8123` or `http://<server-ip>:8123`.
7. Complete onboarding.
8. Set a DHCP reservation in the router.
9. Configure backups before adding many integrations.
10. Add Zigbee/MQTT/Matter/voice-control services after the base system is stable.

Operational notes:

- Treat the mini server as the source of truth for live home control.
- Keep the Home Assistant configuration backed up before major changes.
- Prefer entity-based automations and stable names.
- Record important network, device, and backup decisions in this repository.

## 2. Synology Installation

Use this when there is already an always-on Synology NAS and the goal is to avoid another device.

Recommended installation type:

```text
Home Assistant Container through Synology Container Manager
```

Synology is convenient, but it is usually not the cleanest production choice for this household if the setup needs Home Assistant OS Apps, Supervisor-managed add-ons, or easy USB radio access.

Best use cases:

- A simple Home Assistant instance without many add-ons.
- A test or secondary instance.
- A temporary system while preparing a dedicated mini server.
- Environments where the NAS is already always on and power budget matters.

Important limitations:

- Home Assistant Container does not include Supervisor or Home Assistant OS Apps.
- Updates and restarts are managed through Container Manager or Docker workflows.
- Zigbee/Z-Wave/Bluetooth USB passthrough can require extra Synology configuration.
- Host networking and volume mapping must be configured correctly.
- Backups are not as integrated as HA OS snapshots.

High-level install flow:

1. Confirm the Synology model supports Container Manager.
2. Install Container Manager from Package Center.
3. Download the stable `homeassistant/home-assistant` image.
4. Create a persistent config folder, for example:

```text
/volume1/docker/homeassistant/config
```

5. Mount that folder into the container as:

```text
/config
```

6. Set the timezone environment variable, for example:

```text
TZ=Asia/Seoul
```

7. Use host networking so Home Assistant can discover local devices.
8. Enable auto-restart for the container.
9. Start the container.
10. Open `http://<synology-ip>:8123` and complete onboarding.

When Synology is not ideal:

- The setup needs Zigbee2MQTT, Matterbridge, Node-RED, MariaDB, Nginx Proxy Manager, and other add-on-like services managed together.
- USB radios must be reliable and easy to recover after reboot.
- The NAS is heavily used for storage workloads and should not also be the control plane for the home.

## 3. Raspberry Pi Installation

Use this when starting small, reusing existing hardware, or building a low-power test system.

Recommended hardware:

- Raspberry Pi 4 or 5.
- At least 2 GB RAM; more is better for long-term use.
- Official or high-quality power supply.
- Wired Ethernet.
- SSD storage preferred for production use; microSD is acceptable for testing but less ideal for long-term write-heavy systems.
- Case with cooling if the Pi runs warm.

Recommended installation type:

```text
Home Assistant Operating System for Raspberry Pi
```

Best use cases:

- Starter Home Assistant install.
- Small apartment or simple device count.
- Backup/test instance.
- Low-power always-on system where performance needs are modest.

Tradeoffs:

- Less performance headroom than an x86-64 mini server.
- microSD cards can wear out over time.
- USB power and storage quality matter more.
- Multiple USB radios may need careful placement and powered hubs.

High-level install flow:

1. Download or open Raspberry Pi Imager.
2. Choose the Home Assistant OS image for the correct Raspberry Pi model.
3. Write the image to microSD or SSD.
4. Connect Ethernet.
5. Boot the Raspberry Pi.
6. Open `http://homeassistant.local:8123` or `http://<raspberry-pi-ip>:8123`.
7. Complete onboarding.
8. Configure backups before adding integrations.
9. Move to SSD storage if the system becomes production-critical.

## Choosing Between The Three

Use this decision rule:

```text
If this is the real household control system:
  choose a low-power mini server with Home Assistant OS.

If the NAS is already always on and the setup is simple:
  Synology Container can be acceptable.

If this is a starter, test, or low-cost setup:
  Raspberry Pi with Home Assistant OS is acceptable.
```

For this household, the mini server remains the default production recommendation because the current architecture uses multiple services around Home Assistant: Zigbee2MQTT, MQTT, Matterbridge, Node-RED, Nginx Proxy Manager, MariaDB, and MCP access.

## First-Day Baseline Setup

After Home Assistant first boots:

1. Complete onboarding.
2. Set the correct location, timezone, unit system, and language.
3. Create an admin account and store credentials in a password manager.
4. Configure a fixed LAN IP or DHCP reservation.
5. Confirm access from another computer on the LAN.
6. Configure backups.
7. Install only the minimum required integrations first.
8. Add Zigbee/MQTT/Matter services after the base system is stable.
9. Document the host and access model in this repository.
10. Do not expose Home Assistant directly to the internet without a deliberate security design.

## References

- Home Assistant installation overview: https://www.home-assistant.io/installation/
- Generic x86-64 installation: https://www.home-assistant.io/installation/generic-x86-64
- Raspberry Pi installation: https://www.home-assistant.io/installation/raspberrypi
- Alternative systems and Synology Container notes: https://www.home-assistant.io/installation/alternative
