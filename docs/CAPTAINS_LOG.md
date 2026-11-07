# Captain’s Log

Changes are listed newest first by release version. Original notes retain the
terminology and status recorded at the time. A GitHub release link and date
identify the actual publication where a public release exists. Tag-only entries
use the original tagged commit subject. Follow the commit history for individual
implementation changes between releases.

- [All GitHub releases](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases)
- [Stable-branch commit history](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commits/master/)
- [v2 development commit history](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commits/feature/jefferies-navigation-v2/)
- [All tags](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tags)
- [Complete original Honeycomb Menu NG v1 notes](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/blob/25291186b07bfee81b8877fe731e00a417d56c12/RELEASE_NOTES.md)

## Jefferies Navigation v2.0.0-beta.3

- Show one approved Navigation lockup on Deep Space in both GitHub and Marketplace.

## Jefferies Navigation v2.0.0-beta.2

- Home Assistant Marketplace display name is now **JTS - Jefferies Navigation**.
- The README explains how to refresh stale Marketplace repository information.

## Jefferies Navigation v2.0.0-beta.1

- Jefferies Navigation (JTS-N) succeeds Honeycomb Menu NG for Home Assistant.
  The canonical repository is `Jefferies-Tube-Solutions/jefferies-navigation`.
  The resource, public YAML identifiers and runtime use their v2 names. Register
  the `jefferies-navigation.js` module and configure
  `custom:navigation-hub` or `custom:navigation-control`. The
  [v2 configuration guide](V2_MIGRATION.md) maps identifiers for manual
  reconfiguration.
- The approved round Navigation compass sits in the existing hexagonal cell.
  Tap or use the keyboard to inspect the version. On an expanded Hub, short
  tap returns and hold or Shift+Enter inspects the version. Optional
  `size_debug: true` shows the rendered CSS-pixel width.
- Shared rendering, visibility, allocation and device actions carry forward
  from v1.10.0. Controls include Light palettes and presets, Sonos/Media,
  Climate, Charger, Info Cube, collapsible Hubs, Beam of Origin and classic
  popups with XY Pad. XY gestures stop on cancellation and teardown.
- The README uses the approved theme-specific full Navigation lockup. The
  [branding check](BRANDING.md) pins the image bytes and validates the public
  identity, theme variants and YAML card names. The beta publisher keeps the
  approved public wording separate from the checksum and provenance files.

[Public v2 release notice](../RELEASE_NOTES.md).

## v1.10.0 — Stable

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0) · Published 2026-11-03 (UTC).

Promotes the exact owner-real-Home-Assistant-accepted v1.10.0-beta.10 source
`a54cd007fff030d14d89872c4026b92cf0184405`, without runtime or dependency changes.
The approved public beta bundle is 331735 bytes, SHA-256
`b9a89296839e9bab77de41673547053264617985c2adeec325174367502e15b5`.
Only the banner and two canonical build-info version literals change in the JS.

- Generic Climate controls and capability-aware exact-target adjustments.
- Responsive Collapsible Hubs, selected-cube promotion/Back, mobile free canvas
  and configured parent size ceilings throughout nested navigation.
- Optional Beam of Origin: live inert source cube and subtle measured cyan fan;
  default OFF. Optional size_debug retains measured Bee diagnostics.
- Improved Sonos Join artwork, room status/individual volume, shared Bee and all
  existing Light, Sonos, Charger and Info functionality.
- XY Pad safety: repeat actions stop at close/disposal/removal and cancellation;
  silent interrupted on_release gestures, listener cleanup and late-event guards.
- Existing beta.10 YAML remains compatible; no additional settings are required.

Owner beta.10 acceptance and stable authorization are recorded in issue #163.
Audit #154 is complete; its confirmed blocker was fixed in beta.10. Nonblocking
#165–#167 remain deferred. Full exact-source push/PR/master CI, official HACS,
source approval, reproducible packaging and guarded verify-only then publish are
mandatory. No retention setting changes, historical release modifications,
production HA actions, new features or broad refactors enter this promotion.

HACS: select/redownload v1.10.0 stable, turn off beta versions if desired and
refresh frontend/resource caches on all clients. Keep the existing NG module
resource. See [stable verification](V1_10_STABLE_RELEASE.md),
[Collapsible Hubs](COLLAPSIBLE_HUB.md), [Climate](CLIMATE_MODULE.md)
and [XY Pad](CLASSIC_MENU.md). Owner real-HA testing does not establish every
physical thermostat/charger/browser model; automated coverage uses synthetic HA.

---

## v1.10.0-beta.10 — XY Pad Lifecycle Safety

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.10) · Published 2026-11-02 (UTC).

Cumulative from owner-accepted public beta.9 source
`0f2101d9b1b4377168ae7fd5643bf01672a1683b`.

The repository-wide [#154 audit report](https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/164)
confirmed one release blocker: an active XY Pad could keep sending repeated HA
service calls after close/removal and retain document listeners. This candidate
fixes only that lifecycle defect and adds a mandatory browser regression suite.

- Stop repeat timers at close, including animated close, disposal and removal.
- Cancel interrupted gestures on Info, preview, reconfiguration, page background,
  blur and touch/pointer cancellation; cancellation never dispatches `on_release`.
- Remove document/window listeners on disconnect and rebind once on reconnect.
- Reject late XY callbacks for closed/disconnected/suspended scenes.
- Preserve normal mouse/touch service payloads and existing YAML. Preserve beta.9
  Beam of Origin, approved size ceilings, placement, Bee and all modules.

Optional audit cleanups remain deferred in #165–#167. No dependency upgrades,
new features, broad refactors, stable publication or master merge are included.
Install beta.10 with HACS beta versions enabled, refresh the frontend cache and
validate on PAHA02-DEV. Owner real-Home-Assistant acceptance of this changed
runtime is required before v1.10.0 stable under #163. Synthetic QA alone does not
provide that acceptance. Historical releases/tags/assets remain untouched.

## v1.10.0-beta.9 — Beam of Origin

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.9) · Published 2026-11-02 (UTC).

Cumulative with owner-accepted beta.8 (`3ff151adff815d933ddf786169a795ee704f5790`).
Optional `collapsible.beam_of_origin: true` retains a live, inert room cube at
its floorplan anchor and connects it to the expanded controls with a soft,
transparent cyan SVG fan. Optional `color` changes its hue. Measured physical
hex boundaries follow navigation and responsive layout; overlap suppresses the
reference. Collapse and teardown remove temporary resources. No independent HA
subscription or second active control is created. Default OFF preserves beta.8.

Configured parent size ceilings, placement, shared Bee and module navigation
remain intact. Owner testing on PAHA02-DEV is required before any stable promotion.
No master merge, production HA change or architecture review is part of this beta.

## Honeycomb NG v1.10.0-beta.8 — Configured Hub Size Ceiling and Bee Diagnostics

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.8) · Published 2026-11-02 (UTC).

Cumulative from immutable beta.7 `87c192a0a5f16bd880cf93692d5275d1d6130ed2`.

- Original Hub configuration supplies one ceiling: auto/omitted max 82 CSS px,
  explicit numeric size N max N, optional expanded_size only lowers the target.
  Responsive root fitting, every nested module, recursive menu and exact Back
  obey the same limit. No CSS-only post-fit correction; hover cannot exceed it.
- Optional top-level size_debug:true adds measured rendered CSS-pixel width to the
  shared Bee's existing temporary version reveal. Default false remains version
  only. Actual SVG geometry is measured on reveal/live resize/style events, without
  polling. All observers/frames clean up; normal and expanded Bee gestures remain.
- Keep beta.7 placement solver, mobile free lower canvas, desktop origin fallback,
  0–18 planning, thresholds/hysteresis, renderer/artwork/module behavior unchanged.
- Minimal YAML still needs only collapsible:true. Oversized expanded_size safely
  clamps; deliberately numeric sizes above 82 remain supported. See README and
  Collapsible Hub/shared Bee guides for policy table and optional debug examples.

Mandatory synthetic Node/Chromium/module/geometry/HACS/docs/integrity gates and
fresh exact-head CI are required before the authorized guarded beta.8 publication.
No previous release changes, main/master merge, stable or production HA actions.
Owner physical Home Assistant/Android/PC acceptance remains separate. Beam of Origin
#156 is deferred to beta.9; #154 remains separate. Stop for owner testing after release.

## Honeycomb NG v1.10.0-beta.7 — Mobile Placement Fix

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.7) · Published 2026-11-01 (UTC).

Publishes the completed PR #158 mobile correction from exact source
`7dcf7f252aac1930d65ae71cab8477bf4cedf269`, cumulative with immutable beta.6
`6db9e046da496c5d6d437d8d0da08346136ec11f`. Placement code is unchanged from PR #158.

- Constrained-screen expansion checks the actual visible Hub footprint at the
  already selected size. Prefer fitting free canvas below the floorplan, then
  other external regions by usable space and cube-0 centering. No new breakpoint.
- Preserve desktop beta.6 planning/thresholds/origin fallback, collapsed sizing,
  safe bounds, selected-cube submenu promotion, exact Back, timeout and all modules.
- Shared Bee displays `v1.10.0 beta 7` using the existing version formatter.
- No YAML changes. In HACS enable beta versions, select/redownload v1.10.0-beta.7,
  then refresh the frontend/resource cache. Root bundle/checksums/provenance are
  published through the existing guarded beta-release workflow.

No master/main merge, stable or production HA changes. Beta.6 remains immutable.
Chromium tests are synthetic; owner physical Android/desktop and real Home Assistant
acceptance remain pending. Beam of Origin #156 is deferred to beta.8; #154 remains
separate after layout acceptance. Stop for owner testing after release verification.

## Honeycomb NG v1.10.0-beta.6 — comfortable floorplan placement

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.6) · Published 2026-10-31 (UTC).

Cumulative from published beta.5 source `83cbdd486a924f88f2ad399886dff4fb31d913db`.
Issue #148 only; no main/master merge, stable or production Home Assistant changes.

- Plan image-free placement with the shared physical slots 0–18 envelope, unioned
  with all actual visible controls. No phantom cubes or extra YAML.
- Prefer full expanded size in any region above/below/left/right of the displayed
  image. Accept new free-space placement at >=85% size; retain a previous valid
  region down to 84% to avoid resize oscillation. With no prior choice, the neutral
  84–85% band falls back deterministically to the original floorplan anchor.
- Reject cramped strips and use the largest viewport-safe size near original cube
  0, reserving center/inner ring and every actual visible control. Clamp only as
  necessary. Normal collapsed auto max82 and expanded_size remain independent.
- Preserve actual-footprint submenu promotion, exact parent Back, collapse/timeout,
  safe areas, image clipping, shared Bee, Radio/Sonos/Climate and other modules.

Automated synthetic Chromium geometry/screenshots cover both owner scenarios,
100/85/84% boundaries, extended slots, resize and nested Back. Real Home Assistant,
physical Android/PC and owner floorplans still require owner beta.6 acceptance.
Beam of Origin #156 and architecture review #154 are deferred. Stop for owner testing.

## Honeycomb NG v1.10.0-beta.5 — responsive expansion, promotion and shared Bee

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.5) · Published 2026-10-31 (UTC).

Cumulative from exact published beta.4. No stable promotion or master merge.

- Minimal Collapsible Hubs expand comfortably on desktop, tablet and phone.
  The complete visible footprint prefers usable image-free viewport regions;
  safe viewport fallback prevents clipping and excessive shrinking into strips.
- Shared promotion preserves the selected cube's physical position when the child
  fits, then tries expanded root center and safe fitting. Larger children resize
  independently; Back restores parent sizes/anchors. Gesture-origin backdrop
  handling prevents a follow-up click from collapsing a just-fitted submenu.
- One Bee preset/asset/version system: standard tap/hold reveals version; expanded
  root tap is Back, hold/Shift+Enter reveals version for three seconds. Explicit
  styles and functional generic Bee-icon actions remain supported.
- Approved Radio/Climate appearance and services, Light, Charger, Info Cube,
  allocation, keyboard focus and non-collapsible behavior are protected.
- Numeric collapsed sizing and legacy mobile/small_screen overrides remain;
  only explicit false retains the compact-phone opt-out. Default expansion has
  no device-width eligibility rule.

Chromium uses synthetic HA; physical Android/PC acceptance remains separate.
Modern Popover API and existing very-large-Hub limits remain. Issue #154's broad
post-beta.5 review is deferred until owner acceptance. No production HA changes.

## Honeycomb NG v1.10.0-beta.4 — minimal room controls

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.4) · Published 2026-10-31 (UTC).

Cumulative from exact published beta.3. Hubs without collapsible keep their
existing defaults; explicit numeric sizes retain their meaning.

- `collapsible: true` defaults to responsive floorplan sizing, small-screen
  enlargement and 30-second inactivity collapse. Root center is Back; no separate
  Back rectangle. Both primary and bee center policies remain supported.
- Normal `size: auto` cubes cap at 82px. Overlay sizing is independent. New
  `small_screen` setting retains legacy `mobile`; contradictory values fail.
- Join uses trusted Favorites/native Browse station artwork, compact room name
  and individual volume. Playback/full content remain accessible; joined source
  styling, hidden icons and grouping behavior are preserved.
- Climate upper slots request ±1.0°, lower slots ±0.1°, in HA's native temperature
  unit. Unrepresentable deltas and limits disable the action instead of rounding.
- Keyboard focus follows the hex; mouse/touch clear focus paint. No accessibility
  or keyboard navigation removal.

Chromium phone/tablet/desktop tests use synthetic HA states, not physical Android
acceptance. Modern Popover API, ordinary anchored-menu and very-large-Hub limits
remain. No master merge, stable publication or production Home Assistant changes.

## Honeycomb NG v1.10.0-beta.3 — Real-HA stabilization

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.3) · Published 2026-10-30 (UTC).

Focused fixes over exact published beta.2 `8bbc45af72936630c39f87c4697a0148cc38a047`.
No master merge, stable promotion or production Home Assistant changes.

- Climate roles reuse the approved shared `SUBMENU_FILL` token, including alpha;
  default inner width stays zero, outer border and independent center remain.
- Sonos Join keeps room state/own volume on one readable line, station/title on
  another, and a visible joined checkmark. HA room attributes supply transport
  and individual volume; opening-source data supplies only artwork/visual paint.
  Missing/unavailable metadata is not replaced with the opening room's content.
- Collapsible auto-sized Hubs use the shared image-sizing result independently
  of CSS layout width and temporary overlay geometry. Resize during expansion
  preserves the mobile touch size; Back/timeout restores current floorplan size
  and original position. Both center policies remain supported.

