  document.addEventListener('DOMContentLoaded', () => {
    const filters = document.getElementById('filters');
    const bar = document.querySelector('.results-bar');
    if (window.innerWidth <= 900 && bar) {
      const toggleBtn = document.createElement('button');
      toggleBtn.textContent = 'Filters';
      toggleBtn.className = 'filters-toggle-btn';
      bar.parentNode.insertBefore(toggleBtn, bar);
      toggleBtn.addEventListener('click', () => filters.classList.toggle('open'));
    }
  });