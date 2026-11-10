# Slot 0 controls in collapsible Navigation Hubs

Branch: `fix/expanded-primary-control`. Candidate: `v2.0.1-beta.1`, based on
`6dba21e` after the v2.0.0 stable release. The v2.0.0 bundle reproduced the
expanded slot 0 failure. The beta passed the new browser cases at 1800, 768 and
390 CSS pixels, including keyboard, touch and Back. Its short press in the
collapsed Hub performed the sole expected mock service call in the lone-item test.
Local build and HACS package validation passed. The full local Node suite hit
Windows shell, line-ending and symlink limitations. GitHub CI must validate the
exact publication commit before the beta is published.

Next, install and verify the public beta on Home Assistant, record acceptance,
then prepare the v2.0.1 manifest and run the guarded stable release procedure.

---

# Shared JTS validation and automatic code review

Branch: `governance/shared-jts-check`. Base: `c6268ba`.
Checkpoint: **Use the shared JTS Brand System action**.

The existing required brand job uses the Navigation profile at
`636d896ab6e7d0caecf65955485c4c6aa49c9393`. Local verification covered the
current v2 checkout, a legacy v1.10.0 checkout with the JTS policy reference
required by the governance baseline, and rejection of a changed v2 validator.
Codex is configured for all pull requests and new commits.

---

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