Node/browser tests cover the owner-supplied 1200-reference configuration, layout
width overrides, portrait/landscape, Back/timeout, multiple Hubs/editing, shared
Climate pixel reference and P4 at individual 4% alongside a different source.
The supplied complete picture-elements YAML is tested with the exact public demo
image and sanitized entity IDs. Sonos fixtures are synthetic and HA-shaped; the
owner supplied a template rather than its rendered attribute values. Actual
Android DOM/runtime data was not available at implementation time. Automated passes do not
establish owner real-device acceptance. Existing very-large-Hub/ordinary anchored
menu limits and modern Popover API requirement remain.

## Honeycomb NG v1.10.0-beta.2 — Climate, Sonos Join and collapsible Hub

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.2) · Published 2026-10-30 (UTC).

Cumulative over published v1.10.0-beta.1; development PR remains unmerged.
Latest stable remains v1.9.0. No master/stable/production HA changes.

- Climate function cells use neutral dark gray, no default inner border, and
  normal outer borders. Independent center paint and thermostat services remain.
- Sonos Join lists actual room playback and available content. Joined rooms use
  the opening Sonos source's artwork and resolved visual settings, show their own
  volume percentage, and retain accessible membership information. Grouping stays
  authoritative from HA; no optimistic group changes.
- Optional collapsible Hub: primary-only collapsed view; tap for primary action,
  hold to expand; primary/bee center policies; validated slot conflicts; Back,
  Escape and configurable activity timeout; enlarged phone top-layer overlay.
  See [configuration and limits](COLLAPSIBLE_HUB.md).

Validation includes Node contracts, Chromium touch/hold and phone resize/rotation,
Climate controls, Sonos grouping/artwork, existing Light/Charger/Info/navigation,
documentation, HACS packaging and guarded reproducible release checks.
Real HA/hardware acceptance and Firefox/WebKit are not claimed. Very large Hub
populations can require smaller touch targets to fit a phone. Modern Popover API
support is required for the phone top-layer presentation.

## Honeycomb NG v1.10.0-beta.1 — Climate testing

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.10.0-beta.1) · Published 2026-10-27 (UTC).

Cumulative with v1.9.0 stable; preserves Info Cube, Light Color/White and zoom, Sonos native Favorites/Join/Sleep, Charger/Easee, namespace isolation, layout, visibility and navigation.

Adds generic HA Climate to Hub and standalone Control using the existing shared 82px renderer. Displays current/target temperatures and heating/cooling status; respects native units, increments, min/max and explicit Low/High range selection. Menus offer only advertised HVAC, preset, fan and swing capabilities. Native climate services are used only on explicit interaction.

A different-entity nested Climate view retains its own entity and returns to its parent. Defrost uses explicit mapping, native exact preset, or unambiguous verified metadata; no brand/name guessing. Pending, failed and unconfirmed states are distinct; no automatic command retries.

Setup: see docs/CLIMATE_MODULE.md and examples/climate-*.yaml. No HA helpers or backend integration required. Registry access is optional; denial disables automatic separate-switch discovery safely.

Validation results and immutable source/checksum will be recorded in the PR and release publication evidence after the mandatory cumulative suite completes. Real thermostat/HVAC hardware acceptance is pending; synthetic Chromium testing does not establish physical operation. No Firefox/WebKit validation claimed. Humidity, auxiliary heat and vendor-only controls are outside this first beta.

This is an unmerged prerelease for HACS testing, not v1.10.0 stable. Car, Charger redesign, production HA changes and retention cleanup are excluded. Prior releases/tags/assets and stable/master are preserved.

---

## v1.9.0 — Stable

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0) · Published 2026-10-26 (UTC).

Promotes the complete owner-approved cumulative v1.9.0-beta.9 runtime. No module,
style, navigation or configuration logic changed during stable promotion. Only
stable package/banner/runtime version metadata differs in the JavaScript.

- Generic Charger and Easee adapter: truthful two-row labels, individual and
  aggregate power, connected counts, existing controls and charging pulse.
- Shared renderer and persistent Hub: responsive numeric/auto sizing, stable
  placement/visibility, anchored nested menus, neutral submenu defaults and original
  Honeycomb coexistence. Dashboard editing and multi-instance lifecycle protected.
- Light: ON/OFF/unavailable identity, capability-aware Color/White on cube3,
  short/long press, recursive Hue/Kelvin zoom and exact Back behavior.
- Sonos: native Browse Media Favorites, Radio/artwork containment, grouping/Join,
  native device-owned Sleep Timer and existing media controls.
- Info: centered natural-inner-notch geometry; independent center/inner/outer
  paints, source connector, resolved source solid/gradient/alpha snapshots and
  mixed overrides; static/live scalar data, hex-aware wrapping, positioned blocks,
  pagination, exact return and fixed30-second close-all.
- Stable approval manifest pins public beta.9 source/tree/bundle. Promotion guards
  permit only the banner and the two literals in the canonical build-info module;
  all other executable bytes, runtime source, dependencies and build inputs stay
  pinned. Candidate CI additionally requires retention explicitly false.

The owner approved beta.9 after real Home Assistant testing. Automated coverage
includes synthetic desktop/tablet/mobile Chromium and mocked integration/device
boundaries; no claim that every supported hardware/integration was physically
exercised. No Home Assistant installation or charging commands were deployed.

Known limits: Info snapshots refresh on reopen; a gradient source connector uses
its documented first-stop color, not the complete gradient/stop-opacity. Fixed
30s/128blocks/32768characters/64pages and explicit positioned/tiny-panel limits
remain. Keep floorplan anchors visible. Inherited fixed410px Light palette clipping
on390px remains. No Firefox/WebKit/physical-pinch or exhaustive device matrix claim.
Climate, Car and unrelated roadmap features are excluded.

HACS: select v1.9.0 through the normal stable update/download flow, then reload.
Beta users can select v1.9.0 in Redownload. Keep exactly one normal NG resource
and button-card; do not load the optional private DEV loader alongside HACS.

Retention remains explicitly false. Publication preserves prior releases/tags/assets
and Git history; post-publication retention is a dry-run only, never deletion.
See [stable validation and checklist](V1_9_STABLE_RELEASE.md).

---

## Honeycomb NG v1.9.0-beta.9 — source layer paint inheritance

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.9) · Published 2026-10-26 (UTC).

Honeycomb NG v1.9.0-beta.9 — focused Info source-paint hotfix for owner HACS visual testing.

Cumulative from published beta.8. Exact tested source f95e5fbc7273ae06055bb5f106bdd6a3a82a183d, PR #144, branch fix/issue140-info-source-beta9.

Info colors.center / inner_border / outer_border independently accept source, preserving the actual originating rendered solid or local linear/radial SVG gradient, direction/transforms, all stops, alpha and layer opacity as a snapshot at open. Mix source with explicit CSS colors or supported CSS gradients. Neutral fallback for absent/unsupported/cyclic paint; external paint references never fetched. Existing connector remains live; a gradient border uses the explicitly documented first-stop color fallback. No changes to notch geometry, text wrapping/pagination, navigation or fixed 30-second lifetime. Other modules unchanged.

Validation: 400 Node passes / 3 stable-only skips; six focused desktop/tablet/mobile paint browser cases; full mandatory push CI40387739619 and PR CI40387750886 green (including inherited browser/docs/contracts/performance/workflow/package checks). Independent reproducible normal HACS build; 274272 bytes, SHA256 11d9b1911e5889fed5ce43b2cc1a6e148c5594010c009d3962fa4cb58a21c735. Normal JavaScript, not DEV loader. No optional local exhaustive browser campaign.

Known limits: real-HA visual acceptance pending; Chromium only, no real device/HA installation claim. Source paint layers freeze until reopen; connector first-stop fallback does not reproduce a gradient or stop-opacity. Existing Info size/content limits and inherited narrow fixed Light palette clipping remain. No unrelated development.

Owner explicitly authorizes this beta.9 publication only. Prerelease, not latest stable. Preserve all previous releases/tags/assets, stable v1.8.1/master and retention. PR remains unmerged; no production HA changes. Stop after publication/verification. Stable requires separate approval.

Tested branch: `fix/issue140-info-source-beta9`; commit: `f95e5fbc7273ae06055bb5f106bdd6a3a82a183d`.
Bundle SHA-256: `11d9b1911e5889fed5ce43b2cc1a6e148c5594010c009d3962fa4cb58a21c735` (274272 bytes).

This is a beta. An unmerged branch does not require promotion to master. Owner real Home Assistant testing and explicit approval are required before merge or stable publication.

## v1.9.0-beta.8 — unpublished candidate

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.8) · Published 2026-10-26 (UTC).

- Refines published beta.7 Info Cube #140 to match owner reference designs: one
  centered foreground hex bounded by the six natural inner notches, independently
  configurable center fill/inner/outer borders and transparent input shield.
  Existing background cells stay mounted, stationary, visible where uncovered
  and inactive. Shared renderer and numeric sizing/auto pipeline preserved.
- Optional source-facing connector defaults to the actual calling cube’s resolved
  inner-border color; manual color override and disable supported. Physical slots
  0–18 and nested/promoted module centers use actual screen positions.
- Static/live HA titles, text, blocks and optional footer wrap within the hex.
  Content never enlarges the view or shrinks fonts; bounded pagination persists.
  Tiny panels report content limits instead of looping through empty pages.
- Tap/keyboard exact return and fixed 30-second close-all preserved. Responsive
  position/size observation follows host layout without polling and disposes on close.
- Cumulative Light, Sonos, Charger, namespace, navigation and pulse remain intact.
  No Climate/Car/CM feature, production deployment, merge or publication authorized.

See [candidate review](V1_9_BETA8_REVIEW.md), [Info schema](INFO_CUBE.md)
and permanent development handoff for actual validation and limitations.

## v1.9.0-beta.7 — published baseline

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.7) · Published 2026-10-26 (UTC).

Published from `63a9619d27fe503919389f1a51090a2a01193f80`; generic read-only Info
Cube with three authoring modes, safe bindings, hex containment/pagination, exact
caller preservation and fixed 30-second lifetime. Its older left-shifted enclosure
is superseded by the beta.8 owner-approved inner-notch design, without modifying
its immutable tag, source or assets. Optional private Terminal installer remains
separate from the normal HACS bundle.

## v1.9.0-beta.6 — published cumulative baseline

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.6) · Published 2026-10-26 (UTC).

Published from `68bf88fe07aae0892705f2680a82f38c0e78848d`; owner-tested available Light/bee behavior, broader modules automatically tested.

- OFF Light Hub cubes show the configured short name (HA friendly name/entity
  fallback) above OFF. ON presentation, rings, unknown/unavailable distinction,
  cube-3 Color/White and recursive zoom/Back remain intact.
- Bee interaction shows the short derived release version inside its existing
  golden cell, then restores normal appearance. Technical build/commit metadata
  stays in diagnostics. Reduced motion and detached/repeated animation cleanup
  are covered without changing cube geometry.
- Optional development-only fixed resource uses immutable builds and a verified
  one-command atomic installer; no URL/query edits, polling or production cache
  changes. Old files/releases/tags are retained.
- Cumulative beta.5 shared defaults, native Sonos/Radio/Join/Sleep, Charger,
  editor, sizing, gradient/pulse, visibility/allocation and original coexistence
  are preserved. No unfinished Climate/Car/Charger expansion is included.
- The known 410px fixed-size palette can clip in a 390px viewport. Anchors and
  Back are preserved; no automatic shrink/paging or actual-device success claimed.

See docs/BETA6_REVIEW.md and docs/DEVELOPMENT_BUILDS.md for scope, setup and
acceptance gates. Stable/master/retention and production HA remain untouched.

---

## v1.9.0-beta.5 — Palette launcher and shared submenu defaults

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.5) · Published 2026-10-25 (UTC).

Cumulative from public beta.4 `8f9b1c003529b1df0db08058d26691995f3e9afe`.
Review branches remain unmerged. No master/stable or production HA changes.

- Color/White mode indication belongs to **cube 3**, the existing palette launcher.
  Its primary/secondary labels describe the displayed/alternate supported palette;
  tap/hold keep beta.4's live mode selection and bidirectional switching. Slot 0
  retains its original entity, name/brightness, appearance and Back interaction.
- White Ambiance exposes White only. Fixed-white brightness and on/off restrictions,
  reliable off-mode session memory, no-command navigation, capability validation,
  recursive Hue/Kelvin zoom and exact Back history remain intact.
- Ordinary submenu cubes at every depth share the existing Light control neutral
  fill and inner border. The dark outer border is unchanged. Charger details now
  use that gray fill instead of the root Hub's black fill. Explicit center/inner/
  outer/background overrides and meaningful module/active/palette colors remain
  available. Root Hub black/dark base, status colors and promoted centers stay intact.
- Preserve shared 82px geometry, numeric/auto sizing, anchors, visibility/allocation,
  touch/idle/navigation, gradients, energy waves/power speed, Charger measurements/
  safety, Radio artwork/native Favorites/Join/native Sleep and original coexistence.
  No future Climate/Car/Charger redesign or integration is added.

Complete mandatory CI covers unit/contracts, Chromium desktop/mobile and tablet
scenarios, HACS/license/package checks, docs/YAML/links, performance and workflows.
The guarded publisher must verify exact green source/head, metadata, reproducible
committed/rebuilt/CI/staged/downloaded bytes, SHA256/provenance and new immutable tag.
Public release notes/provenance record final SHA, checksum and matching runs.

Known limits: mock HA and Chromium checks are not actual HA/device acceptance;
Firefox/WebKit and real hardware remain untested. Existing small-screen anchored
palette envelope/clipping is preserved. No YAML migration/new keys are needed.
Retain all old releases/tags/assets and the private beta.5 draft; retention stays
unchanged/disabled. Latest stable remains v1.8.1. No stable promotion authorization.

### Owner real-HA acceptance

1. HACS Redownload: enable beta versions, select `v1.9.0-beta.5`, retain the current
   Honeycomb NG resource path and refresh the dashboard/cache. Manual installation:
   use this release's JS and verify `SHA256SUMS.txt` before replacing the resource.
2. On a dual-capability Light, cube 3 indicates Color/White and the alternative.
   Tap follows current device mode; hold switches the supported view without
   sending a command. Slot 0 remains the familiar Light center with Back and
   name/brightness. Test off/null mode, unavailable recovery and groups.
3. White Ambiance: no Color alternative/hold. Test Color and Kelvin recursive zoom,
   Back restoration, and actual swatch application as separate deliberate actions.
4. Root Hub retains its black/dark/status appearance. Charger and generic submenu
   actions are Light-gray inside the dark outer ring at every depth. Check explicit
   fill/border overrides, meaningful active colors, anchored promotion and Back.
