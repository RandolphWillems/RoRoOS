# FAQ

Q: How do I run the prototype locally?
A: From the repo root run:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/roro-shell/
```

Q: Where do I put icons?
A: Add icon files to `roro-icons/assets/` and commit.

Q: How do I add wallpapers?
A: Drop images into `roro-theme/wallpapers/` and optionally generate thumbnails into `roro-theme/thumbnails/`.

Q: How are themes configured?
A: `roro-shell/themes.json` defines preset themes. The UI reads and applies them.

Q: How can I contribute?
A: Fork the repo, create a feature branch, open a PR with a clear description and tests or screenshots.
