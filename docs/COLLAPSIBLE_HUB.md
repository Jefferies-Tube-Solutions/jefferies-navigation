# Collapsible Hub

Put a single room control on a picture-elements floorplan. Tap performs the
primary action. Hold opens the full Hub when other items are visible or opens
the primary's own controls when it stands alone. The Hub automatically enlarges on a phone, tablet or PC, preferring usable space
outside the floorplan image. Tap center to return, or wait 30 seconds without activity.

```yaml
type: custom:navigation-hub
style: {left: 50%, top: 50%}
collapsible: true
items:
  - type: light
    entity: light.room_a
    slot: 0
  - type: light
    entity: light.room_b
    slot: 2
```

Paste this into the containing card's `elements` list and replace synthetic
entities. The card supplies the floorplan image. A [complete picture-elements
example](../examples/collapsible-picture-elements.yaml) is ready to paste.
Existing Hubs without `collapsible` keep their existing defaults and behavior.

## Optional Beam of Origin (beta.9)

The ordinary `collapsible: true` example above keeps its beta.8 behavior, with
no beam. To keep a live room reference when the expanded Hub moves away, opt in:

```yaml
collapsible:
  beam_of_origin: true
```

Optional custom color (the default is `#8bdcff`):

```yaml
collapsible:
  beam_of_origin:
    color: "#8bdcff"
```

The original room cube remains at its floorplan position and collapsed size,
using the shared cube renderer and the same HA state updates for its icon, name,
brightness, borders and gradients. It is a **visual reference, not a second
clickable control**. Only the expanded Jefferies Navigation accepts actions.

A soft, transparent SVG fan fades from that source toward the nearest facing
hex boundaries along the current expanded cluster silhouette. It shares their top-layer popover,
above the backdrop and behind the cubes; Info Cube keeps higher priority. The
beam follows measured navigation and responsive geometry without changing the
approved placement, parent size ceiling or Compass behavior. No extra sizing,
positioning, opacity or animation settings are needed.

Near/overlapping source and destination suppress both the beam and duplicate
source face. Offscreen/hidden or unsupported source geometry is suppressed safely.
Back, outside click, Escape, idle expiry, reconfiguration and removal clean up
the temporary scene and restore the single interactive floorplan cube. Each Hub
has its own gradient and geometry. No real-device behavior is implied by the
synthetic browser tests; owner testing on PAHA02-DEV remains required.

## Automatic behavior

Collapsed size follows the floorplan responsively, with a normal maximum of
82 CSS pixels. Image calibration remains the shared 1536px display reference;
ordinary setups need no reference setting. When image geometry cannot be resolved
(e.g. unsupported stretching/transforms or no image), the safe numeric fallback
is 82px. Explicit `size: auto` and `auto_reference_width` remain supported.

Expansion is enabled on every screen size. Its desired maximum comes from the
original Hub configuration: auto/omitted size has a nominal 82 CSS px ceiling;
explicit numeric `size: N` has ceiling N. A responsive collapsed auto cube can be
55px while expansion grows to 82px. Deliberate numeric sizes above 82 stay valid.
Optional `collapsible.expanded_size` is a lower target, clamped to the parent
ceiling; when omitted it defaults to that ceiling. Root and every nested menu,
including palettes, Radio, Climate, Charger and recursive menus, obey the same
bound. Viewport fitting may reduce actual size. Back restores the exact parent.

| Hub size | expanded_size | Expanded/nested maximum |
| --- | --- | --- |
| omitted / auto | omitted | 82px |
| auto | 82 or 100 | 82px |
| 60 | omitted or 100 | 60px |
| 82 | omitted | 82px |
| 100 | omitted | 100px |
| 100 | 70 | 70px |

It uses a separate browser top-layer overlay to escape clipped/transformed
parents and prevent click-through. Normal floorplan configuration supplies the nominal ceiling;
the currently downscaled collapsed width is not the ceiling.

The Hub measures the displayed image (including supported contain/cover and
object-position), then considers free regions below, above, left and right. It
plans with the complete physical slots 0–18 working envelope plus all actually
visible controls beyond it. This reserves space without allocating extra cubes.
It first prefers a full-size region and centers cube 0 as close to that region's
center as safe bounds allow. New placements may shrink to 85% of expanded_size;
an existing valid free-space placement is retained down to 84%. In the neutral
84–85% band with no prior free-space choice, fallback wins deterministically.
These thresholds are automatic and require no YAML.

On a constrained screen, the full planning envelope may be wider or taller than
its entire safe viewport at the requested expanded size. In that case, with the
standard small-screen behavior enabled, placement checks the **actual visible
controls** at the size already chosen above. If they fit outside the image, the
Hub uses that free canvas instead of covering the image. A fitting region below
the image wins; other regions are ranked by usable area and cube-0 centering.
This changes placement priority without further shrinking cubes. It uses measured
safe viewport/layout geometry, not a new device-width breakpoint or YAML option.
The desktop planning/threshold rules remain intact when the working envelope fits.
Explicit `small_screen: false` and the legacy `mobile` alias keep their meaning.

