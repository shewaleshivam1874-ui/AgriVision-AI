/**
 * AgriVision AI - Global Scroll Reveal, Micro-Interactions & Cursor Glow Engine
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollProgressBar();
  initScrollRevealObserver();
  initNavbarScrollState();
  initDesktopCursorGlow();
  initFormMicroInteractions();
});

/**
 * 1. Top Thin Scroll Progress Bar
 */
function initScrollProgressBar() {
  const progressBar = document.createElement('div');
  progressBar.className = 'scroll-progress-bar';
  document.body.appendChild(progressBar);

  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    progressBar.style.width = scrolled + '%';
  }, { passive: true });
}

/**
 * 2. IntersectionObserver Scroll Reveal System
 */
function initScrollRevealObserver() {
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.12
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');

        // Handle stagger children delay
        if (entry.target.classList.contains('stagger-reveal')) {
          const children = entry.target.children;
          Array.from(children).forEach((child, index) => {
            child.style.transitionDelay = `${index * 80}ms`;
          });
        }

        // Unobserve after animating unless specified
        if (!entry.target.hasAttribute('data-animate-repeat')) {
          observer.unobserve(entry.target);
        }
      }
    });
  }, observerOptions);

  // Target all elements marked for animation or grid cards
  const animTargets = document.querySelectorAll('[data-animate], .fade-up, .fade-down, .fade-left, .fade-right, .scale-in, .blur-reveal, .stagger-reveal, .feature-card, .step-card, .info-card');

  animTargets.forEach(el => {
    if (!el.hasAttribute('data-animate') && !el.classList.contains('is-visible')) {
      el.classList.add('fade-up');
    }
    revealObserver.observe(el);
  });
}

/**
 * 3. Navbar Scroll Shrink & Shadow
 */
function initNavbarScrollState() {
  const navbar = document.querySelector('.navbar');
  if (!navbar) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      navbar.classList.add('nav-scrolled');
    } else {
      navbar.classList.remove('nav-scrolled');
    }
  }, { passive: true });
}

/**
 * 4. Desktop Cursor Proximity Glow
 */
function initDesktopCursorGlow() {
  // Check if touch device or reduced motion
  if ('ontouchstart' in window || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return;
  }

  const glow = document.createElement('div');
  glow.className = 'cursor-glow';
  document.body.appendChild(glow);

  let mouseX = 0, mouseY = 0;
  let glowX = 0, glowY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    
    // Activate glow when hovering key interactive containers
    const interactiveTarget = e.target.closest('.hero-section, .tree-3d-wrapper, .upload-card, .feature-card, .prob-card, .xai-section');
    if (interactiveTarget) {
      glow.classList.add('active');
    } else {
      glow.classList.remove('active');
    }
  });

  function animateGlow() {
    glowX += (mouseX - glowX) * 0.15;
    glowY += (mouseY - glowY) * 0.15;
    glow.style.transform = `translate3d(${glowX}px, ${glowY}px, 0)`;
    requestAnimationFrame(animateGlow);
  }
  requestAnimationFrame(animateGlow);
}

/**
 * 5. Form Focus & Input Micro-Interactions
 */
function initFormMicroInteractions() {
  const inputs = document.querySelectorAll('input, select, textarea');
  inputs.forEach(input => {
    input.addEventListener('focus', () => {
      if (input.parentElement) {
        input.parentElement.classList.add('input-focused');
      }
    });
    input.addEventListener('blur', () => {
      if (input.parentElement) {
        input.parentElement.classList.remove('input-focused');
      }
    });
  });
}
