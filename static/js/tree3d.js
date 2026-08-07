/**
 * AgriVision AI - Realistic 360° Interactive 3D Smart Tree Engine
 * Clean, instruction-free, high-performance WebGL tree with dynamic cursor states,
 * realistic procedural geometry, breeze physics, occlusion handling, and interactive identity focus panels.
 */

class AgriVisionSmartTree {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    if (!this.container || typeof THREE === 'undefined') return;

    this.scene = null;
    this.camera = null;
    this.renderer = null;
    this.treeGroup = null;
    this.leaves = [];
    this.nodes = [];
    this.particles = [];
    this.raycaster = new THREE.Raycaster();
    this.mouse = new THREE.Vector2(-999, -999);

    this.isDragging = false;
    this.previousMousePosition = { x: 0, y: 0 };
    this.targetRotationY = 0;
    this.currentRotationY = 0;
    this.autoRotate = true;
    this.autoRotateTimer = null;
    this.hoveredNode = null;
    this.focusedNode = null;

    this.identities = [
      {
        id: 'roots_data',
        title: 'Data Foundation',
        tag: 'ROOTS',
        icon: '🌱',
        shortDesc: 'Structured agricultural dataset and disease knowledge.',
        fullDesc: 'Crop images, disease knowledge base, and structured agricultural diagnostics form the foundational layer of AgriVision AI.',
        position: new THREE.Vector3(0, -2.0, 0.5),
        side: 'Roots'
      },
      {
        id: 'trunk_core',
        title: 'AI Intelligence',
        tag: 'TRUNK',
        icon: '🧠',
        shortDesc: 'Central AI system analyzing crop health.',
        fullDesc: 'The central neural engine connects image analysis, crop species identification, and preliminary disease diagnosis.',
        position: new THREE.Vector3(0, -0.2, 0.1),
        side: 'Core'
      },
      {
        id: 'crop_rec',
        title: 'Crop Recognition',
        tag: 'BRANCH',
        icon: '🌿',
        shortDesc: 'Identifies the crop species in uploaded photos.',
        fullDesc: 'Identifies specific crop foliage species (e.g. Tomato, Potato, Pepper, Apple) to contextualize disease detection.',
        position: new THREE.Vector3(1.3, 0.7, 0.8),
        side: 'Front Right'
      },
      {
        id: 'disease_det',
        title: 'Disease Detection',
        tag: 'BRANCH',
        icon: '🔍',
        shortDesc: 'Analyzes visual leaf disease symptoms.',
        fullDesc: 'Scans for chlorosis, necrotic spot lesions, blight, rust, and pest damage patterns across leaf foliage.',
        position: new THREE.Vector3(-1.4, 1.1, 0.7),
        side: 'Front Left'
      },
      {
        id: 'confidence_analysis',
        title: 'Confidence Analysis',
        tag: 'LEAF',
        icon: '📊',
        shortDesc: 'Evaluates diagnostic certainty level.',
        fullDesc: 'Calculates categorical prediction confidence (High, Medium, Low) to ensure transparent diagnostic reporting.',
        position: new THREE.Vector3(1.7, 1.6, -0.7),
        side: 'Right'
      },
      {
        id: 'disease_severity',
        title: 'Disease Severity',
        tag: 'LEAF',
        icon: '🎯',
        shortDesc: 'Estimates pathology progression stage.',
        fullDesc: 'Evaluates affected foliage area and categorizes disease severity into Healthy, Early, Moderate, or Severe bands.',
        position: new THREE.Vector3(-1.9, 1.5, 0.1),
        side: 'Left'
      },
      {
        id: 'xai_explainability',
        title: 'Explainable AI',
        tag: 'LEAF',
        icon: '💡',
        shortDesc: 'Provides visual prediction transparency.',
        fullDesc: 'AgriVision AI uses Explainable AI techniques to clarify which visual regions influenced the model\'s diagnostic assessment.',
        position: new THREE.Vector3(-1.4, 2.1, -1.0),
        side: 'Back Left'
      },
      {
        id: 'gradcam_vis',
        title: 'Grad-CAM',
        tag: 'LEAF',
        icon: '🔥',
        shortDesc: 'Visual heatmap of neural attention.',
        fullDesc: 'Generates visual spatial heatmaps highlighting leaf regions that contributed most to the AI model prediction.',
        position: new THREE.Vector3(1.1, 2.3, -1.3),
        side: 'Back Right'
      },
      {
        id: 'smart_guidance',
        title: 'Smart Guidance',
        tag: 'FRUIT',
        icon: '⚙️',
        shortDesc: 'Actionable organic & chemical recommendations.',
        fullDesc: 'Connects preliminary diagnostics with prioritized farmer actions, organic options, chemical guidelines, and fertilizer advice.',
        position: new THREE.Vector3(0.5, 2.6, 0.9),
        side: 'Front Canopy'
      },
      {
        id: 'sustainable_agri',
        title: 'Sustainable Agriculture',
        tag: 'CANOPY',
        icon: '🌾',
        shortDesc: 'Promotes early detection and smarter crop management.',
        fullDesc: 'Supports earlier disease identification to minimize crop loss and reduce unnecessary chemical pesticide overuse.',
        position: new THREE.Vector3(0, 3.3, 0),
        side: 'Top'
      }
    ];