5. Smoke-test Sonos Radio artwork/Favorites/Join/Sleep, Light presets, floorplan
   auto sizing/editor, touch/idle close and Charger power/pulse behavior.

Keep #133/#134 and other acceptance issues open until owner verification. Automated
success and public beta publication do not authorize master merge or stable.

---

## v1.9.0-beta.4 — Capability-aware Light and anchored submenus

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.4) · Published 2026-10-24 (UTC).

Cumulative prerelease from published beta.3, through the existing unmerged v1.9.0
candidate. No master merge or stable publication. Climate/Car and later Charger
redesign/guest authorization are excluded.

- Light uses advertised HA `supported_color_modes` to expose Color and/or White.
  For dual-capability lights, tap opens the current `color_mode` palette; hold
  opens the other supported palette. Center labels show displayed/alternative
  palette. UI navigation sends no light commands and manual selection survives
  passive HA updates. Off/null mode can use bounded entity/session memory; safe
  supported fallback otherwise. Fixed-white retains brightness, on/off-only toggle.
- Color and Kelvin selections recheck live capabilities/unavailability. Existing
  swatches, recursive zoom, native Kelvin limits, presets and Back remain intact.
- Shared promotion keeps the clicked cube at its pixel center at deeper levels;
  it becomes logical slot 0. Back restores each prior saved anchor. Existing
  Light expansion and Sonos Radio/Join/Sleep sibling navigation remain intact.
- Charger detail actions use neutral-gray inner borders, with explicit per-item
  overrides respected. Root status colors, selected center, outer borders, pulse,
  controls and current/aggregate measurements remain intact.
- Includes all beta.3 Radio artwork containment, two-row Charger labels,
  dashboard editor ownership, responsive sizing and coexistence fixes. Native
  Sonos Favorites/Join/Sleep, shared 82px geometry, gradients, energy-wave color
  and power speed, visibility/slots and pointer/touch behavior are preserved.

Validation: complete mandatory Build CI and manual beta publisher must pass at the
exact source commit. They validate unit/contracts, full Chromium desktop/mobile
(including Light/Sonos/Charger/editor/Radio), docs/YAML, performance, HACS/license,
workflow lint, reproducible committed/rebuilt/CI/staged bundles, SHA256 and provenance.
Public release notes/provenance identify the exact runs and checksum.

Known limits: synthetic HA tests do not establish real-device acceptance. Firefox,
WebKit and actual hardware are not covered. Large anchored palettes retain the
existing small-screen envelope/clipping behavior; this release does not redesign
protected Light/Sonos geometry. No new configuration keys are required. Retention
stays disabled; previous tags/releases/assets, including the private beta.5 draft,
remain untouched.

### Owner Home Assistant acceptance

1. HACS → Honeycomb Menu NG → Redownload → show beta versions → select
   `v1.9.0-beta.4`. Keep the existing resource path, then refresh dashboard/cache.
   Manual install: use only this release's `honeycomb-menu-ng.js`, verify against
   `SHA256SUMS.txt`, replace the existing local resource and refresh the browser.
2. Dual-capability Light: open while in White, then Color; confirm short tap follows
   mode and hold switches both ways. Check center labels, off/null mode, unavailable
   recovery and groups. Navigation/long press must never change the lamp itself.
3. White-only: no Color alternative. Fixed white: brightness only. On/off: toggle
   only. Test Color and Kelvin recursive hold/Back and an actual chosen swatch.
4. Charger overview at root and inside a real parent menu: promote different cells,
   check no center movement and exact Back restoration; repeat at auto/fixed sizes.
   Detail action inner borders gray; explicit overrides and root status stay correct.
5. Smoke-test Radio artwork/favorites, Join/Back, native Sleep, Light presets,
   touch/idle close, editor positioning, charging measurements/pulse and coexistence.
   Use owner-approved targets for any deliberate device commands.

Keep #133/#134 and relevant hardware-acceptance issues open until owner feedback.
Stable v1.9.0 requires separate explicit owner authorization and a new approved pin.

---

### Additional history from the README

### Anchored child menus (v1.9.0-beta.4)

Opening a promoted child keeps the selected cube at its exact physical position;
it becomes that submenu's slot 0. Back restores the previous anchor and layout.
This also applies to deeper Charger/generic menus and responsive floorplans.
Light palettes/zoom and Sonos Radio/Join/Sleep retain their existing navigation.
In v1.9.0-beta.5, every ordinary submenu depth defaults to the same neutral gray
fill and inner border as Light controls; the dark outer border remains unchanged.
Charger details use that shared gray rather than a black fill. Root Hub base
fill/status styling and meaningful module/center/palette colors are preserved. Explicit
`colors.inner_border` overrides still win; the promoted center keeps its selected
appearance. Root status colors and intentional Light/Sonos colors are preserved.

## v1.9.0 — Stable candidate (not published)

### Historical notes (prior stable proposal remains unpublished)


Prepared from exact public v1.9.0-beta.3 source, with **no functional changes**.
Latest stable remains v1.8.1. These notes and the release-approval manifest are a
proposal for owner review, not evidence of real-HA acceptance or authorization to
merge/publish. See the [stable checklist](V1_9_RELEASE_CANDIDATE.md).

- Generic Charger with explicit HA mappings and optional verified Easee discovery;
  individual and aggregate fresh power, physical connection counts, session energy,
  separate lock semantics, truthful unavailable/stale/partial states and safe pulses.
- Two Charger body rows retain the vehicle/connection or safety state and fixed
  charger name, with measured power beside the icon; no third body row.
- Radio logos of square/wide/tall proportions remain aspect-contained inside the
  six sloping inner-hex boundaries on launcher, promoted center and favorites.
- Dashboard/editor overlays retain their actual card ownership, lifecycle cleanup
  and anchoring. Numeric/automatic sizes, shared 82px geometry, 40% gradients and
  power-sensitive true hex wave are preserved.
- Native-only Sonos Browse Media, Radio/Join/Sleep, Light Hue/Kelvin/presets,
  visibility, placement, classic menus, touch and original Honeycomb coexistence
  retain their beta.3 behavior. No Climate/Car, Charger redesign or guest UI.

Complete synthetic dashboards: [one charger](../examples/charger-easee.yaml),
[two chargers](../examples/charger-multi.yaml), [floorplan elements](../examples/charger-elements.yaml).
External HA automation owns charging policy, scheduling and optional associations;
this candidate does not modify HA, Node-RED or send any production command.

HACS stable users will receive v1.9.0 only after owner approval and verified public
stable publication. Existing beta users can select that stable version at the same
repository/resource path then refresh the dashboard. No old tag, Release or asset
is replaced. Retention remains disabled; no external catalog submission is made.

---

## v1.9.0-beta.3 — Radio artwork containment

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.3) · Published 2026-10-23 (UTC).

Focused cumulative stabilization release from immutable v1.9.0-beta.2. Owner
real-HA acceptance confirmed Charger two-row labels, two-charger metrics/pulse
and dashboard editor positioning in beta.2; these implementations are unchanged.

- Station artwork stays inside the sloping inner hex edges on the launcher,
  promoted Sonos center and Radio favorite cubes. One inset policy, aspect-ratio
  containment, centered unlabeled logos and reserved name/volume text space.
- Regression fixtures include opaque square, wide and tall logos, default/compact
  numeric sizes, larger borders, playing/paused/idle, fallback and live recovery.
  Assertions measure actual contained image pixels against all six polygon edges.
- Native Radio ordering/recognition/Browse Media, Join/Sleep, Light Hue/Kelvin,
  shared 82px geometry, reference autosizing, approved gradients, Charger and
  editor lifecycle behavior remain intact.

Latest stable/master remain v1.8.1. No master merge, stable publication, retention
change, prior tag/release/asset rewrite or real HA/charging command. Issue #125
remains open until owner real-HA artwork acceptance. Climate is a separate
v1.10 development PR, never part of beta.3; Charger Level B and guest UI are deferred.

---

## v1.9.0-beta.2 — Charger labels, artwork padding and editor lifecycle

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.2) · Published 2026-10-23 (UTC).

Cumulative prerelease from immutable v1.9.0-beta.1. Latest stable remains v1.8.1;
PR #124 and this focused fix remain unmerged. No real HA charging commands or
Node-RED changes were performed.

- Individual Charger faces have two readable body rows: vehicle/connection or
  safety/Disabled status, then the fixed charger name. Fresh positive charging
  power appears beside the icon. Aggregate and detail capabilities remain intact.
- Sonos launcher/promoted artwork has additional padding and retains aspect ratio;
  custom Sonos/Media background artwork is contained inside the border.
- Persistent overlays belong to their actual picture-elements/editor container.
  Detached views dispose synchronously, including already-disconnected DOM;
  ancestor layout/scale changes update geometry. Preview interactions send no actions.
- Desktop/mobile regressions cover numeric/auto sizes, artwork shapes, multiple
  hubs, separate previews, transformed cards, repeated view reattachment and cleanup.
- [Element-only example](../examples/charger-elements.yaml) for existing floorplans;
  optional exact Easee registry discovery. Wave reference power is animation
  scaling, never an electrical load limit. Missing optional roles remain truthful.

Issue #126's future forecast menu is not shipped: Brain association and Optimizer
forecast entity contracts must be agreed and implemented externally first. Current
session/current/diagnostic details remain. Native-only Sonos, Light Hue/Kelvin,
navigation, shared 82px geometry, approved gradients and energy-wave behavior persist.
Synthetic validation does not establish real-device acceptance. Owner testing and
explicit approval remain required before any master merge or stable release.

---

## v1.9.0-beta.1 — Generic Charger / Easee

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.9.0-beta.1) · Published 2026-10-22 (UTC).

Prerelease from published v1.8.1, using the existing shared 82px renderer, 40%
gradients, numeric/auto sizing, dynamic placement and six-sided power-sensitive wave.
Latest stable remains v1.8.1; no Charger code is merged into master.

- Generic explicitly mapped `charger` and aggregate `charging-hub`; fresh W/kW
  power, physical connection counts, honest unknown/partial values and deduplication.
- Easee adapter based on verified integration source and exact same-device registry
  keys; explicit fallback, separate physical lock and permanent-lock policy.
- Named launchers, optional read-only vehicle associations, fixed detail slots,
  explicit verified switch controls with pending/failed/unconfirmed feedback.
- No charging command from navigation/render/reconnect; no retries, optimizer,
  scheduling, vehicle inference, Node-RED edits or Car/Climate implementation.
- Shared optional third text row and module-supplied health/dependency snapshot;
  one-shot expiry correctly arms when a cube connects. Existing modules retained.
- [Complete single-Easee dashboard](../examples/charger-easee.yaml),
  [complete multi-charger dashboard](../examples/charger-multi.yaml),
  [installation, entity checklist, capability sources and supervised hardware tests](CHARGER_MODULE.md).
- [HACS catalog submission package](HACS_CATALOG_SUBMISSION.md) remains
  prepared for owner review only; Charger is not advertised as stable.

Synthetic unit/browser tests are not real-device acceptance. Verify installed
Easee entity IDs/units, permission/lock semantics, fresh reporting and external
association feed at hardware. The optional feed may be absent. HA acknowledgement
is not independent hardware confirmation; a timeout may still have reached a device.
Owner real-HA testing and explicit approval are required before stable publication.

---

## v1.8.1 — Stable

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.1) · Published 2026-10-22 (UTC).

Version-only maintenance release for HACS catalog readiness after successful
official validation. Preserves the owner-approved v1.8.0 runtime without changes
to application logic, styles, dependencies, APIs or configuration behavior.

The matching v1.8.1-beta.1 supplies the immutable public source required by the
unchanged stable publisher. The stable bundle differs from that beta, and from
v1.8.0, only in its deterministic version banner. No Home Assistant configuration
migration is required. HACS package identity, root JavaScript filename, GPL
license and original-project attribution remain unchanged.

Stable publication and master integration require separate owner approval.
The external HACS catalog submission remains an owner-reviewed follow-up under
Issue #92; this maintenance release does not imply catalog acceptance.

---

## Honeycomb NG v1.8.1-beta.1 — HACS readiness maintenance

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.1-beta.1) · Published 2026-10-22 (UTC).

Version-only maintenance beta for Issue #92, based on published v1.8.0 stable. No application logic, styles, dependencies, APIs or configuration behavior changes. Only package/release version metadata and the deterministic JavaScript banner change.

The bundle body is byte-identical to published v1.8.0 after removing only the expected version banner. Two local production builds are identical. Local core contracts and unit tests pass (319 passed, 3 stable-only checks skipped for prerelease metadata); HACS packaging, full GPL/NOTICE attribution and artifact validation pass. Mandatory exact-source Build CI, desktop/mobile/browser/coexistence, documentation/YAML, lifecycle/performance and workflow lint must all pass before this guarded publisher runs.

This beta supplies the matching immutable public prerelease required by the existing stable approval guard. It does not authorize a master merge or stable publication. A separate stable integration PR will be presented for owner approval. No new real Home Assistant feature-testing campaign was performed for this version-only artifact; existing owner-approved v1.8.0 behavior is preserved.

Mandatory CI: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/39841902606
Official HACS validation on unchanged master: https://github.com/NicolaiTandrup/honeycomb-menu-ng/actions/runs/39837224467

HACS test installation: use the existing Dashboard custom repository NicolaiTandrup/honeycomb-menu-ng, enable prereleases, choose v1.8.1-beta.1, download and reload Home Assistant frontend resources. The resource remains /hacsfiles/honeycomb-menu-ng/honeycomb-menu-ng.js. Stable users remain on v1.8.0 unless they explicitly select the beta. No beta.1 functional differences are expected.

Tested branch: `release/v1.8.1-beta.1`; commit: `fe39cf04995d62e9a978d70eb4eae026b8221632`.
Bundle SHA-256: `98d605a1be6d770b59c7b98b07c0bf87217744d9f027cc849ee9af5ceed878d7` (218407 bytes).

This is a beta. An unmerged branch does not require promotion to master. Owner real Home Assistant testing and explicit approval are required before merge or stable publication.

## v1.8.0 — Stable

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.0) · Published 2026-10-22 (UTC).

Promotes the complete owner-tested cumulative v1.8.0-beta.7 functionality.
Runtime source, dependencies, HACS identity and executable bundle body are
unchanged; only the deterministic version banner changes in the JavaScript.

- NG-owned runtime namespace and API, with original Honeycomb coexistence in
  either load order. Persistent Hub/Control names and module resource stay the same.
- One shared 82px renderer with Light as the visual reference, 40% active fill
  depth, decorative logo gradient, independent borders and solid inactive fills.
