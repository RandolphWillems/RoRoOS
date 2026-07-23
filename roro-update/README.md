# roro-update

This folder contains update-related files for RoRoOS.

Structure:
- `manifests/` — JSON manifests describing available updates and metadata (version, checksum, package path URL).
- `packages/` — packaged update bundles produced by the package generator.
- `scripts/` — helper scripts for applying updates or preparing update packages.
- `logs/` — local logs produced by update runs (kept out of distributed manifests).

Security notes:
- Always sign update manifests and verify signatures before applying updates.
- Never run unreviewed update scripts as root without verification.

Use the package generator to create a new update package and manifest:

```bash
cd roro-update
python3 scripts/package_update.py ../roro-shell --version 0.1.0 --release-notes "Initial prototype update"
```

Then apply the update with:

```bash
python3 scripts/updater.py manifests/update-manifest.json
```

Example manifest: `roro-update/manifests/update-manifest.json`