    this.init();
  }

  init() {
    this.createScene();
    this.createLights();
    this.createRealisticTree();
    this.createIdentityNodes();
    this.createEnvironmentalParticles();
    this.createUIElements();
    this.bindEvents();
    this.render();
  }

  createScene() {
    const width = this.container.clientWidth;
    const height = this.container.clientHeight;

    this.scene = new THREE.Scene();

    this.camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
    this.camera.position.set(0, 0.4, 9.0);
    this.camera.lookAt(0, 0.4, 0);


    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    const canvas = this.renderer.domElement;
    canvas.className = 'tree-3d-canvas';
    canvas.style.cursor = 'grab';
    this.container.appendChild(canvas);
  }

  createLights() {
    // Natural Sunlight & Skylight
    const ambientLight = new THREE.AmbientLight(0xf8fafc, 0.85);
    this.scene.add(ambientLight);

    const sunLight = new THREE.DirectionalLight(0x10b981, 1.1);
    sunLight.position.set(6, 14, 8);
    sunLight.castShadow = true;
    sunLight.shadow.mapSize.width = 1024;
    sunLight.shadow.mapSize.height = 1024;
    this.scene.add(sunLight);

    // Warm Ground Fill Light
    const groundLight = new THREE.DirectionalLight(0x064e3b, 0.4);
    groundLight.position.set(-5, -5, -5);
    this.scene.add(groundLight);

    // Soft Core Glow Point Light
    this.coreLight = new THREE.PointLight(0x34d399, 1.2, 5);
    this.coreLight.position.set(0, 0.2, 0);
    this.scene.add(this.coreLight);
  }

  createRealisticTree() {
    this.treeGroup = new THREE.Group();
    this.scene.add(this.treeGroup);

    // 1. Natural Ground Base Mound & Soft Contact Shadow
    const moundGeo = new THREE.CylinderGeometry(2.8, 3.4, 0.4, 32);
    const moundMat = new THREE.MeshStandardMaterial({
      color: 0x1e293b,
      roughness: 0.95,
      metalness: 0.05
    });
    const mound = new THREE.Mesh(moundGeo, moundMat);
    mound.position.y = -2.4;
    mound.receiveShadow = true;
    this.treeGroup.add(mound);

    // 2. Realistic Bark Trunk with Spreading Roots
    const trunkGeo = new THREE.CylinderGeometry(0.38, 0.72, 4.0, 16);
    const trunkMat = new THREE.MeshStandardMaterial({
      color: 0x334155,
      roughness: 0.75,
      metalness: 0.1
    });
    this.trunkMesh = new THREE.Mesh(trunkGeo, trunkMat);
    this.trunkMesh.position.y = -0.4;
    this.trunkMesh.castShadow = true;
    this.treeGroup.add(this.trunkMesh);

    // Spreading Natural Root Bases
    const rootMat = new THREE.MeshStandardMaterial({ color: 0x243347, roughness: 0.8 });
    for (let r = 0; r < 5; r++) {
      const rootGeo = new THREE.CylinderGeometry(0.12, 0.35, 1.2, 8);
      const rootMesh = new THREE.Mesh(rootGeo, rootMat);
      const angle = (r / 5) * Math.PI * 2;
      rootMesh.position.set(Math.cos(angle) * 0.65, -2.1, Math.sin(angle) * 0.65);
      rootMesh.rotation.z = Math.cos(angle) * 0.5;
      rootMesh.rotation.x = Math.sin(angle) * 0.5;
      this.treeGroup.add(rootMesh);
    }

    // Glowing Internal AI Core Mesh
    const coreGeo = new THREE.CylinderGeometry(0.16, 0.22, 3.6, 12);
    const coreMat = new THREE.MeshBasicMaterial({
      color: 0x10b981,
      wireframe: true,
      transparent: true,
      opacity: 0.5
    });
    this.aiCoreMesh = new THREE.Mesh(coreGeo, coreMat);
    this.aiCoreMesh.position.y = -0.4;
    this.treeGroup.add(this.aiCoreMesh);

    // 3. Curved Branch Network
    const branchMat = new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.6 });
    const branchConfigs = [
      { rTop: 0.14, rBot: 0.28, h: 2.3, rotZ: -0.65, rotY: 0.2, pos: [0.65, 0.7, 0.1] },
      { rTop: 0.14, rBot: 0.28, h: 2.3, rotZ: 0.65, rotY: 1.7, pos: [-0.65, 0.9, 0] },
      { rTop: 0.12, rBot: 0.24, h: 2.1, rotZ: -0.5, rotY: 3.2, pos: [0.55, 1.3, -0.4] },
      { rTop: 0.12, rBot: 0.24, h: 2.1, rotZ: 0.5, rotY: 4.8, pos: [-0.55, 1.5, 0.4] },
      { rTop: 0.1, rBot: 0.2, h: 1.8, rotZ: -0.4, rotY: 0.9, pos: [0.4, 2.1, 0.3] },
      { rTop: 0.1, rBot: 0.2, h: 1.8, rotZ: 0.4, rotY: 2.5, pos: [-0.4, 2.3, -0.3] }
    ];

    branchConfigs.forEach(cfg => {
      const bGeo = new THREE.CylinderGeometry(cfg.rTop, cfg.rBot, cfg.h, 10);
      const bMesh = new THREE.Mesh(bGeo, branchMat);
      bMesh.position.set(...cfg.pos);
      bMesh.rotation.z = cfg.rotZ;
      bMesh.rotation.y = cfg.rotY;
      bMesh.castShadow = true;
      this.treeGroup.add(bMesh);
    });

    // 4. Dense Multi-Hued Leaf Canopy
    const leafGeo = new THREE.ConeGeometry(0.24, 0.55, 5);
    const leafColors = [0x10b981, 0x059669, 0x34d399, 0x047857, 0x059669, 0x10b981];

    for (let i = 0; i < 160; i++) {
      const color = leafColors[i % leafColors.length];
      const leafMat = new THREE.MeshStandardMaterial({
        color: color,
        roughness: 0.35,
        metalness: 0.1
      });
      const leaf = new THREE.Mesh(leafGeo, leafMat);

      const radius = 1.1 + Math.random() * 1.7;
      const theta = Math.random() * Math.PI * 2;
      const phi = (Math.random() - 0.2) * Math.PI * 0.7;

      const x = radius * Math.cos(theta) * Math.cos(phi);
      const y = 0.5 + Math.random() * 2.9;
      const z = radius * Math.sin(theta) * Math.cos(phi);

      leaf.position.set(x, y, z);
      leaf.rotation.set(Math.random() * Math.PI, Math.random() * Math.PI, Math.random() * Math.PI);

      leaf.userData = {
        basePos: new THREE.Vector3(x, y, z),
        baseRot: leaf.rotation.clone(),
        phase: Math.random() * Math.PI * 2,
        speed: 0.7 + Math.random() * 1.1
      };

      this.leaves.push(leaf);
      this.treeGroup.add(leaf);
    }
  }

  createIdentityNodes() {
    this.identities.forEach(idData => {
      const nodeGroup = new THREE.Group();
      nodeGroup.position.copy(idData.position);

      // Subtle Illuminated Leaf/Orb Node
      const sphereGeo = new THREE.SphereGeometry(0.18, 16, 16);
      const sphereMat = new THREE.MeshStandardMaterial({
        color: 0x10b981,
        emissive: 0x059669,
        emissiveIntensity: 0.5,
        roughness: 0.3,
        metalness: 0.7
      });
      const sphereMesh = new THREE.Mesh(sphereGeo, sphereMat);
      nodeGroup.add(sphereMesh);

      // Subtle Outer Ring Marker
      const ringGeo = new THREE.RingGeometry(0.22, 0.26, 20);
      const ringMat = new THREE.MeshBasicMaterial({
        color: 0x34d399,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.5
      });
      const ringMesh = new THREE.Mesh(ringGeo, ringMat);
      ringMesh.rotation.x = Math.PI / 2;
      nodeGroup.add(ringMesh);

      nodeGroup.userData = {
        identity: idData,
        sphereMesh: sphereMesh,
        ringMesh: ringMesh
      };

      this.nodes.push(nodeGroup);
      this.treeGroup.add(nodeGroup);
    });
  }

  createEnvironmentalParticles() {
    const pGeo = new THREE.BufferGeometry();
    const pCount = 35;
    const posArray = new Float32Array(pCount * 3);

    for (let i = 0; i < pCount * 3; i += 3) {
      posArray[i] = (Math.random() - 0.5) * 7.5;
      posArray[i + 1] = -1.5 + Math.random() * 5.5;
      posArray[i + 2] = (Math.random() - 0.5) * 7.5;
    }

    pGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
    const pMat = new THREE.PointsMaterial({
      size: 0.07,
      color: 0x6ee7b7,
      transparent: true,
      opacity: 0.65
    });

    this.particleSystem = new THREE.Points(pGeo, pMat);
    this.scene.add(this.particleSystem);
  }

  createUIElements() {
    // 1. Hover Mini Title Tooltip
    this.hoverTooltip = document.createElement('div');
    this.hoverTooltip.className = 'tree-mini-tooltip';
    this.hoverTooltip.style.cssText = `
      position: absolute;
      z-index: 999;
      pointer-events: none;
      padding: 6px 14px;
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(16, 185, 129, 0.4);
      border-radius: 20px;
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
      opacity: 0;
      transform: scale(0.9) translateY(5px);
      transition: opacity 0.2s ease, transform 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    `;
    this.container.appendChild(this.hoverTooltip);

    // 2. Click Full Detail Side Panel
    this.detailPanel = document.createElement('div');
    this.detailPanel.className = 'tree-detail-panel';
    this.detailPanel.style.cssText = `
      position: absolute;
      top: 1rem;
      right: 1rem;
      width: 310px;
      padding: 1.4rem;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-xl, 16px);
      color: var(--text-main);
      box-shadow: var(--shadow-3d-lg);
      z-index: 1001;
      opacity: 0;
      transform: translateX(30px);
      pointer-events: none;
      transition: opacity 0.3s ease, transform 0.3s ease;
    `;
    this.detailPanel.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
        <span style="font-size:0.75rem; font-weight:800; text-transform:uppercase; color:var(--primary);" id="panelTag">CAPABILITY</span>
        <button type="button" id="closePanelBtn" style="background:none; border:none; color:var(--text-muted); font-size:1.2rem; cursor:pointer;">✕</button>
      </div>
      <div style="display:flex; align-items:center; gap:10px; margin-bottom:0.75rem;">
        <span style="font-size:1.6rem;" id="panelIcon">🧠</span>
        <h4 style="font-size:1.15rem; margin:0;" id="panelTitle">AI Intelligence</h4>
      </div>
      <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.6; margin-bottom:1rem;" id="panelDesc">Full description.</p>
      <div style="display:flex; gap:8px; flex-wrap:wrap;" id="panelTags"></div>
    `;
    this.container.appendChild(this.detailPanel);

    const closeBtn = document.getElementById('closePanelBtn');
    if (closeBtn) {
      closeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        this.closeDetailPanel();
      });
    }
  }

  bindEvents() {
    const canvas = this.renderer.domElement;

    // Mouse Drag Rotation Controls & Cursor Styling
    canvas.addEventListener('mousedown', (e) => {
      this.isDragging = true;
      this.autoRotate = false;
      canvas.style.cursor = 'grabbing';
      this.previousMousePosition = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener('mouseup', () => {
      if (this.isDragging) {
        this.isDragging = false;
        canvas.style.cursor = this.hoveredNode ? 'pointer' : 'grab';
        this.resetAutoRotateTimer();
      }
    });

    canvas.addEventListener('mousemove', (e) => {
      const rect = canvas.getBoundingClientRect();
      this.mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      this.mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

      if (this.isDragging) {
        const deltaX = e.clientX - this.previousMousePosition.x;
        this.targetRotationY += deltaX * 0.007;
        this.previousMousePosition = { x: e.clientX, y: e.clientY };
      }
    });

    // Click Node to Focus & Open Detail Panel
    canvas.addEventListener('click', () => {
      if (this.hoveredNode) {
        const idData = this.hoveredNode.userData.identity;
        this.openDetailPanel(idData, this.hoveredNode);
      }
    });

    // Touch Controls
    canvas.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        this.isDragging = true;
        this.autoRotate = false;
        this.previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
      }
    }, { passive: true });

    window.addEventListener('touchmove', (e) => {
      if (this.isDragging && e.touches.length === 1) {
        const deltaX = e.touches[0].clientX - this.previousMousePosition.x;
        this.targetRotationY += deltaX * 0.009;
        this.previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
      }
    }, { passive: true });

    window.addEventListener('touchend', () => {
      this.isDragging = false;
      this.resetAutoRotateTimer();
    });

    const handleResize = () => {
      if (!this.container || !this.camera || !this.renderer) return;
      const w = this.container.clientWidth;
      const h = this.container.clientHeight;
      if (w > 0 && h > 0) {
        this.camera.aspect = w / h;
        // On portrait/mobile aspect ratios, step camera back so top canopy & roots fit 100% without cropping
        if (w / h < 0.95) {
          this.camera.position.z = 10.2;
        } else if (w / h < 1.2) {
          this.camera.position.z = 9.5;
        } else {
          this.camera.position.z = 8.8;
        }
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(w, h);
      }
    };


    window.addEventListener('resize', handleResize);
    window.addEventListener('orientationchange', () => setTimeout(handleResize, 120));

    if (window.ResizeObserver && this.container) {
      const observer = new ResizeObserver(() => handleResize());
      observer.observe(this.container);
    }
  }


  resetAutoRotateTimer() {
    clearTimeout(this.autoRotateTimer);
    this.autoRotateTimer = setTimeout(() => {
      this.autoRotate = true;
    }, 5000);
  }

  checkRaycastIntersections() {
    const canvas = this.renderer.domElement;

    if (this.isDragging) {
      this.hideHoverTooltip();
      return;
    }

    this.raycaster.setFromCamera(this.mouse, this.camera);
    const nodeMeshes = this.nodes.map(n => n.userData.sphereMesh);
    const intersects = this.raycaster.intersectObjects(nodeMeshes);

    if (intersects.length > 0) {
      const hitMesh = intersects[0].object;
      const parentNode = hitMesh.parent;
      const idData = parentNode.userData.identity;

      // Occlusion Check: Hide node if rotated behind tree trunk
      const worldPos = new THREE.Vector3();
      parentNode.getWorldPosition(worldPos);

      if (worldPos.z > -1.7) {
        canvas.style.cursor = 'pointer';
        this.setHoveredNode(parentNode, idData, worldPos);
        return;
      }
    }

    canvas.style.cursor = this.isDragging ? 'grabbing' : 'grab';
    this.clearHoveredNode();
  }

  setHoveredNode(nodeGroup, idData, worldPos) {
    if (this.hoveredNode !== nodeGroup) {
      this.clearHoveredNode();
      this.hoveredNode = nodeGroup;
      nodeGroup.userData.sphereMesh.scale.set(1.25, 1.25, 1.25);
      nodeGroup.userData.sphereMesh.material.emissiveIntensity = 1.1;
    }

    // Project world pos to 2D screen coords
    const screenVec = worldPos.clone().project(this.camera);
    const w = this.container.clientWidth;
    const h = this.container.clientHeight;

    let posX = (screenVec.x * 0.5 + 0.5) * w;
    let posY = (-(screenVec.y * 0.5) + 0.5) * h;

    // Viewport bounds protection
    if (posX > w - 150) posX = w - 150;
    if (posX < 20) posX = 20;

    this.hoverTooltip.style.left = `${posX}px`;
    this.hoverTooltip.style.top = `${posY - 35}px`;
    this.hoverTooltip.innerHTML = `<span>${idData.icon}</span> <strong>${idData.title}</strong>`;
    this.hoverTooltip.style.opacity = '1';
    this.hoverTooltip.style.transform = 'scale(1) translateY(0)';
  }

  clearHoveredNode() {
    if (this.hoveredNode) {
      this.hoveredNode.userData.sphereMesh.scale.set(1, 1, 1);
      this.hoveredNode.userData.sphereMesh.material.emissiveIntensity = 0.5;
      this.hoveredNode = null;
    }
    this.hideHoverTooltip();
  }

  hideHoverTooltip() {
    if (this.hoverTooltip) {
      this.hoverTooltip.style.opacity = '0';
      this.hoverTooltip.style.transform = 'scale(0.9) translateY(5px)';
    }
  }

  openDetailPanel(idData, nodeGroup) {
    this.autoRotate = false;
    this.resetAutoRotateTimer();

    document.getElementById('panelIcon').textContent = idData.icon;
    document.getElementById('panelTag').textContent = idData.tag;
    document.getElementById('panelTitle').textContent = idData.title;
    document.getElementById('panelDesc').textContent = idData.fullDesc;

    const tagsContainer = document.getElementById('panelTags');
    if (tagsContainer) {
      tagsContainer.innerHTML = `
        <span class="hero-badge" style="font-size:0.75rem; margin:0;">${idData.side}</span>
        <span class="hero-badge" style="font-size:0.75rem; margin:0; background:var(--primary-dark); color:#fff;">AgriVision AI</span>
      `;
    }

    this.detailPanel.style.pointerEvents = 'auto';
    this.detailPanel.style.opacity = '1';
    this.detailPanel.style.transform = 'translateX(0)';

    // Pulse core light
    if (this.coreLight) {
      this.coreLight.intensity = 2.5;
      setTimeout(() => { this.coreLight.intensity = 1.2; }, 800);
    }
  }

  closeDetailPanel() {
    if (this.detailPanel) {
      this.detailPanel.style.opacity = '0';
      this.detailPanel.style.transform = 'translateX(30px)';
      this.detailPanel.style.pointerEvents = 'none';
    }
  }

  updatePhysics(time) {
    // 1. Smooth 360° Tree Rotation Lerp
    if (this.autoRotate) {
      this.targetRotationY += 0.0025;
    }
    this.currentRotationY += (this.targetRotationY - this.currentRotationY) * 0.08;
    this.treeGroup.rotation.y = this.currentRotationY;

    // 2. Leaf Wind Oscillation & Cursor Breeze Proximity
    this.leaves.forEach(leaf => {
      const u = leaf.userData;
      const windX = Math.sin(time * u.speed + u.phase) * 0.035;
      const windY = Math.cos(time * u.speed * 0.8 + u.phase) * 0.035;

      const leafWorldPos = new THREE.Vector3();
      leaf.getWorldPosition(leafWorldPos);
      const dist = this.mouse.distanceTo(new THREE.Vector2(leafWorldPos.x / 4, leafWorldPos.y / 4));

      let breezeX = 0, breezeY = 0;
      if (dist < 0.55) {
        const force = (0.55 - dist) * 0.25;
        breezeX = (leafWorldPos.x > 0 ? force : -force);
        breezeY = force * 0.4;
      }

      leaf.position.x = u.basePos.x + windX + breezeX;
      leaf.position.y = u.basePos.y + windY + breezeY;
      leaf.rotation.z = u.baseRot.z + windX * 1.5;
    });

    // 3. AI Core Pulsing
    if (this.aiCoreMesh) {
      this.aiCoreMesh.rotation.y += 0.008;
      this.aiCoreMesh.material.opacity = 0.35 + Math.sin(time * 2.5) * 0.2;
    }

    // 4. Node Ring Rotation
    this.nodes.forEach(node => {
      node.userData.ringMesh.rotation.z += 0.015;
    });

    // 5. Environmental Particles Drift
    if (this.particleSystem) {
      const positions = this.particleSystem.geometry.attributes.position.array;
      for (let i = 1; i < positions.length; i += 3) {
        positions[i] += 0.0025;
        if (positions[i] > 4.2) positions[i] = -1.5;
      }
      this.particleSystem.geometry.attributes.position.needsUpdate = true;
    }
  }

  render() {
    requestAnimationFrame((t) => {
      this.updatePhysics(t * 0.001);
      this.checkRaycastIntersections();
      this.renderer.render(this.scene, this.camera);
      this.render();
    });
  }
}

// Instantiate clean 3D Tree
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('tree3DContainer');
  if (container) {
    window.agriTree = new AgriVisionSmartTree('tree3DContainer');
  }
});
