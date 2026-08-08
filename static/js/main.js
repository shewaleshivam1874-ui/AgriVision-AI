/**
 * AgriVision AI - Global Application JavaScript & Responsive Interactivity Engine
 * Multilingual toast notices, localized copy summaries, and form validation.
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initDiseaseLibraryFilter();
  initContactFormValidation();
});

function getActiveLang() {
  return localStorage.getItem('agrivision_lang') || document.documentElement.getAttribute('lang') || 'en';
}

function getLocalizedText(key, fallback) {
  if (typeof getTranslation === 'function') {
    return getTranslation(key, getActiveLang());
  }
  return fallback;
}

/**
 * Mobile Navigation Menu Toggle & Accessibility
 */
function initMobileMenu() {
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (!navToggle || !navMenu) return;

  function closeMenu() {
    navMenu.classList.remove('active');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.innerHTML = '☰';
  }

  function toggleMenu() {
    const isActive = navMenu.classList.toggle('active');
    navToggle.setAttribute('aria-expanded', String(isActive));
    navToggle.innerHTML = isActive ? '✕' : '☰';
  }

  navToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleMenu();
  });

  // Close when clicking any nav link or CTA button inside mobile menu
  navMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth <= 992) {
        closeMenu();
      }
    });
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
      if (navMenu.classList.contains('active')) {
        closeMenu();
      }
    }
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navMenu.classList.contains('active')) {
      closeMenu();
    }
  });

  // Reset menu state on desktop resize / orientation change
  window.addEventListener('resize', () => {
    if (window.innerWidth > 992 && navMenu.classList.contains('active')) {
      closeMenu();
    }
  }, { passive: true });
}

/**
 * Toast Notification Generator
 */
function showToast(message, type = 'info') {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  
  const icon = type === 'success' ? '✓' : type === 'error' ? '✕' : 'ℹ️';
  toast.innerHTML = `<span>${icon}</span> <div>${message}</div>`;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

/**
 * Disease Library Search & Crop Filters
 */
function initDiseaseLibraryFilter() {
  const searchInput = document.getElementById('diseaseSearchInput');
  const filterChips = document.querySelectorAll('.filter-chip');
  const diseaseCards = document.querySelectorAll('.disease-card');

  if (!diseaseCards.length) return;

  let currentCrop = 'All';
  let searchQuery = '';

  function filterCards() {
    diseaseCards.forEach(card => {
      const cardCrop = card.getAttribute('data-crop') || '';
      const cardTitle = card.querySelector('.disease-card-title')?.textContent.toLowerCase() || '';
      const cardDesc = card.querySelector('.disease-card-desc')?.textContent.toLowerCase() || '';
      
      const matchesCrop = (currentCrop === 'All') || (cardCrop.toLowerCase() === currentCrop.toLowerCase());
      const matchesSearch = !searchQuery || cardTitle.includes(searchQuery) || cardDesc.includes(searchQuery) || cardCrop.toLowerCase().includes(searchQuery);

      if (matchesCrop && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
      filterChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      currentCrop = chip.getAttribute('data-crop') || 'All';
      filterCards();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      filterCards();
    });
  }
}

/**
 * Contact Form Validation
 */
function initContactFormValidation() {
  const contactForm = document.getElementById('contactForm');
  if (!contactForm) return;

  contactForm.addEventListener('submit', (e) => {
    const name = document.getElementById('name')?.value.trim();
    const email = document.getElementById('email')?.value.trim();
    const message = document.getElementById('message')?.value.trim();

    if (!name || !email || !message) {
      e.preventDefault();
      showToast(getLocalizedText('toast_form_required', 'Please fill in all required fields before submitting.'), 'error');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      e.preventDefault();
      showToast(getLocalizedText('toast_valid_email', 'Please enter a valid email address.'), 'error');
    }
  });
}

/**
 * Diagnostic Dashboard Print Trigger
 */
function printReport() {
  window.print();
}

/**
 * Diagnostic Dashboard Copy Summary to Clipboard
 */
function copyDiagnosticSummary(cropName, condition, confidence, urgency) {
  const lang = getActiveLang();
  const reportHeader = getLocalizedText('report_title', 'AgriVision AI Diagnostic Report');
  const cropLabel = getLocalizedText('card_crop_species', 'Crop');
  const condLabel = getLocalizedText('card_condition', 'Condition');
  const confLabel = getLocalizedText('card_confidence', 'Confidence');
  const urgLabel = getLocalizedText('card_action_urgency', 'Action Urgency');
  
  const summaryText = `${reportHeader}:\n• ${cropLabel}: ${cropName}\n• ${condLabel}: ${condition}\n• ${confLabel}: ${confidence}\n• ${urgLabel}: ${urgency}\n• Date: ${new Date().toLocaleDateString()}`;
  
  const successMsg = getLocalizedText('toast_copied', 'Diagnostic summary copied to clipboard!');
  const failMsg = getLocalizedText('toast_copy_failed', 'Failed to copy summary to clipboard.');

  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(summaryText)
      .then(() => showToast(successMsg, 'success'))
      .catch(() => showToast(failMsg, 'error'));
  } else {
    // Fallback for non-https contexts
    const textArea = document.createElement('textarea');
    textArea.value = summaryText;
    textArea.style.position = 'fixed';
    textArea.style.opacity = '0';
    document.body.appendChild(textArea);
    textArea.select();
    try {
      document.execCommand('copy');
      showToast(successMsg, 'success');
    } catch (err) {
      showToast(failMsg, 'error');
    }
    document.body.removeChild(textArea);
  }
}

/**
 * Smooth Jump Navigation
 */
function scrollToSection(sectionId) {
  const target = document.getElementById(sectionId);
  if (target) {
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}
