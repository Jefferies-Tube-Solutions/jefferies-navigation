# Upgrade to Jefferies Navigation v2

Jefferies Navigation v2 uses its own Home Assistant resource, cards and popup
keys. Update the resource and YAML together. The examples in this branch use v2.

| Honeycomb Menu NG v1 | Jefferies Navigation v2 |
| --- | --- |
| `honeycomb-menu-ng.js` | `jefferies-navigation.js` |
| `custom:honeycomb-persistent-hub` | `custom:navigation-hub` |
| `custom:honeycomb-persistent-control` | `custom:navigation-control` |
| `honeycomb_menu` or `honeycomb_ng_menu` popup key | `jts_n_menu` |
| `honeycomb_nested_menu` | `jts_n_nested_menu` |
| `honeycomb_ng_info` event payload | `jts_n_info` |
| `honeycomb_menu_templates` | `jts_n_menu_templates` |
| `HCJS:` expression prefix | `JTSJS:` |
| `honeycomb:bee` | `jts-n:compass` |
| `expanded_center: bee` | `expanded_center: compass` |
| `honeycomb-bee-flap` | `jts-n-compass-inspect` |
| Other `honeycomb-*` actions | Corresponding `jts-n-*` action |
| `--honeycomb-menu-ng-*` theme variables | `--jts-n-menu-*` |
| Other `--honeycomb-*` variables | Corresponding `--jts-n-*` variable |
| `window.honeycombNG` | `window.jefferiesNavigation` |

For HACS, select the v2 prerelease and check that the JavaScript module resource
is `/hacsfiles/jefferies-navigation/jefferies-navigation.js`. For a manual install,
copy the bundle into `/config/www` and use `/local/jefferies-navigation.js`.
Reload the dashboard after changing resources. On a development Home Assistant
instance, use the [isolated development loader](DEVELOPMENT_BUILDS.md).

For example, a picture-elements card can open the renamed popup using:

```yaml
type: state-icon
entity: light.room_a
tap_action:
  action: fire-dom-event
  jts_n_menu:
    entity: light.room_a
    buttons:
      - icon: mdi:lightbulb
        tap_action:
          action: toggle
```

Keep functional YAML such as slots, module settings, colors, presets, visibility
rules, XY Pad axes, Beam of Origin and responsive sizing. If you use `Info Cube`,
keep its `info` descriptor and use the `jts-n-info` action. The Info Cube opens
from a control and returns to the invoking menu.

Before migrating, delete the existing dashboards and their YAML files.
HACS automatically restores your dashboard layouts from the installed card
bundle after the upgrade. A backup of the dashboards is unnecessary.
