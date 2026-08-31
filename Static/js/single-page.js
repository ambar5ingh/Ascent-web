/* ═══════════════════════════════════════════════════════
   ASCENT — Single-page nav patch
   Load AFTER form.js. Converts the multi-step UX into a
   scroll-spy single-page experience without touching the
   existing form fields, save/restore, or submit logic.
═══════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ── 1. Smooth-scroll when a progress-strip label is clicked ──
  // form.js already binds .ps clicks to its multi-step goTo().
  // We need to override that: re-bind in the capture phase so we run first
  // and stop the original handler from firing.
  document.querySelectorAll('.ps').forEach((p) => {
    p.addEventListener(
      'click',
      (e) => {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        const idx = parseInt(p.dataset.sec, 10);
        const target = document.querySelector(`.form-section[data-section="${idx}"]`);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      },
      true /* capture */
    );
  });

  // ── 2. Scroll-spy: highlight section as it enters viewport ──
  const sections = Array.from(document.querySelectorAll('.form-section'));
  const labels = Array.from(document.querySelectorAll('.ps'));

  function clearActive() {
    sections.forEach((s) => s.classList.remove('in-view'));
    labels.forEach((l) => l.classList.remove('in-view', 'active'));
    const fill = document.getElementById('progressFill');
    if (fill) fill.style.width = '0%';
  }

  const io = new IntersectionObserver(
    (entries) => {
      // Pick the entry closest to the top of the viewport
      const visible = entries
        .filter((e) => e.isIntersecting)
        .sort((a, b) => Math.abs(a.boundingClientRect.top) - Math.abs(b.boundingClientRect.top));
      if (!visible.length) return;
      const top = visible[0].target;
      const idx = parseInt(top.dataset.section, 10);
      clearActive();
      top.classList.add('in-view');
      const label = labels.find((l) => parseInt(l.dataset.sec, 10) === idx);
      if (label) label.classList.add('in-view', 'active');
      // Progress bar reflects scroll progress through the form
      const fill = document.getElementById('progressFill');
      if (fill && sections.length > 1) {
        fill.style.width = ((idx / (sections.length - 1)) * 100) + '%';
      }
    },
    { rootMargin: '-30% 0px -55% 0px', threshold: 0 }
  );
  sections.forEach((s) => io.observe(s));

  // ── 3. Floating "Calculate" + "Back to top" buttons ──
  const calcBtn = document.getElementById('calculateBtn');
  if (calcBtn) {
    const fab = document.createElement('button');
    fab.className = 'spc-fab';
    fab.type = 'button';
    fab.id = 'spcFab';
    fab.innerHTML = `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
        <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
      </svg>
      Calculate
    `;
    fab.addEventListener('click', () => {
      // Submit the form via the real button so existing handlers fire
      calcBtn.click();
      // Smooth-scroll to the submit area so the user sees the loading state
      const sa = document.querySelector('.submit-area');
      if (sa) sa.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
    document.body.appendChild(fab);

    const top = document.createElement('button');
    top.className = 'spc-top';
    top.type = 'button';
    top.id = 'spcTop';
    top.title = 'Back to top';
    top.innerHTML = `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
        <path d="M18 15l-6-6-6 6"/>
      </svg>
    `;
    top.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    document.body.appendChild(top);

    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) top.classList.add('visible');
      else top.classList.remove('visible');
    });
  }

  // ── 4. Neutralize form.js' goTo so its restore-on-load doesn't
  //       hide all but one section on subsequent restoreFormData() calls.
  //       We monkey-patch by re-asserting visibility shortly after load.
  function reassertVisible() {
    sections.forEach((s) => {
      s.classList.add('active');
      s.style.display = 'block';
    });
  }
  reassertVisible();
  // Catch the post-cities restoreFormData call (which fires goTo)
  setTimeout(reassertVisible, 300);
  setTimeout(reassertVisible, 1500);

})();
