# One shared Jefferies Navigation Compass

The standard Hub Compass and expanded Collapsible Hub Compass use one preset, approved
compass artwork, fill/borders, dimensions, animation and installed-version renderer.
No new YAML is needed. The optional expanded Compass center is:

```yaml
collapsible:
  expanded_center: compass
  primary_slot: 1
```

| Context | Short tap / Enter / Space | Hold / Shift+Enter / Shift+Space |
| --- | --- | --- |
| Standard branded Compass | Reveal installed version | Reveal installed version |
| Expanded root Compass | Back / Collapse | Reveal installed version without collapse |

The label is derived from actual build/release metadata, e.g. **v2.0.0 beta 1**.
It remains readable for three seconds; calibration motion itself lasts 430ms. Repeated
inspection restarts one reveal window. Reduced-motion users retain the label
without motion. Detach cancels timers/frames. A hold never also triggers collapse
or the primary room action. Keyboard users can also use Alt+V on a Compass icon.

Explicit colors, backgrounds, borders and gradients remain supported. Functional
generic controls that happen to use a Compass icon retain their module semantics
and configured actions/styles; Alt+V makes the shared version available without
replacing those actions. A generic fallback icon is not a decorative status-free
Hub logo. Radio, Climate and other module appearances are unchanged.

## Optional rendered-size diagnostics

Top-level Hub `size_debug: true` adds one temporary line during version inspection:

```yaml
size_debug: true
```

Default is false; omitted/false has exactly the ordinary version-only reveal,
resting appearance, animation and gestures. No per-module YAML is needed. The Hub
opt-in follows all Compass instances in its navigation context, including expanded
Compass center and generic Compass icons. The common version formatter and renderer remain
shared. An automatic expanded Compass can show:

```text
v2.0.0
beta 1
82 px
```

The value comes directly from the rendered visible hex SVG bounding rectangle in
CSS pixels. It includes applicable transforms/scale and never substitutes configured
size, expanded_size, menu width or physical device pixels. Values use whole pixels
or one decimal (for example `79.4 px`); missing geometry says `N/A`.
Measurement runs on reveal and resize/ancestor-style events while visible, without
polling; observers/listeners/queued measurement frames are removed on hide/detach.
The accessible live status includes the measured size only in debug mode. Debug
uses compact three-line typography within the hex; standard version-only typography
is unchanged. Version reveal stays temporary for three seconds.

The diagnostic does not change the size policy: auto/omitted Hub maximum is 82px,
numeric size N is authoritative, and expanded_size may only lower that target.
The geometry engine and every child renderer use the same context ceiling.

## Artwork and embedded asset

Replace only `assets/navigation-compass.png`, then run `npm run prepare:brand` and the
normal build. `scripts/generate-compass-asset.js` generates the embedded derivative
`src/brand/compass.generated.js`. Do not hand-edit or duplicate that derivative.
`src/core/compass.js` owns shared preset/tokens, asset reference and version metadata;
`src/cube-element.js` remains the single renderer and gesture/animation owner.
The existing `src/core/version-label.js` remains the only version formatter.

The embedded 192×192 PNG renders the round dial from the approved Draft 02
Blender scene with a transparent background. The Home Assistant cell supplies
the outer hexagonal frame. See [artwork provenance](BRANDING.md).
