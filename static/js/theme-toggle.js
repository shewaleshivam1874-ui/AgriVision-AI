/**
 * AgriVision AI - Light / Dark Theme Switcher
 * Persists user preference using localStorage and respects system prefers-color-scheme.
 */

(function () {
  // Execute immediately before DOM render to prevent theme flash
  const savedTheme = localStorage.getItem('agrivision_theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  const theme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
  document.documentElement.setAttribute('data-theme', theme);
})();

document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  const themeIcon = document.getElementById('themeIcon');

  function updateToggleUI(theme) {
    if (themeIcon) {
      themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
    }
    if (themeToggleBtn) {
      themeToggleBtn.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`);
      themeToggleBtn.setAttribute('title', `Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`);
    }
  }

  const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
  updateToggleUI(currentTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const activeTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = activeTheme === 'dark' ? 'light' : 'dark';
      
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('agrivision_theme', newTheme);
      updateToggleUI(newTheme);
    });
  }
});
