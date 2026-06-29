# Dashboard Management

This document records how the home's Home Assistant dashboards are organized and how they should be maintained.

## Current Dashboards

The home currently uses two tablet-oriented dashboard surfaces derived from the same button-card design language.

| Dashboard | URL path | Mode | Purpose |
| --- | --- | --- | --- |
| 개요 | `lovelace` | YAML | Main tablet dashboard backed by `ui-lovelace.yaml` |
| SweetHome | `lovelace-sweetkitchen` | Storage | Smaller tablet dashboard derived from the main dashboard |

Other dashboards may exist, but these two are the primary living-room tablet dashboards.

## Design Relationship

`ui-lovelace.yaml` is the baseline dashboard.

`SweetHome` is a smaller-screen derivative. It keeps the same overall layout and button-card behavior, but scales the card dimensions and typography down for a smaller tablet screen.

Known differences:

| Setting | `ui-lovelace.yaml` | `SweetHome` |
| --- | --- | --- |
| `custom_base_card` height | `100px` | `80px` |
| name font size | `0.8em` | `0.7em` |
| state font size | `0.7em` | `0.6em` |
| main icon width | `2em` | `1.7em` |

## Template Strategy

The dashboards are based on `custom:button-card`.

Important template groups:

- `custom_base_card`: base layout, card height, grid areas, common animation hooks.
- `custom_light_card`: light state, color, background, and icon animation.
- `custom_switch_card`: switch state, optional power-aware display, and icon animation.
- `custom_media_card`: media state, playback display, background image handling.
- `custom_climate_card`: climate state and cooling/fan display.
- `custom_cover_card`: curtain, blind, and cover display.
- `custom_vacuum_card`: robot vacuum state display.
- `custom_floor_card`: floor-plan button state display.
- Display templates for temperature, humidity, power, signal, sliders, and option fields.
- `custom_action`: tap, double-tap, hold, haptic, and button animation behavior.

Because `SweetHome` is storage-mode, it cannot conveniently share YAML `!include` files such as `button_card_templates.yaml`. For now, keep the current dashboard modes and document differences here instead of converting dashboards immediately.

## Maintenance Rules

- Treat `ui-lovelace.yaml` as the source design reference.
- Treat `SweetHome` as a smaller-screen derivative, not an unrelated dashboard.
- Before changing either dashboard, inspect `button_card_templates` first.
- Decide whether a change is:
  - shared behavior that should be reflected in both dashboards, or
  - screen-size-specific behavior that should stay different.
- Do not edit Home Assistant `.storage` files directly.
- Use Home Assistant dashboard APIs/MCP tools for storage-mode dashboards.
- For YAML-mode dashboard changes, edit the dashboard YAML file directly through a managed, validated path.
- Preserve tablet usability: avoid increasing card height, font size, or spacing without checking the target tablet screen.
- Prefer small, reversible dashboard edits.

## Future Improvement Path

The most maintainable long-term structure would be to convert derivative dashboards to YAML-mode and share common files:

```yaml
button_card_templates: !include button_card_templates.yaml
views: !include lovelace/sweethome/views.yaml
```

Then small-screen differences could be handled through explicit override templates, such as:

```yaml
custom_base_card_small:
  template: custom_base_card
  styles:
    card:
      - height: 80px
```

Do not perform this conversion casually. It should be treated as a planned dashboard migration because the current tablet dashboards are already in active use.

