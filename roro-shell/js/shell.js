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
      applyTheme(themes.default || Object.keys(themes)[0]);
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
    dock.textContent = `Dock: theme=${name}`;
    localStorage.setItem('roos.theme', name);
  }

  themeToggle.addEventListener('click', ()=>{
    const themes = window.RoOSThemes || {};
    const names = Object.keys(themes).filter(n=>n!=='default');
    if(names.length===0) return;
    const current = localStorage.getItem('roos.theme') || themes.default || names[0];
    const idx = names.indexOf(current);
    const next = names[(idx+1)%names.length];
    applyTheme(next);
  });

  document.querySelectorAll('.icon').forEach(el=>{
    el.addEventListener('click', ()=>{
      const app = el.dataset.app;
      dock.textContent = `Dock: opened ${app}`;
    });
  });

  loadThemes();
})();
