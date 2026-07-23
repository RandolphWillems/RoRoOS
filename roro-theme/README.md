# roro-theme

This folder contains wallpapers for the RoRoOS appearance settings.

Structure:
- `wallpapers/` - full-resolution wallpaper image files (jpg/png/webp)
- `thumbnails/` - generated thumbnail images for preview in the appearance picker

Naming and formats:
- Preferred formats: `jpg`, `png`, `webp`. SVGs are allowed but may not preview well.
- Recommended sizes: 1920x1080 (FHD) and 3840x2160 (4K) for high-res displays.
- Filenames: use `kebab-case` (e.g. `ocean-dusk-1920x1080.jpg`) and include a short description.

How to add wallpapers locally:

```bash
# copy files into the folder
cp ~/Downloads/my-wallpaper.jpg roro-theme/wallpapers/
# add, commit and push
git add roro-theme/wallpapers/my-wallpaper.jpg
git commit -m "Add wallpaper: my-wallpaper"
git push
```

Optional: generate thumbnails (requires ImageMagick):

```bash
# from repo root
mogrify -path roro-theme/thumbnails -resize 320x180 roro-theme/wallpapers/*.{jpg,png,webp}
```

