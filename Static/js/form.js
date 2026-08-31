/* ═══════════════════════════════════════════════════════
   ASCENT — Form.js
   Multi-step form logic, city cascading, validation
═══════════════════════════════════════════════════════ */

(function () {
  'use strict';
 
  const TOTAL_SECTIONS = 8;  // sections 0 (Info) … 7 (Targets)
  const STORAGE_KEY    = 'ascentFormData';
  let currentSection   = 0;
 
  // ── City data ──────────────────────────────────────────
  let citiesData = [];
 
  async function loadCities() {
    const sel = document.getElementById('stateSelect');
    if (!sel) {
      alert('CRITICAL: #stateSelect not found in DOM. form.js loaded before HTML.');
      return;
    }

    // ── Acquire city data ──
    // Try embedded JSON first; fall back to API.
    const embedded = document.getElementById('citiesData');
    if (embedded && embedded.textContent.trim()) {
      try {
        const parsed = JSON.parse(embedded.textContent);
        if (Array.isArray(parsed) && parsed.length) {
          citiesData = parsed;
          console.log('[ASCENT] OK: ' + citiesData.length + ' cities loaded from embedded JSON');
        }
      } catch (e) {
        console.error('[ASCENT] Embedded JSON parse failed:', e);
      }
    }

    if (!citiesData.length) {
      try {
        const res = await fetch('/api/cities', { credentials: 'same-origin' });
        if (!res.ok) {
          sel.innerHTML = '<option value="">— API error ' + res.status + ', please re-login —</option>';
          return;
        }
        const text = await res.text();
        try {
          const parsed = JSON.parse(text);
          if (Array.isArray(parsed) && parsed.length) {
            citiesData = parsed;
            console.log('[ASCENT] OK: ' + citiesData.length + ' cities loaded from API');
          }
        } catch (e) {
          sel.innerHTML = '<option value="">— API returned non-JSON, please re-login —</option>';
          console.error('[ASCENT] /api/cities body (first 200 chars):', text.substring(0, 200));
          return;
        }
      } catch (e) {
        sel.innerHTML = '<option value="">— Network error: ' + e.message + ' —</option>';
        console.error('[ASCENT] loadCities failed:', e);
        return;
      }
    }

    if (!citiesData.length) {
      sel.innerHTML = '<option value="">— No city data available —</option>';
      return;
    }

    // ── Hydrate saved form data BEFORE populating, so restoreFormData
    //    has both the cities and the saved values available ──
    try { await _hydrateFromServer(); } catch(e) {}

    // ── CRITICAL ORDER: populate states LAST so nothing wipes them ──
    populateStates();

    // restoreFormData uses change events to cascade through state→district→city
    // and runs AFTER states are in the dropdown so the saved state matches a real option.
    restoreFormData();

    // Belt-and-suspenders: if anything cleared the dropdown later, repopulate it.
    setTimeout(() => {
      const currentOpts = document.getElementById('stateSelect').options.length;
      if (currentOpts <= 1) {
        console.warn('[ASCENT] State dropdown was wiped after init; repopulating.');
        const savedState = document.getElementById('stateSelect').value;
        populateStates();
        if (savedState) {
          document.getElementById('stateSelect').value = savedState;
        }
      }
    }, 500);
  }

  // Fetch saved form data for the logged-in user. If it exists, copy it into
  // sessionStorage under STORAGE_KEY so restoreFormData() picks it up.
  async function _hydrateFromServer() {
    try {
      const res = await fetch('/api/user-data', { credentials: 'same-origin' });
      if (!res.ok) return;
      const payload = await res.json();
      if (payload && payload.form && Object.keys(payload.form).length) {
        sessionStorage.setItem(STORAGE_KEY, JSON.stringify(payload.form));
      }
    } catch (e) { /* no-op — sessionStorage will be used */ }
  }
 
  function populateStates() {
    const states = [...new Set(citiesData.map(c => c.state))].sort();
    const sel    = document.getElementById('stateSelect');
    sel.innerHTML = '<option value="">— Choose a state —</option>';
    states.forEach(s => {
      const opt = document.createElement('option');
      opt.value = s; opt.textContent = s;
      sel.appendChild(opt);
    });
  }
 
  // ── Cascade: State → District → City ──────────────────
  document.getElementById('stateSelect').addEventListener('change', function () {
    const state = this.value;
    document.getElementById('stateHidden').value = state;
 
    const distSel = document.getElementById('districtSelect');
    const citySel = document.getElementById('citySelect');
    distSel.innerHTML = '<option value="">— Choose district —</option>';
    citySel.innerHTML  = '<option value="">— Choose city —</option>';
    document.getElementById('climateDisplay').value = '';
    document.getElementById('climateHidden').value  = '';
 
    if (!state) return;
 
    const districts = [...new Set(
      citiesData.filter(c => c.state === state).map(c => c.district)
    )].sort();
 
    districts.forEach(d => {
      const opt = document.createElement('option');
      opt.value = d; opt.textContent = d;
      distSel.appendChild(opt);
    });
 
    saveFormData();
    updateSummary();
  });
 
  document.getElementById('districtSelect').addEventListener('change', function () {
    const state    = document.getElementById('stateSelect').value;
    const district = this.value;
    document.getElementById('districtHidden').value = district;

    const citySel = document.getElementById('citySelect');
    citySel.innerHTML = '<option value="">— Choose city —</option>';

    // Clear climate first; re-set below if district has data
    document.getElementById('climateDisplay').value = '';
    document.getElementById('climateHidden').value  = '';

    if (!district) { saveFormData(); return; }

    const districtCities = citiesData
      .filter(c => c.state === state && c.district === district)
      .sort((a, b) => a.city.localeCompare(b.city));

    // ── Climate zone is district-level in the ASCENT city master ──
    // Every city in a district shares the same zone, so we read it
    // from the first entry and display it immediately on district pick.
    const districtClimate = districtCities.length ? (districtCities[0].climate || '') : '';
    if (districtClimate) {
      document.getElementById('climateDisplay').value = districtClimate;
      document.getElementById('climateHidden').value  = districtClimate;
      // Visual pulse to confirm auto-detection fired
      const disp = document.getElementById('climateDisplay');
      disp.classList.add('climate-autofilled');
      setTimeout(() => disp.classList.remove('climate-autofilled'), 1200);
    }

    districtCities.forEach(c => {
      const opt           = document.createElement('option');
      opt.value           = c.city;
      opt.textContent     = c.city;
      opt.dataset.climate = c.climate;   // kept so city-level override still works
      citySel.appendChild(opt);
    });

    saveFormData();
    updateSummary();   // header city display updates with state at least

    // Secondary data: if the toggle is on, pull pre-populated values now.
    maybeFillSecondaryData();
  });
 
  document.getElementById('citySelect').addEventListener('change', function () {
    const opt = this.options[this.selectedIndex];
    // Climate was already set by district selection; city confirms it.
    // We only write if the district handler somehow left it blank.
    const existing = document.getElementById('climateDisplay').value;
    const fromCity = opt.dataset.climate || '';
    if (!existing && fromCity) {
      document.getElementById('climateDisplay').value = fromCity;
      document.getElementById('climateHidden').value  = fromCity;
    }
    saveFormData();
    updateSummary();
  });

  // ── Secondary-data toggle: fill (or clear the status) when flipped ──
  const secToggle = document.getElementById('useSecondaryData');
  if (secToggle) {
    secToggle.addEventListener('change', function () {
      const status = document.getElementById('secondaryStatus');
      if (this.checked) {
        maybeFillSecondaryData();
      } else if (status) {
        status.style.display = 'none';
        // remove the "filled from metadata" badges
        document.querySelectorAll('.meta-filled').forEach(el => {
          el.classList.remove('meta-filled');
          el.removeAttribute('title');
        });
        document.querySelectorAll('.meta-source-note').forEach(n => n.remove());
      }
      saveFormData();
    });
  }

  // Fetch metadata for the selected district and populate matching fields.
  async function maybeFillSecondaryData() {
    const toggle = document.getElementById('useSecondaryData');
    const status = document.getElementById('secondaryStatus');
    if (!toggle || !toggle.checked) return;
    const state    = document.getElementById('stateHidden').value;
    const district = document.getElementById('districtHidden').value;
    if (!state || !district) {
      if (status) {
        status.style.display = 'block';
        status.className = 'secondary-status warn';
        status.textContent = 'Pick a state and district first, then secondary data will fill automatically.';
      }
      return;
    }
    if (status) {
      status.style.display = 'block';
      status.className = 'secondary-status loading';
      status.textContent = 'Fetching secondary data for ' + district + '…';
    }
    try {
      const res = await fetch('/api/metadata?state=' + encodeURIComponent(state) +
                              '&district=' + encodeURIComponent(district));
      const data = await res.json();
      if (!data.ok || !data.fields) {
        if (status) { status.className = 'secondary-status warn';
          status.textContent = 'No secondary data available for this location.'; }
        return;
      }
      const filledNames = applySecondaryData(data.fields);
      if (status) {
        status.className = 'secondary-status ok';
        status.innerHTML = '✓ Filled <strong>' + filledNames + '</strong> field(s) from ASCENT metadata for ' +
          district + '. Every value is editable — adjust anything that differs from your records.';
      }
      updateSummary();
    } catch (e) {
      if (status) { status.className = 'secondary-status warn';
        status.textContent = 'Could not load secondary data (' + e.message + ').'; }
    }
  }

  // Write each metadata value into its form field + tag it with a source note.
  function applySecondaryData(fields) {
    let count = 0;
    Object.keys(fields).forEach(name => {
      const meta = fields[name];
      const el = document.querySelector('[name="' + name + '"]');
      if (!el) return;
      // Round sensibly: counts/areas to whole numbers, rates keep decimals.
      let v = meta.value;
      if (typeof v === 'number') {
        v = (name.indexOf('growth') > -1) ? Math.round(v * 100) / 100 : Math.round(v);
      }
      el.value = v;
      el.classList.add('meta-filled');
      const src = [meta.source, meta.year].filter(Boolean).join(' · ');
      if (src) el.title = 'From ASCENT metadata: ' + src;
      // add a small source note under the field (once)
      const holder = el.closest('.field-group') || el.parentElement;
      if (holder && !holder.querySelector('.meta-source-note')) {
        const note = document.createElement('div');
        note.className = 'meta-source-note';
        note.textContent = 'Source: ' + (meta.source || '—') + (meta.year ? ' (' + meta.year + ')' : '');
        holder.appendChild(note);
      }
      // fire input/change so any dependent calc updates
      el.dispatchEvent(new Event('input',  { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
      count++;
    });
    return count;
  }
 
  // ── Subsection tabs (works for ALL sections) ───────────
  document.querySelectorAll('.sub-tab').forEach(btn => {
    btn.addEventListener('click', function () {
      const parentSection = this.closest('.form-section');
      parentSection.querySelectorAll('.sub-tab').forEach(t => t.classList.remove('active'));
      parentSection.querySelectorAll('.sub-panel').forEach(p => p.classList.remove('active'));
      this.classList.add('active');
      const subId = 'sub-' + this.dataset.sub;
      const panel = document.getElementById(subId);
      if (panel) panel.classList.add('active');
    });
  });
 
  // ── Transport Approach Toggle (lives in Section 2) ─────
  // The toggle buttons use data-trans="1" or data-trans="2"
  document.querySelectorAll('[data-trans]').forEach(btn => {
    btn.addEventListener('click', function () {
      document.querySelectorAll('[data-trans]').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      const opt = this.dataset.trans;
      const transOptInput = document.getElementById('transOption');
      if (transOptInput) transOptInput.value = opt;
 
      const fuelPanel = document.getElementById('trans-fuel-panel');
      const vktPanel  = document.getElementById('trans-vkt-panel');
      if (fuelPanel) fuelPanel.style.display = opt === '1' ? '' : 'none';
      if (vktPanel)  vktPanel.style.display  = opt === '2' ? '' : 'none';
      saveFormData();
    });
  });
 
  // ── Sliders ────────────────────────────────────────────
  const renewableSlider = document.querySelector('[name="renewable_pct"]');
  const evSlider        = document.querySelector('[name="ev_pct"]');
 
  if (renewableSlider) {
    renewableSlider.addEventListener('input', function () {
      document.getElementById('renewableVal').textContent = this.value + '%';
      updateSliderFill(this);
      saveFormData();
    });
    updateSliderFill(renewableSlider);
  }
 
  if (evSlider) {
    evSlider.addEventListener('input', function () {
      document.getElementById('evVal').textContent = this.value + '%';
      updateSliderFill(this);
      saveFormData();
    });
    updateSliderFill(evSlider);
  }
 
  function updateSliderFill(slider) {
    const pct = ((slider.value - slider.min) / (slider.max - slider.min)) * 100;
    slider.style.background =
      `linear-gradient(90deg, var(--teal) ${pct}%, #e2e8f0 ${pct}%)`;
  }
 
  // ── Save all form inputs to sessionStorage ─────────────
  function saveFormData() {
    const form = document.getElementById('ascentForm');
    if (!form) return;
    const fd   = new FormData(form);
    const data = {};
    fd.forEach((v, k) => { data[k] = v; });
    // also save the hidden/display fields not captured by FormData
    data['_state']    = document.getElementById('stateSelect').value;
    data['_district'] = document.getElementById('districtSelect').value;
    data['_climate']  = document.getElementById('climateDisplay').value;
    data['_transOpt'] = document.getElementById('transOption')?.value || '1';
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    // ── Also persist to the user's account on the server (debounced) ──
    _scheduleServerSave(data);
  }

  // Debounced server-save: writes to /api/user-data so a logged-in
  // user's questionnaire survives across browsers and sessions.
  let _serverSaveTimer = null;
  function _scheduleServerSave(data) {
    if (_serverSaveTimer) clearTimeout(_serverSaveTimer);
    _serverSaveTimer = setTimeout(() => {
      fetch('/api/user-data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'same-origin',
        body: JSON.stringify({ form: data })
      }).catch(() => { /* offline / not signed in — fall back to sessionStorage */ });
    }, 800);
  }
 
  // ── Restore saved form data ────────────────────────────
  function restoreFormData() {
    const raw = sessionStorage.getItem(STORAGE_KEY);
    if (!raw) return;
    let saved;
    try { saved = JSON.parse(raw); } catch (e) { return; }

    // Guard: only restore state if it actually exists in the loaded citiesData
    // (prevents stale sessionStorage from previous deploys from breaking the cascade)
    const savedState = saved['_state'];
    const stateIsValid = savedState && citiesData.some(c => c.state === savedState);

    // 1. Restore state dropdown
    if (stateIsValid) {
      const stateSel = document.getElementById('stateSelect');
      stateSel.value = savedState;
      stateSel.dispatchEvent(new Event('change')); // triggers district population
 
      // 2. Restore district after state cascade
      setTimeout(() => {
        if (saved['_district']) {
          const distSel = document.getElementById('districtSelect');
          distSel.value = saved['_district'];
          distSel.dispatchEvent(new Event('change')); // triggers city population
 
          // 3. Restore city after district cascade
          setTimeout(() => {
            if (saved['city']) {
              const citySel = document.getElementById('citySelect');
              citySel.value = saved['city'];
              // restore climate manually (dataset not set on restored options until change fires)
              document.getElementById('climateDisplay').value = saved['_climate'] || '';
              document.getElementById('climateHidden').value  = saved['_climate'] || '';
            }
            // restore all other plain inputs
            _restoreInputs(saved);
          }, 50);
        } else {
          _restoreInputs(saved);
        }
      }, 50);
    } else {
      _restoreInputs(saved);
    }
  }
 
  function _restoreInputs(saved) {
    const form = document.getElementById('ascentForm');
    // Restore all regular inputs/selects/textareas by name
    form.querySelectorAll('[name]').forEach(el => {
      const name = el.getAttribute('name');
      if (saved[name] === undefined) return;
      if (el.type === 'checkbox') {
        el.checked = saved[name] === 'on';
      } else if (el.type === 'radio') {
        el.checked = el.value === saved[name];
      } else {
        el.value = saved[name];
      }
    });
 
    // Restore sliders visual fill
    document.querySelectorAll('.range-slider').forEach(updateSliderFill);
 
    // Restore renewable/ev display labels
    if (saved['renewable_pct']) {
      const rv = document.getElementById('renewableVal');
      if (rv) rv.textContent = saved['renewable_pct'] + '%';
    }
    if (saved['ev_pct']) {
      const ev = document.getElementById('evVal');
      if (ev) ev.textContent = saved['ev_pct'] + '%';
    }
 
    // Restore transport option toggle
    const transOpt = saved['_transOpt'] || '1';
    const transOptInput = document.getElementById('transOption');
    if (transOptInput) transOptInput.value = transOpt;
    document.querySelectorAll('[data-trans]').forEach(b => {
      b.classList.toggle('active', b.dataset.trans === transOpt);
    });
    const fuelPanel = document.getElementById('trans-fuel-panel');
    const vktPanel  = document.getElementById('trans-vkt-panel');
    if (fuelPanel) fuelPanel.style.display = transOpt === '1' ? '' : 'none';
    if (vktPanel)  vktPanel.style.display  = transOpt === '2' ? '' : 'none';
 
    updateSummary();
  }
 
  // ── Auto-save on any input change ─────────────────────
  document.getElementById('ascentForm').addEventListener('input', saveFormData);
  document.getElementById('ascentForm').addEventListener('change', saveFormData);
 
  // ── Live summary update ────────────────────────────────
  function updateSummary() {
    const city = document.getElementById('citySelect').value || '—';
    const state = document.getElementById('stateSelect').value || '—';
    const pop   = document.querySelector('[name="population"]')?.value;
    const yr    = document.querySelector('[name="target_year"]')?.value;
 
    const ssCity  = document.getElementById('ss-city');
    const ssState = document.getElementById('ss-state');
    const ssPop   = document.getElementById('ss-pop');
    const ssYr    = document.getElementById('ss-yr');
    const rhCity  = document.getElementById('rhCity');
 
    if (ssCity)  ssCity.textContent  = city;
    if (ssState) ssState.textContent = state;
    if (ssPop)   ssPop.textContent   = pop ? Number(pop).toLocaleString('en-IN') : '—';
    if (ssYr)    ssYr.textContent    = yr || '2050';
    if (rhCity)  rhCity.textContent  = city !== '—' ? `${city}, ${state}` : '';
  }
 
  // ── Navigation dots builder ────────────────────────────
  function buildDots() {
    const container = document.getElementById('navDots');
    if (!container) return;
    container.innerHTML = '';
    for (let i = 0; i < TOTAL_SECTIONS; i++) {
      const dot = document.createElement('div');
      dot.className = 'nav-dot'
        + (i === currentSection ? ' active' : '')
        + (i < currentSection  ? ' done'   : '');
      dot.addEventListener('click', () => goTo(i));
      container.appendChild(dot);
    }
  }
 
  // ── Go to section ──────────────────────────────────────
  function goTo(idx) {
    if (idx < 0 || idx >= TOTAL_SECTIONS) return;
 
    document.querySelectorAll('.form-section').forEach((s, i) => {
      s.classList.toggle('active', i === idx);
    });
 
    document.querySelectorAll('.ps').forEach((p, i) => {
      p.classList.toggle('active', i === idx);
      p.classList.toggle('done',   i < idx);
    });
 
    currentSection = idx;
 
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');
    if (prevBtn) prevBtn.disabled = idx === 0;
    if (nextBtn) nextBtn.style.display = idx === TOTAL_SECTIONS - 1 ? 'none' : '';
 
    const fill = (idx / (TOTAL_SECTIONS - 1)) * 100;
    const pf   = document.getElementById('progressFill');
    if (pf) pf.style.width = fill + '%';
 
    buildDots();
    window.scrollTo({ top: 0, behavior: 'smooth' });
    updateSummary();
    saveFormData();
  }
 
  // ── Nav button wiring ──────────────────────────────────
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  if (prevBtn) prevBtn.addEventListener('click', () => goTo(currentSection - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => goTo(currentSection + 1));
 
  // Progress section label clicks
  document.querySelectorAll('.ps').forEach((p, i) => {
    p.addEventListener('click', () => goTo(i));
  });
 
  // ── Refresh / Reset button ─────────────────────────────
  // Inject a refresh button into the header badge area
  function injectRefreshButton() {
    const header = document.querySelector('.site-header');
    if (!header) return;
 
    // Remove existing refresh btn if any
    const existing = document.getElementById('refreshBtn');
    if (existing) existing.remove();
 
    const btn = document.createElement('button');
    btn.id = 'refreshBtn';
    btn.type = 'button';
    btn.title = 'Clear all inputs and start fresh';
    btn.innerHTML = `
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2.5">
        <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/>
        <path d="M3 3v5h5"/>
      </svg>
      Reset Form
    `;
    btn.style.cssText = `
      margin-left:12px; display:flex; align-items:center; gap:6px;
      padding:6px 14px; border-radius:8px; cursor:pointer;
      border:1.5px solid #ef4444; background:transparent;
      color:#ef4444; font-size:0.75rem; font-weight:700;
      font-family:var(--font-body); letter-spacing:0.03em;
      transition:all 0.2s;
    `;
    btn.addEventListener('mouseenter', () => {
      btn.style.background = '#ef4444';
      btn.style.color = '#fff';
    });
    btn.addEventListener('mouseleave', () => {
      btn.style.background = 'transparent';
      btn.style.color = '#ef4444';
    });
    btn.addEventListener('click', resetForm);
 
    // Insert before the header badge (note: badge is inside .header-meta, not a direct
    // child of .site-header, so we must insert relative to badge.parentNode, not header)
    const badge = header.querySelector('.header-badge');
    if (badge && badge.parentNode) {
      badge.parentNode.insertBefore(btn, badge);
    } else {
      header.appendChild(btn);
    }
  }
 
  function resetForm() {
    if (!confirm('Clear all entered data and start fresh?')) return;
    sessionStorage.removeItem(STORAGE_KEY);
    sessionStorage.removeItem('ascentPayload');
    // Also clear the account-side copy
    fetch('/api/user-data', {
      method: 'DELETE',
      credentials: 'same-origin'
    }).catch(() => { /* ignore — local clear already happened */ });
 
    // Reset the actual form
    document.getElementById('ascentForm').reset();
 
    // Reset dropdowns
    document.getElementById('stateSelect').innerHTML  = '<option value="">— Choose a state —</option>';
    document.getElementById('districtSelect').innerHTML = '<option value="">— Choose district —</option>';
    document.getElementById('citySelect').innerHTML    = '<option value="">— Choose city —</option>';
    document.getElementById('climateDisplay').value   = '';
    document.getElementById('climateHidden').value    = '';
    document.getElementById('stateHidden').value      = '';
    document.getElementById('districtHidden').value   = '';
 
    // Re-populate states
    populateStates();
 
    // Reset sliders
    document.querySelectorAll('.range-slider').forEach(updateSliderFill);
    const rv = document.getElementById('renewableVal');
    const ev = document.getElementById('evVal');
    if (rv) rv.textContent = '40%';
    if (ev) ev.textContent = '30%';
 
    // Reset transport toggle
    const transOptInput = document.getElementById('transOption');
    if (transOptInput) transOptInput.value = '1';
    document.querySelectorAll('[data-trans]').forEach(b => {
      b.classList.toggle('active', b.dataset.trans === '1');
    });
    const fp = document.getElementById('trans-fuel-panel');
    const vp = document.getElementById('trans-vkt-panel');
    if (fp) fp.style.display = '';
    if (vp) vp.style.display = 'none';
 
    goTo(0);
    updateSummary();
  }
 
  // ── Form submission ────────────────────────────────────
  document.getElementById('ascentForm').addEventListener('submit', async function (e) {
    e.preventDefault();
 
    const city  = document.getElementById('citySelect').value;
    const state = document.getElementById('stateSelect').value;
    const pop   = document.querySelector('[name="population"]').value;
 
    if (!city || !state || !pop) {
      alert('Please fill in City, State, and Population before calculating.');
      goTo(0);
      return;
    }
 
    const btn = document.getElementById('calculateBtn');
    btn.querySelector('.btn-text').classList.add('hidden');
    btn.querySelector('.btn-loading').classList.remove('hidden');
    btn.disabled = true;
 
    const fd   = new FormData(this);
    const data = {};
    fd.forEach((v, k) => { data[k] = v; });
 
    // Percent fields → decimals
    const pctFields = {
      'sw_food_frac_pct':      'sw_food_frac',
      'sw_lfm_pct':            'sw_lfm',
      'sw_inc_pct':            'sw_inc',
      'sw_gas_collection_pct': 'sw_gas_collection',
      'ww_aer_pct':            'ww_aer',
      'ww_uasb_pct':           'ww_uasb',
      'ww_sep_pct':            'ww_sep',
      'ww_open_pct':           'ww_open',
      'target_pct_input':      'target_pct',
    };
    Object.entries(pctFields).forEach(([src, dst]) => {
      if (data[src] !== undefined && data[src] !== '') {
        data[dst] = parseFloat(data[src]) / 100;
      }
    });
 
    if (data.growth_rate) data.growth_rate = parseFloat(data.growth_rate) / 100;
 
    sessionStorage.setItem('ascentPayload', JSON.stringify(data));
    window.location.href = '/results';
  });
 
  // ── Init ──────────────────────────────────────────────
  injectRefreshButton();
  buildDots();
  goTo(0);
  loadCities(); // restoreFormData() is called inside after cities load

  // ═══════════════════════════════════════════════════════════════════
  //                EXPANDED QUESTIONNAIRE WIRING (v3)
  // ═══════════════════════════════════════════════════════════════════

  // ── 1. Government Tier gating with tooltips ──
  const govTier      = document.getElementById('govTier');
  const stateWrap    = document.getElementById('stateWrap');
  const districtWrap = document.getElementById('districtWrap');
  const cityWrap     = document.getElementById('cityWrap');
  const villageWrap  = document.getElementById('villageWrap');
  const stateSel     = document.getElementById('stateSelect');
  const distSel      = document.getElementById('districtSelect');
  const citySel      = document.getElementById('citySelect');

  function applyTierGating() {
    if (!govTier) return;
    const tier = govTier.value;
    const enable = (wrap, sel, on, reason) => {
      if (!wrap || !sel) return;
      sel.disabled = !on;
      wrap.classList.toggle('locked', !on);
      wrap.title = on ? '' : reason;
      if (!on) sel.value = '';
    };

    const showVillage = (tier === 'Village');
    if (villageWrap) villageWrap.style.display = showVillage ? '' : 'none';

    // Default: everything off until tier picked
    if (!tier) {
      enable(stateWrap,    stateSel, false, 'Choose a Government Tier first');
      enable(districtWrap, distSel,  false, 'Choose a Government Tier first');
      enable(cityWrap,     citySel,  false, 'Choose a Government Tier first');
      return;
    }
    if (tier === 'State') {
      enable(stateWrap,    stateSel, true,  '');
      enable(districtWrap, distSel,  false, 'State-level analysis selected — District unavailable');
      enable(cityWrap,     citySel,  false, 'State-level analysis selected — City unavailable');
    } else if (tier === 'District') {
      enable(stateWrap,    stateSel, true,  '');
      enable(districtWrap, distSel,  true,  '');
      enable(cityWrap,     citySel,  false, 'District-level analysis selected — City unavailable');
    } else if (tier === 'City') {
      enable(stateWrap,    stateSel, true,  '');
      enable(districtWrap, distSel,  true,  '');
      enable(cityWrap,     citySel,  true,  '');
    } else if (tier === 'Village') {
      enable(stateWrap,    stateSel, true,  '');
      enable(districtWrap, distSel,  true,  '');
      enable(cityWrap,     citySel,  false, 'Village mode — use the Village Name field instead');
    }
  }
  if (govTier) {
    govTier.addEventListener('change', () => { applyTierGating(); saveFormData(); });
    applyTierGating();
  }

  // ── 2. Floor Space table → auto-fill panel floor-area inputs ──
  document.querySelectorAll('[data-floor-from]').forEach(target => {
    const sourceId = target.dataset.floorFrom;
    const source   = document.getElementById(sourceId);
    if (!source) return;
    const sync = () => { target.value = source.value || ''; };
    source.addEventListener('input', sync);
    sync();
  });

  // ── 3. Conv-factor table (optional background load — tables build immediately) ──
  let convFactors = { fuels: [], factors: {} };   // safe default so getFuelUnits never breaks

  // Build all rows RIGHT NOW (synchronous, no API dependency)
  // This fires on first script execution (IIFE), which is DOMContentLoaded-safe
  // because the <script> tag is deferred or at the bottom of <body>.
  setTimeout(buildAllInitialRows, 0);

  // Optionally load conv-factors from API in background for future unit-conversion use.
  // This does NOT gate table rendering any more.
  fetch('/api/conv-factors', { credentials: 'same-origin' })
    .then(r => r.ok ? r.json() : null)
    .then(j => { if (j) convFactors = j; })
    .catch(() => {});   // silent fail — curated FUEL_UNIT_MAP is the source of truth

  function unitsForFuel(name) {
    if (!convFactors || !convFactors.factors) return [];
    const f = convFactors.factors[String(name || '').toLowerCase()];
    return f ? Object.keys(f) : [];
  }

  // ═══════════════════════════════════════════════════════════════════
  //  ENERGY & BUILDINGS + ELECTRICITY GENERATION
  //  Source of truth: Questionnaire.xlsx  (B. Building and Energy + C. Electricity Generation)
  //
  //  COLUMN STRUCTURES (exact match to questionnaire):
  //  Residential / Commercial / Institutional  (rows 46, 60, 73):
  //    Fuel ▾ | Value | Unit ▾ | Source | ×
  //
  //  Manufacturing & Construction  (row 86):
  //    Sub category ▾ | Fuel ▾ | Production Capacity (tonnes) | Value | Unit ▾ | Source | ×
  //
  //  Energy Industries  (row 99):
  //    Sub category ▾ | Fuel ▾ | Production Capacity (MW) | Value | Unit ▾ | Source | ×
  //    Sub-category list = C100:C119 data validation (6 options)
  //
  //  Fugitive Emissions  (row 112):
  //    Sub category ▾ | Sector ▾ | Value | Unit (auto-fill, readonly) | Source | ×
  //    NO Rate column.
  //
  //  Energy Generated from Renewables  (row 122):
  //    Activity ▾ | Value (MWh) | Source | ×
  //    Activity = C123:C125 DV: Solar, Wind, Hybrid, Waste to Energy
  //
  //  Electricity Generation  (rows 129-149) — FIXED rows, not dynamic:
  //    Electricity Generation Source | Generation Technology |
  //    Installed Capacity (MW) | Generation for Base Year (MWh) |
  //    Operational Capacity for Base Year (%) | Source
  // ═══════════════════════════════════════════════════════════════════

  // ── 1. Fuel lists — from Emission_Factors.xlsx Activity column ────
  const SECTOR_FUELS = {
    // Residential rows 19-25, Commercial 32-38, Institutional 45-51 → 7 fuels each
    res: ['Electricity','LPG','Firewood','Coal (charcoal)','PNG/City Gas','Kerosene','Diesel Gen set'],
    com: ['Electricity','LPG','Firewood','Coal (charcoal)','PNG/City Gas','Kerosene','Diesel Gen set'],
    ins: ['Electricity','LPG','Firewood','Coal (charcoal)','PNG/City Gas','Kerosene','Diesel Gen set'],
    // Manufacturing rows 58-88 → 31 fuels
    mfg: [
      'LPG','Biodiesels','Biogasoline','Bitumen',
      'Coal (charcoal)','Coal (other bituminous)','Coal (Sub - Bituminous)','Coal (Lignite)',
      'Coke','Coking coal','Anthracite',
      'Compressed Natural Gas (CNG)','Diesel oil','Ethanol','Gas oil','Paraffin',
      'Liquefied Natural Gas (LNG)','Lubricants',
      'Municipal wastes (non-biomass fraction)','Municipal wastes (biomass fraction)',
      'Naphtha','Natural gas','Other biogas','Other Liquid BioFuels',
      'Petroleum coke','Residual fuel oil','Sludge gas',
      'Town gas or city gas','Wood or wood waste','Electricity','Hydrogen'
    ],
    // Energy Industries rows 97-127 → same 31 fuels
    eind: [
      'LPG','Biodiesels','Biogasoline','Bitumen',
      'Coal (charcoal)','Coal (other bituminous)','Coal (Sub - Bituminous)','Coal (Lignite)',
      'Coke','Coking coal','Anthracite',
      'Compressed Natural Gas (CNG)','Diesel oil','Ethanol','Gas oil','Paraffin',
      'Liquefied Natural Gas (LNG)','Lubricants',
      'Municipal wastes (non-biomass fraction)','Municipal wastes (biomass fraction)',
      'Naphtha','Natural gas','Other biogas','Other Liquid BioFuels',
      'Petroleum coke','Residual fuel oil','Sludge gas',
      'Town gas or city gas','Wood or wood waste','Electricity','Hydrogen'
    ],
  };

  // ── 2. Per-fuel unit map — strict, no global fallback ─────────────
  const FUEL_UNIT_MAP = {
    'Auto LPG':                               ['kg','tonne','m3'],
    'Aviation Gasoline':                      ['l (liter)','kL','m3'],
    'Biodiesels':                             ['kL'],
    'Biogasoline':                            ['kL'],
    'Bitumen':                                ['tonne'],
    'Butane':                                 ['m3'],
    'Coal (charcoal)':                        ['kg','tonne'],
    'Coal (Charcoal)':                        ['kg','tonne'],
    'Coal (Lignite)':                         ['tonne'],
    'Coal (other bituminous)':                ['tonne'],
    'Coal (Sub - Bituminous)':                ['tonne'],
    'Coke':                                   ['tonne'],
    'Coking coal':                            ['tonne'],
    'Compressed Natural Gas (CNG)':           ['kg','tonne','SCM','m3'],
    'Crude oil':                              ['kL'],
    'Diesel Gen set':                         ['kL','m3'],
    'Diesel oil':                             ['kL'],
    'E10':['kL'],'E15':['kL'],'E30':['kL'],'E85':['kL'],
    'Electricity':                            ['kWh','MWh'],
    'Ethanol':                                ['kL'],
    'Firewood':                               ['kg','tonne'],
    'Gas oil':                                ['kL'],
    'Hydrogen':                               ['m3'],
    'Jet gasoline':                           ['kL'],
    'Jet kerosene':                           ['kL'],
    'Jet Kerosene':                           ['kL'],
    'Kerosene':                               ['l (liter)','kL','m3'],
    'Landfill gas':                           ['m3'],
    'Liqu. Natural Gas':                      ['kg','tonne','m3'],
    'Liquefied Natural Gas (LNG)':            ['m3'],
    'LNG':                                    ['m3'],
    'LPG':                                    ['kg','tonne','SCM'],
    'Lubricants':                             ['kL'],
    'Methanol':                               ['kL'],
    'Motor gasoline (petrol)':                ['kL'],
    'Municipal wastes (all)':                 ['tonne'],
    'Municipal wastes (biomass fraction)':    ['tonne'],
    'Municipal wastes (non-biomass fraction)':['tonne'],
    'Naphtha':                                ['kL'],
    'Natural gas':                            ['m3','tonne'],
    'Other biogas':                           ['m3'],
    'Other Liquid BioFuels':                  ['kL'],
    'Paraffin':                               ['kL'],
    'Petrol':                                 ['kL','m3'],
    'Petroleum coke':                         ['tonne'],
    'PNG/City Gas':                           ['kg','tonne','Mmbtu','SCM'],
    'Propane':                                ['m3'],
    'Residual fuel oil':                      ['kL'],
    'Residue Fuel oil':                       ['m3'],
    'Sewage sludge':                          ['tonne'],
    'Sludge gas':                             ['m3'],
    'Town gas or city gas':                   ['tonne','m3'],
    'Wood or wood waste':                     ['tonne'],
    'Anthracite':                             ['tonne'],
  };

  function getFuelUnits(fuel) {
    return FUEL_UNIT_MAP[fuel] || [];
  }

  // ── 3. Shared HTML helpers ────────────────────────────────────────
  function fuelOptsHtml(fuels) {
    return '<option value="">— select fuel —</option>'
      + fuels.map(f => `<option value="${f}">${f}</option>`).join('');
  }
  function unitOptsHtml(fuel) {
    const units = getFuelUnits(fuel);
    if (!units.length) return '<option value="">— select fuel first —</option>';
    return '<option value="">— unit —</option>'
      + units.map(u => `<option value="${u}">${u}</option>`).join('');
  }

  const X_SVG = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none"
      stroke="currentColor" stroke-width="2.8" stroke-linecap="round">
      <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
    </svg>`;

  // Wire fuel→unit cascade and delete on any <tr>
  function wireRow(tr) {
    const fuelSel = tr.querySelector('.fuel-sel');
    const unitSel = tr.querySelector('.unit-sel');
    if (fuelSel && unitSel) {
      fuelSel.addEventListener('change', e => {
        unitSel.innerHTML = unitOptsHtml(e.target.value);
        saveFormData();
      });
    }
    const delBtn = tr.querySelector('.row-x-btn');
    if (delBtn) delBtn.addEventListener('click', () => { tr.remove(); saveFormData(); });
    tr.querySelectorAll('input, select').forEach(el =>
      el.addEventListener('change', () => saveFormData()));
  }

  // Build bty-table inside host; return tbody
  function buildBtyTable(host, theadHtml, tbodyId, minWidth) {
    const scroll = document.createElement('div');
    scroll.className = 'bty-table-scroll';
    const table = document.createElement('table');
    table.className = 'bty-table';
    if (minWidth) table.style.minWidth = minWidth;
    table.innerHTML = `<thead>${theadHtml}</thead>`;
    const tbody = document.createElement('tbody');
    if (tbodyId) tbody.id = tbodyId;
    table.appendChild(tbody);
    scroll.appendChild(table);
    host.appendChild(scroll);
    return tbody;
  }

  function appendAddBtn(host, onClick) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'add-row-btn';
    btn.textContent = '+ Add activity data';
    btn.addEventListener('click', onClick);
    host.appendChild(btn);
  }

  // ══════════════════════════════════════════════════════════════════
  //  TAB 1-3: RESIDENTIAL / COMMERCIAL / INSTITUTIONAL
  //  Questionnaire cols (row 46/60/73): Fuel | Value | Unit | Source
  //  + Floor Area auto-fill block above the table
  // ══════════════════════════════════════════════════════════════════
  function makeSimpleRow(prefix, idx) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>
        <select name="${prefix}_fuel_${idx}" class="field-input bty-input fuel-sel">
          ${fuelOptsHtml(SECTOR_FUELS[prefix] || [])}
        </select>
      </td>
      <td>
        <input type="number" name="${prefix}_value_${idx}"
               class="field-input bty-input" placeholder="0" step="any" min="0"/>
      </td>
      <td>
        <select name="${prefix}_unit_${idx}" class="field-input bty-input unit-sel">
          <option value="">— select fuel first —</option>
        </select>
      </td>
      <td>
        <input type="text" name="${prefix}_source_${idx}"
               class="field-input bty-input" placeholder="Source"/>
      </td>
      <td class="bty-x-cell">
        <button type="button" class="row-x-btn" title="Remove">${X_SVG}</button>
      </td>`;
    wireRow(tr);
    return tr;
  }

  function buildSimpleTable(hostId, prefix, floorName) {
    const host = document.getElementById(hostId);
    if (!host) return;
    host.innerHTML = '';

    // Floor Area auto-fill from Floor Space table
    const floorKey = prefix === 'res' ? 'fsRes' : prefix === 'com' ? 'fsCom' : 'fsIns';
    const bar = document.createElement('div');
    bar.className = 'floor-area-block';
    bar.innerHTML = `
      <label class="floor-area-label">Floor Area (m²)</label>
      <input type="number" name="${floorName}" class="field-input floor-area-input"
             data-floor-from="${floorKey}" readonly
             placeholder="Auto-filled from Floor Space table"/>
      <span class="eb-floor-badge">Auto</span>`;
    host.appendChild(bar);

    const tbody = buildBtyTable(host,
      `<tr>
         <th style="min-width:200px">Fuel</th>
         <th style="min-width:110px">Value</th>
         <th style="min-width:130px">Unit</th>
         <th style="min-width:150px">Source</th>
         <th style="width:32px"></th>
       </tr>`,
      `${prefix}Tbody`, '620px');

    let ctr = 0;
    tbody.appendChild(makeSimpleRow(prefix, ctr++));

    appendAddBtn(host, () => {
      tbody.appendChild(makeSimpleRow(prefix, ctr++));
      saveFormData();
    });
  }

  // ══════════════════════════════════════════════════════════════════
  //  TAB 4: MANUFACTURING & CONSTRUCTION
  //  Questionnaire row 86: Sub category | Fuel | Production Capacity (tonnes) | Value | Unit | Source
  // ══════════════════════════════════════════════════════════════════
  const MFG_SUBCATS = [
    'All Manufacturing & Construction',
    'Iron and Steel','Non-ferrous Metals','Chemicals',
    'Pulp, Paper and Print','Food Processing',
    'Beverages and Tobacco','Non-metallic Minerals',
    'Transport Equipment','Engineering',
    'Mining (excl. fuels) and Quarrying',
    'Wood and Wood Products','Construction',
    'Textile and Leather','Non-specified Industries',
  ];

  function makeMfgRow(idx) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>
        <select name="mfg_row_${idx}_subcat" class="field-input bty-input">
          <option value="">— sub-category —</option>
          ${MFG_SUBCATS.map(s => `<option value="${s}">${s}</option>`).join('')}
        </select>
      </td>
      <td>
        <select name="mfg_row_${idx}_fuel" class="field-input bty-input fuel-sel">
          ${fuelOptsHtml(SECTOR_FUELS.mfg)}
        </select>
      </td>
      <td>
        <input type="number" name="mfg_row_${idx}_capacity"
               class="field-input bty-input" placeholder="0" step="any" min="0"/>
      </td>
      <td>
        <input type="number" name="mfg_row_${idx}_value"
               class="field-input bty-input" placeholder="0" step="any" min="0"/>
      </td>
      <td>
        <select name="mfg_row_${idx}_unit" class="field-input bty-input unit-sel">
          <option value="">— select fuel first —</option>
        </select>
      </td>
      <td>
        <input type="text" name="mfg_row_${idx}_source"
               class="field-input bty-input" placeholder="Source"/>
      </td>
      <td class="bty-x-cell">
        <button type="button" class="row-x-btn" title="Remove">${X_SVG}</button>
      </td>`;
    wireRow(tr);
    return tr;
  }

  function buildMfgTable(host) {
    host.innerHTML = '';
    const tbody = buildBtyTable(host,
      `<tr>
         <th style="min-width:210px">Sub category</th>
         <th style="min-width:195px">Fuel</th>
         <th style="min-width:185px">Production Capacity (tonnes)</th>
         <th style="min-width:100px">Value</th>
         <th style="min-width:125px">Unit</th>
         <th style="min-width:130px">Source</th>
         <th style="width:32px"></th>
       </tr>`,
      'mfgTbody', '980px');

    let ctr = 0;
    tbody.appendChild(makeMfgRow(ctr++));

    appendAddBtn(host, () => {
      tbody.appendChild(makeMfgRow(ctr++));
      saveFormData();
    });
  }

  // ══════════════════════════════════════════════════════════════════
  //  TAB 5: ENERGY INDUSTRIES
  //  Questionnaire row 99: Sub category | Fuel | Production Capacity (MW) | Value | Unit | Source
  //  Sub-category DV (C100:C119): 6 options from questionnaire
  // ══════════════════════════════════════════════════════════════════
  const EIND_SUBCATS = [
    'Electricity generation',
    'Combined heat and power generation',
    'Heat plants',
    'Petroleum refining',
    'Manufacture of solid fuels',
    'Other energy industries',
  ];

  function makeEindRow(idx) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>
        <select name="eind_row_${idx}_subcat" class="field-input bty-input">
          <option value="">— sub-category —</option>
          ${EIND_SUBCATS.map(s => `<option value="${s}">${s}</option>`).join('')}
        </select>
      </td>
      <td>
        <select name="eind_row_${idx}_fuel" class="field-input bty-input fuel-sel">
          ${fuelOptsHtml(SECTOR_FUELS.eind)}
        </select>
      </td>
      <td>
        <input type="number" name="eind_row_${idx}_capacity"
               class="field-input bty-input" placeholder="0" step="any" min="0"/>
      </td>
      <td>
        <input type="number" name="eind_row_${idx}_value"
               class="field-input bty-input" placeholder="0" step="any" min="0"/>
      </td>
      <td>
        <select name="eind_row_${idx}_unit" class="field-input bty-input unit-sel">
          <option value="">— select fuel first —</option>
        </select>
      </td>
      <td>
        <input type="text" name="eind_row_${idx}_source"
               class="field-input bty-input" placeholder="Source"/>
      </td>
      <td class="bty-x-cell">
        <button type="button" class="row-x-btn" title="Remove">${X_SVG}</button>
      </td>`;
    wireRow(tr);
    return tr;
  }

  function buildEindTable(host) {
    host.innerHTML = '';
    const tbody = buildBtyTable(host,
      `<tr>
         <th style="min-width:230px">Sub category</th>
         <th style="min-width:195px">Fuel</th>
         <th style="min-width:175px">Production Capacity (MW)</th>
         <th style="min-width:100px">Value</th>
         <th style="min-width:125px">Unit</th>
         <th style="min-width:130px">Source</th>
         <th style="width:32px"></th>
       </tr>`,
      'eindTbody', '980px');

    let ctr = 0;
    tbody.appendChild(makeEindRow(ctr++));

    appendAddBtn(host, () => {
      tbody.appendChild(makeEindRow(ctr++));
      saveFormData();
    });
  }

  // ══════════════════════════════════════════════════════════════════
  //  TAB 6: FUGITIVE EMISSIONS
  //  Questionnaire row 112: Sub category | Sector | Value | Unit | Source
  //  Sub-category: Mining | Solid Fuels
  //  Mining sectors (5) with auto-fill unit formula (from questionnaire H113 formula):
  //    IF sector=blank → "-"
  //    IF "Flaring or conversion of drained methane" → "Volume of Methane Oxidized (m3/year)"
  //    IF "Post-mining seam gas emissions*" → "No. of Abandoned Mines"
  //    else → "Coal Production in tonnes"
  //  Solid Fuels sectors (22) — unit auto-fills from lookup
  //  NO Rate column (removed per user requirement)
  // ══════════════════════════════════════════════════════════════════
  const MINING_SECTORS = [
    'Mining (Underground)',
    'Post-mining seam gas emissions',
    'Flaring or conversion of drained methane',
    'Mining (Surface)',
    'Post-mining seam gas emissions (Surface)',
  ];

  function miningUnit(sector) {
    if (!sector) return '—';
    if (sector === 'Flaring or conversion of drained methane')
      return 'Volume of Methane Oxidized (m3/year)';
    if (sector.startsWith('Post-mining seam gas'))
      return 'No. of Abandoned Mines';
    return 'Coal Production in tonnes';
  }

  const SOLID_SECTORS = [
    ['Oil and Natural Gas',                   'thousand cubic meters (10³ m³)'],
    ['Oil',                                   'thousand cubic meters (10³ m³)'],
    ['Venting (Oil)',                          'thousand cubic meters (10³ m³)'],
    ['Flaring (Oil)',                          'thousand cubic meters (10³ m³)'],
    ['All Other Fugitive Emissions (Oil)',     'thousand cubic meters (10³ m³)'],
    ['Exploration (Oil)',                      'thousand cubic meters (10³ m³)'],
    ['Production and Upgrading (Oil)',         'thousand cubic meters (10³ m³)'],
    ['Transport (Oil)',                        'thousand cubic meters (10³ m³)'],
    ['Refining (Oil)',                         'thousand cubic meters (10³ m³)'],
    ['Distribution of Oil Products',          'thousand cubic meters (10³ m³)'],
    ['Other (Oil)',                            'thousand cubic meters (10³ m³)'],
    ['Natural Gas',                            'thousand cubic meters (10³ m³)'],
    ['Venting (Gas)',                          'million cubic meters (10⁶ m³ gas)'],
    ['Flaring (Gas)',                          'million cubic meters (10⁶ m³ gas)'],
    ['All Other Fugitive Emissions (Gas)',     'million cubic meters (10⁶ m³ gas)'],
    ['Exploration (Gas)',                      'million cubic meters (10⁶ m³ gas)'],
    ['Production (Gas)',                       'million cubic meters (10⁶ m³ gas)'],
    ['Processing (Gas)',                       'million cubic meters (10⁶ m³ gas)'],
    ['Transmission & Storage (Gas)',           'million cubic meters (10⁶ m³ gas)'],
    ['Distribution (Gas)',                     'million cubic meters (10⁶ m³ gas)'],
    ['Other (Gas)',                            'million cubic meters (10⁶ m³ gas)'],
    ['Other Emissions from Energy Production', 'million cubic meters (10⁶ m³ gas)'],
  ];

  function solidUnit(sector) {
    const found = SOLID_SECTORS.find(([s]) => s === sector);
    return found ? found[1] : '';
  }

  function makeFugRow(idx, defaultSub) {
    const sub      = defaultSub || 'Mining';
    const isMining = (sub === 'Mining');
    const defSec   = isMining ? MINING_SECTORS[0] : SOLID_SECTORS[0][0];
    const defUnit  = isMining ? miningUnit(defSec) : solidUnit(defSec);

    const sectorOpts = isMining
      ? MINING_SECTORS.map(s => `<option value="${s}">${s}</option>`).join('')
      : SOLID_SECTORS.map(([s]) => `<option value="${s}">${s}</option>`).join('');

    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>
        <select name="fug_row_${idx}_subcat" class="field-input bty-input fug-sub">
          <option value="Mining"${sub === 'Mining' ? ' selected' : ''}>Mining</option>
          <option value="Solid Fuels"${sub === 'Solid Fuels' ? ' selected' : ''}>Solid Fuels</option>
        </select>
      </td>
      <td>
        <select name="fug_row_${idx}_sector" class="field-input bty-input fug-sec">
          ${sectorOpts}
        </select>
      </td>
      <td>
        <input type="number" name="fug_row_${idx}_value"
               class="field-input bty-input" placeholder="0" step="any" min="0"/>
      </td>
      <td>
        <input type="text" name="fug_row_${idx}_unit"
               class="field-input bty-input fug-unit" value="${defUnit}" readonly/>
      </td>
      <td>
        <input type="text" name="fug_row_${idx}_source"
               class="field-input bty-input" placeholder="Source"/>
      </td>
      <td class="bty-x-cell">
        <button type="button" class="row-x-btn" title="Remove">${X_SVG}</button>
      </td>`;

    tr.querySelector('.fug-sub').addEventListener('change', function () {
      const mine    = (this.value === 'Mining');
      const secSel  = tr.querySelector('.fug-sec');
      const unitInp = tr.querySelector('.fug-unit');
      if (mine) {
        secSel.innerHTML = MINING_SECTORS.map(s => `<option value="${s}">${s}</option>`).join('');
        unitInp.value = miningUnit(MINING_SECTORS[0]);
      } else {
        secSel.innerHTML = SOLID_SECTORS.map(([s]) => `<option value="${s}">${s}</option>`).join('');
        unitInp.value = solidUnit(SOLID_SECTORS[0][0]);
      }
      saveFormData();
    });

    tr.querySelector('.fug-sec').addEventListener('change', function () {
      const mine = (tr.querySelector('.fug-sub').value === 'Mining');
      tr.querySelector('.fug-unit').value =
        mine ? miningUnit(this.value) : solidUnit(this.value);
      saveFormData();
    });

    const del = tr.querySelector('.row-x-btn');
    if (del) del.addEventListener('click', () => { tr.remove(); saveFormData(); });
    tr.querySelectorAll('input, select').forEach(el =>
      el.addEventListener('change', () => saveFormData()));

    return tr;
  }

  function buildFugTable(host) {
    host.innerHTML = '';
    const tbody = buildBtyTable(host,
      `<tr>
         <th style="min-width:140px">Sub category</th>
         <th style="min-width:290px">Sector</th>
         <th style="min-width:110px">Value</th>
         <th style="min-width:270px">Unit</th>
         <th style="min-width:130px">Source</th>
         <th style="width:32px"></th>
       </tr>`,
      'fugTbody', '980px');

    let ctr = 0;
    tbody.appendChild(makeFugRow(ctr++, 'Mining'));

    appendAddBtn(host, () => {
      tbody.appendChild(makeFugRow(ctr++, 'Mining'));
      saveFormData();
    });
  }

  // ══════════════════════════════════════════════════════════════════
  //  TAB 7: ENERGY GENERATED FROM RENEWABLES
  //  Questionnaire row 122: Activity | Value (MWh) | Source
  //  Activity DV (C123:C125): Solar, Wind, Hybrid, Waste to Energy
  // ══════════════════════════════════════════════════════════════════
  const REN_ACTIVITIES = ['Solar', 'Wind', 'Hybrid', 'Waste to Energy'];

  function makeRenRow(idx) {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>
        <select name="ren_row_${idx}_activity" class="field-input bty-input">
          <option value="">— select activity —</option>
          ${REN_ACTIVITIES.map(a => `<option value="${a}">${a}</option>`).join('')}
        </select>
      </td>
      <td>
        <input type="number" name="ren_row_${idx}_value"
               class="field-input bty-input" placeholder="0" step="any" min="0"/>
      </td>
      <td>
        <input type="text" name="ren_row_${idx}_source"
               class="field-input bty-input" placeholder="Source"/>
      </td>
      <td class="bty-x-cell">
        <button type="button" class="row-x-btn" title="Remove">${X_SVG}</button>
      </td>`;
    const del = tr.querySelector('.row-x-btn');
    if (del) del.addEventListener('click', () => { tr.remove(); saveFormData(); });
    tr.querySelectorAll('input, select').forEach(el =>
      el.addEventListener('change', () => saveFormData()));
    return tr;
  }

  function buildRenTable(host) {
    host.innerHTML = '';
    const tbody = buildBtyTable(host,
      `<tr>
         <th style="min-width:200px">Activity</th>
         <th style="min-width:130px">Value (MWh)</th>
         <th style="min-width:160px">Source</th>
         <th style="width:32px"></th>
       </tr>`,
      'renTbody', '520px');

    let ctr = 0;
    tbody.appendChild(makeRenRow(ctr++));

    appendAddBtn(host, () => {
      tbody.appendChild(makeRenRow(ctr++));
      saveFormData();
    });
  }

  // ══════════════════════════════════════════════════════════════════
  //  C. ELECTRICITY GENERATION — FIXED rows (questionnaire rows 129-149)
  //  Columns (row 129): Electricity Generation Source | Generation Technology |
  //    Installed Capacity (MW) | Generation for Base Year (MWh) |
  //    Operational Capacity for Base Year (%) | Source
  //  Structure: group header rows + data rows + TOTAL auto-sum row
  //  Ocean Energy has 3 technology sub-rows (Tidal / wave / Ocean Thermal)
  // ══════════════════════════════════════════════════════════════════
  const ELEC_GEN_ROWS = [
    // RENEWABLE MIX (row 130)
    { group: 'RENEWABLE MIX' },
    { src: 'Solar (Photovoltaic)', tech: 'Solar PV' },        // row 131
    { src: 'Solar (CSP)',          tech: 'Solar PV' },        // row 132
    { src: 'Wind',                 tech: 'Wind Turbines' },   // row 133
    { src: 'Large Hydel',          tech: 'Hydroelectric' },   // row 134
    { src: 'Small Hydel',          tech: 'Hydroelectric' },   // row 135
    { src: 'Biomass',              tech: '' },                 // row 136
    { src: 'Geothermal Energy',    tech: 'Geothermal' },      // row 137
    { src: 'Ocean Energy',         tech: 'Tidal' },           // row 138 — first sub-row
    { src: '',                     tech: 'wave' },            // row 139 — blank source, sub-row
    { src: '',                     tech: 'Ocean Thermal' },   // row 140 — blank source, sub-row
    // NUCLEAR (row 141)
    { group: 'NUCLEAR' },
    { src: 'Nuclear',              tech: 'Nuclear Fission/Fusion' }, // row 142
    // GAS (row 143)
    { group: 'GAS' },
    { src: 'Natural Gas',          tech: 'Combined Cycle' },  // row 144
    // SOLID WASTE (row 145)
    { group: 'SOLID WASTE' },
    { src: 'Municipal Wastes (all)', tech: 'Steam Generator' }, // row 146
    // COAL (row 147)
    { group: 'COAL' },
    { src: 'Coal',                 tech: 'Combined Cycle' },  // row 148
    // TOTAL (row 149)
    { total: true },
  ];

  function buildElecGenTable(host) {
    host.innerHTML = '';
    const scroll = document.createElement('div');
    scroll.className = 'bty-table-scroll';
    const table = document.createElement('table');
    table.className = 'bty-table';
    table.style.minWidth = '900px';
    table.innerHTML = `
      <thead><tr>
        <th style="min-width:220px">Electricity Generation Source</th>
        <th style="min-width:185px">Generation Technology</th>
        <th style="min-width:155px">Installed Capacity (MW)</th>
        <th style="min-width:195px">Generation for Base Year (MWh)</th>
        <th style="min-width:220px">Operational Capacity for Base Year (%)</th>
        <th style="min-width:130px">Source</th>
      </tr></thead>`;
    const tbody = document.createElement('tbody');

    ELEC_GEN_ROWS.forEach(row => {
      const tr = document.createElement('tr');
      if (row.group) {
        tr.className = 'group-row';
        tr.innerHTML = `<td colspan="6">${row.group}</td>`;
      } else if (row.total) {
        tr.className = 'subtotal-row';
        tr.innerHTML = `
          <td class="bty-label" style="font-weight:700">TOTAL</td>
          <td></td>
          <td><input type="number" name="elec_total_cap" class="field-input bty-input"
                     placeholder="0" readonly style="font-weight:700;background:var(--light,#f4f7fc)"/></td>
          <td><input type="number" name="elec_total_gen" class="field-input bty-input"
                     placeholder="0" readonly style="font-weight:700;background:var(--light,#f4f7fc)"/></td>
          <td></td><td></td>`;
      } else {
        const slug = (row.src + '_' + row.tech).toLowerCase().replace(/[^a-z0-9]+/g, '_');
        tr.innerHTML = `
          <td class="bty-label">${row.src || ''}</td>
          <td><input type="text" name="elec_${slug}_tech" class="field-input bty-input"
                     value="${row.tech}" placeholder="Technology"/></td>
          <td><input type="number" name="elec_${slug}_cap" class="field-input bty-input"
                     placeholder="0" step="any" min="0"/></td>
          <td><input type="number" name="elec_${slug}_gen" class="field-input bty-input"
                     placeholder="0" step="any" min="0"/></td>
          <td><input type="number" name="elec_${slug}_pct" class="field-input bty-input"
                     placeholder="%" step="0.01" min="0" max="100"/></td>
          <td><input type="text" name="elec_${slug}_src" class="field-input bty-input"
                     placeholder="Source"/></td>`;
      }
      tbody.appendChild(tr);
    });

    table.appendChild(tbody);
    scroll.appendChild(table);
    host.appendChild(scroll);

    // Auto-sum TOTAL: sum all _cap and _gen inputs (excluding total row)
    table.addEventListener('input', () => {
      let tc = 0, tg = 0;
      table.querySelectorAll('input[name$="_cap"]:not([name="elec_total_cap"])')
        .forEach(el => { tc += parseFloat(el.value) || 0; });
      table.querySelectorAll('input[name$="_gen"]:not([name="elec_total_gen"])')
        .forEach(el => { tg += parseFloat(el.value) || 0; });
      const ce = table.querySelector('[name="elec_total_cap"]');
      const ge = table.querySelector('[name="elec_total_gen"]');
      if (ce) ce.value = tc || '';
      if (ge) ge.value = tg || '';
      saveFormData();
    });
  }

  // ══════════════════════════════════════════════════════════════════
  //  BOOTSTRAP
  // ══════════════════════════════════════════════════════════════════
  let extraCounters = { res: 0, com: 0, ins: 0 };   // legacy compat shim

  function buildAllInitialRows() {
    buildSimpleTable('resHost', 'res', 'res_area');
    buildSimpleTable('comHost', 'com', 'com_area');
    buildSimpleTable('insHost', 'ins', 'ins_area');

    const mh = document.getElementById('mfgRowsHost');
    if (mh) buildMfgTable(mh);

    const eh = document.getElementById('eindRowsHost');
    if (eh) buildEindTable(eh);

    const fh = document.getElementById('fugRowsHost');
    if (fh) buildFugTable(fh);

    const rh = document.getElementById('renRowsHost');
    if (rh) buildRenTable(rh);

    const eg = document.getElementById('elecGenHost');
    if (eg) buildElecGenTable(eg);
  }

})();
