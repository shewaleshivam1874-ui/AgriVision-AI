/**
 * AgriVision AI - Analyze Leaf Controller & 7-Stage Loader Engine
 * Multilingual error messaging, sample loading, and state management.
 */

document.addEventListener('DOMContentLoaded', () => {
  const uploadCard = document.getElementById('uploadCard');
  const fileInput = document.getElementById('fileInput');
  const browseBtn = document.getElementById('browseBtn');
  const previewWrapper = document.getElementById('previewWrapper');
  const previewImg = document.getElementById('previewImg');
  const removeBtn = document.getElementById('removeImgBtn');
  const changeImgBtn = document.getElementById('changeImgBtn');
  const analyzeBtn = document.getElementById('analyzeBtn');
  const loadingOverlay = document.getElementById('loadingOverlay');
  const errorAlert = document.getElementById('uploadErrorAlert');
  const defaultState = document.getElementById('dropzoneDefaultState');
  const fileMetaInfo = document.getElementById('fileMetaInfo');
  const sampleCards = document.querySelectorAll('.sample-leaf-card');

  if (!uploadCard || !fileInput) return;

  let selectedFile = null;

  function getLang() {
    return localStorage.getItem('agrivision_lang') || document.documentElement.getAttribute('lang') || 'en';
  }

  function getMsg(key, fallback) {
    if (typeof getTranslation === 'function') {
      return getTranslation(key, getLang());
    }
    return fallback;
  }

  // 1. Browse & Click Triggers
  if (browseBtn) {
    browseBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      fileInput.click();
    });
  }

  if (changeImgBtn) {
    changeImgBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      fileInput.click();
    });
  }

  uploadCard.addEventListener('click', () => {
    if (!selectedFile) {
      fileInput.click();
    }
  });

  // 2. Drag & Drop Handlers
  ['dragenter', 'dragover'].forEach(eventName => {
    uploadCard.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      uploadCard.classList.add('drag-over');
    }, false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    uploadCard.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      uploadCard.classList.remove('drag-over');
    }, false);
  });

  uploadCard.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length > 0) {
      handleFile(files[0]);
    }
  });

  fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
      handleFile(fileInput.files[0]);
    }
  });

  // 3. Sample Quick Test Cards Click Handler
  sampleCards.forEach(card => {
    card.addEventListener('click', () => {
      const sampleUrl = card.getAttribute('data-sample');
      if (sampleUrl) {
        fetch(sampleUrl)
          .then(res => res.blob())
          .then(blob => {
            const file = new File([blob], "sample_leaf.jpg", { type: "image/jpeg" });
            handleFile(file);
          })
          .catch(err => {
            console.error("Failed to load sample image:", err);
          });
      }
    });
  });

  // 4. File Processing & Pre-Upload Validation
  function handleFile(file) {
    hideError();

    const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
    const ext = file.name.split('.').pop().toLowerCase();
    
    if (!allowedTypes.includes(file.type) && !['jpg', 'jpeg', 'png', 'webp'].includes(ext)) {
      showError(getMsg('err_unsupported_format', 'Unsupported file format. Please upload a JPG, JPEG, PNG, or WEBP image.'));
      return;
    }

    if (file.size > 10 * 1024 * 1024) {
      showError(getMsg('err_file_too_large', 'File size exceeds the 10 MB limit. Please select a smaller leaf image.'));
      return;
    }

    selectedFile = file;

    const reader = new FileReader();
    reader.onload = (e) => {
      previewImg.src = e.target.result;
      previewWrapper.style.display = 'block';
      if (defaultState) defaultState.style.display = 'none';
      if (analyzeBtn) analyzeBtn.removeAttribute('disabled');
      
      const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
      if (fileMetaInfo) {
        const prefix = getMsg('selected_file_label', 'Selected: ');
        fileMetaInfo.textContent = `${prefix}${file.name} (${sizeMB} MB)`;
      }
      
      uploadCard.style.borderStyle = 'solid';
    };
    reader.readAsDataURL(file);
  }

  // 5. Remove Image
  if (removeBtn) {
    removeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      resetUpload();
    });
  }

  function resetUpload() {
    selectedFile = null;
    fileInput.value = '';
    previewImg.src = '';
    previewWrapper.style.display = 'none';
    if (defaultState) defaultState.style.display = 'block';
    if (analyzeBtn) analyzeBtn.setAttribute('disabled', 'true');
    if (fileMetaInfo) fileMetaInfo.textContent = '';
    uploadCard.style.borderStyle = 'dashed';
    hideError();
  }

  // 6. Submit to /api/analyze-leaf API with Gemini AI Vision & Animated Loader
  if (analyzeBtn) {
    analyzeBtn.addEventListener('click', () => {
      if (!selectedFile) {
        showError(getMsg('err_select_image', 'Please select or drop a crop leaf image first.'));
        return;
      }

      showLoading();
      animate7StageProgress();
      analyzeBtn.setAttribute('disabled', 'true');

      const currentLang = getLang();
      const formData = new FormData();
      formData.append('file', selectedFile);
      formData.append('lang', currentLang);

      fetch('/api/analyze-leaf', {
        method: 'POST',
        body: formData
      })
      .then(async response => {
        const data = await response.json();
        if (!response.ok || !data.success) {
          const errMsg = data.message || data.error || getMsg('err_analysis_failed', 'Failed to complete crop analysis.');
          throw new Error(errMsg);
        }
        return data;
      })
      .then(data => {
        if (data.success && data.redirect_url) {
          window.location.href = data.redirect_url;
        } else {
          hideLoading();
          analyzeBtn.removeAttribute('disabled');
          showError(data.message || getMsg('err_analysis_failed', 'Failed to complete crop analysis.'));
        }
      })
      .catch(err => {
        hideLoading();
        analyzeBtn.removeAttribute('disabled');
        showError(err.message || getMsg('err_network_error', 'Network error occurred while processing image.'));
      });
    });
  }

  function animate7StageProgress() {
    const stageIds = ['stage1', 'stage2', 'stage3', 'stage4'];
    let currentStage = 0;
    
    const interval = setInterval(() => {
      stageIds.forEach((id, idx) => {
        const elem = document.getElementById(id);
        if (elem) {
          if (idx <= currentStage) {
            elem.classList.add('active');
            if (!elem.textContent.startsWith('✓')) {
              elem.textContent = '✓ ' + elem.textContent;
            }
          }
        }
      });
      currentStage++;
      if (currentStage >= stageIds.length) {
        clearInterval(interval);
      }
    }, 400);
  }

  function showLoading() {
    if (loadingOverlay) loadingOverlay.style.display = 'flex';
  }

  function hideLoading() {
    if (loadingOverlay) loadingOverlay.style.display = 'none';
  }

  function showError(msg) {
    if (errorAlert) {
      errorAlert.textContent = msg;
      errorAlert.style.display = 'block';
    }
  }

  function hideError() {
    if (errorAlert) {
      errorAlert.style.display = 'none';
      errorAlert.textContent = '';
    }
  }
});
