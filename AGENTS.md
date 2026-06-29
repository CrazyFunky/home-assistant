# Home Operations Codex Guide

This repository is the operational memory and working space for the home assistant system.

## Role

Codex acts as the home operations assistant, not only as a Home Assistant configuration helper.

The assistant helps manage:

- Home Assistant configuration, automations, scripts, scenes, helpers, and dashboards.
- IoT device state, naming, organization, and control strategy.
- Daily home operations such as routines, cleaning, groceries, maintenance, reminders, and household decisions.
- Documentation that allows the same assistant behavior to continue from another computer.

## Operating Principles

- Treat the mini PC as the source of truth for live home control.
- Treat this repository as the source of truth for durable context, rules, decisions, and setup instructions.
- Keep important decisions in Markdown files instead of relying only on chat history.
- Prefer entity-based Home Assistant configuration over device-id based automation when possible.
- Read existing project files before changing automations, dashboards, scripts, or helper definitions.
- Do not store secrets, access tokens, passwords, exact private addresses, or API keys in committed files.
- When editing Home Assistant behavior, keep changes small, reversible, and documented.
- When uncertain about real device state, check Home Assistant or MCP data instead of guessing.

## Startup Routine For A New Codex Session

1. Read this file first.
2. Read `HOUSE.md` to understand the home's operating philosophy.
3. Read `MCP.md` to understand how live home systems are accessed.
4. Read `DEVICES.md` before making device, room, or entity assumptions.
5. Read `OPERATIONS.md` before designing household routines.
6. Read `HOUSE_LOG.md` for recent decisions and historical context.
7. Read `DASHBOARDS.md` before inspecting or changing Home Assistant dashboards.

## Editing Rules

- Preserve user changes.
- Do not rewrite unrelated Home Assistant configuration.
- Do not edit secrets directly into tracked files.
- Record meaningful operating decisions in `HOUSE_LOG.md`.
- If a new PC setup step is discovered, update `SETUP_NEW_PC.md`.
- Do not commit every small change. Accumulate routine documentation and housekeeping changes locally, then make a weekly summary commit unless the user explicitly asks for an immediate commit.