- Native-only Sonos Browse Media favorite metadata/artwork, verified station
  recognition and live launcher/promoted-center updates. Radio ordering/playback,
  Join/grouping, native no-helper Sleep Timer and sibling navigation are retained.
- Floorplan `size: auto` using actual rendered image bounds and a stable display
  reference; optional `auto_reference_width` defaults to1536 CSS pixels. Fixed
  numeric sizes and omitted82 remain fixed; no duplicate sizing engine.
- Genuine six-sided outward energy contour with optional fixed/power-proportional
  speed, smooth phase-preserving updates, resolved inner-border color by default
  and optional `energy_wave.color`. Explicit health/power, reduced-motion,
  visibility, lifecycle and bounded animation budgets remain mandatory.
- Light brightness, recursive Hue/Kelvin zoom, presets, generic Media, dynamic
  visibility/placement, nested Back/idle, drag-select, classic menus and touch
  behavior are preserved. Charger, Climate and Car modules remain future work.

The sole owner/user already uses the1.8 track and reports successful real-HA
beta.7 acceptance. [Candidate audit/checklist](V1_8_RELEASE_CANDIDATE.md),
[runtime API](NG_RUNTIME.md), [native Sonos](SONOS_NATIVE_FAVORITES.md),
[sizing](FLOORPLAN_SIZING.md), [pulse configuration](ENERGY_WAVE.md).

HACS custom repository and root `honeycomb-menu-ng.js` asset are unchanged.
After verified publication, redownload stable and hard-refresh all clients;
beta users may disable Show beta versions. Keep one NG module resource. Official
HACS catalog admission remains separate. Existing image-frame/fallback/touch-size,
browser color support, power normalization and native Sonos/Sleep limits remain.
All previous releases/assets/tags/history and retention settings are preserved.

---

### Additional history from the README

Candidate reference: [v1.8 runtime namespace and mixed-install routing](NG_RUNTIME.md).
Stable v1.7.1 remains published and unchanged until separate owner approval.

The v1.8.0 candidate includes [40% active depth and decorative logo gradients](CUBE_PRESENTATION.md), [image-aligned `size: auto`](FLOORPLAN_SIZING.md), and an opt-in [six-sided energy pulse](ENERGY_WAVE.md). Inactive physical cubes remain solid. Numeric sizes and non-collapsible omitted fixed-82 defaults stay unchanged.

## v1.8.0-beta.7 — resolved energy-wave contour color

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.0-beta.7) · Published 2026-10-22 (UTC).

Approved functional source: PR #120 commit
`ad057f7133871826cab631b7a0f5e78fdb63dc2a`, directly on immutable published
beta.6. Release preparation changes version metadata, documentation and the
generated version banner only; every source and test file is unchanged.

- Omitted `energy_wave.color` inherits the final resolved inner-border color,
  including live Light/Sonos status/station colors and user border overrides.
- Optional color overrides use safe CSS color syntax and the existing frontend
  HA JS template evaluator. Invalid literals reject in-browser; missing,
  invalid or throwing template results suppress only the contour until valid.
- Same renderer/model, SVG contour and alpha/opacity. No geometry, timing,
  phase, scheduler, visibility/reduced-motion/health or performance-budget change.
- Complete cumulative beta.6 functionality remains: owner-approved 40%/logo
  gradients, display-reference auto sizing and fixed numeric sizes, power/fixed
  speed, native-only Sonos, Light zoom/presets, all navigation and coexistence.

[Complete no-hardware green/blue example](../examples/energy-wave-color.yaml),
[color contract](ENERGY_WAVE.md#contour-color--v180-beta7),
[sizing guide](FLOORPLAN_SIZING.md). Full exact-release-head CI,
reproducible HACS bundle/checksums and the normal manually authorized publisher
must pass. This is a prerelease from an unmerged PR; installed HA and other
browser engines remain owner acceptance. Existing image-frame/touch-size and
Sonos/Sleep limits remain. No future Charger/Climate/Car modules, master merge,
stable promotion, retention changes or old release/tag/asset edits/deletions.

### Additional history from the README

### v1.8.0-beta.7: energy-wave contour color (#119)

The scoped beta.6 follow-up makes the pulse inherit the cube's resolved inner
border, including live Light/Sonos colors and user overrides. Optional
`energy_wave.color: '#00bfff'` changes only the contour. Existing gradients,
six-sided geometry, power/fixed speed and sizing stay unchanged. Try the
[complete synthetic green/blue demo](../examples/energy-wave-color.yaml) and read
the [color and template rules](ENERGY_WAVE.md#contour-color--v180-beta7).
This setting starts in beta.7; published beta.6 remains immutable.

## v1.8.0-beta.6 — stable display baseline and power-responsive pulse

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.0-beta.6) · Published 2026-10-22 (UTC).

Cumulative on exact published beta.5 `ece8f9e5af7e92b1629cfe164cf000028b0b1068`.
The accepted40% gradient, logo gradient, all existing modules/actions, native-only
Sonos, numeric sizing, navigation and original coexistence are retained.

- `size: auto` now uses rendered image width / stable **display reference**,
  default1536 CSS pixels. Optional positive `auto_reference_width: 1500` makes
  1500px →82px,750px →41px regardless of bitmap1500/3000/6000px. This corrects
  beta.5's tiny baseline; never infer the reference separately on each client.
- Existing energy_wave defaults to fixed3000ms. Explicit power mode requires a
  per-cube max_power_w, with default900–2200ms bounds; fixed cycle_ms is supported.
  Effective cycles500–10000ms, safe validation and runtime static fallback.
- Hex contour/keyframes unchanged. One shared350ms playback-rate transition
  preserves animation phase/node identity; no per-cube timer, polling or DOM
  rebuild per power update. All health/visibility/reduced-motion gates and
  24-visible-motion budget remain. No Charger adapter or HA commands.

[Copy/paste sizing and migration](FLOORPLAN_SIZING.md),
[rate mapping and sensor prerequisites](ENERGY_WAVE.md),
[no-hardware power demo](../examples/energy-wave-power.yaml). The19400W aggregate
reference is illustrative theoretical3×28A/400V capacity, not actual measured
power or a limit for all users. Individual references remain independent.

Full exact-head CI and manually authorized publisher must pass before an unused
immutable prerelease tag. #115/#117 remain open for owner real-HA verification.
Known static-image DOM/fallback/touch-size and native Sonos/Sleep limits remain;
HACS catalog and stable SemVer/migration review are separate owner gates.
No master/stable/retention change or prior release/tag/asset overwrite/deletion.

### Additional history from the README

### Floorplan sizing in v1.8.0-beta.6

For a persistent Hub or Control inside `picture-elements`, opt in with
`size: auto`. A floorplan displayed at 50% of its reference design width gets
41px cubes; 75% gets61.5px. Reference defaults to1536 CSS pixels; set
`auto_reference_width` to your intended normal display width. Existing numeric sizes stay fixed. No detectable image
means a harmless 82px fallback. See [complete copy/paste YAML, coordinate-frame
support and touch-size limits](FLOORPLAN_SIZING.md).

The [synthetic charging-pulse demo](../examples/energy-wave.yaml) uses the shared
renderer without a charger or service call. Charger and Climate use this same renderer. [HACS listing readiness](HACS_SUBMISSION.md) is
separate from installing this stable release as a custom repository.

### v1.8.0-beta.6: corrected auto reference and power pulse speed

`size: auto` uses a stable **display/design reference width**, default1536 CSS
pixels. Use `auto_reference_width: 1500` for82px at a1500px displayed floorplan,
41px at750px. High-resolution source images no longer make cubes start tiny.
Current beta.4 caps normal auto sizing at 82px. Explicit numeric sizes remain
fixed; ordinary omitted size remains 82px, while Collapsible Hubs default to auto.
Read the
[complete floorplan YAML and migration](FLOORPLAN_SIZING.md).

The [power-speed demo](../examples/energy-wave-power.yaml) keeps true hexagonal
geometry and adds bounded power/fixed speed with phase-preserving smooth rate
changes. It requires no charger or service call. Existing energy_wave settings
retain their three-second cycle. [Rate settings and real sensor mapping](ENERGY_WAVE.md).
The owner-approved40% and logo gradients, native Sonos and other modules remain.

## v1.8.0-beta.5 — cumulative floorplan and shared presentation beta

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.0-beta.5) · Published 2026-10-22 (UTC).

Starts from the exact owner-accepted beta.4 commit
`355caa680ada9c38f7562fbc3a4df8344068140a`. Native-only Sonos, namespace
isolation, recursive Light zoom and existing actions/navigation are retained.

- Opt-in `size: auto` derives an effective numeric size from the actual floorplan
  image; contain/cover offsets, shared lifecycle observation, live menu geometry.
  Numeric sizes and omitted fixed-82 default remain. Unsupported frames safely
  fall back to 82px. No additional scaling engine or YAML dimensions.
- Default active gradient edge darkening is 40% with softer visible spread;
  decorative Hub logos receive shared depth. Independent borders, explicit
  styling precedence and solid inactive physical fills remain.
- Optional normalized `energy_wave` draws a genuinely six-sided expanding SVG
  contour in the existing renderer, with healthy positive-power/motion/visibility
  gates, one shared observer and a 24-animation budget. No Charger module.
- Consolidated reviewed English terminology/dark anatomy diagram/stable badge,
  complete GPL/NOTICE/SPDX metadata, local HACS payload validation and manual
  official catalog readiness review. No upstream listing submission.

See [floorplan YAML/limits](FLOORPLAN_SIZING.md),
[synthetic no-device wave demo](../examples/energy-wave.yaml),
[shared visual policy](CUBE_PRESENTATION.md),
[Sonos migration](SONOS_NATIVE_FAVORITES.md) and
[HACS readiness](HACS_SUBMISSION.md). Small auto-scaled touch targets,
HA DOM compatibility, non-Chromium hardware and GPU/battery behavior still
need owner real-HA testing. HACS topics/default-branch license/fork admission
remain owner/external gates; local checks do not certify catalog approval.
Beta.4's intentional Sonos cache removal and NG namespace migration still
require SemVer/stable review. No master merge, stable promotion, retention
change, existing tag/asset overwrite or mutation of private v1.7.1-beta.5.

## Honeycomb NG v1.8.0-beta.4 — native-only Sonos favorites

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.0-beta.4) · Published 2026-10-22 (UTC).

v1.8.0-beta.4 — cumulative native-only Sonos Favorites

BREAKING BETA MIGRATION — OWNER-APPROVED FINAL #93 CONTRACT
Browse Media is the default and ONLY favorite-artwork/metadata enrichment source. All legacy template-cache support is removed: no implicit sensor.sonos_favorites_cache lookup, no explicit favorites_cache_sensor configuration, no fallback or migration shim. Remove favorites_cache_sensor from dashboard YAML (it now produces a migration error), and remove the custom favorites-cache template definition and refresh setup used only for Honeycomb. Keep unrelated templates/helpers and the OFFICIAL native Sonos favorites entity. Remove the unpublished experimental favorites_browse option too. Honeycomb does not edit live HA configuration.

The owner explicitly confirmed this revised contract and beta.4 publication in chat, superseding the earlier opt-in/cache-compatible proposal. Removing a public configuration option is a SemVer breaking change. This prerelease intentionally retains the approved v1.8.0-beta.4 test train; a major-version/stable compatibility decision must be reviewed before any stable promotion. Stable v1.7.1/master remain unchanged.

Exact tested source: 355caa680ada9c38f7562fbc3a4df8344068140a, PR #114, based on exact tested/published cumulative beta.3 4b3bbede9fc8966305b3ee6cb80ef4f49001f89f. Both PRs remain unmerged. Includes beta.1 namespace isolation, beta.2 shared 82px presentation and beta.3's 30% default active-fill edge. No Light/shared-gradient source changes relative to beta.3.

NATIVE DATA FLOW
A simple type: sonos (or legacy type: media) Hub item, or module: sonos Control, now retrieves thumbnails through Home Assistant's supported authenticated read-only media_player/browse_media WebSocket API. No artwork option, templates.yaml, helper, script, automation or backend installation is needed. The enabled OFFICIAL favorites_sensor still owns IDs/order/playback (default sensor.sonos_favorites). Missing/empty native map means no browsing. Browse only enriches IDs; it never creates favorites or changes playback.

Only returned favorites_folder IDs are traversed. Exact official/browse ID and corroborating title are required; duplicates/stale/foreign-library collisions fall back. Browse exposes no universal FV-to-stream mapping. Recognition uses exact favorite ID or strict unique radio-channel/programme corroboration; arbitrary track titles, ambiguous names, unknown stream URLs and former URI aliases never identify a station. Known artwork/accent updates both parent Hub launcher and promoted Sonos center live. Playing is active; paused/stopped fill stays neutral. Radio keeps its twelve positions/order/actions, reusing the existing image/error path to restore icon/title on broken images.

BOUNDS AND PRESERVED FEATURES
Per-tab/HA-connection shared memory cache, no storage/auth globals or synthetic states. Dedup: 120ms debounce, eight-second deadline including queue wait, five-minute shared refresh only while observed, 60-second negative cache. Bounds: 32 contexts, 512 map entries/returned leaves, eight folders, two actual outstanding WS reads. Unresolved reads retain their budget until response/disconnect. Group/config/map/reconnect/disposal ownership guards discard late results without ghost menus. No per-cube polling, web scraping, HA service calls or config-file mutations by the provider.

Shared 82px geometry, independent borders, Sonos native Sleep/Join/volume/Radio playback/sibling Back/idle, Light Hue/Kelvin zoom/presets and dynamic slots remain. Existing explicit presentation styling overrides remain. Default-only/native API data is now used instead of the removed template path.

VALIDATION
307 passing Node tests, 3 stable-only approval tests correctly inapplicable/skipped on beta metadata; 13 core contract groups. Exact push CI 39732799037 and PR CI 39732805734 must both be green before publication: 136 inherited desktop/mobile regressions, 8 full-original/NG coexistence scenarios, 10 presentation tests, 22 native Favorites scenarios, 16 docs interactions, 6 native Sleep boundary-model tests, performance, build/checksum and workflow lint. Documentation validation: 54 YAML blocks, 30 complete cards, 10 contextual fragments, 56 module descriptors, 129 local links. Public examples/fixtures are synthetic.

Tests prove absent/conflicting legacy cache sensors are never consulted, removed options reject clearly, minimal media items need no artwork config, API failures fall back, both station surfaces and Radio receive native artwork, and grouping/reconnect/reload/timeout/idle/disposal/ambiguous identity are safe. Historical captures still run immutable older bundles; new fixtures use Browse responses, with independent hostile Proxy/sentinel tests. Radio comparison preserves geometry/order/fills/styles/actions while accounting explicitly for native img/error delivery replacing legacy CSS backgrounds. Shared-cube-evidence includes desktop/mobile before/after screenshots and metrics.

