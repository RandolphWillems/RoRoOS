(function(){
  const root = document.documentElement;
  const themeToggle = document.getElementById('theme-toggle');
  const dock = document.getElementById('dock');

  // Load themes.json and apply default
  async function loadThemes(){
    try{
      const res = await fetch('themes.json');
      const themes = await res.json();
      window.RoOSThemes = themes;
      // prefer saved user theme if present
      const saved = localStorage.getItem('roos.theme');
      const defaultName = themes.default || Object.keys(themes).find(k=>k!=='default');
      if(saved && themes[saved]){
        applyTheme(saved);
      }else{
        applyTheme(defaultName);
      }
    }catch(e){
      console.warn('Could not load themes.json', e);
    }
  }

  function applyTheme(name){
    const themes = window.RoOSThemes || {};
    const t = themes[name];
    if(!t) return;
    // set CSS variables on :root
    Object.entries(t.vars||{}).forEach(([k,v])=>{
      root.style.setProperty(k, v);
    });
    root.setAttribute('data-theme', t.type || 'dark');
    if(dock) dock.textContent = `Dock: theme=${name}`;
    try{ localStorage.setItem('roos.theme', name); }catch(e){}
  }

  if(themeToggle){
    themeToggle.addEventListener('click', ()=>{
      const themes = window.RoOSThemes || {};
      const names = Object.keys(themes).filter(n=>n!=='default' && typeof themes[n] === 'object');
      if(names.length===0) return;
      const current = localStorage.getItem('roos.theme') || themes.default || names[0];
      const idx = names.indexOf(current);
      const next = names[(idx+1+names.length)%names.length];
      applyTheme(next);
    });
  }

  document.querySelectorAll('.icon').forEach(el=>{
    el.addEventListener('click', ()=>{
      const app = el.dataset.app;
      if(dock) dock.textContent = `Dock: opened ${app}`;
    });
  });

  // Start button / menu handling
  const startButton = document.getElementById('start-button');
  const startMenu = document.getElementById('start-menu');
  if(startButton && startMenu){
    startButton.addEventListener('click', (e)=>{
      e.stopPropagation();
      const open = startMenu.classList.toggle('open');
      startMenu.setAttribute('aria-hidden', String(!open));
    });

    // close when clicking outside
    document.addEventListener('click', (e)=>{
      if(!startMenu.contains(e.target) && !startButton.contains(e.target)){
        if(startMenu.classList.contains('open')){
          startMenu.classList.remove('open');
          startMenu.setAttribute('aria-hidden', 'true');
        }
      }
    });
  }

  loadThemes();
})();
