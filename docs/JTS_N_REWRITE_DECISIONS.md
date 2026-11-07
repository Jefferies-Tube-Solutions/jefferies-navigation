# Jefferies Navigation v2 rewrite decisions

## 2026-11-06

| Decision | Reason | Consequence |
| --- | --- | --- |
| Use Sol Medium for implementation and keep deployment and release verification separate. | This is a broad cross-file refactor with established behavior to preserve. | One implementation owner; deployment and publication use independent verification. |
| Start from the current master commit `25291186b07bfee81b8877fe731e00a417d56c12`. | The stable HC behavior is the comparison baseline. | Prior releases and unrelated historical work are preserved. |
| Rename product-owned namespaces, element names, modules, assets and configuration keys as required for JTS-N. Preserve the shared rendering and control behavior. | The owner explicitly waived backward compatibility while requiring feature parity. | Existing HC configurations will need new names when manually moved to JTS-N. Attribution and historical records remain. |
| Use the approved Draft 02 compass from the JTS Brand System. | The icon already has owner approval and a registered source. | Preserve compass provenance and the existing control's behavior and accessibility. |
| Use a separate test dashboard and resource on development HA. | This allows side-by-side checks and an independent rollback path. | Existing HC dashboard is retained as a comparison baseline. Tests that could actuate real devices use mocks. |
| Publish only from the guarded beta workflow after exact-candidate CI and development-HA acceptance. | This is the agreed publication gate. | No stable promotion or release until the exact tested candidate passes. |
| Keep this running log on its own GitHub branch. | The owner requested an independent, recoverable record. | Decisions are available independently of the rewrite worktree or feature branch. |

## Current checkpoint

Baseline located. Development host and file-share access verified. Rewrite and acceptance pending; no beta has been published.

### Namespace and packaging

- The dashboard card types are `custom:jts-n-hub` and `custom:jts-n-control`. The Info Cube is the `jts-n-info-cube` overlay, opened with the `jts-n-info` action. Product-owned popup configuration uses `jts_n_menu`; shared domain terms such as Light, Sonos and Climate remain recognizable.
- Use `jefferies-navigation.js` as the distribution bundle and `window.jefferiesNavigation` for build diagnostics. Keep the GitHub repository and its release history under the current slug for this beta. Changing the repository itself is a separate catalog and distribution decision.
- Use SemVer `v2.0.0-beta.1` for the requested v2.0 beta-1, as required by the guarded publisher.
- Register resources and create the separate dashboard through Home Assistant's supported interface. Do not edit live `.storage` files directly. File access to the dev host and an existing authenticated browser view were verified. Browser input later became unavailable, so dashboard creation is still pending.
- Development installs use `/local/jts-n-dev/jefferies-navigation.js` and an immutable, content-hashed runtime. The legacy dashboard resource is kept separate.

### Verification checkpoint

- The rebrand uses the existing shared renderer, action dispatch and control modules. The Compass replaces the Bee as the visible brand control and retains version inspection and collapse/back semantics.
- The initial v2 build passed local HACS, license, checksum and eight legacy coexistence checks. A Windows run passed 457 Node tests; seven local shell/platform checks require the Linux CI run. Historical browser fixture mismatches are being repaired separately from the runtime.
- The deployment check compares the running diagnostics with the installed manifest and exact commit. Device writes are exercised using mocks, with a read-only dashboard for real Home Assistant smoke testing.

### Candidate handoff

