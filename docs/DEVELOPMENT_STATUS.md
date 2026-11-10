# Published v2.0.1 slot 0 hotfix

[v2.0.1 stable](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/releases/tag/v2.0.1)
is public and latest at master `e3495665a7e3486c4c447e00f1b852c1a70679b5`.
The immutable beta is `v2.0.1-beta.1` at
`1e2d17dfeecb38f29619e6da7ec6028eabe94d1c`. The stable runtime passes
the source-tree and byte-equivalence guard against that beta.

The owner authorized stable after successful beta validation. The affected Home
Assistant floorplan was tested with both the Marketplace-installed beta and stable.
Hold expanded the Hub, then hold on slot 0 opened the Light controls. Back returned
through the Hub to the floorplan. The lone-visible-primary path, short-press mock
service call, touch, keyboard, preview guard and dynamic visibility were verified
with synthetic entities at desktop, tablet and mobile sizes. Local build, HACS,
brand and focused Node/browser checks passed. Local full Node checks hit Windows
shell, line-ending and symlink limitations. The complete GitHub suite passed.

The public stable bundle and the Home Assistant-served file both have SHA-256
`e6d3762e0c57886d4c44f8fd17dde445740360da0cb78e4cbe247077ce7f26d0`
and size 375679 bytes. All three public assets, tag and provenance were verified.
The publisher verified historical release retention; cleanup was skipped.
Home Assistant is on stable with prerelease tracking off.

- [Merged PR #180](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/pull/180)
- [Closed approval record #179](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/issues/179)
- [Exact-master Build CI](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42902416174)
- [Verification-only workflow](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42909406674)
- [Publication and retention report](https://github.com/Jefferies-Tube-Solutions/jefferies-navigation/actions/runs/42909533711)

Handoff branch: `docs/v2.0.1-published-handoff`. This hotfix is complete.
There is no remaining release action for it. Reconstruct current master and new
owner requests before starting unrelated work.

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
