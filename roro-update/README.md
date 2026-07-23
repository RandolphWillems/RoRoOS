# roro-update

This folder contains update-related files for RoRoOS.

Structure:
- `manifests/` — JSON manifests describing available updates and metadata (version, checksum, URL).
- `scripts/` — helper scripts for applying updates or preparing update packages. These are examples; the actual updater should validate signatures and checksums.
- `logs/` — local logs produced by update runs (kept out of distributed manifests).

Security notes:
- Always sign update manifests and verify signatures before applying updates.
- Never run unreviewed update scripts as root without verification.

Example manifest: `roro-update/manifests/update-manifest.json`

