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
