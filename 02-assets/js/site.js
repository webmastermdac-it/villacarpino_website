/* Minimal progressive enhancement. The mobile menu uses native HTML details. */
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('request-form');
  const status = document.getElementById('form-status');
  if (form && status) {
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      status.classList.add('visible');
      status.textContent = 'Questo è un prototipo HTML: nessun dato è stato inviato. Per contattare Villa Carpino chiama il numero 030 652114.';
      status.focus?.();
    });
  }
  // Only one mobile menu stays open at a time; Escape closes it.
  const menu = document.querySelector('.vc-mobile-menu');
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu?.open) {
      menu.open = false;
      menu.querySelector('summary')?.focus();
    }
  });
});
