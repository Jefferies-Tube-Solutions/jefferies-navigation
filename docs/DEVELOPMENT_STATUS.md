# Jefferies Navigation v2.0.0 stable promotion

The owner authorized stable after installing beta.3 in Home Assistant. The
[approval record](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/issues/171)
tracks this promotion. The manifest pins the public beta.3 tag, source tree and
bundle checksum. The stable candidate retains the tested runtime, Marketplace
display name and single approved Deep Space product logo.

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
`node scripts/check-release.js --stable` and `node scripts/check-hacs-package.js`.
Follow the [stable publication procedure](RELEASING.md) for exact-head CI,
master verification and guarded publication. Keep release retention disabled.
Check the logo in Home Assistant Marketplace once it refreshes the release.