- [Draft PR #170](https://github.com/Jefferies-Tube-Solutions/honeycomb-menu-ng/pull/170) records the v2 feature branch. Candidate commit `e1747ddf0fa6645565c64d2815d53732a66517ec` has the same Git tree as the local candidate.
- The production bundle SHA-256 is `c368a81f5a154e6accf1494d4fb3f7bd0cb7c5b73879d990ef4ed46dcd8f3a0a`. Historical test-fixture fixes do not change the bundle.
- The repository remains under the old slug while the dashboard product and release asset use Jefferies Navigation. The draft PR starts CI while keeping the stable branch intact.

### Development deployment and release hold

- Installed exact candidate `e1747ddf0fa6645565c64d2815d53732a66517ec` on the development Home Assistant under its separate static resource folder. The server serves version `2.0.0-beta.1-dev+e1747ddf0fa6`. Runtime SHA-256 is `0691711888d7ed70104661a49b7c5536435062f61d974490a00a32aac6499126`.
- Downloaded the loader and runtime from the development host and verified both manifest hashes. Ran those exact bytes in a synthetic browser fixture at 1280×820 and 390×844. Both passed custom element registration, Compass version inspection and Info Cube open/return, with no browser errors or device service calls.
- Do not treat the fixture as a real Home Assistant dashboard acceptance. The authenticated browser view was readable, but browser input was denied. Dashboard resource registration and the dedicated Lovelace test page remain pending. The [read-only test dashboard YAML](fixtures/jts-n-dev-dashboard.yaml) is available on this branch. Keep the existing HC dashboard as a comparison and do not edit Home Assistant internal storage directly.
- To resume in the authenticated development UI, register the JavaScript module `/local/jts-n-dev/jefferies-navigation.js`, create the separate read-only test dashboard, reload, and verify the compass, installed version, Info return and collapse/back behavior. The production beta workflow remains on hold until the acceptance and exact-head CI gates pass.

### Exact-head CI result

- The [pull request build](https://github.com/Jefferies-Tube-Solutions/honeycomb-menu-ng/actions/runs/42300758884) and [push build](https://github.com/Jefferies-Tube-Solutions/honeycomb-menu-ng/actions/runs/42300731558) both finished green for `e1747ddf0fa6645565c64d2815d53732a66517ec`. Both passed the build and workflow-lint jobs, including Ubuntu tests, browser regressions, documentation and reproducibility.
- The beta has not been tagged or released. The remaining gate is acceptance in the authenticated Home Assistant dashboard on the development instance. After acceptance, use `release.yml` on `feature/jefferies-navigation-v2` with the same full SHA and tag `v2.0.0-beta.1`: verify first, then publish. Preserve the stable release and existing retention policy.

### 2026-11-07 dashboard and Compass correction

- Reuse the existing Honeycomb NG Test dashboard at its current URL. This supersedes the separate-dashboard decision. Preserve the layout, entities, actions and other cards. Keep a local backup before saving the converted dashboard. The live dashboard config and identifiers stay out of GitHub.
- Use the round compass dial from approved Draft 02 for the in-card graphic. Keep the approved full hexagonal brand artwork for standalone branding. The card renderer already supplies the hexagonal frame.
- The previous development installation copied and verified static assets. It did not register the resource or migrate the live dashboard. Those steps remain separate acceptance gates.

### Repository identity and future releases

- The desired repository slug is `Jefferies-Tube-Solutions/jefferies-navigation`. This supersedes the earlier choice to retain the old slug for beta. Keep the same repository history and existing release records.
- v2 is a clean cutover. Do not add HC aliases, resource shims, compatibility adapters or fallback bundle filenames. Historical documentation, license notices and existing release records keep their original identity.
- Future candidates must pass an automated branding check through the existing CI and release test entry points. Document the approved artwork source and separate the circular in-card image from the full hexagonal product logo. Record asset hashes and confirm naming/packaging rules.

### Existing dashboard acceptance and release candidate

- Renamed the GitHub repository in place to [jefferies-navigation](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation). PR #170 and repository history were retained. The GitHub About text now uses Jefferies Navigation.
- Registered the JTS-N resource in the Home Assistant UI. Converted the existing test dashboard, including its Hub and standalone Control, at the same URL. It now displays as JTS-N DEV / JTS-N Test. Preserved the floorplan, entity assignments and geometry. A local backup was taken.
- Rendered the round compass directly from the approved Blender compass collection, leaving the enclosing hexagon to the JTS-N card. Verified the new dial in real Home Assistant and activated it to display `v2.0.0 beta 1`. No device service was called.
- Future builds and guarded releases run the JTS branding check through `npm test`. It enforces the package, runtime, HACS and release names, checksums for the approved artwork, and README brand elements.
- Public release notes contain only the owner-requested breaking-change notice. Branch, commit and checksum evidence remains in the release provenance assets. Exact final candidate `d7ecfa61b4be4752379b1f2b761d730d3a055ae3` contains the publisher-only follow-up. Final exact-head CI and publication are pending.

- Installed the final `d7ecfa61b4be4752379b1f2b761d730d3a055ae3` development build on the same server and verified the served commit and file hashes. The exact hosted bytes passed the synthetic desktop and mobile Compass/Info checks. The live browser check was completed on the preceding build, which differs only in the release publisher and its test. The subsequent live reload was blocked when Edge automation again lost input access.
- [Final exact-head CI](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42344710023). The prerelease remains unpublished. When the matching push and PR checks are green, resume the guarded manual workflow with the single-sentence note in `RELEASE_NOTES.md`.

### Public dashboard card names

- Use `custom:navigation-hub` and `custom:navigation-control` for v2. These replace the interim `custom:jts-n-hub` and `custom:jts-n-control` names in the candidate and on the existing test dashboard.
- Keep this a clean cutover. Install a matching build, then save both new card names in Home Assistant before validating and publishing. The previous candidate is superseded even if its CI passes.

- Installed exact candidate `593965172b7a1b6f93afa1af1e3dc298623199b3` and converted the existing dashboard to both new tags. Home Assistant saved both names and displayed the Hub, standalone Control and round Compass after reload. Compass activation displayed `v2.0.0 beta 1`.
- All 49 Markdown/YAML files touched by the card rename matched the prior text after the two substitutions. A separate audit restored earlier shortened runtime, Info, support and stable verification details and linked the complete immutable v1 release history. Exact-candidate docs checks passed for 77 YAML blocks, 222 links/anchors and 22 browser cases.
- The branding gate now requires the two correct public card types in the README as well as the already pinned product identity and artwork. [Exact-candidate CI](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42346378966).

### README lockup

- The owner selected a single full Jefferies Navigation product lockup for this README. Use its white lettering on the dark GitHub theme and Deep Space lettering on the light theme. This is a scoped override of the generic publisher-plus-product README layout.
- Pin both approved v1 images and the theme selectors in the product's branding gate. Keep the circular in-card compass as a separate asset. Retain the version badge and the rest of the README.
- The change supersedes the candidate that was previously in CI. The public beta remains on hold until the updated candidate passes its own checks.

- JTS Brand System PR [#7](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/pull/7) merged after its self-check passed. It records the Navigation product-lockup exception and separate change-history rule.
- The [Captain’s Log](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/blob/feature/jefferies-navigation-v2/docs/CAPTAINS_LOG.md) preserves prior release notes and moved README history, records all 67 public releases and 52 additional tag-only entries, and links the complete commit history. The branding gate requires the log link and the one visible themed product lockup. Exact candidate: `21f8f91ff10aff73c17b2a9b888ab249750f1a48`.

### JTS product README structure

- Use the same top-level flow as JTS Tariff Engine: Mission Directive, System Registry, Commissioning, Operational Protocol, Verification, Fault Isolation and Recovery, Manuals, Operations Log and Approved artwork. Navigation retains its separately approved full product lockup and Captain’s Log link.
- Existing technical prose, YAML, links and examples were retained. The Navigation branding check now enforces section order. Candidate: `63a41d5c255a7ab59116bc6ff1c47017d664d6a6`.

### Stable release authorization

- The owner reported testing v2 on the development Home Assistant instance and authorized stable publication. [Approval issue #171](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/issues/171).
- The earlier CI exposed the stale mobile diagram-width assertion. The corrected diagram and browser test pass locally on both desktop and mobile. Exact beta candidate: `8814ee7481a95bf523b155889d1d4981b93dd445`; its production bundle is unchanged from the owner-tested runtime. [Beta CI](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42357030031).
- Stable candidate `00a8fb66bd2f3aa907105fa1883afd31aaa17b9c` is staged as [draft PR #172](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/pull/172). The stable bundle differs only in the guarded version metadata. The visible release note remains the single approved sentence.
- Next gate: exact beta CI, guarded beta prepare/publish and independent public tag/asset verification. Then exact stable checks, normal merge, exact master CI, and guarded stable prepare/publish. No release has been asserted from a workflow request alone.

- Exact beta push and PR builds passed ([push](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42357025141), [PR](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42357030031)). Exact stable preparation push and PR builds also passed ([push](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42357459927), [PR](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42357464652)).
- The GitHub release workflow was accessible in the signed-in browser, but Windows denied input before the verification dispatch. No beta or stable publication was started. Resume on [Publish manually authorized beta](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/workflows/release.yml), using branch `feature/jefferies-navigation-v2`, exact commit `8814ee7481a95bf523b155889d1d4981b93dd445`, tag `v2.0.0-beta.1` and the one-sentence note. Verify first with publish off; after success run with publish on. Verify the public beta before marking #172 ready and merging it normally. No guarded step was skipped.

- The owner authorized beta publication. Guarded [verification](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42361488888) and [publication](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42361721545) both passed. The [public v2.0.0-beta.1 prerelease](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v2.0.0-beta.1) resolves to `8814ee7481a95bf523b155889d1d4981b93dd445`; the JavaScript asset digest and byte count match the candidate, all three assets are present, and the visible note is the approved sentence. v1.10.0 remains latest stable.

### Marketplace display name follow-up

- Set the Marketplace manifest display name to **JTS - Jefferies Navigation** in [beta.2 candidate PR #173](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/pull/173). Dashboard card identifiers, runtime behavior and approved artwork remain intact. The native Marketplace Dashboard icon has no supported project logo field; the full logo is already in the README.
- The public beta.1 tag has the Navigation README. Home Assistant 2026.11 selects the installed version for documentation, so stale repository information is the likely explanation for the old Honeycomb README. Refresh the repository from its Marketplace page and re-open it.
- Rebuild and test the beta.2 candidate before release. The existing stable draft is pinned to beta.1 and cannot carry the new manifest unchanged through the stable approval gate. Rebase stable preparation on the verified beta.2 if this name is included in v2.0.0 stable.

- The owner authorized beta.2 publication. Guarded [verification](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42365631666) and [publication](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42365776657) passed. [Public v2.0.0-beta.2](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v2.0.0-beta.2) resolves to `93c5d4137d8b0801a56fe5495821bfd2c56ceede`; the JavaScript asset digest and byte count match, all three assets are present, and the public note is unchanged. v1.10.0 remains latest stable.

## 2026-11-07 · Beta 3 Marketplace logo

- Use one approved full Jefferies Navigation logo with a Deep Space background in the shared README. The beta.2 Marketplace screenshot showed both theme-specific images. A single image gives GitHub and Marketplace the same artwork. The [JTS Brand System change](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/pull/8) makes this rule reusable.
- The owner authorized [v2.0.0-beta.3](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v2.0.0-beta.3) as a prerelease for the Marketplace display check. [Regression tests](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42393044510), [guarded verification](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42396689515) and [publication](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42396813438) passed on `a8fb229678a3452f9db273160381ddce17b8a303`. The public release and JavaScript checksum were verified. v1.10.0 remains the latest stable release. The tagged README contains one product logo. The live Marketplace rendering still needs to be checked.

## 2026-11-07 · Stable v2.0.0 from beta 3

- The owner installed beta.3 and authorized a stable release to check how Marketplace renders the single Deep Space product logo. Promote the public beta.3 at `a8fb229678a3452f9db273160381ddce17b8a303` with only executable version metadata changes and preserve the JTS Brand Compliance checks on master. [PR #176](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/pull/176) supersedes the beta.1 preparation in #172. The local stable guard tests, HACS package and brand validation passed.
- Verify [push CI](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42402094109) and [PR CI](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42402102428), merge normally, and wait for full exact-master CI. Run the guarded stable workflow with publication disabled and then enabled. Keep retention disabled. The Marketplace result remains a separate check.

- [v2.0.0 stable](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v2.0.0) is public and marked latest. Exact master `c6268ba6aa580e6f8305f5b0917c6d0e7e27baf7` passed [CI](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42405623879), [verification without publication](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42409077311) and [publication](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42409167598). All three public assets were independently downloaded and verified. The tagged README has one product logo and HACS still uses the approved display name. The retention inventory ran in preview and cleanup was skipped. The live Marketplace view remains unverified.
