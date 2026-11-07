# Jefferies Navigation branding

Jefferies Navigation (JTS-N) uses its approved full product lockup in the public
README and the round Navigation compass in Home Assistant. The public repository
slug is `Jefferies-Tube-Solutions/jefferies-navigation`. Historical release
references and the original author's GPL attribution retain their original
identity. Home Assistant Marketplace displays **JTS - Jefferies Navigation**
from the package manifest. The product artwork is shown in the README; the
Dashboard listing uses Marketplace's category icon.

Follow JTS Brand System v1.1.0 for theme variants, documentation, Home Assistant
applicability and release status. The owner approved a product-specific README
override for this repository. The centered header uses the full Navigation
lockup on its approved Deep Space background below the release-status badge.
The same image is readable in both themes. GitHub-only theme fragments render
as duplicate images in Home Assistant Marketplace. The
publisher-plus-product layout remains the generic JTS policy.
[Canonical brand policy](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/blob/7826deae0ed3d681a902c9e85af7959408fe00d4/docs/README_LAYOUT.md).

| Use | Source | Preview |
| --- | --- | --- |
| Transparent lockup, dark surfaces | [Full Navigation lockup, white text](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/blob/7826deae0ed3d681a902c9e85af7959408fe00d4/assets/products/jefferies-navigation/v1/JTS_Jefferies_Navigation_Full.png) | <img src="../assets/brand/navigation-lockup-white.png" width="160" alt="Full Navigation lockup with white text"> |
| Transparent lockup, light surfaces | [Full Navigation lockup, Deep Space text](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/blob/7826deae0ed3d681a902c9e85af7959408fe00d4/assets/products/jefferies-navigation/v1/JTS_Jefferies_Navigation_Full_Transparent_Deep_Space.png) | <img src="../assets/brand/navigation-lockup-deep-space.png" width="160" alt="Full Navigation lockup with Deep Space text"> |
| README, GitHub and Marketplace | [Full Navigation lockup on Deep Space](https://github.com/Jefferies-Tube-Solutions/jts-brand-system/blob/7826deae0ed3d681a902c9e85af7959408fe00d4/assets/products/jefferies-navigation/v1/JTS_Jefferies_Navigation_Full_Deep_Space_Background.png) | <img src="../assets/brand/navigation-lockup-background.png" width="160" alt="Full Navigation lockup on Deep Space"> |
| Runtime compass, inside a Home Assistant cell | Draft 02 Blender dial collection | <img src="../assets/navigation-compass.png" width="100" alt="Round compass dial with cyan bezel and amber needle"> |

The README's Deep Space PNG is byte-identical to the approved original
(SHA-256 `ecb31199fd5cb1d6972da0fc2aacdf379361c3e853706eb8a65957b38979eb89`). The 4337 × 1100 transparent variants preserve the exact decoded RGBA pixels and color data
of the approved originals. Export comments and metadata with local authoring paths
were removed. The hashes below identify the original and public files.

- White text source `94535deee177a3626ac2d66ad79757e481cbb85a72651b48eecb04aac42f6440`.
  Public `d6ecf4c931250da855f4b051df9003a5c0fe6a975631494d6d67ec1fc9857f08`.
- Deep Space text source `7f31e8f300a5e581813e22435c1dbc2284ad6edd3a2671e11accb9ee8ae71495`.
  Public `f19e85d9886b44e57a634b7d5eae9cec96f9e856bc078eef799f28086747e451`.

The runtime compass was rendered from
`Jefferies Navigation - Blender draft 02.blend`
(SHA-256 `0dc41d483c4fcd15ba5287be2f44e93f01356770188b219749ff4b83f6c5d3b2`)
in Blender 5.2.3 LTS. Render the `NAVIGATION / Editable compass` collection with
the original camera and lights, hiding all other geometry. Set the camera to
73 mm and render a transparent, 192×192 RGBA PNG. The Home Assistant cell supplies
the outer hexagon. The product lockups retain their approved frame in the README.

Run `npm run check:brand` after any artwork or identity edit. The check pins
the current public PNG hashes and verifies package, HACS, release, runtime,
card names and the exact single-logo README header. The core suite runs this
check in CI and release verification. When artwork or identity changes with
owner approval, record the exact source and approval, update the hashes and
verify both GitHub themes and the Home Assistant compass at supported sizes.
