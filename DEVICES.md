# Devices And Areas

This document records the home's physical layout, important devices, and Home Assistant entities.

Keep this file updated as the system grows.

## Areas

Add rooms and areas here.

| Area | Purpose | Notes |
| --- | --- | --- |
| TBD | TBD | TBD |

## Core Systems

| System | Location | Notes |
| --- | --- | --- |
| Wired/wireless router | Network edge | Connects the public internet to the home LAN and Wi-Fi |
| Mini PC | TBD | Runs Home Assistant and MCP services |
| Home Assistant | Mini PC | Main IoT state and automation engine |
| MCP server | Mini PC | Live access layer for Codex |
| Zigbee antenna | Home Assistant server | Provides the physical Zigbee radio path |
| Zigbee2MQTT | Home Assistant server | Bridges Zigbee devices into MQTT/Home Assistant |
| Nginx Proxy Manager | Home Assistant environment | Routes external DNS-based HTTPS access to configured internal services |
| NAS server | Home LAN | Storage/server device connected behind the router |
| Matterbridge | Mini PC / Home Assistant environment | Bridges selected Home Assistant devices into Google Home |
| Google Home | Cloud / Google Home app | Voice-control surface for household members |
| Google speakers | Rooms | Spoken command entry points for Google Home controlled devices |

## Device Inventory

| Device | Area | Home Assistant Entity | Purpose | Notes |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD |

## Naming Rules

- Prefer stable, human-readable entity names.
- Keep area names consistent across Home Assistant, documentation, and dashboards.
- Avoid making automations depend on unclear or temporary names.
- Before renaming entities, check automations, scripts, dashboards, helpers, and documentation that may reference them.

## Device Notes

Use this section for device-specific quirks, battery behavior, calibration notes, or known problems.
