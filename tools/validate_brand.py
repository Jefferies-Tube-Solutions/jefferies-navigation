"""Check the repository's current JTS brand adoption baseline."""

import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
AGENTS = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
errors = []
if "## JTS Brand System" not in AGENTS or "jts-brand-system" not in AGENTS:
    errors.append("AGENTS.md must reference the JTS Brand System policy.")

package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
if package["name"] == "jefferies-navigation":
    subprocess.run(["node", "scripts/check-brand.js"], cwd=ROOT, check=True)
else:
    from_logo = ROOT / "assets/honeycomb-menu-ng-logo.png"
    image = from_logo.read_bytes()
    git_blob = f"blob {len(image)}\0".encode() + image
    if hashlib.sha1(git_blob).hexdigest() != "b86d9f007db8b2c7460085fbb7fa4b3e2213eaf7":
        errors.append("Legacy artwork changed without a reviewed JTS migration.")
    if not README.startswith('<p align="right">') or not re.search(
        r"github/v/release/[^?]+\?label=stable&amp;color=2ea44f", README
    ):
        errors.append("README must keep its stable release badge.")
    if 'src="assets/honeycomb-menu-ng-logo.png"' not in README or "# Honeycomb Menu NG for Home Assistant" not in README:
        errors.append("Preserve the published Honeycomb Menu NG identity until migration.")
    if "Sian Croser" not in README or "[GPLv3](LICENSE)" not in README:
        errors.append("Preserve upstream attribution and licensing.")

if errors:
    raise SystemExit("\n".join(errors))
print("JTS adoption baseline passed.")
