/**
 * AgriVision AI - Multi-Language Translation System (English | हिंदी | मराठी)
 */

const translations = {
  en: {
    // Navigation
    home: "Home",
    detect_disease: "Detect Disease",
    disease_library: "Disease Library",
    about: "About",
    contact: "Contact",
    analyze_crop: "🔍 Analyze Crop",
    
    // Hero & Home
    hero_badge: "🤖 Deep Learning & Grad-CAM XAI",
    hero_title_1: "Protect Your Crops with ",
    hero_title_2: "AI-Powered",
    hero_title_3: " Disease Detection",
    hero_subtitle: "Upload a crop leaf image and let AgriVision AI identify possible diseases, explain the prediction using visual heatmaps, and provide useful crop-management information.",
    detect_now: "🔍 Detect Disease Now",
    explore_library: "📚 Explore Disease Library",
    how_it_works: "How It Works",
    how_subtitle: "Get instant disease diagnostics and visual AI explanations in 5 easy steps.",
    
    // Steps
    step1_title: "Upload Leaf Image",
    step1_desc: "Take or upload a high-resolution photo of a single crop leaf showing affected areas.",
    step2_title: "AI Analyzes Image",
    step2_desc: "Our TensorFlow deep learning model preprocesses pixels and runs instant inference.",
    step3_title: "Disease is Detected",
    step3_desc: "The system classifies crop health status and calculates a precise confidence score.",
    step4_title: "View AI Explanation",
    step4_desc: "Grad-CAM generates a visual heatmap highlighting the exact leaf regions influencing the AI.",
    step5_title: "Get Prevention Info",
    step5_desc: "Access organic solutions, nutrient guidelines, and database-backed management practices.",
    
    // Upload & Scanner Page
    upload_header: "Upload Leaf Image for Analysis",
    upload_title: "Upload a Crop Leaf Image",
    upload_subtitle: "Drag and drop your leaf photo here, or click to browse files",
    browse_btn: "📁 Browse Image (JPG, JPEG, PNG)",
    tip_title: "Best Results Tip:",
    tip_desc: "Upload a clear, well-lit image of a single crop leaf against a neutral background for maximum prediction accuracy.",
    sample_quick_test: "Quick Test Sample Leaves:",
    sample_tomato_early: "Tomato Early Blight",
    sample_tomato_healthy: "Tomato Healthy",
    sample_potato_late: "Potato Late Blight",
    btn_start_analysis: "🔬 Analyze Crop Image",
    analyzing_img: "Analyzing your crop image…",
    scan_step_1: "1. Preprocessing pixels & resizing to 224x224",
    scan_step_2: "2. Extracting spatial convolutional features",
    scan_step_3: "3. Evaluating Softmax class probabilities",
    scan_step_4: "4. Synthesizing Grad-CAM attention heatmap",

    // Result Dashboard
    report_title: "AI Disease Prediction Report",
    crop_name: "Crop Name",
    disease_detected: "Disease Detected",
    health_status: "Plant Health Status",
    confidence_score: "AI Confidence Score",
    status_healthy: "🟢 Healthy",
    status_disease: "🔴 Disease Detected",
    status_warning: "⚠️ Low Confidence",
    
    // XAI & Opacity Slider
    xai_title: "AI Explanation (Grad-CAM Visualizer)",
    xai_subtitle: "The highlighted regions indicate the areas that had the greatest influence on the AI model’s prediction.",
    orig_image: "Original Leaf Image",
    heatmap_attention: "Grad-CAM Heatmap Attention",
    interactive_overlay: "Interactive Heatmap Cross-Fade",
    slider_label: "Adjust Heatmap Opacity:",
    
    // Accuracy Breakdown & Severity
    top_predictions: "Top Candidate Predictions Breakdown",
    foliage_metrics: "Foliage Pathology Analysis Metrics",
    necrosis_ratio: "Necrosis / Lesion Spot Ratio",
    healthy_green_ratio: "Healthy Chlorophyll Ratio",
    severity_level: "Pathology Severity Rating",
    severity_mild: "Mild (Low Defoliation Risk)",
    severity_moderate: "Moderate (Active Treatment Needed)",
    severity_severe: "Severe (Immediate Quarantine Recommended)",
    
    // Detail Cards
    symptoms: "Visible Symptoms",
    causes: "Possible Causes & Pathogen",
    prevention: "Preventive Practices",
    management: "Disease Management",
    organic_solution: "Organic Solutions",
    nutrient_info: "Nutrient & Fertilizer Info",
    disclaimer_notice: "📢 Notice: AI-generated predictions are intended for preliminary identification and should not completely replace advice from qualified agricultural experts or laboratory diagnosis."
  },
  hi: {
    // Navigation
    home: "मुख्य पृष्ठ",
    detect_disease: "रोग की पहचान करें",
    disease_library: "रोग पुस्तकालय",
    about: "हमारे बारे में",
    contact: "संपर्क करें",
    analyze_crop: "🔍 फसल की जांच करें",
    
    // Hero & Home
    hero_badge: "🤖 दीप लर्निंग एवं Grad-CAM XAI",
    hero_title_1: "एआई द्वारा अपनी ",
    hero_title_2: "फसलों को",
    hero_title_3: " बीमारियों से बचाएं",
    hero_subtitle: "अपनी फसल की पत्ती की फोटो अपलोड करें और एआई द्वारा बीमारी की सटीक पहचान, दृश्य व्याख्या (Heatmap), तथा जैविक उपचार जानकारी प्राप्त करें।",
    detect_now: "🔍 रोग पहचान शुरू करें",
    explore_library: "📚 रोग पुस्तकालय देखें",
    how_it_works: "यह कैसे काम करता है",
    how_subtitle: "केवल 5 आसान चरणों में तुरंत रोग निदान और दृश्य एआई व्याख्या प्राप्त करें।",
    
    // Steps
    step1_title: "पत्ती की फोटो अपलोड करें",
    step1_desc: "प्रभावित फसल की स्पष्ट और उच्च गुणवत्ता वाली पत्ती की फोटो अपलोड करें।",
    step2_title: "एआई द्वारा विश्लेषण",
    step2_desc: "हमारा टेंसरफ्लो दीप लर्निंग मॉडल फोटो का तुरंत विश्लेषण करता है।",
    step3_title: "रोग की पहचान",
    step3_desc: "सिस्टम फसल के स्वास्थ्य की स्थिति और सटीक आत्मविश्वास स्कोर (Confidence Score) बताता है।",
    step4_title: "एआई व्याख्या देखें",
    step4_desc: "Grad-CAM हीटमैप दिखाता है कि एआई ने पत्ती के किन हिस्सों के आधार पर निर्णय लिया।",
    step5_title: "उपचार एवं रोकथाम जानकारी",
    step5_desc: "जैविक उपाय, खाद की मात्रा, और रोग रोकथाम के कृषि सुझाव प्राप्त करें।",
    
    // Upload & Scanner Page
    upload_header: "विश्लेषण के लिए पत्ती की फोटो अपलोड करें",
    upload_title: "फसल की पत्ती की फोटो अपलोड करें",
    upload_subtitle: "फोटो को यहां ड्रैग एंड ड्रॉप करें, या फाइल चुनें",
    browse_btn: "📁 फोटो चुनें (JPG, JPEG, PNG)",
    tip_title: "बेहतर परिणाम का सुझाव:",
    tip_desc: "सटीक परिणाम के लिए एक ही पत्ती की साफ, अच्छी रोशनी वाली फोटो अपलोड करें।",
    sample_quick_test: "त्वरित परीक्षण नमूना पत्तियां:",
    sample_tomato_early: "टमाटर - अगेती झुलसा",
    sample_tomato_healthy: "टमाटर - स्वस्थ",
    sample_potato_late: "आलू - पछेती झुलसा",
    btn_start_analysis: "🔬 फसल फोटो का विश्लेषण करें",
    analyzing_img: "आपकी फसल की पत्ती का विश्लेषण हो रहा है…",
    scan_step_1: "1. पिक्सल प्रीप्रोसेसिंग और 224x224 आकार देना",
    scan_step_2: "2. गहरे कंवोल्यूशन फीचर्स निष्कर्षण",
    scan_step_3: "3. सॉफ्टमैक्स क्लास संभावनाओं की गणना",
    scan_step_4: "4. Grad-CAM ध्यान हीटमैप का निर्माण",

    // Result Dashboard
    report_title: "एआई फसल रोग निदान रिपोर्ट",
    crop_name: "फसल का नाम",
    disease_detected: "पहचाना गया रोग",
    health_status: "पौधे के स्वास्थ्य की स्थिति",
    confidence_score: "एआई आत्मविश्वास स्कोर",
    status_healthy: "🟢 स्वस्थ (Healthy)",
    status_disease: "🔴 रोग पाया गया (Disease Detected)",
    status_warning: "⚠️ कम आत्मविश्वास (Low Confidence)",
    
    // XAI & Opacity Slider
    xai_title: "एआई व्याख्या (Grad-CAM विज़ुअलाइज़र)",
    xai_subtitle: "हाइलाइट किए गए लाल/पीले क्षेत्र दर्शाते हैं कि एआई मॉडल ने किन हिस्सों को देखकर यह निर्णय लिया है।",
    orig_image: "मूल पत्ती की फोटो",
    heatmap_attention: "Grad-CAM ध्यान हीटमैप",
    interactive_overlay: "इंटरएक्टिव हीटमैप मिश्रण",
    slider_label: "हीटमैप की पारदर्शिता समायोजित करें:",
    
    // Accuracy Breakdown & Severity
    top_predictions: "शीर्ष संभावित रोगों का विवरण",
    foliage_metrics: "पत्ती क्षति विश्लेषण मेट्रिक्स",
    necrosis_ratio: "पत्ती पर धब्बों का प्रतिशत",
    healthy_green_ratio: "स्वस्थ क्लोरोफिल प्रतिशत",
    severity_level: "बीमारी की गंभीरता श्रेणी",
    severity_mild: "हल्की (कम जोखिम)",
    severity_moderate: "मध्यम (तुरंत उपचार आवश्यक)",
    severity_severe: "गंभीर (तत्काल पृथक्करण और दवा छिड़काव)",
    
    // Detail Cards
    symptoms: "प्रमुख लक्षण",
    causes: "संभावित कारण और रोगजनक",
    prevention: "रोकथाम के उपाय",
    management: "फसल प्रबंधन",
    organic_solution: "जैविक समाधान",
    nutrient_info: "पोषण और उर्वरक जानकारी",
    disclaimer_notice: "📢 सूचना: एआई पूर्वानुमान प्रारंभिक पहचान के लिए हैं। अंतिम निर्णय के लिए कृषि विशेषज्ञों या प्रयोगशाला जांच की सलाह लें।"
  },
  mr: {
    // Navigation
    home: "मुख्य पृष्ठ",
    detect_disease: "रोग ओळखा",
    disease_library: "रोग वाचनालय",
    about: "आमच्याबद्दल",
    contact: "संपर्क साधा",
    analyze_crop: "🔍 पिकाची तपासणी करा",
    
    // Hero & Home
    hero_badge: "🤖 दीप लर्निंग आणि Grad-CAM XAI",
    hero_title_1: "एआय तंत्रज्ञानाने तुमच्या ",
    hero_title_2: "पिकांचे",
    hero_title_3: " रोगांपासून संरक्षण करा",
    hero_subtitle: "तुमच्या पिकाच्या पानाचा फोटो अपलोड करा आणि एआयद्वारे रोगाची अचूक ओळख, दृश्य विश्लेषण (Heatmap) आणि जैविक उपाय मिळवा.",
    detect_now: "🔍 रोग ओळख सुरू करा",
    explore_library: "📚 रोग वाचनालय पहा",
    how_it_works: "हे कसे कार्य करते",
    how_subtitle: "कवळ ५ सोप्या पायऱ्यांमध्ये त्वरित रोग निदान आणि दृश्य एआय स्पष्टीकरण मिळवा.",
    
    // Steps
    step1_title: "पानाचा फोटो अपलोड करा",
    step1_desc: "बाधित पिकाच्या पानाचा स्पष्ट फोटो अपलोड करा.",
    step2_title: "एआयद्वारे विश्लेषण",
    step2_desc: "आमचे टेन्सरफ्लो मॉडेल फोटोचे त्वरित विश्लेषण करते.",
    step3_title: "रोगाची ओळख",
    step3_desc: "सिस्टम पिकाच्या आरोग्याची स्थिती आणि अचूक आत्मविश्वास दाखवते.",
    step4_title: "एआय स्पष्टीकरण पहा",
    step4_desc: "Grad-CAM हीटमॅप दाखवतो की एआयने पानातील कोणत्या भागावरून निर्णय घेतला.",
    step5_title: "प्रतिबंध व व्यवस्थापन",
    step5_desc: "जैविक उपाय, खतांचे प्रमाण आणि रोग नियंत्रणाची माहिती मिळवा.",
    
    // Upload & Scanner Page
    upload_header: "विश्लेषणासाठी पानाचा फोटो अपलोड करा",
    upload_title: "पिकाच्या पानाचा फोटो अपलोड करा",
    upload_subtitle: "फोटो येथे ड्रॅग आणि ड्रॉप करा, किंवा फाईल निवडा",
    browse_btn: "📁 फोटो निवडा (JPG, JPEG, PNG)",
    tip_title: "अचूक निकालासाठी टीप:",
    tip_desc: "अचूक निकालासाठी एकाच पानाचा चांगल्या प्रकाशातील फोटो अपलोड करा.",
    sample_quick_test: "त्वरित चाचणी नमुना पाने:",
    sample_tomato_early: "टोमॅटो - करपा",
    sample_tomato_healthy: "टोमॅटो - निरोगी",
    sample_potato_late: "बटाटा - तांबेरा",
    btn_start_analysis: "🔬 पानाचे विश्लेषण करा",
    analyzing_img: "पिकाच्या पानाचे विश्लेषण सुरू आहे…",
    scan_step_1: "१. पिक्सेल प्रीप्रोसेसिंग आणि २२४x२२४ आकार बदलणे",
    scan_step_2: "२. वैशिष्ट्य काढणे (Feature Extraction)",
    scan_step_3: "३. सॉफ्टमॅक्स वर्ग संभाव्यता मूल्यमापन",
    scan_step_4: "४. Grad-CAM लक्ष हीटमॅप तयार करणे",

    // Result Dashboard
    report_title: "एआय पीक रोग निदान अहवाल",
    crop_name: "पिकाचे नाव",
    disease_detected: "ओळखलेला रोग",
    health_status: "पिकाच्या आरोग्याची स्थिती",
    confidence_score: "एआय आत्मविश्वास स्कोर",
    status_healthy: "🟢 निरोगी (Healthy)",
    status_disease: "🔴 रोग आढळला (Disease Detected)",
    status_warning: "⚠️ कमी आत्मविश्वास (Low Confidence)",
    
    // XAI & Opacity Slider
    xai_title: "एआय स्पष्टीकरण (Grad-CAM Visualizer)",
    xai_subtitle: "हायलाइट केलेले भाग दाखवतात की एआय मॉडेलने पानातील कोणत्या भागावर लक्ष केंद्रित करून निष्कर्ष काढला आहे.",
    orig_image: "मूळ पानाचा फोटो",
    heatmap_attention: "Grad-CAM लक्ष हीटमॅप",
    interactive_overlay: "परस्परसंवादी हीटमॅप मिश्रण",
    slider_label: "हीटमॅप पारदर्शकता बदला:",
    
    // Accuracy Breakdown & Severity
    top_predictions: "प्रमुख संभाव्य रोगांचे विश्लेषण",
    foliage_metrics: "पान नुकसान विश्लेषण मेट्रिक्स",
    necrosis_ratio: "पानावरील डागांचे प्रमाण (%)",
    healthy_green_ratio: "निरोगी हरितद्रव्य प्रमाण (%)",
    severity_level: "रोगाची तीव्रता श्रेणी",
    severity_mild: "सौम्य (कमी धोका)",
    severity_moderate: "मध्यम (त्वरित उपचारांची गरज)",
    severity_severe: "गंभीर (तत्काळ औषध फवारणी आवश्यक)",
    
    // Detail Cards
    symptoms: "प्रमुख लक्षणे",
    causes: "संभाव्य कारणे व रोगजंतू",
    prevention: "प्रतिबंधात्मक उपाय",
    management: "पीक व्यवस्थापन",
    organic_solution: "जैविक उपाय",
    nutrient_info: "पोषण व खत माहिती",
    disclaimer_notice: "📢 सूचना: एआय अंदाज प्राथमिक ओळखीसाठी आहेत. अंतिम निर्णयासाठी कृषी तज्ञ किंवा प्रयोगशाळा चाचणीचा सल्ला घ्या."
  }
};

/**
 * Switch Active Language
 */
function setLanguage(lang) {
  if (!translations[lang]) lang = 'en';
  localStorage.setItem('agrivision_lang', lang);

  // Update text of elements with data-i18n attribute
  document.querySelectorAll('[data-i18n]').forEach(elem => {
    const key = elem.getAttribute('data-i18n');
    if (translations[lang][key]) {
      elem.textContent = translations[lang][key];
    }
  });

  // Update attribute elements (placeholders, titles)
  document.querySelectorAll('[data-i18n-placeholder]').forEach(elem => {
    const key = elem.getAttribute('data-i18n-placeholder');
    if (translations[lang][key]) {
      elem.placeholder = translations[lang][key];
    }
  });

  // Update active state in selector dropdown
  const langSelect = document.getElementById('languageSelect');
  if (langSelect) {
    langSelect.value = lang;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const savedLang = localStorage.getItem('agrivision_lang') || 'en';
  setLanguage(savedLang);

  const langSelect = document.getElementById('languageSelect');
  if (langSelect) {
    langSelect.addEventListener('change', (e) => {
      setLanguage(e.target.value);
    });
  }
});