Two builds are byte-identical. HACS bundle: 207157 bytes, SHA256 59c25433192a2cbf0f67999644405093d2e27897ff920b9e4ce4c207bba755fd. Normal publisher verifies exact tested head/CI/artifacts/metadata, creates one unused immutable tag and independently checks all staged/public assets and provenance. No old tag/release/asset is overwritten.

INSTALL AND TEST
Migrate the removed cache setup first. In HACS → Honeycomb Menu NG → Redownload → Show beta versions → choose v1.8.0-beta.4 → download; hard-refresh all dashboard clients and keep one NG resource. Manual installation: download honeycomb-menu-ng.js from this release, verify SHA256SUMS.txt and replace the existing NG resource. Official HACS catalog listing is independent; the repository remains usable as a custom Dashboard repository.

Read docs/SONOS_NATIVE_FAVORITES.md for complete copy/paste Hub/Control cards, migration, exact limits and DevTools WS proof; README/docs/AI_SETUP.md use the current native-only schema. Enable the official native favorites entity and specify its actual ID only if different from sensor.sonos_favorites. Do not recreate the custom cache template.

Real HA checklist: verify recorded Browse requests and logos without templates (including with an obsolete conflicting cache entity still present), both launcher/promoted center and Radio order/playback, station switches/pause/unknown content, Join/follower/coordinator changes, reload/HA restart/offline/permissions and five-minute artwork refresh. Check Sleep/Back/idle, Light Hue/Kelvin/presets, dynamic slots and original/NG coexistence. Do not publish tokens/private IDs or full signed/stream URLs in reports.

LIMITATIONS / NEXT GATE
Memory cache is per tab and refetched on reload; enabled native favorites map, verified available Sonos group, Browse permission and accessible artwork URLs are required. Unknown/ambiguous/mismatched metadata deliberately shows standard presentation. Synthetic CI does not prove physical Sonos/HA/tablet behavior. Existing narrow-screen outer-ring clipping and native Sleep estimate/no-device-readback limits remain. Removed cache/URI-alias behavior is an intentional breaking migration, not a silent fallback.

Prerelease only, not latest stable. No merge/master/stable/retention changes, old Release/tag deletion or private v1.7.1-beta.5 mutation. Owner real-HA approval remains required before stable. Additional gradient depth, logo-cube gradient, hexagonal pulse and subsequent fixes are reserved for beta.5/follow-up review; beta.5 is NOT published proactively.

Tested branch: `feature/issue93-native-favorites-beta4`; commit: `355caa680ada9c38f7562fbc3a4df8344068140a`.
Bundle SHA-256: `59c25433192a2cbf0f67999644405093d2e27897ff920b9e4ce4c207bba755fd` (207157 bytes).

This is a beta. An unmerged branch does not require promotion to master. Owner real Home Assistant testing and explicit approval are required before merge or stable publication.

## Honeycomb NG v1.8.0-beta.3 — deeper active fill edges

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.0-beta.3) · Published 2026-10-22 (UTC).

v1.8.0-beta.3 — cumulative active-fill edge calibration

Exact tested source: 4b3bbede9fc8966305b3ee6cb80ef4f49001f89f, PR #111, based directly on published cumulative beta.2 (51d4452c7dd8d6e6660d4e810d669fd08ec4dd42). This branch remains unmerged; master and latest stable v1.7.1 are unchanged.

The shared active radial-gradient default edge darkening increases from 20% to 30%. The center continues to equal the resolved inner-border color. Only the cube fill edge changes; independent borders, inactive/off/paused solid fills, explicit center/edge/darken/solid overrides, 82px geometry and all Light/Sonos/navigation/visibility functionality are preserved. An explicit darken: 0.2 still means 20%. No Favorites provider or future module is added here.

Validation: 290 passing Node tests, 13 core contract groups, 3 stable-only tests inapplicable/skipped on beta metadata; full exact push/PR CI includes 136 desktop/mobile regressions, 8 full-bundle coexistence scenarios, 10 presentation tests with 30% stop assertions and screenshot evidence, 16 documentation interactions, 6 native Sleep boundary models, YAML/local links, performance, build/checksum and workflow lint. Two local builds are byte-identical. Publication additionally verifies matching CI artifacts and immutable tag/release provenance. Bundle SHA256: f56e0bd36a8a8e5a9a89754881adafb3acf73d48335f8f2c4315e0171cc32ca2.

HACS: open Honeycomb Menu NG → Redownload → enable beta versions → v1.8.0-beta.3 → download, then hard-refresh each dashboard browser. Keep one NG resource and follow docs/V1_8_BETA.md. Manual installation: use the release's honeycomb-menu-ng.js and verify SHA256SUMS.txt. Review docs/NG_RUNTIME.md for mixed-original/NG popup routing and custom JavaScript API migration.

Known limitations: 30% remains a visual calibration candidate awaiting real HA owner review; existing narrow-screen outer-ring cropping, native Sleep client estimates/no device readback, and older-browser solid fallback for unresolved named/variable colors remain documented. Physical Sonos/Light hardware and tablet GPU behavior require owner testing. Generic cubes without active semantics remain solid. No stable approval implied.

Owner explicitly authorizes this new immutable prerelease and immediate development/publication of cumulative beta.4 after all gates pass. Beta.5 is reserved for subsequent actionable owner findings. No PR merge, stable publication, retention setting change or previous tag/release/asset mutation; the private v1.7.1-beta.5 draft remains preserved.

Tested branch: `feature/issue104-shared-presentation`; commit: `4b3bbede9fc8966305b3ee6cb80ef4f49001f89f`.
Bundle SHA-256: `f56e0bd36a8a8e5a9a89754881adafb3acf73d48335f8f2c4315e0171cc32ca2` (200054 bytes).

This is a beta. An unmerged branch does not require promotion to master. Owner real Home Assistant testing and explicit approval are required before merge or stable publication.

## Honeycomb NG v1.8.0-beta.2 — shared active fill presentation

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.0-beta.2) · Published 2026-10-21 (UTC).

v1.8.0-beta.2 — cumulative shared CubePresentation

Includes namespace beta.1 from cd82acf4abe0a36685c9574e285ff8f6706d0fb5 and public stable v1.7.1 ancestry. Exact tested source: 51d4452c7dd8d6e6660d4e810d669fd08ec4dd42, PR #111 (stacked on #110). Neither PR is merged; master and latest stable remain unchanged.

One existing 82px renderer owns the visuals. Shared policy supplies active radial cube fill: center equals the resolved inner-border color, edge subtly darker (20% default); borders remain independent. Light off/Sonos paused/disabled remain solid. Existing explicit center/background overrides remain solid unless radial is requested deliberately. colors.fill_gradient supports false/solid or radial with optional edge/darken (0–0.4). Shared bounded artwork helper preserves existing Sonos spacing and aspect ratio. RGB, Kelvin, hue-wheel HSL, named and CSS-variable colors supported; feature-detected CSS color-mix falls back safely to solid on older browsers. No JS polling, animation or new device actions.

Preserved: native Sonos Sleep without HA helpers, Radio recognition/artwork/favorites/cache/order/playback, Join/discovery/grouping, sibling Back/idle, Light presets and recursive Hue/Kelvin zoom, dynamic hard/priority/soft placement and deferred redraw. Generic action/palette cubes without declared active semantics remain solid; no guessed activity from retained accent alone.

Validation: 290 passing Node tests + 13 core groups; 3 stable-only source-approval tests correctly inapplicable/skipped on beta metadata. Exact push CI 39677305949 and PR CI 39677316073 green: 136 desktop/mobile regressions + 8 full-original/NG coexistence scenarios + 10 focused presentation tests; 16 documentation interactions; 6 native Sleep boundary-model tests. 56 YAML blocks, 27 complete cards, 13 fragments, 56 compiled module descriptors, 124 local links. Workflow lint, performance, reproducible build, matching committed/rebuilt/CI assets, SHA256 and provenance verified. A 91-Light fixture performs zero renders for 1000 unrelated HA updates and one render for one changed entity. Synthetic fixture timings are not a real tablet/Raspberry Pi guarantee.

HACS: Redownload → Show beta versions → select v1.8.0-beta.2. Hard-refresh all clients, with one NG resource only. This is one cumulative bundle; it includes beta.1. Follow docs/V1_8_BETA.md, CUBE_PRESENTATION.md and NG_RUNTIME.md. Compare active RGB/Kelvin Light, off/unavailable, playing/paused Sonos launcher/promoted center, station artwork/volume and independent borders. Test explicit colors.center, solid/radial/edge/darken choices and the new examples/presentation-light.yaml. Recheck complete Light/Sonos/Hub/Control/gesture/navigation/visibility flows on desktop/tablet/mobile.

Namespace compatibility: persistent Hub/Control YAML unchanged. In mixed original+NG installations, unmarked external honeycomb_menu events belong to original; select NG with honeycomb_ng_menu or window.honeycombNG.open. Custom JS globals/internal selectors must migrate as documented; owner API review required before stable. Real HA/device/visual testing remains required. Existing narrow-screen outer-cell cropping and Sleep local estimate/no-readback limits remain.

Excluded: Sonos Favorites research provider (#109), charging-wave study (#113), production Charger/Climate/Car, backend integrations and release cleanup. Official HACS catalog readiness (#108) remains blocked by repository topics/license metadata; custom-repository beta installation is separate. No stable publication, PR/master merge, retention change, deletion, overwritten tag/release/assets, or mutation of beta.5 private draft. All prior releases including beta.1 remain untouched. RELEASE_RETENTION_ENABLED remains false. Owner explicitly authorizes this new immutable v1.8 prerelease after normal manual publisher gates; real HA approval is still mandatory before stable.

Tested branch: `feature/issue104-shared-presentation`; commit: `51d4452c7dd8d6e6660d4e810d669fd08ec4dd42`.
Bundle SHA-256: `ce7683cc2b13220d9a2db194e962ffa80e6fbf269ed838041592b03c64be77cb` (200054 bytes).

This is a beta. An unmerged branch does not require promotion to master. Owner real Home Assistant testing and explicit approval are required before merge or stable publication.

## Honeycomb NG v1.8.0-beta.1 — isolated NG runtime

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.8.0-beta.1) · Published 2026-10-21 (UTC).

v1.8.0-beta.1 — NG runtime namespace isolation

Cumulative from public stable v1.7.1 at 4c548d7f45b3622438cde8b03d7ec01f1d7a30c2. PR #110 remains unmerged; master/stable stay unchanged. Internal menu/item/XY elements, runtime APIs, cache, lifecycle events, audio ID and private CSS tokens are NG-owned. One shared 82px renderer and all owner-tested Light/Sonos/navigation/dynamic-slot behavior retained; desktop/mobile Hub baseline captures are pixel-identical to stable.

Compatibility: public persistent Hub/Control YAML unchanged. Existing NG-only classic YAML remains valid. In mixed original+NG installs, unmarked external honeycomb_menu events belong to original; use honeycomb_ng_menu or window.honeycombNG.open for NG. Custom JavaScript/internal-selector callers must use the documented NG API. No conflicting aliases; review docs/NG_RUNTIME.md before mixed testing.

Tests: 284 passing unit tests plus 13 core contract groups; 3 stable-publisher source-approval tests correctly inapplicable/skipped on beta metadata. Full CI: 136 desktop/mobile regressions, 8 full-original/NG both-order coexistence scenarios, 14 documentation interactions, 6 native Sleep boundary-model tests, YAML/link checks, performance, build and workflow lint. Matching push CI 39673899235 and PR CI 39674014785 green at the exact tagged commit. Rebuilt/committed/CI assets and SHA256 are independently verified by this publisher; checksum/provenance files attached.

Install/test: HACS → Honeycomb Menu NG → Redownload → Show beta versions → v1.8.0-beta.1. Hard-refresh all browsers and verify only one NG resource is loaded. Follow docs/V1_8_BETA.md: each plugin alone/both orders, classic routing, Hub/Control, Light tap/hold/presets/Hue/Kelvin Back, Sonos Radio/artwork/Join/native Sleep and sibling idle, dynamic slots and desktop/tablet/mobile. No live HA configuration changed by development.

Known limitations: ambiguous mixed legacy popup routing requires explicit ownership; old JS globals/internal selectors migrate. Real HA/physical Sonos testing and owner approval required before stable. Existing narrow-screen outer-cell cropping and Sleep estimate/no-readback limitations remain. Shared active gradients are a separate PR #111, NOT in this beta. Research favorites provider, charging wave, Charger/Climate/Car are NOT included. Official HACS catalog readiness has separate license/topics blockers (#108); custom-repository installation remains supported.

This is prerelease=true, not latest stable. No merge, stable publication, retention setting change, deletion or overwrite. Every existing release/tag/asset, including beta.5 private draft, must remain unchanged. RELEASE_RETENTION_ENABLED remains false. Owner explicitly authorized new immutable v1.8 beta publication in the overnight sprint.

Tested branch: `feature/issue104-ng-runtime-namespace`; commit: `cd82acf4abe0a36685c9574e285ff8f6706d0fb5`.
Bundle SHA-256: `b4c671a58a783e1dd643aaa81a83fe48b11ddaf5ee126c428fb03a4e20d42fae` (196830 bytes).

This is a beta. An unmerged branch does not require promotion to master. Owner real Home Assistant testing and explicit approval are required before merge or stable publication.

## v1.7.1 — Stable

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.1) · Published 2026-10-21 (UTC).

