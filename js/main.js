/* ============================================================
   SUMMIT WALL SOLUTIONS — main.js
   Header scroll, mobile menu, active link, FAQ, reveal,
   estimate calculator, contact form (Web3Forms-ready)
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ---- Header scroll state ---- */
  const header = document.querySelector('.site-header');
  if (header) {
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 40);
    onScroll();
    window.addEventListener('scroll', onScroll);
  }

  /* ---- Mobile menu ---- */
  const burger = document.querySelector('.burger');
  const navLinks = document.querySelector('.nav-links');
  if (burger && navLinks) {
    burger.addEventListener('click', () => navLinks.classList.toggle('open'));
    navLinks.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => navLinks.classList.remove('open'))
    );
  }

  /* ---- Active nav link (based on current file) ---- */
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    const href = a.getAttribute('href');
    if (href && (href === path || (path === '' && href === 'index.html'))) {
      a.classList.add('active');
    }
  });

  /* ---- Footer year ---- */
  const yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();

  /* ---- FAQ accordion ---- */
  document.querySelectorAll('.faq-q').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.parentElement;
      const open = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!open) item.classList.add('open');
    });
  });

  /* ---- Reveal on scroll ---- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  /* ---- Chip toggles (calculator) ---- */
  document.querySelectorAll('[data-group]').forEach(group => {
    const multi = group.dataset.group === 'multi';
    group.querySelectorAll('.chip').forEach(chip => {
      chip.addEventListener('click', () => {
        if (multi) {
          chip.classList.toggle('active');
        } else {
          group.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
        }
      });
    });
  });

  /* ---- Estimate calculator ---- */
  const calcBtn = document.getElementById('calc-run');
  if (calcBtn) {
    const rates = { frame:[3.5,5.5], insulation:[1.25,2.0], drywall:[1.75,3.0], taping:[0.8,1.75], painting:[1.25,2.0] };
    const flatRates = { cleanup:[300,600] };
    const sizes = { small:250, medium:800, large:1800 };
    calcBtn.addEventListener('click', () => {
      const services = [...document.querySelectorAll('[data-svc].active')].map(c => c.dataset.svc);
      if (!services.length) { alert('Please select at least one service.'); return; }
      const sizeChip = document.querySelector('[data-size].active');
      const size = sizeChip ? sizeChip.dataset.size : 'medium';
      const sqft = sizes[size];
      const commercial = document.querySelector('[data-type].active')?.dataset.type === 'com';
      let lo = 0, hi = 0;
      services.forEach(s => {
        if (rates[s]) { lo += rates[s][0]*sqft; hi += rates[s][1]*sqft; }
        else if (flatRates[s]) { lo += flatRates[s][0]; hi += flatRates[s][1]; }
      });
      if (commercial) { lo *= 1.2; hi *= 1.3; }
      lo = Math.max(Math.round(lo/50)*50, 800);
      hi = Math.max(Math.round(hi/100)*100, 1200);
      document.getElementById('calc-lo').textContent = lo.toLocaleString();
      document.getElementById('calc-hi').textContent = hi.toLocaleString();
      document.getElementById('calc-sqft').textContent = sqft.toLocaleString();
      const res = document.getElementById('calc-result');
      res.classList.add('show');
      res.scrollIntoView({ behavior:'smooth', block:'nearest' });
    });
  }

  /* ---- Contact form ----
     Default: opens a pre-filled email (mailto).
     To make it submit silently, create a free Web3Forms access key
     (https://web3forms.com) and set FORM_ACCESS_KEY below. */
  const FORM_ACCESS_KEY = ''; // <-- paste Web3Forms key here to enable AJAX submit
  const form = document.getElementById('quote-form');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const data = Object.fromEntries(new FormData(form).entries());
      const typeChip = document.querySelector('[data-ptype].active');
      data.project_type = typeChip ? typeChip.dataset.ptype : 'Residential';
      if (!data.name || !data.phone) { alert('Please add your name and phone.'); return; }

      if (FORM_ACCESS_KEY) {
        try {
          const r = await fetch('https://api.web3forms.com/submit', {
            method:'POST', headers:{'Content-Type':'application/json'},
            body: JSON.stringify({ access_key: FORM_ACCESS_KEY, subject:'New estimate request — Summit Wall', ...data })
          });
          if (r.ok) { showSuccess(); return; }
        } catch (_) {}
      }
      // Fallback: mailto
      const subject = encodeURIComponent('Free Estimate Request — ' + (data.service||'') + ' (' + data.project_type + ')');
      const body = encodeURIComponent('Name: '+data.name+'\nPhone: '+data.phone+'\nType: '+data.project_type+'\nService: '+(data.service||'')+'\n\n'+(data.message||''));
      window.location.href = 'mailto:Rodrigo@summitwallsolutions.com?subject='+subject+'&body='+body;
      showSuccess();
    });
  }
  function showSuccess() {
    const ok = document.getElementById('form-success');
    if (ok) { form.style.display = 'none'; ok.style.display = 'block'; }
  }
});
