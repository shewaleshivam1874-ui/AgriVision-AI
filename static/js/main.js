/**
 * AgriVision AI - Global Application JavaScript & Toast Generator
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initDiseaseLibraryFilter();
  initContactFormValidation();
});

/**
 * Mobile Navigation Menu Toggle
 */
function initMobileMenu() {
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
      const isExpanded = navMenu.classList.contains('active');
      navToggle.setAttribute('aria-expanded', isExpanded);
      navToggle.innerHTML = isExpanded ? '✕' : '☰';
    });

    document.addEventListener('click', (e) => {
      if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
        navMenu.classList.remove('active');
        if (navToggle) navToggle.innerHTML = '☰';
      }
    });
  }
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
      showToast('Please fill in all required fields before submitting.', 'error');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      e.preventDefault();
      showToast('Please enter a valid email address.', 'error');
    }
  });
}