Owner-approved on 2026-10-21 after real Home Assistant testing of cumulative
v1.7.1-beta.8 at `c1cdd390bed1c1acfc22b314807ce63050e43248` (Issue #102).
Issues #90, #97 and #99 are completed. Functional source is exactly that beta;
the rebuilt stable JavaScript adds only a `v1.7.1` version comment. All earlier
releases/tags/assets, including beta.5's unpublished private draft, are preserved.

- Sonos controls match Light's icon/text layout at the shared 82 CSS-px size.
  Slots: 1 Radio, 2 Play/Pause, 3 Join, 4 Sleep, 5 Volume Down, 6 Volume Up.
- Known Radio favorites propagate cached artwork and deterministic station colors
  to Hub launchers and promoted centers; playing fill is station-colored,
  paused/idle fill is neutral gray with compact artwork. Existing favorites sensor
  and template-cache YAML, ordering, artwork and playback remain compatible.
- Join supports real group membership, room discovery and configured member/script
  overrides. Radio, Join and Sleep are siblings: switches replace the active view,
  one Back returns to Sonos main. Idle-close inherits the configured timeout
  (8 seconds default, intentional zero preserved). Passive HA updates/discovery
  do not extend it, and late responses cannot resurrect abandoned menus.
- Native Sonos Sleep uses `sonos.set_sleep_timer` / `sonos.clear_sleep_timer` on the
  selected group's coordinator: 15/30/45/60/90 minutes and Cancel/OFF. The speaker
  owns the timer; no HA helper/script/automation setup. Remaining time is a local
  estimate, not device readback. See [timer limitations](SONOS_SLEEP_TIMER.md).
- Recursive Hue and bounded linear Kelvin zoom preserve the exact selected slot
  and value. Holds never apply a Light service; Back restores exact palettes and
  full close resets. White swatches are filled hexagons without visible dots or
  values, with screen-reader labels. Native Kelvin bounds are required; client
  precision is 1 K and devices can quantize more coarsely.
- Accessible responsive SVG layout model, canonical terminology and versioned
  human/AI guides ship with all existing Light presets, media controls, dynamic
  Hub allocation and drag-select behavior.

Stable publication requires a reviewed beta-approval manifest, exact unchanged
runtime/dependencies, a reproducible bundle, matching green CI on the exact master
commit and explicit manual authorization. Version/title gates support future
canonical stable SemVer releases. Retention must remain explicitly false; the
post-publication retention call is forced read-only. No releases, assets, tags,
refs, branches or source history are cleanup targets during this release.

HACS: Redownload Honeycomb Menu NG and select v1.7.1 stable, then hard-refresh all
clients. Keep the existing `honeycomb-menu-ng.js` JavaScript module resource.
Existing HA Sonos services and optional favorites/cache setup remain prerequisites;
no new helpers or configuration keys. Car/Charger, Climate and unrelated
#83/#92/#93/#87/#86 work are excluded. Existing mobile outer-menu edge cropping
and native Sleep readback limitations are unchanged. Future stable versions still
require beta testing and explicit owner approval.

---

## v1.7.1-beta.8 — cumulative Sonos navigation and idle-close

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.1-beta.8) · Published 2026-10-21 (UTC).

Based on exact published beta.7 `737a13c8f1a1020db18e14325a40240708dc2706`.
Radio, Join and Sleep are sibling views: direct switches and repeated opens replace
rather than push; Back once returns to Sonos main. All inherit the configured
module idle timeout (8 seconds default, intentional zero preserved). Passive HA
updates and asynchronous discovery do not renew the deadline. Late responses are
scoped to their originating view and cannot resurrect abandoned menus. Genuine
children and recursive Light Hue/Kelvin zoom keep their exact Back history.

Preserves all beta.7 features and visuals, native Sonos Sleep services without
helpers, Join discovery/grouping, Radio recognition/cache, 82 CSS-px geometry,
Light presets and dynamic placement. Clock-controlled desktop/mobile regressions
cover sibling permutations, deadlines/interaction, pending discovery, native Sleep
selection/cancel and overlay cleanup. See [HA checklist](V1_7_1_BETA.md).

One cumulative HACS prerelease only after full matching CI and normal manual
publisher gates. Real HA/device confirmation remains required; no stable/master
merge or issue closure. Prior beta tags/assets and beta.5's unpublished private
draft stay immutable; retention settings and excluded issues are untouched.

## v1.7.1-beta.7 — cumulative Sonos visuals and Kelvin zoom

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.1-beta.7) · Published 2026-10-21 (UTC).

Based on exact published beta.6 `214443460f827c05f977a8aaeefe48f71a7216b6`.
Sonos/Light work is isolated in reviewable commits; no PR or master merge.

- Sonos function icons and labels inherit ordinary Light's shared hierarchy.
  Playing station artwork shifts down with volume text unobstructed; paused/idle
  artwork stays compact at 62% of usable fill, retaining gray cube fill, station
  inner border, aspect ratio and exact 82 px geometry. Radio behavior is unchanged.
- White outer-menu swatches are solid Kelvin fills without dots/icons/visible
  codes. Screen-reader names preserve exact values. Tap sends one validated native
  temperature; hold/Shift+Enter/Shift+Space opens bounded linear Kelvin refinement
  with no HA service call. Preserve exact selected slot/value and Back snapshots;
  full close resets to native bounds. Existing Color interpolation is unchanged.
- Keep native device-owned Sonos Sleep without helpers, Radio recognition/cache,
  Join Back/grouping, light presets, dynamic placement and terminology.

Limits: native numeric Kelvin bounds are mandatory, with no invented range or
mired conversion. Client precision is 1 K because HA has no standard hardware
Kelvin-step attribute; lamps can quantize more coarsely. Zoom stops before duplicate
or identical refinements. Original ranges with fewer than twelve integer values
keep twelve legal sampled cells with unavoidable repetitions and no zoom. Kelvin
RGB is approximate. Real HA/Sonos/lamp validation and non-Chromium testing remain
necessary; existing narrow-screen outer-menu cropping is unchanged. Sleep labels
are estimates, not hardware status/readback.

[HA beta checklist](V1_7_1_BETA.md), [Kelvin rules](LIGHT_MODULE.md#recursive-white--kelvin-zoom--issue-99-beta7),
[Sonos reference](SONOS_MODULE.md), [terminology](TERMINOLOGY.md).
Existing beta tags/assets and beta.5's unpublished draft stay immutable. No stable
release, master merge, retention changes or issue closure. #90/#97/#99 require
owner validation; #83/#92/#93/#87/#86 are excluded.

---

## v1.7.1-beta.6 candidate — native Sonos device Sleep Timer

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.1-beta.6) · Published 2026-10-21 (UTC).

Unpublished candidate from cumulative beta.5 source, preserving beta.4 recognition
and Light Zoom, beta.5 artwork scaling/Join Back and PR #96 terminology. Replaces
the rejected helper/script/automation timer with official `sonos.set_sleep_timer`
(seconds, maximum 7200) / `sonos.clear_sleep_timer`. No manual HA setup. All five
choices and Cancel/OFF target the freshly validated current coordinator.

Speaker owns expiry; browser/HA restart should not stop a powered speaker's timer.
Real HA/Sonos confirmation is still required. Remaining-time display is explicitly
a local estimate, not device readback; reload/reconnect/group changes show unknown.
Failures/timeouts never claim OFF or retry playback. Native group changes follow
Sonos semantics, without extra Honeycomb cancellation. See
[native API/limitations and checklist](SONOS_SLEEP_TIMER.md).

Beta.5 tag, unpublished draft and assets remain immutable historical artifacts.
New-release publication lookup uses bounded paginated inventory reads for a missing
draft, then exact-ID draft/asset validation before public PATCH. There is no
existing-draft resume or mutation retry; permission failures still stop.
Separate owner approval plus exact head/CI/metadata/reproducibility/checksum guards
are required for a NEW beta.6 publication; no release was published by this change.
No stable/master merge, retention setting change or release/tag deletion.

---

> Historical beta.5 notes below describe the rejected helper implementation in
> its frozen **unpublished draft**, not the beta.6 native device timer.

## v1.7.1-beta.5 — cumulative Sonos Sleep, artwork and navigation

Based on exact immutable beta.4, preserving its Radio recognition/cache behavior,
Join/grouping, media controls and the owner-tested recursive Light Color Zoom.
Documentation-only terminology PR #96 is deliberately integrated into this branch;
no review PR or master is merged by publication.

- Compact playing artwork leaves room for 0/2/42/100% volume labels. Paused artwork
  expands within clipped cube fill, retaining gray fill, station-colored inner
  border and shared 82 px geometry. Both module launcher and promoted center tested.
- Fix repeated Join reentry stacking identical views and stale asynchronous
  discovery after navigation. Accessible center Back returns one level; room
  discovery, native grouping and configured scripts/members remain working.
- Replace Sonos slot 4 Browse with native **Sleep**: 15/30/45/60/90 minutes plus
  Cancel/OFF. Radio, Play/Pause, Join and volume retain their slots and handlers.
  Explicit custom HA Browse navigation remains supported.
- **Sleep requires the optional HA package**: two helpers, one queued script and
  one automation per selected player. HACS frontend cannot create these. HA owns
  the persisted deadline and expiry; there is no browser-only countdown/action.
  Commands bind to one selected player, reject stale expiry and recheck the group.
  Any group change/unavailability cancels; unrelated rooms are never targeted by
  a global pause. Errors are surfaced without delayed playback retries.
- **Browser closure/reload preserves the job; HA restart, automation reload and
  state-helper reload cancel it safely. It does not resume across HA restart.**
  Separate instances remain independent; overlapping timers have no global arbiter.

See [HA setup / test checklist](SONOS_SLEEP_TIMER.md),
[HACS beta instructions](V1_7_1_BETA.md) and [terminology](TERMINOLOGY.md).
Package YAML/Jinja service contracts and browser tests are not a running HA Core
or physical Sonos installation. Real HA group/event behavior, artwork access,
external setup and non-Chromium still require owner validation. Unsupported station
formats fall back; very long helper payload identifiers fail closed. Existing
narrow-screen outer-menu cropping is unchanged. #83 stays independent dry-run only;
#92/#93/#87/#86 are excluded. No stable publication, master merge or deletion of
releases/tags/branches/history is authorized. Owner approval after HA testing is
required before stable promotion.

---

## v1.7.1-beta.4 — cumulative Sonos radio artwork and Light Zoom

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.1-beta.4) · Published 2026-10-21 (UTC).

Continues from immutable cumulative beta.3 (`b61374e6589111642768b305724d52c385eccfa6`),
retaining all Sonos beta.2 fixes and recursive Light Color Zoom. No stable/master
merge is authorized.

- Recognize the owner's real-HA-shaped `Station Alpha · programme text` channel
  using an exact, unique station prefix corroborated by the favorite map and
  typed cache title. Also accept HA's spaced bullet format. No fuzzy names,
  arbitrary suffixes, track-title matching or inferred stream-session mapping.
- Compare plain radio channels against unique exact favorite-map OR cache labels,
  normalizing case/whitespace/NFC and rejecting conflicts. Existing FV IDs,
  four-field caches, sensors, playback actions and favorite order are unchanged.
- Preserve logo, hue inner ring and playing fill on parent Hub ring launchers,
  promoted Sonos centers and deeper Radio/Join centers. Artwork no longer vanishes
  solely because the navigation icon is `mdi:arrow-left`; Back still works.
  Pause/stop stays neutral; unknown content/failed artwork falls back safely.
- Add explicit privacy-safe diagnostic inspection, realistic FV/stream fixtures,
  unit and desktop/mobile transition regressions, and immutable beta.3 before
  screenshots. No automatic logging, polling or identifier/URL disclosure.

Known limitations: only exact identifiers/labels and the two validated structured
channel formats identify stations. Ambiguous names, unverified suffixes and
unavailable artwork fall back. Actual HA/HACS, group metadata, artwork access,
non-Chromium and external automation require owner testing; the existing 82 px
outer ring can crop at narrow viewport edges. Stable v1.7.1 requires explicit
approval after real HA beta testing. No retention settings, releases, tags,
branches or history are deleted/replaced.

See [diagnostics](SONOS_MODULE.md#station-recognition-diagnostics) and
[HACS / real HA checklist](V1_7_1_BETA.md).

---

## v1.7.1-beta.3 — cumulative Sonos and Light owner test

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.1-beta.3) · Published 2026-10-20 (UTC).

One HACS bundle combining **all tested Sonos beta.2 code** from PR #91 at
`282794d3650951d7bc7fd9ce514069ca68fcd121` with isolated Light PR #94 at
`7c7ee3e7ebc528f0aeaa07243631f09ed8d67bd6`. Both original branches remain
unmerged. This integration does not change master or authorize stable publication.

- Preserve Sonos slot/alignment, exact/validated station recognition, cached
  artwork, station/paused colors, native discovery/grouping, script overrides,
  actual HA Browse Media route, Radio behavior and all beta.2 regression tests.
- Add recursive Light Color Zoom: tap applies once; hold refines around the fixed
  selected physical slot/HS without HA calls. Current neighbors bound the new
  palette, with five clockwise and six counterclockwise samples, circular hue
  interpolation, linear saturation and exact endpoints.
- Back restores each complete palette; close/reopen resets. Live HA updates keep
  history. Keyboard Shift+Enter/Space zooms; Escape closes/resets focused swatches.
- Preserve 82 px renderer, inner controls, White/Kelvin, presets, on/off-only
  lights, generic Media, dynamic visibility, nested anchors and gestures.

The isolated Light branch is not published as a competing module-only HACS beta.
No v1.7.2 release is used. Beta.1/beta.2 tags and assets stay immutable. #83 remains
an independent read-only retention audit, with the enable gate false and no deletion.

Known limitations: exact Sonos radio-channel/cache/name matches may not identify
all streams; registry/grouping services and Media panel availability depend on HA.
Browse uses the supported Media panel route rather than a private lazy dialog.
The existing 82 px outer ring may crop at very narrow viewport edges. Physical HA,
external scripts, non-Chromium browsers and actual HACS installation require owner
validation. Stable v1.7.1 requires explicit approval after cumulative beta.3 testing.

See [combined HACS smoke tests](V1_7_1_BETA.md) and
[Color Zoom semantics](LIGHT_MODULE.md#recursive-color-zoom-issue-85-beta3).

---

## v1.7.1-beta.2 — Sonos real-HA corrections

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.1-beta.2) · Published 2026-10-20 (UTC).

Sonos-only follow-up on unmerged PR #91. Beta.1 remains immutable. Stable and
master promotion require owner real-HA approval. Cumulative beta.3 will add Light
Color Zoom only after its isolated PR and combined regression suite pass.

- Bridge FV favorite IDs to Sonos radio stream URIs through a unique exact
  radio-channel/favorite-name/cache-title correspondence, preserving exact ID/URI
  matching, original cache compatibility and all Radio playback/order/artwork.
- Treat legacy `active_color` as fallback; recognized stations provide their
  accent while explicit `colors` still win. Paused/stopped center remains neutral.
- Discover registry-confirmed Sonos players on Join open and use supported native
  join/unjoin without mandatory member/script keys. Preserve manual/script overrides,
  live group visuals, safety checks and explicit metadata/feature/error states.
- Browse opens HA's selected-player Media panel rather than more-info. No private
  dialog loader, invented events or new backend helper is used.
- Generalize the optional HA cache recipe to centrally configured source players,
  failover/startup refresh and source/schema diagnostics. Existing templates work.

Known limits: exact channel names may not identify every stream; ambiguous or
partial names fall back safely. HA registry access, GROUPING features/services,
Media panel availability and browser-accessible logos are external prerequisites.
Actual HA hardware and UI behavior require the owner's beta testing.

See [Sonos details](SONOS_MODULE.md) and [HACS test guide](V1_7_1_BETA.md).

