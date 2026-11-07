# Jefferies Navigation v2.0.0-beta.3 candidate

The README uses a single approved Deep Space lockup to avoid duplicate logos in
Marketplace. The display name and runtime behavior from beta.2 carry forward.
The release candidate remains unpublished.

The rewrite is based on v1.10.0 stable, master commit
`25291186b07bfee81b8877fe731e00a417d56c12` (PR #169). The preceding promotion
and owner acceptance are recorded in [the v1.10.0 release checklist](V1_10_STABLE_RELEASE.md)
and issue #163. Previous release history remains available at the original tags.

Feature branch: `feature/jefferies-navigation-v2`. The public names, resource
and YAML changes are listed in [V2_MIGRATION.md](V2_MIGRATION.md). The compass
is a round dial rendered from the approved Draft 02 scene. The shared cell draws
the outer hexagon. The [branding gate](BRANDING.md) pins the runtime dial, public
publisher artwork and product identity. The shared renderer, positioning
engine, action registry, module boundaries and XY Pad teardown stay in place.

Run `npm ci`, `npm test`, `NODE_OPTIONS=--openssl-legacy-provider npm run build`,
`node scripts/check-beta.js` and `node scripts/check-hacs-package.js`. CI runs
the Chromium and documentation regression matrix. See the feature branch
checks for results tied to its commit.

Use the separate PAHA02-DEV dashboard for real Home Assistant verification.
Publication uses the existing guarded manual beta workflow on the exact green
feature-branch SHA, with a verification-only dispatch before publication. Keep
release retention disabled and keep v1 stable as the default branch.
