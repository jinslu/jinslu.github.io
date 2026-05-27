// ============================================================
//  Integrated & Meta Photonics Lab - main.js
//  Language switcher + Nav active state
// ============================================================

(function () {
  'use strict';

  /* ---- Language Switch ---- */
  const root = document.documentElement;
  const btnEn  = document.getElementById('lang-btn-en');
  const btnCn  = document.getElementById('lang-btn-cn');
  const STORAGE_KEY = 'imp-lab-session-lang';

  let currentLang = sessionStorage.getItem(STORAGE_KEY) || 'en';

  function applyLang(lang) {
    currentLang = lang;
    root.setAttribute('data-lang', lang);
    root.setAttribute('lang', lang === 'cn' ? 'zh-CN' : 'en');

    // Update button states
    if (btnEn) {
      if (lang === 'en') {
        btnEn.classList.add('active');
      } else {
        btnEn.classList.remove('active');
      }
    }
    if (btnCn) {
      if (lang === 'cn') {
        btnCn.classList.add('active');
      } else {
        btnCn.classList.remove('active');
      }
    }

    sessionStorage.setItem(STORAGE_KEY, lang);
  }

  if (btnEn) {
    btnEn.addEventListener('click', function () {
      applyLang('en');
    });
  }

  if (btnCn) {
    btnCn.addEventListener('click', function () {
      applyLang('cn');
    });
  }

  applyLang(currentLang);

  /* ---- Hamburger Menu ---- */
  const hamburger = document.getElementById('nav-hamburger');
  const navLinks  = document.getElementById('nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', function () {
      navLinks.classList.toggle('open');
      hamburger.classList.toggle('active');
    });
    navLinks.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        navLinks.classList.remove('open');
        hamburger.classList.remove('active');
      });
    });
    document.addEventListener('click', function (e) {
      if (!document.getElementById('site-nav').contains(e.target)) {
        navLinks.classList.remove('open');
        hamburger.classList.remove('active');
      }
    });
  }

  /* ---- Nav Active State ---- */
  const links = document.querySelectorAll('.nav-inner a');
  const path  = window.location.pathname.replace(/\/$/, '') || '/';

  links.forEach(function (a) {
    const href = a.getAttribute('href').replace(/\/$/, '') || '/';
    if (path === href || (href !== '/' && path.startsWith(href))) {
      a.classList.add('active');
    }
  });
})();

/* ---- Publications Year Filter ---- */
(function () {
  var container = document.getElementById('pub-year-filter');
  if (!container) return;

  // Collect unique years from pub-items and conf-items with data-year
  var seen = {};
  var years = [];
  document.querySelectorAll('.pub-item[data-year], .conf-item[data-year]').forEach(function (el) {
    var y = el.dataset.year;
    if (y && !seen[y]) { seen[y] = true; years.push(y); }
  });
  years.sort(function (a, b) { return parseInt(b) - parseInt(a); });

  // Build "All" button
  var allBtn = document.createElement('button');
  allBtn.className = 'pyf-btn active';
  allBtn.dataset.year = 'all';
  allBtn.innerHTML = '<span class="cn-text">全部</span><span class="en-text">All</span>';
  container.appendChild(allBtn);

  // Build year buttons
  years.forEach(function (y) {
    var btn = document.createElement('button');
    btn.className = 'pyf-btn';
    btn.dataset.year = y;
    btn.textContent = y;
    container.appendChild(btn);
  });

  function applyFilter(year) {
    // Update active button
    container.querySelectorAll('.pyf-btn').forEach(function (b) {
      b.classList.toggle('active', b.dataset.year === year);
    });

    // Filter journal pub-items
    document.querySelectorAll('.pub-item[data-year]').forEach(function (el) {
      el.style.display = (year === 'all' || el.dataset.year === year) ? '' : 'none';
    });

    // Filter year labels
    document.querySelectorAll('.pub-year-label[data-year]').forEach(function (el) {
      el.style.display = (year === 'all' || el.dataset.year === year) ? '' : 'none';
    });

    // Filter conference items
    document.querySelectorAll('.conf-item[data-year]').forEach(function (el) {
      el.style.display = (year === 'all' || el.dataset.year === year) ? '' : 'none';
    });

    // Hide selected-pubs box when a specific year is active (it has no year filter)
    var selBox = document.querySelector('.selected-pubs-box');
    if (selBox) selBox.style.display = (year === 'all') ? '' : 'none';

    // Hide conference section header if no visible conf items
    var confItems = document.querySelectorAll('.conf-item[data-year]');
    var anyConf = false;
    confItems.forEach(function (el) { if (el.style.display !== 'none') anyConf = true; });
    document.querySelectorAll('.pub-section-conf').forEach(function (el) {
      el.style.display = anyConf ? '' : 'none';
    });
  }

  container.addEventListener('click', function (e) {
    var btn = e.target.closest('.pyf-btn');
    if (btn) applyFilter(btn.dataset.year);
  });
})();

/* ---- Research Sub-Nav Tabs ---- */
(function () {
  var tabs = document.querySelectorAll('.rst-btn');
  if (!tabs.length) return;

  // IDs that live inside the Research Directions panel
  var directionIds = ['light-matter', 'optical-tweezers', 'integrated-chips', 'metaphotonics'];

  function activateTab(panelId) {
    tabs.forEach(function (t) {
      t.classList.toggle('active', t.dataset.panel === panelId);
    });
    document.querySelectorAll('.rst-panel').forEach(function (p) {
      p.classList.toggle('active', p.id === 'rp-' + panelId);
    });
  }

  // Exposed globally so overview cards can call it
  window.showResearchTab = function (panelId, anchorId) {
    activateTab(panelId);
    history.replaceState(null, '', window.location.pathname + (anchorId ? '#' + anchorId : ''));
    if (anchorId) {
      setTimeout(function () {
        var el = document.getElementById(anchorId);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 60);
    }
  };

  tabs.forEach(function (t) {
    t.addEventListener('click', function () {
      activateTab(t.dataset.panel);
      history.replaceState(null, '', window.location.pathname);
    });
  });

  // On load: honour URL hash
  var hash = window.location.hash.replace('#', '');
  if (hash && directionIds.indexOf(hash) !== -1) {
    activateTab('directions');
    setTimeout(function () {
      var el = document.getElementById(hash);
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
  } else {
    activateTab('overview');
  }
})();

/* ---- Hero Slideshow ---- */
(function () {
  const slides = document.querySelectorAll('.hs-slide');
  const dots   = document.querySelectorAll('.hs-dots button');
  if (!slides.length) return;
  let cur = 0;
  function goTo(n) {
    slides[cur].classList.remove('active');
    if (dots[cur]) dots[cur].classList.remove('active');
    cur = ((n % slides.length) + slides.length) % slides.length;
    slides[cur].classList.add('active');
    if (dots[cur]) dots[cur].classList.add('active');
  }
  dots.forEach(function (d, i) { d.addEventListener('click', function () { goTo(i); }); });
  setInterval(function () { goTo(cur + 1); }, 4800);
})();