---

## v1.7.1-beta.1 — Sonos owner test

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.1-beta.1) · Published 2026-10-20 (UTC).

PR #91 remains unmerged. This is beta metadata, not stable v1.7.1 approval.

- Preserve Light-aligned Sonos controls, corrected inner slots, actionable Join
  candidates, accurate HA membership/setup/error states and external script contract.
- Add deterministic Light-wheel Radio accent rings without changing order,
  favorite playback, thumbnails, cache recipe, geometry or navigation.
- Use cached artwork and station accents on reliably identified Sonos launchers
  and main selected centers. Pause/stop restores neutral fill; unknown/invalid or
  inaccessible artwork falls back. Explicit styling precedence is documented.
- Replace README ASCII layout with a checked-in accessible responsive SVG matching
  physical slots 0–18. Retain machine-readable AI mapping and semantic tables.

Known limits: real HA Sonos usually exposes a playback URI rather than a favorite
ID. Exact matching needs an ID or a unique explicit URI in existing external cache
metadata; the shipped recipe is unchanged. No title guessing. Twelve hues can be
shared in larger lists. Chromium/synthetic HA tests do not replace owner hardware
validation. Car, Climate and recursive Color Zoom remain out of scope.

Beta publication supports any branch and SemVer beta train, with explicit manual
authorization, exact branch-head and green CI gates, immutable tags/releases,
reproducible HACS assets and verified draft uploads. Stable publication remains
forbidden in that workflow. See [beta publishing](BETA_RELEASES.md) and
[HACS test instructions](V1_7_1_BETA.md).

---

## v1.7.0 — Stable

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.0) · Published 2026-10-20 (UTC).

Honeycomb Menu NG v1.7.0 promotes the tested restart/v1.5.1 line: Phase 1 PR #77,
Phase 2 PR #81, documentation PR #84 and retention PR #88. No v1.6 implementation
is imported. The versioned JS asset remains `honeycomb-menu-ng.js` for HACS.

- Shared full-cell Hub/Control renderer, default 82 CSS px, consistent icons,
  labels, center fill, rings, colors, actions and anchored nested navigation.
- Preserved Light brightness, capability-aware Color/White palettes, numeric presets
  on separate devices/helpers, explicit on/off-only behavior, Media/Sonos group
  volume, favorites/artwork, Join, Browse and drag-select.
- Issue #78 fixes the disappearing Light launcher/preset after nested navigation;
  the six-action Light layout and working Color action remain unchanged.
- Dynamic HA-state/attribute/numeric AND/OR/NOT visibility on Hub items. Hard
  reservations, priority reclaim and stable soft placement; `logo: false` frees
  slot 0. Structural changes defer during menus, gestures and delayed actions.
- Restored verified Layout model, human onboarding, versioned AI guide and complete
  synthetic examples, including external HA Sonos cache/grouping prerequisites.
- Release retention based on latest stable: stable current/previous MAJOR,
  prerelease current/previous MINOR, future prerelease trains and all drafts kept.
  **Retention remains disabled for this release** (`RELEASE_RETENTION_ENABLED=false`,
  owner-verified); publication forces a fresh read-only report, with no deletion.
- Exact-master stable publisher verifies CI, committed/rebuilt artifact checksums,
  new tag, draft assets, stable/latest flags, HACS filename and retained versions.

Control migration: use explicit `module:` and shared keys; `size: 82` is full-cell
width. Older inset/Menu-size Control YAML may require adaptation. Static Hub layout,
legacy media→Sonos alias and classic popup center/slot semantics remain supported.

Known limits: 217 physical positions (additional configured dependencies are tracked
with overflow diagnostics); no paging/auto-shrink; anchored layouts can clip at
viewport edges; only the documented condition subset; intentional structural deferral;
conservative JS templates; 12 Radio/Join outer choices. Automated browser tests use
Chromium and synthetic HA; actual HA integration setup still requires configuration
checks and device validation. Owner has validated beta.3 visibility/deferred placement
in real HA. Future recursive palette (#85), native Car (#86), Climate/Thermostat (#87)
and Charger modules are not implemented. Charging automation remains external.

Validation suite: **127 unit tests** (including 79 retention and 29 publisher cases),
13 core contract groups, **54 desktop/mobile regressions + 12 documentation
interactions**, 54 YAML blocks, 22 complete cards + 14 contextual fragments and
75 local links. All workflow lint and production/checksum gates are required.

Verification: all unit/contract, desktop/mobile, docs/YAML/link, production-build,
workflow-lint and checksum gates must pass on the exact tagged master commit.
Published `SHA256SUMS.txt` and `release-provenance.json` record bundle checksum,
byte size and source commit. Deleting a Release record in a future approved cleanup
also removes its uploaded assets; Git tags, branches, commits and tagged source
remain permanently. See [publication](RELEASING.md) and
[retention](RELEASE_RETENTION.md) guides.

---

## Honeycomb NG v1.7.0-beta.3 — Dynamic Hub visibility and stable slots

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.0-beta.3) · Published 2026-10-20 (UTC).

Phase 2 of #76 / #79 starts from merged PR #77 on restart/v1.5.1 at
`697dec5846fc6b73199fb39562eef5a733ba49c5`. No v1.6 code is used.

- Live HA-style state/numeric_state/and/or/not visibility on Hub items; precise
  dependency snapshots handle same-object state/attribute changes.
- Pure hard/priority/soft allocation with hidden hard reservations, preferred
  priority preclaims, deterministic fallbacks/collision diagnostics, stable soft
  positions and ordinary slot 0 when logo:false.
- Preserve old automatic layouts, the shared 82 px renderer, Light/Media/Sonos,
  presets/favorites/navigation and the beta.2 missing-Light fix.
- Defer structural transitions through menus, touch/pointer/drag and delayed taps.
  Commit the latest desired state atomically at an on-demand frame boundary.
- Cover conditions, collisions, overflow, deferred navigation/gestures, multiple
  Hubs, availability/show compatibility and current 5/20/50-item performance.
- Current physical capacity is 216 ring slots plus center. Configured items beyond
  capacity remain evaluated and report overflow; no silent truncation/wrapping.

The pre-release is tagged at the verified tested feature commit. The Phase 2 PR
is **not merged** into restart/v1.5.1; master and stable v1.5.1 are unchanged.
Exact test results, artifact checksum and commit are in the GitHub release notes.

Known limits: the documented condition subset only; arbitrary JS show/presentation
is conservative; no paging/auto-shrink; anchored menus can clip near viewport edges.
Actual HA devices/other browsers and long-term memory need owner validation.
Car/Charger modules and charging automations are not implemented.

[Current Phase 2 contract and YAML](V1_7_PHASE2.md).

---

## Honeycomb NG v1.7.0-beta.2 — Light navigation fix

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.0-beta.2) · Published 2026-10-20 (UTC).

Fix #78: menu-owned cubes no longer hide themselves when opening nested menus.
Lit reuses those cells during in-place navigation; the old dashboard-launcher
hide/restore logic left a preset and the returned Hub launcher invisible.
Standalone launchers retain their normal hide/restore behavior.

The v1.5.1 Light mapping is unchanged: 100%, brightness preset, Color/White,
standard color/Kelvin preset, −5%, +5%. Color was already present. The reported
empty position is the reused hidden preset cell (physical slot 2 for the first
Light; slot 4 for the second Light in the three-item fixture).

- Preserve the shared 82 px renderer, all Light/Media/Sonos features and drag-select.
- Add desktop/mobile repeated nested/back/close/reopen, preset/capability and
  standalone restore regressions, including Chromium touch input.
- Validate unit/contract tests, production build and the complete browser suite
  before publication; exact results/commit are recorded in the GitHub release.
- Generalize the guarded manual publisher to validated v1.7.0 beta tags, retaining
  exact tag/commit/CI/artifact checks and prerelease=true/latest=false.

This beta is published from PR #77's tested feature commit, **not merged into
restart/v1.5.1**. Master and stable v1.5.1 remain unchanged. Dynamic visibility,
priority placement and Car/Charger are not implemented. Existing narrow-screen
outer-ring clipping and simulated-HA/Chromium-only test limitations still apply.

See [the investigation and slot map](ISSUE_78.md) for details.

---

## Honeycomb NG v1.7.0-beta.1 — Shared Hub and Control Engine

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.7.0-beta.1) · Published 2026-10-20 (UTC).

Phase 1 of #76, developed exclusively from `restart/v1.5.1` at
`c1d9507ee48e65b951f6302c668dadf17043c195`. No v1.6 implementation was merged,
cherry-picked or ported.

**This pre-release is published from the tested feature-branch commit. Its PR is
not merged into restart/v1.5.1. Master and latest stable v1.5.1 are unchanged.**

- Hub, standalone Control and managed menu cubes share one full-cell renderer,
  proportional content metrics, configurable fills/rings and action handling.
- Both public components default to a physical width of 82 px. Control selects
  the same modules with `module: light`, `media`, `sonos` or `generic`.
- Preserve logo:auto count behavior. logo:false removes branding while allowing
  ordinary cubes at center slot 0. Empty Hubs do not invent a fallback control.
- Preserve Light palettes/preset apply/store, Media/Sonos playback, group volume,
  grouping, favorites/cache artwork and anchored nested navigation.
- Expandable axial ring geometry removes the seven-item Hub truncation and the
  fixed 18-position core ceiling. Regression coverage renders 50 configured items.
- Forward HA events instead of polling every 200 ms; avoid unchanged model renders
  and continuous Hub anchor RAF. Do not infer unmeasured performance gains.
- Capture checksum-recorded v1.5.1 desktop/mobile visual references and add browser
  checks for painted parity, geometry, module actions, live state and gestures.

### Validation

The release assets are built and syntax/metadata checked from the tagged feature
commit. Unit/contract and Chromium browser results and the exact commit are
recorded in the GitHub release description after final validation. Browser tests
use synthetic HA state/services, deterministic icon glyphs and real pinned
button-card 7.0.1 at desktop/mobile sizes.

### Known limitations

- Dynamic declarative visibility and priority placement are not yet implemented;
  these configuration keys are rejected with a clear later-phase message.
- Car and Charger modules are not implemented.
- Existing `show` remains evaluated when opening/configuring a menu.
- Large anchored scenes can extend beyond narrow viewports; no auto-shrink/paging.
- Continuous CSS-only anchor animations are not followed on every frame.
- Advanced button-card-only template/action contexts need installation validation.
- Actual HA/device integrations and browser engines other than Chromium are untested.

Read [docs/V1_7_PHASE1.md](V1_7_PHASE1.md) for configuration and migration.

---

## v1.6.0-beta.4

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.6.0-beta.4).

Tagged commit “Merge v1.6.0-beta.4 nested palette face fix” [a82ffb6bbe39](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/a82ffb6bbe39b5461d129d07cdde306481225e9a).

## v1.6.0-beta.3

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.6.0-beta.3).

Tagged commit “Merge v1.6.0-beta.3 canonical persistent Hub” [4acd205f0efa](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/4acd205f0efa1bed6630390d538ab7120a1364ad).

## v1.6.0-beta.2

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.6.0-beta.2).

Tagged commit “Merge v1.6.0-beta.2 shared rings and nested navigation” [8945372c61af](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/8945372c61af50f65f80fb2111d53abff376a52f).

## v1.6.0-beta.1

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.6.0-beta.1).

Tagged commit “Merge v1.6.0-beta.1 conditional visibility and Charging Hub” [68066cae2f17](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/68066cae2f17523013a2aac6f080a23ac59ae480).

## Honeycomb Menu NG v1.5.1 – Light State Clarity

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.5.1) · Published 2026-10-13 (UTC).

This stable patch improves Light status presentation and adds native handling for simple on/off-only lights.

#### Light status
- Dimmable light on: shows live brightness percentage.
- Dimmable light off: shows `Off`.
- On/off-only light on: shows `On`.
- On/off-only light off: shows `Off`.
- Unavailable light: keeps the existing gray `Unavailable` presentation.

#### On/off-only lights
If Home Assistant explicitly reports `supported_color_modes: ['onoff']`, Honeycomb treats the entity as a simple toggle:
- short tap toggles the light
- no Light detail level is opened on long press
- no meaningless brightness/preset/palette controls are presented

The detection is deliberately conservative. Missing capability information, including temporary remote/unavailable states, does not classify a light as on/off-only.

#### Documentation/tests
README, Light documentation and the AI setup contract now document this behavior. Regression tests cover On/Off labels, on/off-only menu suppression and unavailable-state capability uncertainty.

## Honeycomb Menu NG v1.5.0 – Stable Modular Release

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.5.0) · Published 2026-10-12 (UTC).

### Honeycomb Menu NG v1.5.0 – Stable Modular Release

v1.5.0 is the first stable release of the modular persistent-Hub architecture developed through the v1.4 pre-releases.

### Documentation rebuilt

The README is now human-first and describes the current product instead of acting as a chronological release log.

New dedicated documentation:
- `docs/LIGHT_MODULE.md`
- `docs/SONOS_MODULE.md`
- `docs/AI_SETUP.md`
- `docs/CLASSIC_MENU.md`

New copy-ready examples:
- `examples/persistent-hub.yaml`
- `examples/light-presets.yaml`
- `examples/sonos-favorites-cache.yaml`
- `examples/sonos-toggle-member.yaml`

### AI setup contract

A deterministic AI-oriented setup specification now helps ChatGPT/Codex-style assistants:
- ask for real entity IDs
- choose the correct module
- avoid inventing optional helpers/scripts
- configure Light presets correctly
- enable/document Sonos favorites and optional artwork cache
- add Join grouping only when requested
- validate locked-center navigation

### Light preset helpers

Preset storage now supports both:
- `number.*` entities, including device-owned values such as Shelly numbers
- Home Assistant `input_number.*` helpers

This lets physical wall controls and Honeycomb share the same normal brightness/Kelvin/color values.

### Sonos documentation

Sonos setup now clearly separates:
- native group-aware volume (no scripts required)
- official `sensor.sonos_favorites` names/IDs
- optional thumbnail/artwork cache
- optional Join toggle script

The artwork cache remains a Home Assistant trigger-based template sensor by design. It refreshes independently of dashboard/browser sessions and avoids each frontend polling Sonos.

### Project identity

Honeycomb Menu NG is now described as a project that **originated as a fork** of Sian Croser's GPLv3 `honeycomb-menu`. The repository still retains portions of the original implementation and attribution, while NG is documented as its own substantially expanded project rather than merely an "enhanced fork".

### Stable v1.4 foundation included

