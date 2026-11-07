# Jefferies Navigation runtime API v2

The runtime is available at `window.jefferiesNavigation`. It exposes
`apiVersion === 2`, `version` and `commit`. An existing runtime object with a
different API version raises an error before initialization. The original
Honeycomb runtime keeps its own globals, elements, template cache and audio.

| Runtime surface | Identifier |
| --- | --- |
| Dashboard cards | `custom:navigation-hub`, `custom:navigation-control` |
| Menu and menu cell elements | `jts-n-menu`, `jts-n-menu-item` |
| Info Cube and XY Pad elements | `jts-n-info-cube`, `jts-n-xy-pad` |
| Template cache | `window.jefferiesNavigation.templates` |
| Shared audio element ID | `jts-n-audio` |
| Menu close events | `jts-n-closing`, `jts-n-closed` |
| XY events | `jts-n-drag-start`, `jts-n-drag`, `jts-n-drag-interval`, `jts-n-drag-end` |

Theme and persistent-card CSS properties use the `--jts-n-menu-*` and
`--jts-n-persistent-*` prefixes respectively. Menu shadow-root IDs, classes and
animations are scoped to their elements. Home Assistant keeps ownership of its
own APIs and events.

```js
const navigation = window.jefferiesNavigation;
navigation.open({ entity: 'light.room_a', buttons: [] });
navigation.back();
navigation.close();
```

Persistent owners can use `createContext()`, then pass the resulting context to
`openInContext(context, config)`, `updateBase(context, config)`,
`backInContext(context)`, `closeInContext(context)` and
`disposeContext(context)`. A context owns its scene, navigation stack,
gestures, pending actions and Info overlay. Dispose it when its owner detaches.

## Configuration and routing

Templates live under `jts_n_menu_templates` in dashboard YAML. External
`fire-dom-event` popup actions use `ll-custom.detail.jts_n_menu`, or call
`window.jefferiesNavigation.open(config)` directly. Nested actions use their
own menu context. Original Honeycomb popup keys belong to the original
runtime. See [the migration table](V2_MIGRATION.md) for earlier names.

### Read-only Info view

A mounted menu is required. Within a menu, use `action: jts-n-info` with an
`info` payload, or call `openInfoInContext(context, payload, sourceElement)`.
Omit `sourceElement` to use the menu center. External
`ll-custom.detail.jts_n_info` targets the owning menu from the event path or
the current global menu. `openInfo(payload)` targets the current global menu.
The controller owns the Info lifetime, input blocking, exact return and
teardown. See [Info Cube](INFO_CUBE.md) for configuration and examples.

## Verification scope

The original Honeycomb fixture is pinned to commit
`16a2ac09a98c6837cb092603696e97e3a6102b45`, bundle SHA-256
`dc72dfe01fef91eb720c464eae7374c71c3739773c7503492a30f1f0c7c0c35c`.
Chromium tests load original Honeycomb alone, JTS-N alone and both in both
orders on desktop and touch-sized viewports. They check independent popup
routing, namespaces, element registrations, original template-cache identity,
classic actions, XY service dispatch, persistent cards and screenshot evidence.
The broader regression matrix covers Sonos Sleep, Join, Radio and artwork,
Light Hue/Kelvin zoom, 82px geometry, dynamic slots, gestures and idle/sibling
navigation. These browser fixtures use synthetic Home Assistant states.
