/* ═══════════════════════════════════════════════════════════════════════
   ASCENT — Excel-UX patch  (v3)
   Load AFTER form.js and single-page.js.

   IMPORTANT: This file NO LONGER rebuilds Energy & Buildings panels.
   form.js owns all Energy & Buildings table construction.
   This file handles only:
     1. govTier cascade visibility
     2. AFOLU method tabs
     3. Per-section "Reset to defaults" buttons
     4. Click-to-jump section flash
     5. "Results-ready" banner
═══════════════════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  function onReady(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else { fn(); }
  }
  onReady(function () { setTimeout(init, 100); });

  function init() {
    setupTierCascade();
    injectAfoluTabs();
    injectResetButtons();
    wireProgressFlash();
    setupResultsBanner();
  }

  /* ═══════════════════════════════════════════════════════════════════
     1. govTier cascade visibility
  ═══════════════════════════════════════════════════════════════════ */
  const TIER_RULES = {
    'Village': { hiddenSections: [5], dimMessage: 'Not typically required for Village/Town scope' },
    'Town':    { hiddenSections: [5], dimMessage: 'Not typically required for Village/Town scope' },
    'City':    { hiddenSections: [], dimMessage: '' },
    'District':{ hiddenSections: [], dimMessage: '' },
    'State':   { hiddenSections: [], dimMessage: '' },
  };

  function setupTierCascade() {
    const tier = document.getElementById('govTier');
    if (!tier) return;

    function applyScope(value) {
      document.querySelectorAll('.form-section').forEach(s => {
        s.classList.remove('out-of-scope');
        s.removeAttribute('data-scope-msg');
      });
      if (!value) return;
      const rule = TIER_RULES[value];
      if (!rule) return;
      rule.hiddenSections.forEach(idx => {
        const sec = document.querySelector(`.form-section[data-section="${idx}"]`);
        if (sec) {
          sec.classList.add('out-of-scope');
          sec.setAttribute('data-scope-msg', rule.dimMessage);
        }
      });
      document.querySelectorAll('.ps').forEach(l => {
        const sec = parseInt(l.dataset.sec, 10);
        l.style.opacity = rule.hiddenSections.includes(sec) ? '0.4' : '';
      });
    }

    tier.addEventListener('change', e => applyScope(e.target.value));
    if (tier.value) applyScope(tier.value);
  }

  /* ═══════════════════════════════════════════════════════════════════
     2. AFOLU method tabs
  ═══════════════════════════════════════════════════════════════════ */
  function injectAfoluTabs() {
    const sec = document.querySelector('.form-section[data-section="4"]');
    if (!sec || sec.querySelector('.afolu-tabs')) return;
    const grid = sec.querySelector('.field-grid');
    if (!grid) return;

    const LIVESTOCK = [
      'dairy_cow_indigenous','dairy_cow_crossbred','nondairy_cow_adult',
      'dairy_buffalo','sheep','goat','swine','poultry',
    ];
    const LANDUSE = ['green_ha','paddy_ha'];

    grid.querySelectorAll('.field-group').forEach(fg => {
      const inp = fg.querySelector('input, select');
      if (!inp) return;
      if (LIVESTOCK.includes(inp.name)) fg.dataset.afolu = 'live';
      else if (LANDUSE.includes(inp.name)) fg.dataset.afolu = 'land';
      else fg.dataset.afolu = 'live land';
    });

    const tabs = document.createElement('div');
    tabs.className = 'subsection-tabs afolu-tabs';
    tabs.innerHTML = `
      <button type="button" class="sub-tab active" data-afolu-tab="live">Livestock &amp; Manure</button>
      <button type="button" class="sub-tab" data-afolu-tab="land">Land Use Change</button>
      <button type="button" class="sub-tab" data-afolu-tab="all">Show Both</button>`;
    grid.insertAdjacentElement('beforebegin', tabs);

    function applyAfoluView(view) {
      grid.querySelectorAll('.field-group').forEach(fg => {
        const tags = (fg.dataset.afolu || '').split(' ');
        fg.style.display = (view === 'all' || tags.includes(view)) ? '' : 'none';
      });
      tabs.querySelectorAll('.sub-tab').forEach(b =>
        b.classList.toggle('active', b.dataset.afoluTab === view));
    }
    tabs.querySelectorAll('[data-afolu-tab]').forEach(btn =>
      btn.addEventListener('click', () => applyAfoluView(btn.dataset.afoluTab)));
    applyAfoluView('live');
  }

  /* ═══════════════════════════════════════════════════════════════════
     3. Per-section "Reset to defaults" button
  ═══════════════════════════════════════════════════════════════════ */
  const _snapshot = new WeakMap();

  function injectResetButtons() {
    document.querySelectorAll('.form-section').forEach(section => {
      const header = section.querySelector('.section-header');
      if (!header || header.querySelector('.reset-section-btn')) return;

      section.querySelectorAll('input, select, textarea').forEach(f => {
        _snapshot.set(f, f.type === 'checkbox' || f.type === 'radio' ? f.checked : f.value);
      });

      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'reset-section-btn';
      btn.innerHTML = `
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="2.2"
             stroke-linecap="round" stroke-linejoin="round">
          <path d="M3 12a9 9 0 1 0 3-6.7"/>
          <polyline points="3 4 3 10 9 10"/>
        </svg>
        Reset section`;
      btn.addEventListener('click', () => {
        const title = section.querySelector('.section-title')?.textContent || 'this section';
        if (!confirm(`Reset ${title} to default values? Any edits in this section will be lost.`)) return;
        section.querySelectorAll('input, select, textarea').forEach(f => {
          if (!_snapshot.has(f)) return;
          const v = _snapshot.get(f);
          if (f.type === 'checkbox' || f.type === 'radio') f.checked = !!v;
          else f.value = v;
          f.dispatchEvent(new Event('input',  { bubbles: true }));
          f.dispatchEvent(new Event('change', { bubbles: true }));
        });
        btn.classList.add('just-reset');
        setTimeout(() => btn.classList.remove('just-reset'), 1000);
      });
      header.appendChild(btn);
    });
  }

  /* ═══════════════════════════════════════════════════════════════════
     4. Click-to-jump section flash
  ═══════════════════════════════════════════════════════════════════ */
  function wireProgressFlash() {
    document.querySelectorAll('.ps').forEach(p => {
      p.addEventListener('click', () => {
        const idx = parseInt(p.dataset.sec, 10);
        const target = document.querySelector(`.form-section[data-section="${idx}"]`);
        if (!target) return;
        setTimeout(() => {
          target.classList.add('section-jumped-to');
          setTimeout(() => target.classList.remove('section-jumped-to'), 850);
        }, 0);
      });
    });
  }

  /* ═══════════════════════════════════════════════════════════════════
     5. "Results-ready" banner
  ═══════════════════════════════════════════════════════════════════ */
  function setupResultsBanner() {
    let prior = null;
    try { prior = sessionStorage.getItem('ascentPayload'); } catch (e) {}
    if (!prior) return;
    const form = document.getElementById('ascentForm');
    if (!form || document.querySelector('.results-ready-banner')) return;

    const banner = document.createElement('div');
    banner.className = 'results-ready-banner visible';
    banner.innerHTML = `
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2.2"
           stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
        <polyline points="22 4 12 14.01 9 11.01"/>
      </svg>
      <span><b>You have results from a previous run.</b>
            Edit any field below and re-submit to recalculate, or
            view your existing results.</span>
      <span class="rrb-spacer"></span>
      <a href="/results" class="rrb-link rrb-view">View results →</a>
      <button type="button" class="rrb-link rrb-dismiss">Dismiss</button>`;
    form.insertAdjacentElement('beforebegin', banner);
    banner.querySelector('.rrb-dismiss').addEventListener('click', () =>
      banner.classList.remove('visible'));
  }

})();