- modular core
- isolated Light/Media/Sonos modules
- persistent Hub lifecycle fixes
- locked slot-0 module center
- native Sonos in physical slot 0
- live Light/media presentation
- unavailable-state labels
- shared bee branding
- automated architecture/regression tests

This is a normal stable release, not a pre-release.

## v1.4.9

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.9).

Tagged commit “Merge v1.4.9 bee asset repair” [9eb565921005](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/9eb565921005a03163c19b0e4290ec80d554f485).

## v1.4.8

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.8).

Tagged commit “Merge v1.4.8 shared bee branding” [74bde0795fd6](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/74bde0795fd64fe5eb9943138f7d23583305da6d).

## v1.4.7

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.7).

Tagged commit “Merge v1.4.7 unavailable status” [791d30b5fe76](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/791d30b5fe7661a8d60dd065c79b198335c6983f).

## v1.4.6

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.6).

Tagged commit “Merge v1.4.6 native Sonos slot 0” [58eecb19da9d](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/58eecb19da9d8121798221f725b74ebb0f8685fb).

## v1.4.5

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.5).

Tagged commit “Merge v1.4.5 persistent Hub lifecycle” [1847ca9d3d39](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/1847ca9d3d39a49ca867341f9df8519be20bece3).

## v1.4.4

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.4).

Tagged commit “Merge v1.4.4 Sonos artwork-only favorites” [41acea3ca2dc](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/41acea3ca2dcce0c47e6f219c2ca65cd483d1168).

## v1.4.3

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.3).

Tagged commit “Merge v1.4.3 Sonos visual polish” [2a3e1a03d099](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/2a3e1a03d0996cce0028141a530e2520b4cd69c1).

## v1.4.2

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.2).

Tagged commit “Merge v1.4.2 Light nested context fix” [c6e3da8564e6](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/c6e3da8564e6becea92a7971cf26bb16396a1be3).

## v1.4.1

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.1).

Tagged commit “Merge v1.4.1 base cube geometry” [92b2ef8232f5](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/92b2ef8232f58ed04057f509db7fc3ead896b380).

## v1.4.0

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.4.0).

Tagged commit “Finalize v1.4.0 release pipeline” [7fd504c0a7a9](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/7fd504c0a7a995ff53a4dbd8ec97a6072c6331ff).

## v1.3.2

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.3.2).

Tagged commit “Merge v1.3.2 module anchor lock” [66056aadad20](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/66056aadad206e01b89c466c5ebafc73d06ba6a6).

## v1.3.1

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.3.1).

Tagged commit “Merge v1.3.1 media nested context fix” [87af41a82ce5](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/87af41a82ce5ed292feb676cc8702dc561d5b242).

## v1.3.0

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.3.0).

Tagged commit “Merge v1.3.0 native media control” [1161f53ba51d](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/1161f53ba51db8210b0064b0f0361e41d898b04f).

## v1.2.12

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.12).

Tagged commit “Merge v1.2.12 live state refresh” [5dd630f39e65](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/5dd630f39e6514005ca37e25f202ff1c9e49d6a0).

## Honeycomb Menu NG v1.2.11 – Persistent Border & Instant Hub Return

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v1.2.11) · Published 2026-10-11 (UTC).

### Honeycomb Menu NG v1.2.11 – Persistent Border & Instant Hub Return

This pre-release fixes the two remaining differences observed after v1.2.10.

### Persistent light border parity
Hub light launchers now preserve the same default gray outer border as a standalone `honeycomb-persistent-control` when the light is on.

The root cause was that embedded persistent controls receive configuration directly through Lit, while standalone controls normally receive the defaults through `setConfig()`. With no explicit `outer_border`, an embedded on-state control therefore allowed the outer polygon to follow the live light color, making the border disappear.

- missing `outer_border` now defaults to `#34383d`
- explicit `outer_border: auto` still follows the live light color
- off-state behavior is unchanged

### Instant persistent Hub return
The persistent Hub base is now explicitly non-animated.

- Hub root tiles appear immediately when the dashboard loads
- returning from menu 2 restores the complete Hub base immediately
- no staggered/floating population of root tiles
- classic Honeycomb menu/detail levels retain their normal animation
- nested menus are unaffected

The new `animate: false` path is used by the persistent Hub root only; normal Honeycomb menus default to `animate: true`.

## v1.2.10

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.10).

Tagged commit “Merge v1.2.10 classic dormant light launchers” [9bbd7dffbb11](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/9bbd7dffbb1188e82972af137595e6812225ea7b).

## v1.2.9

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.9).

Tagged commit “Merge v1.2.9 classic multi-instance Hub” [f09855cfb7f0](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/f09855cfb7f0ac26809f66928a7dce5cc124044c).

## v1.2.8

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.8).

Tagged commit “Honeycomb Menu NG v1.2.8” [d7c9f3b7c1b3](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/d7c9f3b7c1b3d84d84982f8f03556ce54417cd82).

## v1.2.7

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.7).

Tagged commit “Honeycomb Menu NG v1.2.7” [56aa0bfee4ec](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/56aa0bfee4ec83eb09fbaec7a85e7045b390eae7).

## v1.2.6

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.6).

Tagged commit “Honeycomb Menu NG v1.2.6” [cea00e92a724](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/cea00e92a724f5e0c8cf1da36c63d1deb51b76d0).

## v1.2.5

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.5).

Tagged commit “Honeycomb Menu NG v1.2.5” [59f35dbf7fed](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/59f35dbf7fed68620808c6df5f571c292d863f5f).

## v1.2.4

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.4).

Tagged commit “Honeycomb Menu NG v1.2.4” [176833289608](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/176833289608806a97ac05799c98a55270ffe785).

## v1.2.3

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.3).

Tagged commit “Honeycomb Menu NG v1.2.3” [531ba4ab3e61](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/531ba4ab3e6137bd347e4b9f5ef11e5c2236552f).

## v1.2.2

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.2).

Tagged commit “Honeycomb Menu NG v1.2.2” [c24bbf9ee634](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/c24bbf9ee6346336a69fc77190afd09fbe06e193).

## v1.2.1

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.1).

Tagged commit “Honeycomb Menu NG v1.2.1” [c28e5df998af](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/c28e5df998affa6a24a71873e7b356057cafabc9).

## v1.2.0

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.2.0).

Tagged commit “Honeycomb Menu NG v1.2.0” [d58adf63fa88](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/d58adf63fa88d86678c43593a5a41586bbc73eb4).

## v1.1.5

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.1.5).

Tagged commit “Honeycomb Menu NG v1.1.5” [fd367966495e](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/fd367966495e80d1008473f2c2828485cb954010).

## v1.1.4_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.1.4_b).

Tagged commit “Honeycomb Menu NG v1.1.4” [afa2a2271ed8](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/afa2a2271ed877d53037c0a87e1c2430cbf223f8).

## v1.1.3_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.1.3_b).

Tagged commit “Honeycomb Menu NG v1.1.3” [98edf6e60d9f](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/98edf6e60d9ff220a66b6226f1f2046c489de379).

## v1.1.2_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.1.2_b).

Tagged commit “Honeycomb Menu NG v1.1.2” [807426871a12](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/807426871a12029b435e4c78b1c11666c0355ae5).

## v1.1.1_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.1.1_b).

Tagged commit “Honeycomb Menu NG v1.1.1” [7d95f9717189](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/7d95f97171899fff12003d796619cd342bc57ac5).

## v1.1.0_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.1.0_b).

Tagged commit “Honeycomb Menu NG v1.1.0” [9ca3c26055c6](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/9ca3c26055c6f113be3c71c23da92365dd302e23).

## v1.0.14_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.14_b).

Tagged commit “Honeycomb Menu NG v1.0.14” [0c4546bfe049](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/0c4546bfe04945c76c10d849154b2431f2a182ac).

## v1.0.13_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.13_b).

Tagged commit “Honeycomb Menu NG v1.0.13” [c1d65855f4f0](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/c1d65855f4f020ea2568317ab7284fa945b576f5).

## v1.0.12_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.12_b).

Tagged commit “Honeycomb Menu NG v1.0.12” [e6f1b0ade907](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/e6f1b0ade9073937bf519a8e7256944799e32f5c).

## v1.0.11_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.11_b).

Tagged commit “Honeycomb Menu NG v1.0.11” [1b07cc2d2f94](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/1b07cc2d2f942beb35503876d09148ba754c4c92).

## v1.0.10_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.10_b).

Tagged commit “Honeycomb Menu NG v1.0.10” [0720dc49bf90](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/0720dc49bf9014528e6730faa430f56b2331a984).

## v1.0.8_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.8_b).

Tagged commit “Honeycomb Menu NG v1.0.8” [c01a780e54e7](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/c01a780e54e738ac0f863085cdc322f131f044ab).

## v1.0.7_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.7_b).

Tagged commit “Honeycomb Menu NG v1.0.7” [00e850425139](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/00e85042513926098b6e91582cfa4def2507f679).

## v1.0.6_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.6_b).

Tagged commit “Honeycomb Menu NG v1.0.6” [d75079cfd8f5](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/d75079cfd8f5e0723a96ee546a62c62b12b55634).

## v1.0.5_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.5_b).

Tagged commit “Honeycomb Menu NG v1.0.5” [b076f1d1c22c](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/b076f1d1c22c58f56b8e3b1a0b7fc054df8c0575).

## v1.0.4_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.4_b).

Tagged commit “Honeycomb Menu NG v1.0.4” [42969aed7cb1](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/42969aed7cb130c2cca585dd607ef9f38449e1f4).

## v1.0.3_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.3_b).

Tagged commit “Honeycomb Menu NG v1.0.3” [7e3dcc83f911](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/7e3dcc83f911feb311c9779dfb45a1d04b5565fe).

## v1.0.2_b

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.2_b).

Tagged commit “Honeycomb Menu NG v1.0.2” [fe4d23911b7e](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/fe4d23911b7ebb07c4cf6cbd771b6cc51b6a2847).

## v1.0.1_B

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.1_B).

Tagged commit “Honeycomb Menu NG v1.0.1” [af48b5f9ca96](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/af48b5f9ca96f27f8f2267d0a2a5003abd94b2cc).

## v1.0.0

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.0).

Tagged commit “Merge pull request #19 from NicolaiTandrup/feature/v1.0.0-persistent-center” [c3a3ad33f2c2](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/c3a3ad33f2c2d21289fcf5b27e982b0f2e7d9308).

## v1.0.0_beta_1

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v1.0.0_beta_1).

Tagged commit “Merge pull request #20 from NicolaiTandrup/feature/v1.0.0-persistent-center” [e07b4872000c](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/e07b4872000ccd302c2d10308e82b6bf67ac0699).

## Honeycomb Menu NG v0.9.1

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.9.1) · Published 2026-10-02 (UTC).

## Honeycomb Menu NG v0.9.0

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.9.0) · Published 2026-10-02 (UTC).

Nested menu placement

## Honeycomb Menu NG v0.8.3

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.8.3) · Published 2026-09-30 (UTC).

New nested menu options

## Honeycomb Menu NG v0.7.6

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.7.6) · Published 2026-09-30 (UTC).

Preserve dynamic button-card action templates

## Honeycomb Menu NG v0.7.5

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.7.5) · Published 2026-09-30 (UTC).

dynamic controls

## Honeycomb Menu NG v0.7.4

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.7.4) · Published 2026-09-30 (UTC).

Live control A

## v.0.7.4

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v.0.7.4).

Tagged commit “Merge pull request #13 from NicolaiTandrup/feature/v0.7.3-live-state” [4d2c40bda754](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/4d2c40bda754e2e167d01e5c8e4347f0655c6424).

## Honeycomb Menu NG v0.7.3

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.7.3) · Published 2026-09-30 (UTC).

Live State

## Honeycomb Menu NG v0.7.2

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.7.2) · Published 2026-09-30 (UTC).

Add drag-select deadzone for press_action

## Honeycomb Menu NG v0.7.1

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.7.1) · Published 2026-09-24 (UTC).

New logo

## v0.7.0

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.7.0) · Published 2026-09-13 (UTC).

Dynamic control

Thermostat controls
EV controls
Sonos/media controls

## Honeycomb Menu NG v0.6.2

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.6.2) · Published 2026-09-11 (UTC).

Fix drag-select release action

## Honeycomb Menu NG v0.6.1

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.6.1) · Published 2026-09-11 (UTC).

Menu changes

## Honeycomb Menu NG v0.6.0

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.6.0) · Published 2026-09-11 (UTC).

Add interaction and nested navigation support

## Honeycomb Menu NG v0.5.0

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.5.0) · Published 2026-09-11 (UTC).

Add paired symmetric animation mode

## Honeycomb Menu NG v0.4.2

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.4.2) · Published 2026-09-11 (UTC).

Fix:
- Increase default center button contrast
- Keep center_brightness configurable
- Preserve explicit center button background overrides

## Honeycomb Menu NG v0.4.1

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.4.1) · Published 2026-09-11 (UTC).

minor fixes

## Honeycomb Menu NG v0.4.0

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.4.0) · Published 2026-09-09 (UTC).

### What's Changed
* Feature/v0.4 soft hard center style by @NicolaiTandrup in https://github.com/NicolaiTandrup/honeycomb-menu-ng/pull/4


**Full Changelog**: https://github.com/NicolaiTandrup/honeycomb-menu-ng/compare/v0.3.0...v0.4.0

## v.0.4.0

[Git tag](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/tree/v.0.4.0).

Tagged commit “Merge pull request #4 from NicolaiTandrup/feature/v0.4-soft-hard-center-style” [facc5fb45073](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/commit/facc5fb4507348c87548c2249f4454e9ed151593).

## Honeycomb Menu NG v0.3.0

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.3.0) · Published 2026-09-09 (UTC).

New:
- Center button support
- Automatic center button based on the Honeycomb entity
- Optional center_button overrides
- Expanded layout from 12 to 18 ring slots
- Inner ring: slots 1-6
- Outer ring: slots 7-18
- Dynamic ring activation based on button count
- empty_slots: visible|hidden support
- Backwards-compatible position support
- Existing nested Honeycomb menus remain supported

## Honeycomb Menu NG v0.2.1

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.2.1) · Published 2026-09-08 (UTC).

Fix:
- Include rebuilt honeycomb-menu-ng.js in release
- 12-slot layout
- empty_slots support
- automatic outer ring activation

## Honeycomb Menu NG v0.2.0

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.2.0) · Published 2026-09-08 (UTC).

Flexible 1–12 button layouts

## Honeycomb Menu NG v0.1.0

[GitHub release](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v0.1.0) · Published 2026-09-08 (UTC).

Initial Honeycomb Menu NG foundation.

Changes:
- Separate NG identity and build output
- Global button_defaults support
- Automated GitHub Actions build
- HACS-ready repository structure