When free space is too cramped, the Hub stays as close as safely possible to its
original floorplan cube-0 anchor. It uses the largest size up to expanded_size
that fits the safe viewport, reserving center + first ring (0–6) and all actual
visible controls. No active control is dropped or clipped. Measurable fixed/sticky
HA headers, sidebars, visual viewport offsets and safe-area insets are respected.
Unsupported image transforms use this same root-near safe viewport fallback.
Submenus keep their actual footprint (no forced 0–18 envelope) so selected-cube
promotion and exact parent restoration remain unchanged.

Image/viewport resize, scrolling and rotation reevaluate placement. Equivalent
regions remain stable; ordinary HA state updates do not move the group. Closing
restores the original floorplan anchor and current collapsed size.

When opening Light, Sonos, Climate, Charger or a generic child, the selected cube
becomes logical center without moving if the full submenu fits there. Otherwise
it tries the original expanded root center, then a usable image-free or safely
fitted viewport placement. Larger Radio/palette children can fit independently
without resizing their saved parents. Back restores parent sizes, anchors and
slots exactly; after a viewport change, the restored parent is fitted to the new
geometry. Info Cube keeps the caller suspended while open; returning refits it
if the viewport changed. This is shared navigation, with no Sonos/slot-specific rule.

Center is Back at the expanded root. The default keeps the primary's live visual
appearance there; tapping it collapses instead of performing its primary action.
Hold the primary at the expanded root to use its configured hold action, such as
opening the Light controls.
Choose compass center below for direct access to the primary action while expanded.
Nested Back returns to its parent before collapsing. Escape follows the same
navigation. There is no separate rectangular Back button.

Configure exactly one hard item at `slot: 0`. This explicit designation avoids
ambiguity with soft/priority placement. Invisible primary items stay invisible.
Multiple Hubs own separate contexts. Removing/reconfiguring a Hub cleans up its
overlay and listeners. Dashboard editing previews do not execute actions.
Keyboard: Tab to the primary and use Shift+Enter/Shift+Space like a hold. Use Enter/Space on
the root center to collapse. On the expanded primary, Shift+Enter/Shift+Space
runs its hold action. With compass center, hold or Shift+Enter/Shift+Space
reveals the installed version for three seconds without collapse. Keyboard focus
has a visible hexagonal ring. See [shared Compass behavior](NAVIGATION_COMPASS.md).

## Optional settings

| Option | Default | Override |
| --- | --- | --- |
| `size` | `auto` when collapsible | Numeric `size: 82` (or another positive value) fixes collapsed size. Numeric sizes are not auto capped. |
| `collapsible.expanded_center` | `primary` | `compass` moves primary to `primary_slot` and shows compass as Back. |
| `collapsible.primary_slot` | Required for `compass` | Available slot 1–216. Hard collisions including hidden reservations fail; soft/priority use existing allocation. |
| `collapsible.idle_timeout` | `30000` | At least 1000ms. Meaningful user activity resets it; HA updates and resize do not. |
| `collapsible.small_screen` | `true` | Explicit `false` retains the legacy compact-phone opt-out. Desktop enlargement stays enabled. |
| `collapsible.expanded_size` | Parent ceiling | Optional 44–200px requested target. Effective target is min(request, parent ceiling); fitting may shrink further. |
| `size_debug` | `false` | Optional boolean developer diagnostic: show measured CSS-pixel width only during Compass version reveal. |

Fixed collapsed size:

```yaml
size: 82
collapsible: true
```

Compass center with primary at slot 1:

```yaml
collapsible:
  expanded_center: compass
  primary_slot: 1
```

A smaller expanded target (all nested cubes also stay at or below 70px):

```yaml
size: 100
collapsible:
  expanded_size: 70
```

Optional shared Compass measurement, without changing normal minimal YAML:

```yaml
size: 65
size_debug: true
collapsible:
  expanded_center: compass
  primary_slot: 1
```

Add your ordinary primary item in slot 0 and other items as usual. Hold the expanded
Compass (or Shift+Enter) to read the version plus measured cube width. Short tap remains
Back/Collapse. The width is the visible hex rectangle in CSS pixels, not configured
size, container width or device pixels. It updates on reveal and geometry changes,
uses whole pixels or one decimal, and reports `N/A` when not measurable.
No continuous polling or permanent label is introduced. With debug omitted/false,
version-only presentation stays unchanged. [Shared Compass guide](NAVIGATION_COMPASS.md).

Retain the legacy compact presentation on narrow phones (explicit opt-out only):

```yaml
collapsible:
  small_screen: false
```

Migration: replace `collapsible.mobile` with `collapsible.small_screen`. The old
boolean alias still works. Matching old/new values are accepted; contradictory
values are a configuration error. Only an explicit false uses the legacy narrow
phone opt-out (up to 600px); default expansion and desktop fitting use actual
geometry, with no breakpoint eligibility rule. [Compass example](../examples/collapsible-hub-compass.yaml)
and [calibrated auto element](../examples/collapsible-hub-auto.yaml) remain available.

Very large Hubs may need targets smaller than 44px to fit a phone; prefer compact
room Hubs with nested menus. Top-layer expansion requires modern Popover API
support (current Chromium/HA Companion WebViews). Physical Android, real HA,
Safari and Firefox acceptance remain separate from Chromium emulation.
