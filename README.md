# RoRoOS

This repository contains a minimal HTML/CSS/JS prototype for a customizable shell UI (RoOS).

Files:
- index.html — entry page
- css/style.css — styling and variables
- js/shell.js — theme loader and simple interactions
- themes.json — theme definitions

Run locally (simple static server):

```bash
# from the project root
python3 -m http.server 8000
# then open http://localhost:8000 in your browser
```

Push to your GitHub repository (replace the remote if needed):

```bash
git init
git add .
git commit -m "Add RoOS starter prototype"
git remote add origin git@github.com:<your-username>/RoRoOS.git
git branch -M main
git push -u origin main
```

Next ideas:
- Expand the JSON schema for apps, panels and widgets
- Add a build/dev workflow (Vite/parcel)
- Persist layout and hotkeys
- Add packaging for Electron or Tauri for a desktop experience
