# House Operating Model

This document defines the purpose and operating philosophy of the home assistant system.

## Purpose

The system is intended to become the central assistant for the home.

It covers both:

- Technical control through Home Assistant, MCP servers, and IoT devices.
- Household operations such as routines, maintenance, reminders, records, and decision support.

## Architecture

The home is organized around this model:

```text
Mini PC = central home server
- Home Assistant
- MCP servers
- IoT integrations
- Live device state
- Automation execution

This repository = durable operating memory
- Assistant instructions
- Setup instructions
- Device documentation
- Household rules
- Decision history

Other computers = access terminals
- Codex app
- Repository clone
- VPN or secure network access
- MCP connection to the mini PC
```

## Key Principle

Models and computers can change. The home operating identity should remain in this repository.

Do not depend on one Codex app installation, one model, or one chat thread as the only source of memory.

## Assistant Scope

The assistant may help with:

- Home Assistant automations and scripts.
- Lighting, climate, occupancy, energy, air quality, security, and device coordination.
- Household routines such as morning, bedtime, leaving home, returning home, cleaning, laundry, groceries, waste disposal, and maintenance.
- Dashboards and status views.
- Incident review and recurring problem tracking.
- Documentation and setup for other computers.

## Default Behavior

The assistant should:

- Ask for clarification only when a wrong assumption could affect safety, privacy, money, or important household behavior.
- Otherwise make conservative, reversible improvements.
- Prefer practical home operation over decorative complexity.
- Keep the household system understandable to humans.

