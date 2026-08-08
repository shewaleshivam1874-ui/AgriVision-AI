"""
AgriVision AI - Multilingual Internationalization (i18n) Module
Supports English (en), Marathi (mr), and Hindi (hi).
Provides complete static translation dictionaries and dynamic translation helpers
for crops, diseases, categories, health statuses, severities, and urgencies.
"""

TRANSLATIONS = {
    'en': {
        # Navigation & Header
        'app_name': 'AgriVision AI',
        'app_subtitle': 'Explainable Crop Disease Detection',
        'home': 'Home',
        'detect_disease': 'Analyze Leaf',
        'history': 'Prediction History',
        'about': 'About',
        'contact': 'Contact',
        'language': 'Language',
        'english': 'English',
        'marathi': 'मराठी',
        'hindi': 'हिंदी',
        'analyze_crop': '🔍 Analyze Crop',
        'toggle_theme': 'Toggle Light/Dark Mode',
        'menu_toggle': 'Toggle Navigation Menu',

        # Footer
        'footer_brand_desc': 'An Explainable AI (XAI) web application designed for early crop leaf disease detection, visual attention heatmaps, disease stage estimation, and agricultural diagnosis support.',
        'footer_nav_heading': 'Navigation',
        'footer_cap_heading': 'Capabilities',
        'footer_tech_heading': 'Technologies',
        'footer_rights': 'All rights reserved. Designed for explainable precision agriculture.',
        'cap_leaf_analysis': 'Real-Time AI Leaf Analysis',
        'cap_severity_est': 'Disease Severity Estimation',
        'cap_heatmaps': 'Grad-CAM Visual Heatmaps',
        'cap_guidance': 'Organic & Chemical Guidance',
        'tech_gemini': 'Google Gemini Vision AI',
        'tech_vision_scanner': 'Computer Vision Leaf Scanner',
        'tech_flask': 'Python Flask Backend',
        'tech_xai': 'Explainable AI Guidance',

        # Hero & Home Page
        'hero_badge': '🤖 Google Gemini Vision AI & Interactive 3D XAI',
        'hero_title_1': 'Detect Crop Diseases Early with ',
        'hero_title_2': 'AI',
        'hero_subtitle': 'Upload a crop leaf image and let AgriVision AI identify possible diseases, explain visible foliage symptoms, estimate disease severity, and provide structured crop management guidance.',
        'btn_analyze_leaf': '🔍 Analyze a Leaf',
        'trust_realtime_ai': '✓ Real-Time Vision AI',
        'trust_explainable': '✓ Explainable AI Guidance',
        'trust_solutions': '✓ Organic & Chemical Solutions',
        'floating_condition_val': 'Early Blight',
        'floating_severity_val': 'Moderate',

        # How AgriVision AI Works
        'how_tag': 'Professional AI Workflow',
        'how_title': 'How AgriVision AI Works',
        'how_subtitle': 'From image capture to actionable crop-care guidance, AgriVision AI transforms a simple crop image into an easy-to-understand AI-powered health assessment.',
        'step_01_title': 'Upload a Crop Image',
        'step_01_desc': 'Take a clear photo of the affected crop leaf or upload an existing image from your smartphone or computer.',
        'step_02_title': 'AI Examines the Leaf',
        'step_02_desc': 'The AI vision model processes the image to extract visual patterns, chlorosis halos, necrotic spot lesions, and foliage texture details.',
        'step_03_title': 'Identify Potential Disease',
        'step_03_desc': 'The trained crop classification engine identifies the likely disease or healthy class with confidence metrics and severity staging.',
        'step_04_title': 'Receive Crop-Care Guidance',
        'step_04_desc': 'Transforms AI diagnostics into structured farmer action steps, organic sanitation options, chemical guidelines, and fertilizer advice.',
        'chip_formats': 'JPG, PNG, WEBP',
        'chip_lighting': 'Clear Lighting',
        'chip_drag_drop': 'Drag & Drop',
        'chip_processing': 'Processing image...',
        'chip_symptoms': 'Analyzing visible symptoms...',
        'chip_disease_name': 'Early Blight',
        'chip_confidence': '94% Confidence',
        'chip_moderate': 'Moderate Stage',
        'workflow_cta_title': 'Ready to check your crop?',
        'workflow_cta_desc': 'Get instant diagnostic results and organic management protocols.',
        'workflow_cta_btn': 'Analyze a Crop Leaf →',

        # Platform Capabilities / 10 Feature Cards
        'features_tag': 'Platform Capabilities',
        'features_title': 'Key Features of AgriVision AI',
        'features_subtitle': 'Designed for agricultural clarity, transparency, and actionable field guidance.',
        'feat_1_title': 'AI Disease Detection',
        'feat_1_desc': 'Identify possible crop diseases using deep learning neural network classification.',
        'feat_2_title': 'Confidence Analysis',
        'feat_2_desc': 'Display the model\'s prediction confidence score with High, Medium, or Low thresholds.',
        'feat_3_title': 'Explainable AI (Grad-CAM)',
        'feat_3_desc': 'Use Grad-CAM visual heatmaps to show specific leaf areas that guided the prediction.',
        'feat_4_title': 'Disease Stage Estimation',
        'feat_4_desc': 'Show estimated disease progression stage (Early, Developing, Moderate, Advanced, Severe).',
        'feat_5_title': 'Disease Severity & Affected Area',
        'feat_5_desc': 'Calculate visible affected leaf spot percentages (0-100%) and severity rating bands.',
        'feat_6_title': 'Disease Information',
        'feat_6_desc': 'Provide detailed information on typical symptoms, causes, and pathogen types.',
        'feat_7_title': 'Organic Management',
        'feat_7_desc': 'Display available organic controls, sanitation practices, and bio-fungicides.',
        'feat_8_title': 'Conventional Management',
        'feat_8_desc': 'Display conventional treatment options separately with strict safety label warnings.',
        'feat_9_title': 'Nutrient Guidance',
        'feat_9_desc': 'Display useful N-P-K nutrient considerations and foliage support factors.',
        'feat_10_title': 'Prevention & Monitoring',
        'feat_10_desc': 'Explain preventative practices that reduce disease spread and future crop recurrence.',

        # Upload Portal (/detect)
        'upload_portal_tag': 'AI Diagnostics Portal',
        'upload_portal_title': 'Upload Leaf Image for Diagnostic Analysis',
        'upload_portal_subtitle': 'Take or upload a clear, well-lit photo of a single crop leaf showing affected symptoms.',
        'quick_tips_title': 'Quick Tips for Best Results',
        'quick_tip_1': 'Use a clear, well-lit image of a single crop leaf.',
        'quick_tip_2': 'Keep the leaf properly focused to avoid excessive blur.',
        'quick_tip_3': 'Ensure sufficient natural lighting without extreme glare or dark shadows.',
        'quick_tip_4': 'Keep the affected diseased region clearly visible.',
        'quick_tip_5': 'Avoid covering the leaf with fingers, tools, or background clutter.',
        'drag_drop_text': 'Drag and drop your crop leaf image here, or',
        'browse_files': '📁 Browse Files',
        'take_photo': '📷 Take Photo',
        'change_image': '🔄 Change Image',
        'remove_image': 'Remove Image',
        'supported_formats': 'Supported formats: JPG, JPEG, PNG, WEBP (Max 10MB)',
        'quick_test_leaves': 'Quick Test Sample Leaves:',
        'sample_1_name': 'Tomato Early Blight',
        'sample_1_sub': 'Dataset Leaf 1',
        'sample_2_name': 'Tomato Healthy',
        'sample_2_sub': 'Dataset Leaf 2',
        'sample_3_name': 'Potato Late Blight',
        'sample_3_sub': 'Dataset Leaf 3',
        'sample_4_name': 'Apple Scab',
        'sample_4_sub': 'Dataset Leaf 4',
        'btn_start_analysis': '🔬 Analyze Crop Image',
        'analyzing_img': 'Analyzing your crop image…',
        'processing_msg': 'Processing image...',
        'analyzing_symptoms': 'Analyzing visible symptoms...',
        'identifying_disease': 'Identifying possible disease...',
        'preparing_guidance': 'Preparing recommendations...',
        'selected_file_label': 'Selected: ',
        'err_select_image': 'Please select or drop a crop leaf image first.',
        'err_unsupported_format': 'Unsupported file format. Please upload a JPG, JPEG, PNG, or WEBP image.',
        'err_file_too_large': 'File size exceeds the 10 MB limit. Please select a smaller leaf image.',
        'err_analysis_failed': 'Failed to complete crop analysis.',
        'err_network_error': 'Network error occurred while processing image.',

        # Diagnostic Result Report (/result & /gemini-result)
        'report_title': 'Crop Health Analysis Report',
        'report_subtitle': 'Real-time visual pathology & diagnostic guidance',
        'gemini_badge_text': 'AI Vision Analysis with Google Gemini AI Vision',
        'gemini_badge_sub': '• Visual Crop Analysis',
        'btn_print_report': 'Print Report',
        'btn_copy_summary': 'Copy Summary',
        'btn_new_analysis': 'New Analysis',
        'jump_overview': '📊 Overview',
        'jump_visual': '📸 Photo & Severity',
        'jump_actions': '⚡ Actions',
        'jump_treatments': '🧪 Treatments',
        'jump_nutrients': '🌾 Soil & Fertilizer',
        'jump_insights': '🔍 Insights',

        # 5 Overview Cards
        'card_crop_species': 'Crop & Species',
        'card_condition': 'Condition Identified',
        'card_confidence': 'AI Confidence',
        'card_health_status': 'Health Status',
        'card_action_urgency': 'Action Urgency',
        'plant_id_label': 'Plant ID:',
        'category_label': 'Category:',
        'diagnostic_status_label': 'Diagnostic Status',

        # Photo & Severity Card
        'analyzed_leaf_photo': 'Analyzed Leaf Photo',
        'leaf_sample_placeholder': 'Uploaded Leaf Sample',
        'pathology_severity_title': 'Pathology Severity Level',
        'severity_assessment_label': 'Severity Assessment:',

        # Actionable Guidance Section
        'actionable_guidance_title': '⚡ Actionable Guidance',
        'actionable_guidance_sub': 'Recommended next steps based on your crop health analysis',
        'ai_guided_actions_badge': 'AI-Guided Actions',
        'what_do_now_title': 'What Should I Do Now?',
        'what_do_now_sub': 'Follow these recommended steps based on the current analysis',
        'immediate_priority': '● IMMEDIATE PRIORITY',
        'do_now': 'DO NOW',
        'primary_action_title': '🔍 Primary Action: Inspect & Isolate',
        'rec_24_hours': '⏱ Recommended: Immediately within 24 Hours',
        'step_inspection_monitoring': 'Inspection & Monitoring',
        'step_sanitation_prevention': 'Sanitation & Prevention',
        'step_treatment_protocol': 'Treatment Protocol',
        'step_expert_support': 'Expert Support',
        'time_24_48_hours': '24–48 HOURS',
        'time_recommended': 'RECOMMENDED',
        'time_if_needed': 'IF NEEDED',
        'default_act_1_title': '🔍 Inspect Nearby Leaves',
        'default_act_1_desc': 'Check surrounding leaves and plants in the same crop row for similar visible spot lesions or chlorosis.',
        'default_act_1_rec': '⏱ Recommended: Now',
        'default_act_2_title': '👁 Monitor Progress',
        'default_act_2_desc': 'Observe whether spot lesions, concentric ring marks, or foliage discoloration expand over the next 24 to 48 hours.',
        'default_act_3_title': '🛡 Apply Organic / Sanitation Measures',
        'default_act_3_desc': 'Remove heavily diseased lower foliage, avoid overhead foliar irrigation, and apply copper-based organic bio-fungicides if appropriate.',
        'default_act_4_title': '👨‍🌾 Seek Expert Support',
        'default_act_4_desc': 'Consult an agricultural extension officer or agronomist if symptoms spread rapidly or severe defoliation occurs.',

        # Action Urgency Status Card
        'urgency_critical_title': 'CRITICAL',
        'urgency_critical_sub': '● Consult Expert Immediately',
        'urgency_critical_desc': 'Pathology risk is high. Prompt isolation and immediate specialist consultation is recommended.',
        'urgency_high_title': 'HIGH',
        'urgency_high_sub': '● Prompt Attention Advised',
        'urgency_high_desc': 'Significant leaf pathology detected. Take corrective sanitation or treatment measures soon.',
        'urgency_mod_title': 'MODERATE',
        'urgency_mod_sub': '● Attention Recommended',
        'urgency_mod_desc': 'Monitor the crop closely and take appropriate preventive actions within 24 to 48 hours.',
        'urgency_low_title': 'LOW',
        'urgency_low_sub': '● Routine Monitoring',
        'urgency_low_desc': 'Foliage displays minimal disease symptoms. Continue standard crop monitoring.',
        'urgency_unk_title': 'UNKNOWN',
        'urgency_unk_sub': '● Status Unconfirmed',
        'urgency_unk_desc': 'Urgency level could not be conclusively derived from this image.',

        # Monitor & Expert Help Cards
        'monitor_signs_title': 'Monitor For Warning Signs',
        'sign_1': 'New spot lesions or expanding halos',
        'sign_2': 'Foliage yellowing (chlorosis)',
        'sign_3': 'Premature leaf drop or wilt',
        'sign_4': 'Symptoms appearing on adjacent crop rows',
        'sign_5': 'Stem or fruit lesion development',
        'expert_help_title': 'When to Seek Expert Help',
        'expert_help_intro': 'Consult an agricultural professional or extension agent if:',
        'expert_help_1': 'Symptoms spread rapidly across multiple plants',
        'expert_help_2': 'AI confidence level is low or uncertain',
        'expert_help_3': 'Organic or chemical treatment fails to slow spread',
        'expert_help_4': 'Condition causes severe defoliation',

        # Management & Treatments Section
        'treatments_title': 'Management & Treatment Solutions',
        'organic_mgmt_title': 'Organic Management Options',
        'conventional_mgmt_title': 'Conventional Management Options',
        'no_organic_req': 'No specific organic treatments required.',
        'no_conventional_req': 'No specific chemical treatments required.',

        # Fertilizer & Nutrient Guidance
        'fertilizer_title': 'Nutrient & Fertilizer Guidance',
        'suspected_deficiency_label': 'Suspected Deficiency:',
        'visible_evidence_label': 'Visible Evidence:',
        'organic_option_label': 'Organic Option:',
        'conventional_option_label': 'Conventional Option:',
        'soil_testing_rec_label': 'Soil Testing Recommendation:',
        'no_nutrient_deficiency': 'No clear nutrient deficiency can be determined from this image.',
        'default_nutrient_correction': 'Nutrient Correction Recommended',
        'default_leaf_symptoms': 'Leaf symptoms suggest nutrient imbalance',
        'default_organic_amendment': 'Compost or organic liquid manure',
        'default_conventional_npk': 'Balanced NPK fertilizer formulation',

        # Additional Diagnostic Insights
        'insights_title': 'Additional Diagnostic Insights',
        'visible_symptoms_title': 'Visible Symptoms',
        'possible_causes_title': 'Possible Causes',
        'pest_analysis_title': 'Pest Analysis',
        'pest_suspected_label': 'Pest Activity Suspected:',
        'evidence_label': 'Evidence:',
        'no_pest_visible': 'No active pest damage or insect activity visible on foliage.',
        'environmental_factors_title': 'Environmental Factors',
        'no_env_stress': 'No severe environmental stress visible.',
        'preventive_measures_title': 'Preventive Measures',
        'standard_gap_rec': 'Maintain standard good agricultural practices.',
        'analysis_notes_title': 'Analysis Notes',
        'none_specified': 'None specified.',

        # Disclaimer & CTA
        'disclaimer_heading': '📢 Important Agricultural Disclaimer:',
        'disclaimer_notice': 'AgriVision AI provides AI-assisted preliminary crop-health information based on visible symptoms. Results may be inaccurate and should not replace laboratory diagnosis or advice from a qualified agricultural professional. Always follow locally approved agricultural product labels and recommendations.',
        'btn_analyze_another': '📷 Analyze Another Leaf Image',

        # History Page (/history)
        'history_tag': 'Saved Diagnostics Log',
        'history_title': 'Prediction History Logs',
        'history_subtitle': 'View past crop diagnostic records, severity scores, and visual heatmaps.',
        'stat_total_analyzed': 'Total Analyzed',
        'stat_healthy_leaf': 'Healthy Leaf',
        'stat_moderate_watch': 'Moderate / Watch',
        'stat_urgent_priority': 'Urgent Priority',
        'search_placeholder': '🔍 Search by crop or disease name...',
        'severity_filter_label': 'Severity:',
        'opt_all_severities': 'All Severities',
        'opt_healthy': '🟢 Healthy',
        'opt_low': '🟡 Low Severity',
        'opt_moderate': '🟠 Moderate',
        'opt_high': '🔴 High Severity',
        'opt_critical': '🚨 Critical',
        'btn_filter': 'Filter',
        'btn_reset': 'Reset',
        'col_date': 'Date & Time',
        'col_image': 'Leaf Preview',
        'col_crop': 'Crop',
        'col_condition': 'Condition Identified',
        'col_confidence': 'Confidence',
        'col_severity': 'Severity',
        'col_actions': 'Actions',
        'btn_view_report': 'View Full Report →',
        'delete_record': 'Delete',
        'tooltip_delete': 'Delete Record',
        'confirm_delete_record': 'Are you sure you want to delete this prediction record?',
        'empty_history': 'No prediction records found in your history yet.',
        'empty_history_desc': 'Upload a crop leaf photograph to initiate real-time AI diagnosis and start tracking pathology records.',

        # About Page (/about)
        'about_tag': 'About AgriVision AI',
        'about_title': 'Explainable AI for Precision Agriculture',
        'about_subtitle': 'Bridging deep learning computer vision and transparent diagnostic guidance for early crop health management.',
        'platform_overview_tag': 'PLATFORM OVERVIEW',
        'platform_overview_title': 'About AgriVision AI',
        'platform_overview_desc': 'AgriVision AI is an intelligent agricultural crop-health assistance system designed for early crop disease identification, visual pathology explanation, and structured disease management support.',
        'core_objective_tag': 'CORE OBJECTIVE',
        'our_mission': 'Our Mission',
        'our_mission_desc': 'To empower farmers, agronomists, and agricultural extension officers with transparent, accessible, and explainable AI insights to identify foliage diseases early, preserve crop yields, and reduce unnecessary chemical pesticide overuse.',
        'how_ai_helps': 'How AI Helps Agriculture',
        'how_ai_helps_desc': 'Computer vision models analyze visual leaf foliage symptoms—such as chlorosis, target-ring spot lesions, fungal spores, and bacterial spots—identifying early pathology stages before extensive crop damage spreads.',
        'xai_title': 'Explainable AI (XAI)',
        'xai_desc': 'Rather than operating as an opaque "black box", AgriVision AI incorporates Explainable AI (Grad-CAM feature heatmaps and visual symptom explanations) to highlight exact leaf regions that influenced the model\'s prediction.',
        'tech_stack_tag': 'Architecture',
        'tech_stack_title': 'Technology Stack',
        'tech_python_desc': 'Core backend language managing data processing, API endpoints, and computer vision pipelines.',
        'tech_flask_desc': 'Lightweight WSGI web framework providing stateless REST API routing and Jinja template rendering.',
        'tech_gemini_desc': 'Official Google GenAI SDK executing real-time visual pathology identification and structured diagnostic reports.',
        'tech_vision_desc': 'Computer vision image processing pipeline for file validation, tensor scaling, and leaf saliency checks.',
        'tech_gradcam_desc': 'Gradient-weighted Class Activation Mapping generating spatial attention heatmaps.',
        'tech_db_desc': 'Relational database system storing prediction history logs and verified agricultural records.',
        'tech_frontend_desc': 'Vanilla CSS design system with CSS custom variables, light/dark mode, and responsive layout.',
        'system_works_title': 'How the System Works',
        'pipe_1_title': 'Upload Image',
        'pipe_1_desc': 'Upload a clear close-up crop leaf photograph.',
        'pipe_2_title': 'Image Processing',
        'pipe_2_desc': 'Server validates MIME format, resolution, and leaf visibility.',
        'pipe_3_title': 'AI Prediction',
        'pipe_3_desc': 'Gemini Vision model classifies species, pathology, and severity.',
        'pipe_4_title': 'Explainable AI',
        'pipe_4_desc': 'Generates visual heatmap attention and symptom breakdown.',
        'pipe_5_title': 'Disease Information',
        'pipe_5_desc': 'Displays verified symptoms, causes, and pest analysis.',
        'pipe_6_title': 'Management Guidance',
        'pipe_6_desc': 'Provides prioritized action steps, organic, and chemical solutions.',
        'limitations_title': 'Important AI Limitations',
        'limitations_intro': 'AgriVision AI is designed as an agricultural decision-support tool. Users should understand the following limitations:',
        'limit_1': 'AI diagnostics rely on visible leaf foliage symptoms and photograph quality.',
        'limit_2': 'Different plant diseases can display visually similar chlorosis or leaf spot lesions.',
        'limit_3': 'Environmental sunburn or physical wind damage can resemble biological disease spots.',
        'limit_4': 'A leaf photo cannot measure exact soil pH, nitrogen/phosphorus levels, or vascular root rot.',
        'limit_5': 'AI assessments assist—and do not replace—qualified agronomists or laboratory diagnostic testing.',

        # Contact Page (/contact)
        'contact_tag': 'Get In Touch',
        'contact_title': 'Contact & Feedback',
        'contact_subtitle': 'Have questions regarding AI leaf diagnosis, model accuracy, or dataset integration? Send us a message.',
        'form_name': 'Full Name *',
        'form_name_placeholder': 'Enter your full name',
        'form_email': 'Email Address *',
        'form_email_placeholder': 'name@example.com',
        'form_subject': 'Subject',
        'form_subject_placeholder': 'e.g. Model feedback or general inquiry',
        'form_message': 'Your Message *',
        'form_message_placeholder': 'Describe your question or feedback...',
        'send_btn': '✉️ Send Message',
        'toast_form_required': 'Please fill in all required fields before submitting.',
        'toast_valid_email': 'Please enter a valid email address.',
        'toast_copied': 'Diagnostic summary copied to clipboard!',
        'toast_copy_failed': 'Failed to copy summary to clipboard.'
    },

    'mr': {
        # Navigation & Header
        'app_name': 'एग्रीव्हिजन एआय',
        'app_subtitle': 'सुलभ व अचूक पीक रोग निदान प्रणाली',
        'home': 'मुख्यपृष्ठ',
        'detect_disease': 'रोग ओळखा',
        'history': 'निदानांचा इतिहास',
        'about': 'आमच्याबद्दल',
        'contact': 'संपर्क साधा',
        'language': 'भाषा',
        'english': 'English',
        'marathi': 'मराठी',
        'hindi': 'हिंदी',
        'analyze_crop': '🔍 पिकाची तपासणी करा',
        'toggle_theme': 'लाइट/डार्क मोड बदला',
        'menu_toggle': 'मेनू उघडा/बंद करा',

        # Footer
        'footer_brand_desc': 'पिकांच्या पानांमधील रोगांचे वेळेवर निदान, दृश्य विश्लेषण (Heatmaps), रोगाची तीव्रता आणि सुलभ कृषी मार्गदर्शनासाठी विकसित केलेली एआय प्रणाली.',
        'footer_nav_heading': 'नेव्हिगेशन',
        'footer_cap_heading': 'वैशिष्ट्ये व क्षमता',
        'footer_tech_heading': 'तंत्रज्ञान',
        'footer_rights': 'सर्व हक्क राखीव. अचूक व सुलभ शेती मार्गदर्शनासाठी तयार केलेले.',
        'cap_leaf_analysis': 'रीअल-टाइम एआय पीक तपासणी',
        'cap_severity_est': 'रोगाच्या तीव्रतेचे मूल्यमापन',
        'cap_heatmaps': 'Grad-CAM दृश्य हीटमॅप्स',
        'cap_guidance': 'सेंद्रिय व रासायनिक मार्गदर्शन',
        'tech_gemini': 'गूगल जेमिनी व्हिजन एआय',
        'tech_vision_scanner': 'कॉम्प्युटर व्हिजन लीफ स्कॅनर',
        'tech_flask': 'पायथन फ्लास्क बॅकएंड',
        'tech_xai': 'सुलभ व पारदर्शक एआय मार्गदर्शन',

        # Hero & Home Page
        'hero_badge': '🤖 गूगल जेमिनी व्हिजन एआय व एक्सएआय निदाने',
        'hero_title_1': 'एआय तंत्रज्ञानाने पिकांचे रोगांपासून ',
        'hero_title_2': 'रक्षण',
        'hero_subtitle': 'तुमच्या पिकाच्या पानाचा फोटो अपलोड करा आणि एआय द्वारे रोगाची अचूक ओळख, दिसणाऱ्या लक्षणांचे स्पष्टीकरण आणि सेंद्रिय व रासायनिक उपचार उपाय मिळवा.',
        'btn_analyze_leaf': '🔍 पिकाचे पान तपासा',
        'trust_realtime_ai': '✓ रीअल-टाइम व्हिजन एआय',
        'trust_explainable': '✓ सुलभ एआय मार्गदर्शन',
        'trust_solutions': '✓ सेंद्रिय व रासायनिक उपाय',
        'floating_condition_val': 'करपा (Early Blight)',
        'floating_severity_val': 'मध्यम',

        # How AgriVision AI Works
        'how_tag': 'व्यावसायिक एआय कार्यप्रणाली',
        'how_title': 'एग्रीव्हिजन एआय कसे कार्य करते',
        'how_subtitle': 'छायाचित्र घेण्यापासून ते पीक सुरक्षेच्या प्रत्यक्ष उपायांपर्यंत, एग्रीव्हिजन एआय पिकाचे सोप्या व सुलभ भाषेत आरोग्य विश्लेषण प्रदान करते.',
        'step_01_title': 'पिकाचे छायाचित्र अपलोड करा',
        'step_01_desc': 'बाधित पानाचे स्पष्ट छायाचित्र घ्या किंवा स्मार्टफोन अथवा संगणकावरून अपलोड करा.',
        'step_02_title': 'एआय पानाचे परीक्षण करते',
        'step_02_desc': 'एआय मॉडेल पिकाच्या पानातील डाग, पिवळेपणा, करपा आणि रचनेचे सखोल विश्लेषण करते.',
        'step_03_title': 'संभाव्य रोग ओळखा',
        'step_03_desc': 'प्रशिक्षित एआय प्रणाली रोगाची अचूक ओळख, विश्वास पातळी आणि तीव्रतेची श्रेणी निश्चित करते.',
        'step_04_title': 'पीक काळजी मार्गदर्शन मिळवा',
        'step_04_desc': 'शेतकऱ्यांसाठी प्रत्यक्ष कृती आराखडा, सेंद्रिय उपाय, रासायनिक फवारणी व खत व्यवस्थापन मार्गदर्शन मिळवा.',
        'chip_formats': 'JPG, PNG, WEBP',
        'chip_lighting': 'चांगला प्रकाश',
        'chip_drag_drop': 'ड्रॅग आणि ड्रॉप',
        'chip_processing': 'छायाचित्र प्रक्रिया सुरू आहे...',
        'chip_symptoms': 'लक्षणांचे विश्लेषण सुरू आहे...',
        'chip_disease_name': 'करपा (Early Blight)',
        'chip_confidence': '९४% विश्वास पातळी',
        'chip_moderate': 'मध्यम टप्पा',
        'workflow_cta_title': 'तुमच्या पिकाची तपासणी करण्यास तयार आहात?',
        'workflow_cta_desc': 'त्वरित रोग निदान आणि सेंद्रिय व्यवस्थापन उपाय मिळवा.',
        'workflow_cta_btn': 'पिकाचे पान तपासा →',

        # Platform Capabilities / 10 Feature Cards
        'features_tag': 'प्लॅटफॉर्मची वैशिष्ट्ये',
        'features_title': 'एग्रीव्हिजन एआय ची प्रमुख वैशिष्ट्ये',
        'features_subtitle': 'शेतीतील सुलभता, पारदर्शकता आणि प्रत्यक्ष कृती मार्गदर्शनासाठी तयार केलेले.',
        'feat_1_title': 'एआय पीक रोग निदान',
        'feat_1_desc': 'अद्ययावत डीप लर्निंग तंत्रज्ञानाचा वापर करून पानांवरील रोगांची अचूक ओळख करा.',
        'feat_2_title': 'विश्वास पातळी विश्लेषण',
        'feat_2_desc': 'मॉडेलच्या अचूकतेची विश्वास पातळी (उच्च, मध्यम, कमी) थेट पहा.',
        'feat_3_title': 'स्पष्ट एआय (Grad-CAM)',
        'feat_3_desc': 'एआयने पानातील कोणत्या भागावरून निर्णय घेतला हे दर्शवणारा व्हिज्युअल हीटमॅप पहा.',
        'feat_4_title': 'रोगाच्या टप्प्याचे मूल्यमापन',
        'feat_4_desc': 'रोगाचा नेमका टप्पा (सुरुवातीचा, वाढणारा, मध्यम, प्रगत, गंभीर) ओळखा.',
        'feat_5_title': 'रोगाची तीव्रता व बाधित क्षेत्र',
        'feat_5_desc': 'पानावरील डागांचे प्रमाण (०-१००%) आणि तीव्रतेची वर्गवारी तपासा.',
        'feat_6_title': 'रोगाची सविस्तर माहिती',
        'feat_6_desc': 'रोगाची ठळक लक्षणे, कारणे आणि रोगजंतूंचा प्रकार जाणून घ्या.',
        'feat_7_title': 'सेंद्रिय व्यवस्थापन',
        'feat_7_desc': 'जैविक कीटकनाशके, स्वच्छता पद्धती आणि सेंद्रिय उपाययोजना मिळवा.',
        'feat_8_title': 'रासायनिक फवारणी उपाय',
        'feat_8_desc': 'सुरक्षितता नियमांसह योग्य रासायनिक फवारणी व सक्रिय घटकांची माहिती.',
        'feat_9_title': 'खत व अन्नद्रव्य मार्गदर्शन',
        'feat_9_desc': 'पिकांच्या प्रतिकारशक्तीसाठी नत्र, स्फुरद, पालाश आणि सूक्ष्म अन्नद्रव्यांचे मार्गदर्शन.',
        'feat_10_title': 'प्रतिबंध व शेती निरीक्षण',
        'feat_10_desc': 'रोग पसरण्यापासून रोखण्यासाठी आणि भविष्यातील संरक्षणासाठी प्रतिबंधात्मक उपाय.',

        # Upload Portal (/detect)
        'upload_portal_tag': 'एआय निदान पोर्टल',
        'upload_portal_title': 'रोग निदानासाठी पिकाच्या पानाचे छायाचित्र अपलोड करा',
        'upload_portal_subtitle': 'रोग लक्षणे दिसणाऱ्या पानाचे स्पष्ट, चांगल्या प्रकाशातील छायाचित्र अपलोड करा.',
        'quick_tips_title': 'उत्कृष्ट निदानासाठी महत्त्वाच्या टिप्स',
        'quick_tip_1': 'एकाच पिकाच्या पानाचे स्पष्ट व चांगल्या प्रकाशातील छायाचित्र वापरा.',
        'quick_tip_2': 'पानाचे छायाचित्र अस्पष्ट (Blur) होणार नाही याची काळजी घ्या.',
        'quick_tip_3': 'अतिप्रभावी सावली किंवा लखलखत्या प्रकाशाऐवजी नैसर्गिक प्रकाशात फोटो घ्या.',
        'quick_tip_4': 'रोगाचे लक्षण किंवा डाग असणारा भाग स्पष्टपणे दिसेल असे ठेवा.',
        'quick_tip_5': 'पान बोटांनी अथवा साधनांनी झाकले जाणार नाही याची दक्षता घ्या.',
        'drag_drop_text': 'येथे छायाचित्र ड्रॅग आणि ड्रॉप करा, किंवा',
        'browse_files': '📁 छायाचित्र निवडा',
        'take_photo': '📷 फोटो घ्या',
        'change_image': '🔄 छायाचित्र बदला',
        'remove_image': 'छायाचित्र हटवा',
        'supported_formats': 'समर्थित फॉरमॅट: JPG, JPEG, PNG, WEBP (कमाल १० MB)',
        'quick_test_leaves': 'त्वरित चाचणीसाठी नमुना पाने:',
        'sample_1_name': 'टोमॅटो - करपा (Early Blight)',
        'sample_1_sub': 'नमुना पान १',
        'sample_2_name': 'टोमॅटो - निरोगी (Healthy)',
        'sample_2_sub': 'नमुना पान २',
        'sample_3_name': 'बटाटा - तांबेरा (Late Blight)',
        'sample_3_sub': 'नमुना पान ३',
        'sample_4_name': 'सफरचंद - खपल्या (Apple Scab)',
        'sample_4_sub': 'नमुना पान ४',
        'btn_start_analysis': '🔬 पिकाचे विश्लेषण करा',
        'analyzing_img': 'तुमच्या पिकाच्या पानाचे विश्लेषण सुरू आहे…',
        'processing_msg': 'छायाचित्र प्रक्रिया सुरू आहे...',
        'analyzing_symptoms': 'दिसणाऱ्या लक्षणांचे विश्लेषण सुरू आहे...',
        'identifying_disease': 'संभाव्य रोग ओळखला जात आहे...',
        'preparing_guidance': 'शिफारसी तयार केल्या जात आहेत...',
        'selected_file_label': 'निवडलेली फाईल: ',
        'err_select_image': 'कृपया प्रथम पिकाच्या पानाचे छायाचित्र निवडा किंवा ड्रॅग करा.',
        'err_unsupported_format': 'असमर्थित फॉरमॅट. कृपया JPG, JPEG, PNG किंवा WEBP छायाचित्र अपलोड करा.',
        'err_file_too_large': 'फाईलचा आकार १० MB मर्यादेपेक्षा जास्त आहे. कृपया लहान छायाचित्र निवडा.',
        'err_analysis_failed': 'पीक विश्लेषण पूर्ण करण्यात अडचण आली.',
        'err_network_error': 'छायाचित्र प्रक्रियेदरम्यान नेटवर्क त्रुटी आली.',

        # Diagnostic Result Report (/result & /gemini-result)
        'report_title': 'एआय पीक आरोग्य निदान अहवाल',
        'report_subtitle': 'रीअल-टाइम दृश्य पॅथॉलॉजी व अचूक कृषी मार्गदर्शन',
        'gemini_badge_text': 'गूगल जेमिनी एआय व्हिजन द्वारे विश्लेषण',
        'gemini_badge_sub': '• दृश्य पीक विश्लेषण',
        'btn_print_report': 'अहवाल प्रिंट करा',
        'btn_copy_summary': 'अहवाल कॉपी करा',
        'btn_new_analysis': 'नवीन विश्लेषण करा',
        'jump_overview': '📊 आढावा',
        'jump_visual': '📸 छायाचित्र व तीव्रता',
        'jump_actions': '⚡ उपाययोजना',
        'jump_treatments': '🧪 उपचार पद्धती',
        'jump_nutrients': '🌾 खत व माती',
        'jump_insights': '🔍 सखोल माहिती',

        # 5 Overview Cards
        'card_crop_species': 'पिकाचे नाव व जात',
        'card_condition': 'आढळलेला रोग / स्थिती',
        'card_confidence': 'विश्वास पातळी (Confidence)',
        'card_health_status': 'आरोग्य स्थिती',
        'card_action_urgency': 'कृतीची तातडी',
        'plant_id_label': 'पीक ओळख:',
        'category_label': 'रोग वर्ग:',
        'diagnostic_status_label': 'निदान स्थिती',

        # Photo & Severity Card
        'analyzed_leaf_photo': 'तपासलेले पानाचे छायाचित्र',
        'leaf_sample_placeholder': 'अपलोड केलेले पानाचे छायाचित्र',
        'pathology_severity_title': 'रोगाच्या तीव्रतेचा टप्पा',
        'severity_assessment_label': 'तीव्रतेचे सविस्तर कारण:',

        # Actionable Guidance Section
        'actionable_guidance_title': '⚡ शेतकऱ्यांसाठी प्रत्यक्ष कृती मार्गदर्शन',
        'actionable_guidance_sub': 'पीक आरोग्य विश्लेषणानुसार पुढील शिफारस केलेल्या पायऱ्या',
        'ai_guided_actions_badge': 'एआय मार्गदर्शित कृती',
        'what_do_now_title': 'मी आता प्रथम काय करावे?',
        'what_do_now_sub': 'सध्याच्या निदानानुसार खालील उपाययोजनांचे पालन करा',
        'immediate_priority': '● तात्काळ प्राधान्य',
        'do_now': 'आता करा',
        'primary_action_title': '🔍 प्राथमिक कृती: पाहणी व बाधित भाग वेगळा करा',
        'rec_24_hours': '⏱ शिफारस: २४ तासांच्या आत त्वरित अंमलबजावणी करा',
        'step_inspection_monitoring': 'पाहणी व निरीक्षण',
        'step_sanitation_prevention': 'स्वच्छता व प्रतिबंध',
        'step_treatment_protocol': 'उपचार पद्धती',
        'step_expert_support': 'तज्ज्ञांचा सल्ला',
        'time_24_48_hours': '२४–४८ तास',
        'time_recommended': 'शिफारस केलेले',
        'time_if_needed': 'आवश्यकतेनुसार',
        'default_act_1_title': '🔍 लगतच्या पानांची पाहणी करा',
        'default_act_1_desc': 'त्याच ओळीतील लगतच्या झाडांवर व पानांवर असे डाग किंवा पिवळेपणा आला आहे का ते तपासा.',
        'default_act_1_rec': '⏱ शिफारस: त्वरित',
        'default_act_2_title': '👁 रोगाच्या वाढीवर लक्ष ठेवा',
        'default_act_2_desc': 'पुढील २४ ते ४८ तासांत डाग किंवा पिवळेपणा वाढत आहे का याचे निरीक्षण करा.',
        'default_act_3_title': '🛡 सेंद्रिय व स्वच्छता उपाययोजना करा',
        'default_act_3_desc': 'जास्त बाधित पाने काढून नष्ट करा, तुषार सिंचन टाळा आणि तांबायुक्त सेंद्रिय बुरशीनाशक वापरा.',
        'default_act_4_title': '👨‍🌾 कृषी तज्ज्ञांचा सल्ला घ्या',
        'default_act_4_desc': 'लक्षणे वेगाने पसरत असल्यास किंवा पाने गळत असल्यास जवळच्या कृषी विस्तार अधिकाऱ्यांशी संपर्क साधा.',

        # Action Urgency Status Card
        'urgency_critical_title': 'अत्यंत गंभीर',
        'urgency_critical_sub': '● कृषी तज्ज्ञांचा त्वरित सल्ला घ्या',
        'urgency_critical_desc': 'रोगाचा धोका जास्त आहे. त्वरित बाधित भाग वेगळा करून तज्ज्ञांचा सल्ला घेणे आवश्यक आहे.',
        'urgency_high_title': 'उच्च तातडी',
        'urgency_high_sub': '● त्वरित लक्ष देणे आवश्यक',
        'urgency_high_desc': 'पानांवर लक्षणीय रोग आढळला आहे. स्वच्छता आणि उपचारांची तत्काळ अंमलबजावणी करा.',
        'urgency_mod_title': 'मध्यम',
        'urgency_mod_sub': '● योग्य लक्ष व काळजी घ्या',
        'urgency_mod_desc': 'पिकाचे बारकाईने निरीक्षण करा आणि २४ ते ४८ तासांत योग्य प्रतिबंधात्मक पावले उचला.',
        'urgency_low_title': 'कमी / सामान्य',
        'urgency_low_sub': '● नियमित निरीक्षण ठेवा',
        'urgency_low_desc': 'पानांवर अत्यल्प किंवा कोणतीही रोग लक्षणे नाहीत. नेहमीप्रमाणे पीक व्यवस्थापन चालू ठेवा.',
        'urgency_unk_title': 'अज्ञात',
        'urgency_unk_sub': '● स्थिती अनिश्चित',
        'urgency_unk_desc': 'छायाचित्रावरून तातडीची पातळी निश्चित करता आली नाही.',

        # Monitor & Expert Help Cards
        'monitor_signs_title': 'पुढील निरीक्षणासाठी धोक्याची लक्षणे',
        'sign_1': 'नवीन डाग किंवा कडा पिवळ्या पडणे',
        'sign_2': 'पानांचा पिवळेपणा वाढणे (क्लोरोसिस)',
        'sign_3': 'वेळेआधी पाने गळणे किंवा कोमेजणे',
        'sign_4': 'लगतच्या ओळींमधील झाडांवर लक्षणे दिसणे',
        'sign_5': 'खोड किंवा फळांवर डाग पडणे',
        'expert_help_title': 'कृषी तज्ज्ञांचा सल्ला कधी घ्यावा?',
        'expert_help_intro': 'खालील परिस्थिती आढळल्यास कृषी तज्ज्ञांचा सल्ला नक्की घ्या:',
        'expert_help_1': 'लक्षणे वेगाने एकापेक्षा जास्त झाडांवर पसरत असल्यास',
        'expert_help_2': 'एआयची विश्वास पातळी कमी किंवा अनिश्चित असल्यास',
        'expert_help_3': 'सेंद्रिय किंवा रासायनिक उपायांनंतरही रोग नियंत्रणात येत नसल्यास',
        'expert_help_4': 'मोठ्या प्रमाणावर पाने गळून पडत असल्यास',

        # Management & Treatments Section
        'treatments_title': 'व्यवस्थापन व उपचार पर्याय',
        'organic_mgmt_title': 'सेंद्रिय व्यवस्थापन पर्याय',
        'conventional_mgmt_title': 'रासायनिक फवारणी मार्गदर्शन',
        'no_organic_req': 'विशिष्ट सेंद्रिय उपचारांची आवश्यकता नाही.',
        'no_conventional_req': 'विशिष्ट रासायनिक फवारणीची आवश्यकता नाही.',

        # Fertilizer & Nutrient Guidance
        'fertilizer_title': 'खत व अन्नद्रव्य व्यवस्थापन',
        'suspected_deficiency_label': 'संभाव्य अन्नद्रव्य कमतरता:',
        'visible_evidence_label': 'दिसणारी लक्षणे:',
        'organic_option_label': 'सेंद्रिय पर्याय:',
        'conventional_option_label': 'रासायनिक पर्याय:',
        'soil_testing_rec_label': 'माती परीक्षण शिफारस:',
        'no_nutrient_deficiency': 'या पानावरून अन्नद्रव्यांची कोणतीही स्पष्ट कमतरता दिसून येत नाही.',
        'default_nutrient_correction': 'अन्नद्रव्य समतोल राखण्याची शिफारस',
        'default_leaf_symptoms': 'पानावरील लक्षणे अन्नद्रव्य असमतोल दर्शवतात',
        'default_organic_amendment': 'कंपोस्ट खत किंवा जीवामृत वापरा',
        'default_conventional_npk': 'संतुलित एनपीके खतांचा वापर',

        # Additional Diagnostic Insights
        'insights_title': 'अतिरिक्त रोग निदान माहिती',
        'visible_symptoms_title': 'पानावर दिसणारी लक्षणे',
        'possible_causes_title': 'संभाव्य कारणे व रोगजंतू',
        'pest_analysis_title': 'कीड व कीटक विश्लेषण',
        'pest_suspected_label': 'कीड प्रादुर्भावाची शक्यता:',
        'evidence_label': 'दिसणारे पुरावे:',
        'no_pest_visible': 'पानावर कोणताही कीटक प्रादुर्भाव किंवा नुकसान दिसत नाही.',
        'environmental_factors_title': 'वातावरणाचा ताण व घटक',
        'no_env_stress': 'वातावरणाचा गंभीर ताण दिसत नाही.',
        'preventive_measures_title': 'प्रतिबंधात्मक उपाययोजना',
        'standard_gap_rec': 'चांगल्या कृषी पद्धतींचे (GAP) नियमित पालन करा.',
        'analysis_notes_title': 'निदान टीप व मर्यादा',
        'none_specified': 'कोणतीही विशिष्ट नोंद नाही.',

        # Disclaimer & CTA
        'disclaimer_heading': '📢 महत्त्वाची कृषी सूचना (Disclaimer):',
        'disclaimer_notice': 'एग्रीव्हिजन एआय दृश्य लक्षणांवर आधारित प्राथमिक माहिती प्रदान करते. अंतिम प्रमाणीकरणासाठी व औषध फवारणीच्या योग्य प्रमाणासाठी स्थानिक कृषी तज्ज्ञांचा किंवा कृषी विद्यापीठाचा सल्ला घ्या. औषध फवारताना पाकिटावरील सूचनांचे काटेकोर पालन करा.',
        'btn_analyze_another': '📷 दुसऱ्या पानाचे छायाचित्र तपासा',

        # History Page (/history)
        'history_tag': 'जतन केलेले निदान नोंदी',
        'history_title': 'पिकांच्या निदानांचा इतिहास',
        'history_subtitle': 'पूर्वीच्या पीक आरोग्य निदानांची नोंद, रोगाची तीव्रता आणि अहवाल पहा.',
        'stat_total_analyzed': 'एकूण विश्लेषण',
        'stat_healthy_leaf': 'निरोगी पाने',
        'stat_moderate_watch': 'मध्यम / देखरेख',
        'stat_urgent_priority': 'तातडीचे उपचार',
        'search_placeholder': '🔍 पीक किंवा रोगाच्या नावाने शोधा...',
        'severity_filter_label': 'तीव्रता:',
        'opt_all_severities': 'सर्व तीव्रता',
        'opt_healthy': '🟢 निरोगी (Healthy)',
        'opt_low': '🟡 कमी तीव्रता',
        'opt_moderate': '🟠 मध्यम',
        'opt_high': '🔴 उच्च तीव्रता',
        'opt_critical': '🚨 अत्यंत गंभीर',
        'btn_filter': 'शोधा / फिल्टर',
        'btn_reset': 'रीसेट करा',
        'col_date': 'दिनांक व वेळ',
        'col_image': 'पानाचे छायाचित्र',
        'col_crop': 'पीक',
        'col_condition': 'ओळखलेला रोग',
        'col_confidence': 'विश्वास पातळी',
        'col_severity': 'तीव्रता',
        'col_actions': 'कृती',
        'btn_view_report': 'पूर्ण अहवाल पहा →',
        'delete_record': 'हटवा',
        'tooltip_delete': 'नोंद हटवा',
        'confirm_delete_record': 'तुम्हाला ही निदानाची नोंद खरंच हटवायची आहे का?',
        'empty_history': 'तुमच्या इतिहासात अद्याप कोणत्याही निदानाची नोंद नाही.',
        'empty_history_desc': 'पिकाच्या पानाचा फोटो अपलोड करून एआय रोग निदान सुरू करा आणि नोंदी ठेवा.',

        # About Page (/about)
        'about_tag': 'एग्रीव्हिजन एआय बद्दल',
        'about_title': 'अचूक शेतीसाठी सुलभ व पारदर्शक एआय तंत्रज्ञान',
        'about_subtitle': 'डीप लर्निंग कॉम्प्युटर व्हिजन आणि पारदर्शक पीक मार्गदर्शनाचा संगम.',
        'platform_overview_tag': 'प्लॅटफॉर्मचा परिचय',
        'platform_overview_title': 'एग्रीव्हिजन एआय बद्दल',
        'platform_overview_desc': 'एग्रीव्हिजन एआय ही एक प्रगत कृषी सहाय्यक प्रणाली आहे, जी पिकांच्या रोगांचे प्राथमिक निदान, दृश्य विश्लेषण आणि शेतकऱ्यांसाठी प्रत्यक्ष कृती मार्गदर्शन प्रदान करते.',
        'core_objective_tag': 'मुख्य उद्दिष्ट',
        'our_mission': 'आमचे ध्येय',
        'our_mission_desc': 'शेतकरी, कृषी विस्तारक आणि कृषी तज्ज्ञांना सुलभ एआय तंत्रज्ञानाद्वारे सक्षम करणे, पिकांचे वेळेवर रक्षण करणे आणि अनावश्यक रासायनिक कीटकनाशकांचा वापर कमी करणे.',
        'how_ai_helps': 'एआय शेतीला कशी मदत करते',
        'how_ai_helps_desc': 'कॉम्प्युटर व्हिजन मॉडेल्स पानांमधील करपा, डाग, बुरशी आणि पिवळेपणाचे बारकाईने विश्लेषण करून रोग मोठ्या प्रमाणावर पसरण्याआधीच त्याची अचूक माहिती देतात.',
        'xai_title': 'सुलभ व पारदर्शक एआय (XAI)',
        'xai_desc': 'केवळ निकाल देण्याऐवजी, एग्रीव्हिजन एआय पानातील नेमक्या कोणत्या भागावरून निर्णय घेतला हे Grad-CAM हीटमॅपद्वारे स्पष्टपणे दाखवते.',
        'tech_stack_tag': 'तांत्रिक रचना',
        'tech_stack_title': 'वापरलेले तंत्रज्ञान',
        'tech_python_desc': 'डेटा प्रोसेसिंग, एपीआय आणि कॉम्प्युटर व्हिजन चालवणारी प्रमुख बॅकएंड भाषा.',
        'tech_flask_desc': 'हलके व जलद WSGI वेब फ्रेमवर्क, जे रेस्ट एपीआय आणि टेम्पलेट्स व्यवस्थापित करते.',
        'tech_gemini_desc': 'अधिकृत गूगल जेमिनी व्हिजन मॉडेल, जे रिअल-टाइम दृश्य पॅथॉलॉजी ओळखते.',
        'tech_vision_desc': 'छायाचित्र तपासणी, स्केलिंग आणि पानांच्या गुणवत्तेसाठी कॉम्प्युटर व्हिजन लायब्ररी.',
        'tech_gradcam_desc': 'एआयच्या निर्णयाचे दृश्य स्पष्टीकरण देणारे प्रगत हीटमॅप तंत्रज्ञान.',
        'tech_db_desc': 'निदान नोंदी आणि कृषी माहिती जतन करणारी डेटाबेस प्रणाली.',
        'tech_frontend_desc': 'सर्व उपकरणांवर सुरळीत चालणारी आधुनिक सीएसएस आणि जावास्क्रिप्ट डिझाइन प्रणाली.',
        'system_works_title': 'प्रणाली कशी कार्य करते',
        'pipe_1_title': 'छायाचित्र अपलोड करा',
        'pipe_1_desc': 'बाधित पिकाच्या पानाचा स्पष्ट व जवळून घेतलेला फोटो अपलोड करा.',
        'pipe_2_title': 'छायाचित्र प्रक्रिया',
        'pipe_2_desc': 'सर्व्हर छायाचित्राचा फॉरमॅट, रिझोल्यूशन आणि पानाची गुणवत्ता तपासतो.',
        'pipe_3_title': 'एआय निदान',
        'pipe_3_desc': 'जेमिनी व्हिजन मॉडेल पिकाची जात, रोग आणि त्याची तीव्रता ओळखते.',
        'pipe_4_title': 'सुलभ दृश्य स्पष्टीकरण',
        'pipe_4_desc': 'पानावरील डागांचे प्रमाण आणि व्हिज्युअल हीटमॅप तयार करतो.',
        'pipe_5_title': 'रोगाची सविस्तर माहिती',
        'pipe_5_desc': 'रोगाची लक्षणे, संभाव्य कारणे आणि कीड विश्लेषण दर्शवतो.',
        'pipe_6_title': 'व्यवस्थापन मार्गदर्शन',
        'pipe_6_desc': 'शेतकऱ्यांसाठी प्राधान्यक्रमाने कृती, सेंद्रिय उपाय आणि फवारणी मार्गदर्शन देतो.',
        'limitations_title': 'महत्त्वाच्या एआय मर्यादा',
        'limitations_intro': 'एग्रीव्हिजन एआय हे निर्णय-सहाय्यक साधन आहे. वापरकर्त्यांनी खालील मर्यादा लक्षात घ्याव्यात:',
        'limit_1': 'एआय निदान हे छायाचित्रातील दृश्य लक्षणांवर आणि फोटोच्या गुणवत्तेवर अवलंबून असते.',
        'limit_2': 'काही वेगवेगळ्या रोगांमध्ये पानांवर एकसारखेच डाग किंवा पिवळेपणा दिसू शकतो.',
        'limit_3': 'उन्हामुळे करपणे किंवा वाऱ्यामुळे झालेले नुकसान रोगासारखे भासू शकते.',
        'limit_4': 'छायाचित्रावरून जमिनीचा सामू (pH), नत्राचे प्रमाण किंवा मुळांची कूज तपासता येत नाही.',
        'limit_5': 'एआय माहिती कृषी तज्ज्ञांच्या प्रत्यक्ष सल्ल्याची किंवा प्रयोगशाळा चाचणीची जागा घेऊ शकत नाही.',

        # Contact Page (/contact)
        'contact_tag': 'संपर्क करा',
        'contact_title': 'संपर्क व अभिप्राय',
        'contact_subtitle': 'तुमच्या काही शंका, अभिप्राय किंवा सूचना असल्यास आमच्याशी नक्की संपर्क साधा.',
        'form_name': 'तुमचे पूर्ण नाव *',
        'form_name_placeholder': 'तुमचे नाव टाका',
        'form_email': 'ईमेल पत्ता *',
        'form_email_placeholder': 'name@example.com',
        'form_subject': 'विषय',
        'form_subject_placeholder': 'उदा. मॉडेलबद्दल अभिप्राय किंवा सामान्य विचारणा',
        'form_message': 'तुमचा संदेश *',
        'form_message_placeholder': 'तुमचा प्रश्न किंवा अभिप्राय येथे लिहा...',
        'send_btn': '✉️ संदेश पाठवा',
        'toast_form_required': 'कृपया संदेश पाठवण्यापूर्वी सर्व आवश्यक रकाने भरा.',
        'toast_valid_email': 'कृपया वैध ईमेल पत्ता टाका.',
        'toast_copied': 'निदान सारांश क्लिपबोर्डवर कॉपी झाला!',
        'toast_copy_failed': 'सारांश कॉपी करता आला नाही.'
    },

    'hi': {
        # Navigation & Header
        'app_name': 'एग्रीविज़न एआई',
        'app_subtitle': 'सटीक एवं आसान फसल रोग निदान प्रणाली',
        'home': 'मुख्य पृष्ठ',
        'detect_disease': 'रोग पहचानें',
        'history': 'निदान इतिहास',
        'about': 'हमारे बारे में',
        'contact': 'संपर्क करें',
        'language': 'भाषा',
        'english': 'English',
        'marathi': 'मराठी',
        'hindi': 'हिंदी',
        'analyze_crop': '🔍 फसल की जांच करें',
        'toggle_theme': 'लाइट/डार्क मोड बदलें',
        'menu_toggle': 'मेनू खोलें/बंद करें',

        # Footer
        'footer_brand_desc': 'फसल की पत्तियों में बीमारियों की समय पर पहचान, विज़ुअल विश्लेषण (Heatmaps), रोग की गंभीरता और आसान कृषि सलाह के लिए निर्मित एआई प्रणाली।',
        'footer_nav_heading': 'नेविगेशन',
        'footer_cap_heading': 'क्षमताएं एवं सुविधाएं',
        'footer_tech_heading': 'तकनीकी ढांचा',
        'footer_rights': 'सर्वाधिकार सुरक्षित। सटीक एवं आसान कृषि सलाह के लिए निर्मित।',
        'cap_leaf_analysis': 'रियल-टाइम एआई पत्ती जांच',
        'cap_severity_est': 'रोग गंभीरता का सटीक आंकलन',
        'cap_heatmaps': 'Grad-CAM विज़ुअल हीटमैप्स',
        'cap_guidance': 'जैविक एवं रासायनिक मार्गदर्शन',
        'tech_gemini': 'गूगल जेमिनी विज़न एआई',
        'tech_vision_scanner': 'कंप्यूटर विज़न लीफ स्कैनर',
        'tech_flask': 'पायथन फ्लास्क बैकएंड',
        'tech_xai': 'पारदर्शी एवं सुगम एआई सलाह',

        # Hero & Home Page
        'hero_badge': '🤖 गूगल जेमिनी विजन एआई एवं एक्सएआई',
        'hero_title_1': 'एआई तकनीक से अपनी फसलों को ',
        'hero_title_2': 'बीमारियों',
        'hero_subtitle': 'अपनी फसल की पत्ती की तस्वीर अपलोड करें और एआई द्वारा बीमारी की सटीक पहचान, लक्षणों का विश्लेषण तथा जैविक व रासायनिक उपचार पाएं।',
        'btn_analyze_leaf': '🔍 फसल की पत्ती जांचें',
        'trust_realtime_ai': '✓ रियल-टाइम विजन एआई',
        'trust_explainable': '✓ आसान एआई मार्गदर्शन',
        'trust_solutions': '✓ जैविक और रासायनिक उपाय',
        'floating_condition_val': 'अगेती झुलसा (Early Blight)',
        'floating_severity_val': 'मध्यम',

        # How AgriVision AI Works
        'how_tag': 'पेशेवर एआई कार्यप्रणाली',
        'how_title': 'एग्रीविज़न एआई कैसे काम करता है',
        'how_subtitle': 'तस्वीर खींचने से लेकर फसल सुरक्षा के व्यावहारिक सुझावों तक, एग्रीविज़न एआई आपकी फसल का आसान और समझने योग्य स्वास्थ्य विश्लेषण प्रदान करता है।',
        'step_01_title': 'फसल की तस्वीर अपलोड करें',
        'step_01_desc': 'प्रभावित पत्ते की स्पष्ट तस्वीर लें या अपने स्मार्टफोन अथवा कंप्यूटर से अपलोड करें।',
        'step_02_title': 'एआई पत्ते का विश्लेषण करता है',
        'step_02_desc': 'एआई विजन मॉडल पत्ते पर मौजूद धब्बों, पीलेपन, झुलसा और बनावट का गहराई से विश्लेषण करता है।',
        'step_03_title': 'संभावित रोग की पहचान करें',
        'step_03_desc': 'प्रशिक्षित एआई मॉडल बीमारी की सटीक पहचान, विश्वास स्तर और गंभीरता का निर्धारण करता है।',
        'step_04_title': 'फसल सुरक्षा सुझाव प्राप्त करें',
        'step_04_desc': 'किसानों के लिए प्रत्यक्ष कदम, जैविक समाधान, रासायनिक छिड़काव और उर्वरक प्रबंधन की सलाह पाएं।',
        'chip_formats': 'JPG, PNG, WEBP',
        'chip_lighting': 'उचित रोशनी',
        'chip_drag_drop': 'ड्रैग एंड ड्रॉप',
        'chip_processing': 'तस्वीर संसाधित की जा रही है...',
        'chip_symptoms': 'लक्षणों का विश्लेषण जारी है...',
        'chip_disease_name': 'अगेती झुलसा (Early Blight)',
        'chip_confidence': '९४% विश्वास स्तर',
        'chip_moderate': 'मध्यम चरण',
        'workflow_cta_title': 'क्या आप अपनी फसल की जांच करने के लिए तैयार हैं?',
        'workflow_cta_desc': 'तुरंत बीमारी की पहचान और जैविक प्रबंधन के उपाय प्राप्त करें।',
        'workflow_cta_btn': 'फसल के पत्ते की जांच करें →',

        # Platform Capabilities / 10 Feature Cards
        'features_tag': 'मंच की क्षमताएं',
        'features_title': 'एग्रीविज़न एआई की मुख्य विशेषताएं',
        'features_subtitle': 'कृषि में पारदर्शिता, सहजता और व्यावहारिक मार्गदर्शन के लिए विशेष रूप से डिज़ाइन किया गया।',
        'feat_1_title': 'एआई फसल रोग पहचान',
        'feat_1_desc': 'डीप लर्निंग न्यूरल नेटवर्क द्वारा पत्तियों में लगने वाली बीमारियों की तुरंत पहचान करें।',
        'feat_2_title': 'विश्वास स्तर विश्लेषण',
        'feat_2_desc': 'मॉडल के पूर्वानुमान का विश्वास स्तर (उच्च, मध्यम, निम्न) स्पष्ट रूप से देखें।',
        'feat_3_title': 'स्पष्ट एआई (Grad-CAM)',
        'feat_3_desc': 'हीटमैप द्वारा देखें कि एआई ने पत्ते के किन हिस्सों के आधार पर निष्कर्ष निकाला है।',
        'feat_4_title': 'रोग अवस्था का आंकलन',
        'feat_4_desc': 'रोग के फैलाव का चरण (प्रारंभिक, विकासशील, मध्यम, गंभीर) जानें।',
        'feat_5_title': 'रोग की गंभीरता एवं प्रभावित क्षेत्र',
        'feat_5_desc': 'पत्ती पर धब्बों का प्रतिशत (०-१००%) और गंभीरता की श्रेणी जांचें।',
        'feat_6_title': 'रोग की विस्तृत जानकारी',
        'feat_6_desc': 'रोग के मुख्य लक्षण, कारक और रोगाणु के प्रकार की पूरी जानकारी प्राप्त करें।',
        'feat_7_title': 'जैविक प्रबंधन',
        'feat_7_desc': 'जैविक कीटनाशक, स्वच्छता के तरीके और सुरक्षित प्राकृतिक उपचार पाएं।',
        'feat_8_title': 'रासायनिक छिड़काव निर्देश',
        'feat_8_desc': 'सुरक्षा चेतावनी के साथ उचित रासायनिक दवाओं एवं सक्रिय तत्वों की जानकारी।',
        'feat_9_title': 'उर्वरक एवं पोषण सलाह',
        'feat_9_desc': 'फसल की मजबूती के लिए नाइट्रोजन, फॉस्फोरस, पोटाश व पोषक तत्वों की सलाह।',
        'feat_10_title': 'रोकथाम एवं निगरानी',
        'feat_10_desc': 'रोग को फैलने से रोकने और आगामी फसल को सुरक्षित रखने के उपाय।',

        # Upload Portal (/detect)
        'upload_portal_tag': 'एआई निदान पोर्टल',
        'upload_portal_title': 'रोग पहचान के लिए फसल के पत्ते की तस्वीर अपलोड करें',
        'upload_portal_subtitle': 'बीमारी के लक्षण दिखाई देने वाले पत्ते की साफ और अच्छी रोशनी वाली तस्वीर अपलोड करें।',
        'quick_tips_title': 'बेहतर परिणाम के लिए जरूरी टिप्स',
        'quick_tip_1': 'एक ही फसल के पत्ते की साफ और अच्छी रोशनी वाली तस्वीर लें।',
        'quick_tip_2': 'तस्वीर को धुंधली होने से बचाएं और पत्ते पर फोकस रखें।',
        'quick_tip_3': 'अत्यधिक चमक या गहरे साये के बिना प्राकृतिक रोशनी में फोटो लें।',
        'quick_tip_4': 'बीमारी से प्रभावित हिस्सा स्पष्ट रूप से दिखाई देना चाहिए।',
        'quick_tip_5': 'पत्ते को उंगलियों, औजारों या अन्य वस्तुओं से न ढकें।',
        'drag_drop_text': 'तस्वीर को यहां ड्रैग और ड्रॉप करें, या',
        'browse_files': '📁 तस्वीर चुनें',
        'take_photo': '📷 फोटो खींचें',
        'change_image': '🔄 तस्वीर बदलें',
        'remove_image': 'तस्वीर हटाएं',
        'supported_formats': 'समर्थित प्रारूप: JPG, JPEG, PNG, WEBP (अधिकतम 10MB)',
        'quick_test_leaves': 'त्वरित परीक्षण के लिए नमूना पत्तियां:',
        'sample_1_name': 'टमाटर - अगेती झुलसा (Early Blight)',
        'sample_1_sub': 'नमूना पत्ता 1',
        'sample_2_name': 'टमाटर - स्वस्थ (Healthy)',
        'sample_2_sub': 'नमूना पत्ता 2',
        'sample_3_name': 'आलू - पछेती झुलसा (Late Blight)',
        'sample_3_sub': 'नमूना पत्ता 3',
        'sample_4_name': 'सेब - पपड़ी रोग (Apple Scab)',
        'sample_4_sub': 'नमूना पत्ता 4',
        'btn_start_analysis': '🔬 फसल का विश्लेषण करें',
        'analyzing_img': 'आपकी फसल की पत्ती का विश्लेषण किया जा रहा है…',
        'processing_msg': 'तस्वीर संसाधित की जा रही है...',
        'analyzing_symptoms': 'दिखाई देने वाले लक्षणों का विश्लेषण किया जा रहा है...',
        'identifying_disease': 'संभावित रोग की पहचान की जा रही है...',
        'preparing_guidance': 'सुझाव तैयार किए जा रहे हैं...',
        'selected_file_label': 'चयनित फ़ाइल: ',
        'err_select_image': 'कृपया पहले फसल की पत्ती की तस्वीर चुनें या ड्रैग करें।',
        'err_unsupported_format': 'असमर्थित प्रारूप। कृपया JPG, JPEG, PNG या WEBP तस्वीर अपलोड करें।',
        'err_file_too_large': 'फ़ाइल का आकार 10 MB सीमा से अधिक है। कृपया छोटी तस्वीर चुनें।',
        'err_analysis_failed': 'फसल विश्लेषण पूरा करने में असमर्थ।',
        'err_network_error': 'तस्वीर प्रसंस्करण के दौरान नेटवर्क त्रुटि हुई।',

        # Diagnostic Result Report (/result & /gemini-result)
        'report_title': 'एआई फसल स्वास्थ्य निदान रिपोर्ट',
        'report_subtitle': 'रीयल-टाइम विज़ुअल पैथोलॉजी एवं सटीक कृषि मार्गदर्शन',
        'gemini_badge_text': 'गूगल जेमिनी एआई विज़न द्वारा विश्लेषण',
        'gemini_badge_sub': '• विज़ुअल फसल विश्लेषण',
        'btn_print_report': 'रिपोर्ट प्रिंट करें',
        'btn_copy_summary': 'सारांश कॉपी करें',
        'btn_new_analysis': 'नई जांच करें',
        'jump_overview': '📊 अवलोकन',
        'jump_visual': '📸 फोटो व गंभीरता',
        'jump_actions': '⚡ उपाय',
        'jump_treatments': '🧪 उपचार विधि',
        'jump_nutrients': '🌾 खाद व मिट्टी',
        'jump_insights': '🔍 गहन जानकारी',

        # 5 Overview Cards
        'card_crop_species': 'फसल का नाम एवं प्रजाति',
        'card_condition': 'पहचाना गया रोग / स्थिति',
        'card_confidence': 'विश्वास स्तर (Confidence)',
        'card_health_status': 'स्वास्थ्य स्थिति',
        'card_action_urgency': 'कार्रवाई की गंभीरता',
        'plant_id_label': 'पौधे की पहचान:',
        'category_label': 'रोग श्रेणी:',
        'diagnostic_status_label': 'निदान स्थिति',

        # Photo & Severity Card
        'analyzed_leaf_photo': 'विश्लेषित पत्ती की फोटो',
        'leaf_sample_placeholder': 'अपलोड की गई पत्ती का नमूना',
        'pathology_severity_title': 'रोग गंभीरता का स्तर',
        'severity_assessment_label': 'गंभीरता का विवरण:',

        # Actionable Guidance Section
        'actionable_guidance_title': '⚡ किसानों के लिए प्रत्यक्ष कार्रवाई मार्गदर्शन',
        'actionable_guidance_sub': 'फसल स्वास्थ्य विश्लेषण के आधार पर अनुशंसित अगले कदम',
        'ai_guided_actions_badge': 'एआई निर्देशित कदम',
        'what_do_now_title': 'मुझे अभी पहले क्या करना चाहिए?',
        'what_do_now_sub': 'वर्तमान विश्लेषण के आधार पर इन सुझाई गई प्रक्रियाओं का पालन करें',
        'immediate_priority': '● तत्काल प्राथमिकता',
        'do_now': 'अभी करें',
        'primary_action_title': '🔍 प्राथमिक कदम: निरीक्षण एवं प्रभावित भाग अलग करें',
        'rec_24_hours': '⏱ अनुशंसित: २४ घंटे के भीतर तुरंत अमल में लाएं',
        'step_inspection_monitoring': 'निरीक्षण एवं निगरानी',
        'step_sanitation_prevention': 'स्वच्छता एवं रोकथाम',
        'step_treatment_protocol': 'उपचार प्रक्रिया',
        'step_expert_support': 'विशेषज्ञ सहायता',
        'time_24_48_hours': '२४–४८ घंटे',
        'time_recommended': 'अनुशंसित',
        'time_if_needed': 'आवश्यकतानुसार',
        'default_act_1_title': '🔍 आस-पास की पत्तियों का निरीक्षण करें',
        'default_act_1_desc': 'उसी पंक्ति के आस-पास के पौधों और पत्तियों पर ऐसे धब्बे या पीलापन जांचें।',
        'default_act_1_rec': '⏱ अनुशंसित: अभी',
        'default_act_2_title': '👁 रोग के फैलाव पर नजर रखें',
        'default_act_2_desc': 'अगले २४ से ४८ घंटों में देखें कि धब्बे या पीलापन और बढ़ तो नहीं रहा।',
        'default_act_3_title': '🛡 जैविक एवं स्वच्छता के उपाय करें',
        'default_act_3_desc': 'अधिक संक्रमित निचली पत्तियां हटा दें, फव्वारा सिंचाई से बचें और कॉपर युक्त जैविक कवकनाशी का प्रयोग करें।',
        'default_act_4_title': '👨‍🌾 कृषि विशेषज्ञ से सलाह लें',
        'default_act_4_desc': 'यदि लक्षण तेजी से फैल रहे हों या पत्ते झड़ रहे हों तो नजदीकी कृषि प्रसार अधिकारी से संपर्क करें।',

        # Action Urgency Status Card
        'urgency_critical_title': 'अत्यंत गंभीर',
        'urgency_critical_sub': '● तुरंत विशेषज्ञ से सलाह लें',
        'urgency_critical_desc': 'रोग का जोखिम अधिक है। तुरंत प्रभावित हिस्से को अलग कर विशेषज्ञ से परामर्श लें।',
        'urgency_high_title': 'उच्च प्राथमिकता',
        'urgency_high_sub': '● तुरंत ध्यान देना आवश्यक',
        'urgency_high_desc': 'पत्तियों पर गहरा रोग पाया गया है। स्वच्छता एवं उपचार के उपाय शीघ्र शुरू करें।',
        'urgency_mod_title': 'मध्यम',
        'urgency_mod_sub': '● उचित ध्यान एवं देखभाल रखें',
        'urgency_mod_desc': 'फसल की बारीकी से निगरानी करें और २४ से ४८ घंटों में उचित निवारक कदम उठाएं।',
        'urgency_low_title': 'सामान्य / कम',
        'urgency_low_sub': '● नियमित निगरानी रखें',
        'urgency_low_desc': 'पत्तियों पर रोग के कोई गंभीर लक्षण नहीं हैं। सामान्य रूप से फसल प्रबंधन जारी रखें।',
        'urgency_unk_title': 'अज्ञात',
        'urgency_unk_sub': '● स्थिति अपुष्ट',
        'urgency_unk_desc': 'तस्वीर से तात्कालिकता स्तर स्पष्ट रूप से निर्धारित नहीं हो सका।',

        # Monitor & Expert Help Cards
        'monitor_signs_title': 'आगे की निगरानी के लिए चेतावनी लक्षण',
        'sign_1': 'नए धब्बे या किनारों का पीला पड़ना',
        'sign_2': 'पत्तियों में पीलापन बढ़ना (क्लोरोसिस)',
        'sign_3': 'समय से पहले पत्तियां गिरना या मुरझाना',
        'sign_4': 'पास के पौधों पर भी लक्षण दिखाई देना',
        'sign_5': 'तनों या फलों पर काले धब्बे बनना',
        'expert_help_title': 'कृषि विशेषज्ञ की सलाह कब लें?',
        'expert_help_intro': 'निम्नलिखित स्थितियां होने पर कृषि विशेषज्ञ से परामर्श अवश्य लें:',
        'expert_help_1': 'लक्षण तेजी से कई पौधों में फैलने लगें',
        'expert_help_2': 'एआई का विश्वास स्तर कम या अनिश्चित हो',
        'expert_help_3': 'जैविक या रासायनिक उपचार के बाद भी फैलाव न रुके',
        'expert_help_4': 'पत्तियां अत्यधिक मात्रा में गिरने लगें',

        # Management & Treatments Section
        'treatments_title': 'प्रबंधन एवं उपचार समाधान',
        'organic_mgmt_title': 'जैविक प्रबंधन विकल्प',
        'conventional_mgmt_title': 'रासायनिक छिड़काव निर्देश',
        'no_organic_req': 'विशिष्ट जैविक उपचार की आवश्यकता नहीं है।',
        'no_conventional_req': 'विशिष्ट रासायनिक छिड़काव की आवश्यकता नहीं है।',

        # Fertilizer & Nutrient Guidance
        'fertilizer_title': 'उर्वरक एवं पोषण प्रबंधन',
        'suspected_deficiency_label': 'संभावित पोषण कमी:',
        'visible_evidence_label': 'दिखाई देने वाले लक्षण:',
        'organic_option_label': 'जैविक विकल्प:',
        'conventional_option_label': 'रासायनिक विकल्प:',
        'soil_testing_rec_label': 'मिट्टी परीक्षण सलाह:',
        'no_nutrient_deficiency': 'इस तस्वीर से किसी स्पष्ट पोषक तत्व की कमी दिखाई नहीं देती।',
        'default_nutrient_correction': 'पोषक तत्व संतुलन बनाए रखने की सलाह',
        'default_leaf_symptoms': 'पत्ती के लक्षण पोषक तत्वों के असंतुलन का संकेत देते हैं',
        'default_organic_amendment': 'कम्पोस्ट खाद या जैविक तरल खाद का प्रयोग',
        'default_conventional_npk': 'संतुलित एनपीके उर्वरक का उपयोग',

        # Additional Diagnostic Insights
        'insights_title': 'अतिरिक्त रोग निदान जानकारी',
        'visible_symptoms_title': 'पत्ती पर दिखाई देने वाले लक्षण',
        'possible_causes_title': 'संभावित कारण एवं रोगाणु',
        'pest_analysis_title': 'कीट एवं कीड़ा विश्लेषण',
        'pest_suspected_label': 'कीट प्रकोप की संभावना:',
        'evidence_label': 'दिखाई देने वाले प्रमाण:',
        'no_pest_visible': 'पत्ती पर किसी सक्रिय कीट या कीड़े का नुकसान नहीं दिख रहा है।',
        'environmental_factors_title': 'वातावरणीय तनाव एवं कारक',
        'no_env_stress': 'कोई गंभीर वातावरणीय तनाव दिखाई नहीं देता।',
        'preventive_measures_title': 'निवारक उपाय एवं सुरक्षा',
        'standard_gap_rec': 'उत्कृष्ट कृषि पद्धतियों (GAP) का नियमित पालन करें।',
        'analysis_notes_title': 'निदान टिप्पणी एवं सीमाएं',
        'none_specified': 'कोई विशेष उल्लेख नहीं।',

        # Disclaimer & CTA
        'disclaimer_heading': '📢 महत्वपूर्ण कृषि सूचना (Disclaimer):',
        'disclaimer_notice': 'एग्रीविज़न एआई दृश्य लक्षणों पर आधारित प्राथमिक जानकारी प्रदान करता है। अंतिम पुष्टि एवं दवा छिड़काव की सटीक मात्रा के लिए स्थानीय कृषि विशेषज्ञ या अनुसंधान केंद्र से सलाह लें। हमेशा स्थानीय रूप से स्वीकृत कृषि उत्पाद लेबल के निर्देशों का पालन करें।',
        'btn_analyze_another': '📷 किसी अन्य पत्ती की जांच करें',

        # History Page (/history)
        'history_tag': 'सुरक्षित निदान रिकॉर्ड',
        'history_title': 'निदान इतिहास लॉग',
        'history_subtitle': 'पिछली फसल जांच रिपोर्ट, बीमारी की गंभीरता और हीटमैप देखें।',
        'stat_total_analyzed': 'कुल विश्लेषण',
        'stat_healthy_leaf': 'स्वस्थ पत्तियां',
        'stat_moderate_watch': 'मध्यम / निगरानी',
        'stat_urgent_priority': 'तत्काल प्राथमिकता',
        'search_placeholder': '🔍 फसल या रोग के नाम से खोजें...',
        'severity_filter_label': 'गंभीरता:',
        'opt_all_severities': 'सभी गंभीरता स्तर',
        'opt_healthy': '🟢 स्वस्थ (Healthy)',
        'opt_low': '🟡 कम गंभीरता',
        'opt_moderate': '🟠 मध्यम',
        'opt_high': '🔴 उच्च गंभीरता',
        'opt_critical': '🚨 अत्यंत गंभीर',
        'btn_filter': 'खोजें / फ़िल्टर',
        'btn_reset': 'रीसेट करें',
        'col_date': 'दिनांक व समय',
        'col_image': 'पत्ते की तस्वीर',
        'col_crop': 'फसल',
        'col_condition': 'पहचाना गया रोग',
        'col_confidence': 'विश्वास स्तर',
        'col_severity': 'गंभीरता',
        'col_actions': 'कार्रवाई',
        'btn_view_report': 'पूरी रिपोर्ट देखें →',
        'delete_record': 'हटाएं',
        'tooltip_delete': 'रिकॉर्ड हटाएं',
        'confirm_delete_record': 'क्या आप वाकई इस निदान रिकॉर्ड को हटाना चाहते हैं?',
        'empty_history': 'आपके इतिहास में अभी कोई रिकॉर्ड मौजूद नहीं है।',
        'empty_history_desc': 'फसल की पत्ती की तस्वीर अपलोड करके एआई रोग पहचान शुरू करें और रिकॉर्ड सुरक्षित रखें।',

        # About Page (/about)
        'about_tag': 'एग्रीविज़न एआई के बारे में',
        'about_title': 'सटीक खेती के लिए पारदर्शी एवं सुलभ एआई तकनीक',
        'about_subtitle': 'डीप लर्निंग कंप्यूटर विज़न और पारदर्शी फसल सलाह का सशक्त संगम।',
        'platform_overview_tag': 'मंच का परिचय',
        'platform_overview_title': 'एग्रीविज़न एआई के बारे में',
        'platform_overview_desc': 'एग्रीविज़न एआई एक अत्याधुनिक कृषि सहायक प्रणाली है, जो फसल रोगों की समय पर पहचान, विज़ुअल विश्लेषण और किसानों के लिए व्यावहारिक मार्गदर्शन प्रदान करती है।',
        'core_objective_tag': 'मुख्य उद्देश्य',
        'our_mission': 'हमारा लक्ष्य',
        'our_mission_desc': 'किसानों, कृषि प्रसारकों और कृषि कार्यकर्ताओं को सुलभ एआई तकनीक द्वारा सशक्त बनाना, फसलों का समय पर बचाव करना और अनावश्यक रासायनिक कीटनाशकों का प्रयोग कम करना।',
        'how_ai_helps': 'एआई खेती में कैसे मदद करता है',
        'how_ai_helps_desc': 'कंप्यूटर विज़न मॉडल पत्तियों में होने वाले झुलसा, धब्बों, फफूंद और पीलेपन का गहराई से विश्लेषण करके बीमारी फैलने से पहले ही सटीक जानकारी देते हैं।',
        'xai_title': 'स्पष्ट एवं पारदर्शी एआई (XAI)',
        'xai_desc': 'केवल परिणाम देने के बजाय, एग्रीविज़न एआई Grad-CAM हीटमैप के माध्यम से स्पष्ट रूप से दिखाता है कि पत्ते के किन हिस्सों के आधार पर निर्णय लिया गया।',
        'tech_stack_tag': 'तकनीकी वास्तुकला',
        'tech_stack_title': 'प्रयुक्त तकनीकें',
        'tech_python_desc': 'डेटा प्रोसेसिंग, एपीआई और कंप्यूटर विज़न पाइपलाइन को संचालित करने वाली मुख्य भाषा।',
        'tech_flask_desc': 'हल्का और तेज़ WSGI वेब फ्रेमवर्क, जो रेस्ट एपीआई और टेम्पलेट्स का प्रबंधन करता है।',
        'tech_gemini_desc': 'आधिकारिक गूगल जेमिनी विज़न मॉडल, जो रियल-टाइम विज़ुअल पैथोलॉजी की पहचान करता है।',
        'tech_vision_desc': 'फ़ाइल सत्यापन, स्केलिंग और पत्ती की गुणवत्ता जांच के लिए कंप्यूटर विज़न टूल।',
        'tech_gradcam_desc': 'एआई के निर्णय की विज़ुअल व्याख्या करने वाली अत्याधुनिक हीटमैप तकनीक।',
        'tech_db_desc': 'निदान इतिहास और कृषि अभिलेखों को सुरक्षित रखने वाली रिलेशनल डेटाबेस प्रणाली।',
        'tech_frontend_desc': 'सभी उपकरणों पर सुचारू रूप से चलने वाली आधुनिक सीएसएस और जावास्क्रिप्ट डिज़ाइन प्रणाली।',
        'system_works_title': 'प्रणाली कैसे काम करती है',
        'pipe_1_title': 'तस्वीर अपलोड करें',
        'pipe_1_desc': 'प्रभावित फसल की पत्ती की साफ और नजदीकी तस्वीर अपलोड करें।',
        'pipe_2_title': 'तस्वीर प्रसंस्करण',
        'pipe_2_desc': 'सर्वर फ़ाइल प्रारूप, रिज़ॉल्यूशन और पत्ती की स्पष्टता की जांच करता है।',
        'pipe_3_title': 'एआई निदान',
        'pipe_3_desc': 'जेमिनी विज़न मॉडल फसल की किस्म, बीमारी और उसकी गंभीरता की पहचान करता है।',
        'pipe_4_title': 'पारदर्शी विज़ुअल व्याख्या',
        'pipe_4_desc': 'पत्ती पर धब्बों का प्रतिशत और विज़ुअल हीटमैप तैयार करता है।',
        'pipe_5_title': 'रोग की विस्तृत जानकारी',
        'pipe_5_desc': 'बीमारी के लक्षण, संभावित कारण और कीट विश्लेषण प्रदर्शित करता है।',
        'pipe_6_title': 'प्रबंधन मार्गदर्शन',
        'pipe_6_desc': 'किसानों के लिए प्राथमिकता वाले कदम, जैविक उपाय और छिड़काव सलाह देता है।',
        'limitations_title': 'महत्वपूर्ण एआई सीमाएं',
        'limitations_intro': 'एग्रीविज़न एआई एक निर्णय-सहायक उपकरण है। उपयोगकर्ताओं को निम्नलिखित सीमाओं का ध्यान रखना चाहिए:',
        'limit_1': 'एआई निदान तस्वीर में दिखाई देने वाले लक्षणों और फोटो की गुणवत्ता पर निर्भर करता है।',
        'limit_2': 'कुछ अलग-अलग बीमारियों में पत्तियों पर एक जैसे ही धब्बे या पीलापन दिखाई दे सकता है।',
        'limit_3': 'धूप से झुलसना या हवा से होने वाली क्षति भी बीमारी के धब्बों जैसी प्रतीत हो सकती है।',
        'limit_4': 'तस्वीर से मिट्टी का पीएच (pH), पोषक तत्वों की सटीक मात्रा या जड़ों की सड़न नहीं मापी जा सकती।',
        'limit_5': 'एआई सलाह कृषि विशेषज्ञों के प्रत्यक्ष परामर्श या प्रयोगशाला जांच का विकल्प नहीं है।',

        # Contact Page (/contact)
        'contact_tag': 'संपर्क करें',
        'contact_title': 'संपर्क एवं प्रतिक्रिया',
        'contact_subtitle': 'यदि आपके पास कोई प्रश्न, सुझाव या प्रतिक्रिया है तो हमसे अवश्य संपर्क करें।',
        'form_name': 'आपका पूरा नाम *',
        'form_name_placeholder': 'अपना पूरा नाम दर्ज करें',
        'form_email': 'ईमेल पता *',
        'form_email_placeholder': 'name@example.com',
        'form_subject': 'विषय',
        'form_subject_placeholder': 'उदा. मॉडल पर प्रतिक्रिया या सामान्य पूछताछ',
        'form_message': 'आपका संदेश *',
        'form_message_placeholder': 'अपना प्रश्न या प्रतिक्रिया यहां लिखें...',
        'send_btn': '✉️ संदेश भेजें',
        'toast_form_required': 'कृपया संदेश भेजने से पहले सभी आवश्यक फ़ील्ड भरें।',
        'toast_valid_email': 'कृपया एक वैध ईमेल पता दर्ज करें।',
        'toast_copied': 'निदान सारांश क्लिपबोर्ड पर कॉपी हो गया!',
        'toast_copy_failed': 'सारांश कॉपी करने में विफल।'
    }
}

# =====================================================================
# DYNAMIC CROP NAME TRANSLATION MAP
# =====================================================================
CROP_NAME_MAP = {
    'tomato': {'mr': 'टोमॅटो', 'hi': 'टमाटर', 'en': 'Tomato'},
    'potato': {'mr': 'बटाटा', 'hi': 'आलू', 'en': 'Potato'},
    'pepper': {'mr': 'शिमला मिरची', 'hi': 'शिमला मिर्च', 'en': 'Pepper'},
    'pepper bell': {'mr': 'शिमला मिरची', 'hi': 'शिमला मिर्च', 'en': 'Pepper bell'},
    'pepper, bell': {'mr': 'शिमला मिरची', 'hi': 'शिमला मिर्च', 'en': 'Pepper bell'},
    'apple': {'mr': 'सफरचंद', 'hi': 'सेब', 'en': 'Apple'},
    'corn': {'mr': 'मका', 'hi': 'मक्का', 'en': 'Corn'},
    'corn (maize)': {'mr': 'मका (Corn)', 'hi': 'मक्का (Corn)', 'en': 'Corn (maize)'},
    'corn_(maize)': {'mr': 'मका (Corn)', 'hi': 'मक्का (Corn)', 'en': 'Corn (maize)'},
    'grape': {'mr': 'द्राक्षे', 'hi': 'अंगूर', 'en': 'Grape'},
    'orange': {'mr': 'संत्रे', 'hi': 'संतरा', 'en': 'Orange'},
    'peach': {'mr': 'पीच (Peach)', 'hi': 'आड़ू (Peach)', 'en': 'Peach'},
    'blueberry': {'mr': 'ब्लूबेरी', 'hi': 'ब्लूबेरी', 'en': 'Blueberry'},
    'cherry': {'mr': 'चेरी', 'hi': 'चेरी', 'en': 'Cherry'},
    'cherry (including sour)': {'mr': 'चेरी (Cherry)', 'hi': 'चेरी (Cherry)', 'en': 'Cherry (including sour)'},
    'raspberry': {'mr': 'रासबेरी', 'hi': 'रास्पबेरी', 'en': 'Raspberry'},
    'soybean': {'mr': 'सोयाबीन', 'hi': 'सोयाबीन', 'en': 'Soybean'},
    'squash': {'mr': 'भोपळा (Squash)', 'hi': 'कद्दू (Squash)', 'en': 'Squash'},
    'strawberry': {'mr': 'स्ट्रॉबेरी', 'hi': 'स्ट्रॉबेरी', 'en': 'Strawberry'},
    'unknown crop': {'mr': 'अज्ञात पीक', 'hi': 'अज्ञात फसल', 'en': 'Unknown Crop'},
    'crop': {'mr': 'पीक', 'hi': 'फसल', 'en': 'Crop'}
}

# =====================================================================
# DYNAMIC DISEASE NAME TRANSLATION MAP
# =====================================================================
DISEASE_NAME_MAP = {
    # Tomato Diseases
    'tomato healthy': {'mr': 'टोमॅटो - निरोगी (Healthy)', 'hi': 'टमाटर - स्वस्थ (Healthy)', 'en': 'Tomato Healthy'},
    'tomato early blight': {'mr': 'टोमॅटो - करपा (Early Blight)', 'hi': 'टमाटर - अगेती झुलसा (Early Blight)', 'en': 'Tomato Early Blight'},
    'early blight': {'mr': 'करपा (Early Blight)', 'hi': 'अगेती झुलसा (Early Blight)', 'en': 'Early Blight'},
    'tomato late blight': {'mr': 'टोमॅटो - तांबेरा / पछेती करपा (Late Blight)', 'hi': 'टमाटर - पछेती झुलसा (Late Blight)', 'en': 'Tomato Late Blight'},
    'late blight': {'mr': 'तांबेरा / पछेती करपा (Late Blight)', 'hi': 'पछेती झुलसा (Late Blight)', 'en': 'Late Blight'},
    'tomato bacterial spot': {'mr': 'टोमॅटो - जिवाणूजन्य डाग (Bacterial Spot)', 'hi': 'टमाटर - जीवाणु धब्बा (Bacterial Spot)', 'en': 'Tomato Bacterial Spot'},
    'bacterial spot': {'mr': 'जिवाणूजन्य डाग (Bacterial Spot)', 'hi': 'जीवाणु धब्बा (Bacterial Spot)', 'en': 'Bacterial Spot'},
    'tomato septoria leaf spot': {'mr': 'टोमॅटो - सेप्टोरिया पानावरील डाग', 'hi': 'टमाटर - सेप्टोरिया पत्ती धब्बा', 'en': 'Tomato Septoria Leaf Spot'},
    'septoria leaf spot': {'mr': 'सेप्टोरिया पानावरील डाग', 'hi': 'सेप्टोरिया पत्ती धब्बा', 'en': 'Septoria Leaf Spot'},
    'tomato spider mites': {'mr': 'टोमॅटो - लाल कोळी कीड (Spider Mites)', 'hi': 'टमाटर - लाल मकड़ी कीट (Spider Mites)', 'en': 'Tomato Spider Mites'},
    'tomato target spot': {'mr': 'टोमॅटो - टार्गेट स्पॉट बुरशी', 'hi': 'टमाटर - टारगेट स्पॉट कवक', 'en': 'Tomato Target Spot'},
    'tomato yellow leaf curl virus': {'mr': 'टोमॅटो - पिवळा पाने मुरडणारा विषाणू (TYLCV)', 'hi': 'टमाटर - पीली पत्ती मरोड़ विषाणु (TYLCV)', 'en': 'Tomato Yellow Leaf Curl Virus'},
    'tomato mosaic virus': {'mr': 'टोमॅटो - मोझॅक विषाणू (Mosaic Virus)', 'hi': 'टमाटर - मोज़ेक विषाणु (Mosaic Virus)', 'en': 'Tomato Mosaic Virus'},

    # Potato Diseases
    'potato healthy': {'mr': 'बटाटा - निरोगी (Healthy)', 'hi': 'आलू - स्वस्थ (Healthy)', 'en': 'Potato Healthy'},
    'potato early blight': {'mr': 'बटाटा - करपा (Early Blight)', 'hi': 'आलू - अगेती झुलसा (Early Blight)', 'en': 'Potato Early Blight'},
    'potato late blight': {'mr': 'बटाटा - पछेती तांबेरा (Late Blight)', 'hi': 'आलू - पछेती झुलसा (Late Blight)', 'en': 'Potato Late Blight'},

    # Pepper Diseases
    'pepper healthy': {'mr': 'शिमला मिरची - निरोगी (Healthy)', 'hi': 'शिमला मिर्च - स्वस्थ (Healthy)', 'en': 'Pepper Healthy'},
    'pepper bell healthy': {'mr': 'शिमला मिरची - निरोगी (Healthy)', 'hi': 'शिमला मिर्च - स्वस्थ (Healthy)', 'en': 'Pepper bell Healthy'},
    'pepper bacterial spot': {'mr': 'शिमला मिरची - जिवाणूजन्य डाग', 'hi': 'शिमला मिर्च - जीवाणु धब्बा', 'en': 'Pepper Bacterial Spot'},
    'pepper bell bacterial spot': {'mr': 'शिमला मिरची - जिवाणूजन्य डाग', 'hi': 'शिमला मिर्च - जीवाणु धब्बा', 'en': 'Pepper bell Bacterial Spot'},

    # Apple Diseases
    'apple healthy': {'mr': 'सफरचंद - निरोगी (Healthy)', 'hi': 'सेब - स्वस्थ (Healthy)', 'en': 'Apple Healthy'},
    'apple scab': {'mr': 'सफरचंद - खपल्या रोग (Apple Scab)', 'hi': 'सेब - पपड़ी रोग (Apple Scab)', 'en': 'Apple Scab'},
    'apple black rot': {'mr': 'सफरचंद - काळी कूज (Black Rot)', 'hi': 'सेब - काला सड़न रोग (Black Rot)', 'en': 'Apple Black Rot'},
    'cedar apple rust': {'mr': 'सफरचंद - तांबेरा बुरशी (Cedar Rust)', 'hi': 'सेब - रतुआ कवक (Cedar Rust)', 'en': 'Cedar Apple Rust'},

    # Corn Diseases
    'corn healthy': {'mr': 'मका - निरोगी (Healthy)', 'hi': 'मक्का - स्वस्थ (Healthy)', 'en': 'Corn Healthy'},
    'corn (maize) healthy': {'mr': 'मका - निरोगी (Healthy)', 'hi': 'मक्का - स्वस्थ (Healthy)', 'en': 'Corn (maize) Healthy'},
    'corn common rust': {'mr': 'मका - तांबेरा रोग (Common Rust)', 'hi': 'मक्का - सामान्य रतुआ (Common Rust)', 'en': 'Corn Common Rust'},
    'corn cercospora leaf spot gray leaf spot': {'mr': 'मका - करडा पानावरील डाग (Gray Leaf Spot)', 'hi': 'मक्का - धूसर पत्ती धब्बा (Gray Leaf Spot)', 'en': 'Corn Gray Leaf Spot'},
    'corn northern leaf blight': {'mr': 'मका - उत्तरेकडील करपा (Northern Blight)', 'hi': 'मक्का - उत्तरी पत्ती झुलसा (Northern Blight)', 'en': 'Corn Northern Leaf Blight'},

    # Grape Diseases
    'grape healthy': {'mr': 'द्राक्षे - निरोगी (Healthy)', 'hi': 'अंगूर - स्वस्थ (Healthy)', 'en': 'Grape Healthy'},
    'grape black rot': {'mr': 'द्राक्षे - काळी कूज (Black Rot)', 'hi': 'अंगूर - काला सड़न (Black Rot)', 'en': 'Grape Black Rot'},
    'grape esca (black measles)': {'mr': 'द्राक्षे - एस्का रोग (Black Measles)', 'hi': 'अंगूर - एस्का रोग (Black Measles)', 'en': 'Grape Esca (Black Measles)'},
    'grape leaf blight (isariopsis leaf spot)': {'mr': 'द्राक्षे - पानावरील करपा (Leaf Blight)', 'hi': 'अंगूर - पत्ती झुलसा (Leaf Blight)', 'en': 'Grape Leaf Blight'},

    # Orange / Citrus
    'orange haunglongbing (citrus greening)': {'mr': 'संत्रे - सिट्रस ग्रीनिंग (Huanglongbing)', 'hi': 'संतरा - सिट्रस ग्रीनिंग (Huanglongbing)', 'en': 'Orange Haunglongbing (Citrus Greening)'},
    'citrus greening': {'mr': 'सिट्रस ग्रीनिंग (Citrus Greening)', 'hi': 'सिट्रस ग्रीनिंग (Citrus Greening)', 'en': 'Citrus Greening'},

    # Peach Diseases
    'peach healthy': {'mr': 'पीच - निरोगी (Healthy)', 'hi': 'आड़ू - स्वस्थ (Healthy)', 'en': 'Peach Healthy'},
    'peach bacterial spot': {'mr': 'पीच - जिवाणूजन्य डाग', 'hi': 'आड़ू - जीवाणु धब्बा', 'en': 'Peach Bacterial Spot'},

    # Blueberry, Cherry, Raspberry, Soybean, Squash, Strawberry
    'blueberry healthy': {'mr': 'ब्लूबेरी - निरोगी (Healthy)', 'hi': 'ब्लूबेरी - स्वस्थ (Healthy)', 'en': 'Blueberry Healthy'},
    'cherry healthy': {'mr': 'चेरी - निरोगी (Healthy)', 'hi': 'चेरी - स्वस्थ (Healthy)', 'en': 'Cherry Healthy'},
    'cherry powdery mildew': {'mr': 'चेरी - भुरी रोग (Powdery Mildew)', 'hi': 'चेरी - चूर्णिल आसिता / फफूंद (Powdery Mildew)', 'en': 'Cherry Powdery Mildew'},
    'raspberry healthy': {'mr': 'रासबेरी - निरोगी (Healthy)', 'hi': 'रास्पबेरी - स्वस्थ (Healthy)', 'en': 'Raspberry Healthy'},
    'soybean healthy': {'mr': 'सोयाबीन - निरोगी (Healthy)', 'hi': 'सोयाबीन - स्वस्थ (Healthy)', 'en': 'Soybean Healthy'},
    'squash powdery mildew': {'mr': 'भोपळा - भुरी रोग (Powdery Mildew)', 'hi': 'कद्दू - चूर्णिल फफूंद (Powdery Mildew)', 'en': 'Squash Powdery Mildew'},
    'powdery mildew': {'mr': 'भुरी रोग (Powdery Mildew)', 'hi': 'चूर्णिल फफूंद (Powdery Mildew)', 'en': 'Powdery Mildew'},
    'strawberry healthy': {'mr': 'स्ट्रॉबेरी - निरोगी (Healthy)', 'hi': 'स्ट्रॉबेरी - स्वस्थ (Healthy)', 'en': 'Strawberry Healthy'},
    'strawberry leaf scorch': {'mr': 'स्ट्रॉबेरी - पान करपा (Leaf Scorch)', 'hi': 'स्ट्रॉबेरी - पत्ती झुलसा (Leaf Scorch)', 'en': 'Strawberry Leaf Scorch'},

    # Generic
    'crop pathology': {'mr': 'पिकाचा रोग', 'hi': 'फसल रोग', 'en': 'Crop Pathology'},
    'crop pathology identified': {'mr': 'पिकाचा रोग आढळला', 'hi': 'फसल रोग पाया गया', 'en': 'Crop Pathology Identified'},
    'healthy': {'mr': 'निरोगी (Healthy)', 'hi': 'स्वस्थ (Healthy)', 'en': 'Healthy'},
    'disease detected': {'mr': 'रोग आढळला', 'hi': 'रोग पाया गया', 'en': 'Disease Detected'}
}

# =====================================================================
# DYNAMIC CATEGORY TRANSLATION MAP
# =====================================================================
CATEGORY_MAP = {
    'fungal': {'mr': 'बुरशीजन्य रोग (Fungal)', 'hi': 'फफूंदजन्य रोग (Fungal)', 'en': 'Fungal'},
    'bacterial': {'mr': 'जिवाणूजन्य रोग (Bacterial)', 'hi': 'जीवाणुजन्य रोग (Bacterial)', 'en': 'Bacterial'},
    'viral': {'mr': 'विषाणूजन्य रोग (Viral)', 'hi': 'विषाणुजन्य रोग (Viral)', 'en': 'Viral'},
    'pest': {'mr': 'कीड / कीटक प्रादुर्भाव (Pest)', 'hi': 'कीट प्रकोप (Pest Damage)', 'en': 'Pest'},
    'nutrient': {'mr': 'अन्नद्रव्यांची कमतरता (Nutrient Deficiency)', 'hi': 'पोषक तत्वों की कमी (Nutrient Deficiency)', 'en': 'Nutrient'},
    'environmental': {'mr': 'वातावरणाचा ताण (Environmental Stress)', 'hi': 'वातावरणीय तनाव (Environmental Stress)', 'en': 'Environmental'},
    'healthy': {'mr': 'निरोगी पीक (Healthy)', 'hi': 'स्वस्थ फसल (Healthy)', 'en': 'Healthy'},
    'general crop disease': {'mr': 'सामान्य पीक रोग', 'hi': 'सामान्य फसल रोग', 'en': 'General Crop Disease'}
}

# =====================================================================
# DYNAMIC HEALTH STATUS TRANSLATION MAP
# =====================================================================
HEALTH_STATUS_MAP = {
    'healthy': {'mr': 'निरोगी (Healthy)', 'hi': 'स्वस्थ (Healthy)', 'en': 'Healthy'},
    'diseased': {'mr': 'रोगग्रस्त (Diseased)', 'hi': 'रोगग्रस्त (Diseased)', 'en': 'Diseased'},
    'possibly_diseased': {'mr': 'संभाव्य रोगग्रस्त', 'hi': 'संभावित रोगग्रस्त', 'en': 'Possibly Diseased'},
    'pest_damage': {'mr': 'किडीचा प्रादुर्भाव (Pest Damage)', 'hi': 'कीट प्रकोप (Pest Damage)', 'en': 'Pest Damage'},
    'nutrient_deficiency': {'mr': 'अन्नद्रव्यांची कमतरता', 'hi': 'पोषक तत्वों की कमी', 'en': 'Nutrient Deficiency'},
    'environmental_stress': {'mr': 'वातावरणाचा ताण', 'hi': 'वातावरणीय तनाव', 'en': 'Environmental Stress'},
    'unknown': {'mr': 'अज्ञात स्थिती', 'hi': 'अज्ञात स्थिति', 'en': 'Unknown'}
}

# =====================================================================
# DYNAMIC SEVERITY TRANSLATION MAP
# =====================================================================
SEVERITY_MAP = {
    'healthy': {'mr': 'निरोगी (Healthy)', 'hi': 'स्वस्थ (Healthy)', 'en': 'Healthy'},
    'healthy leaf': {'mr': 'निरोगी पान (Healthy)', 'hi': 'स्वस्थ पत्ती (Healthy)', 'en': 'Healthy Leaf'},
    'very early': {'mr': 'अतिशय सुरुवातीचा टप्पा', 'hi': 'अत्यंत प्रारंभिक चरण', 'en': 'Very Early'},
    'early': {'mr': 'सुरुवातीचा टप्पा (Early)', 'hi': 'प्रारंभिक चरण (Early)', 'en': 'Early'},
    'early stage': {'mr': 'सुरुवातीचा टप्पा', 'hi': 'प्रारंभिक चरण', 'en': 'Early Stage'},
    'moderate': {'mr': 'मध्यम टप्पा (Moderate)', 'hi': 'मध्यम चरण (Moderate)', 'en': 'Moderate'},
    'moderate stage': {'mr': 'मध्यम टप्पा', 'hi': 'मध्यम चरण', 'en': 'Moderate Stage'},
    'developing': {'mr': 'वाढणारा टप्पा', 'hi': 'विकासशील चरण', 'en': 'Developing'},
    'advanced': {'mr': 'प्रगत टप्पा', 'hi': 'उन्नत चरण', 'en': 'Advanced'},
    'advanced stage': {'mr': 'प्रगत टप्पा', 'hi': 'उन्नत चरण', 'en': 'Advanced Stage'},
    'severe': {'mr': 'गंभीर टप्पा (Severe)', 'hi': 'गंभीर चरण (Severe)', 'en': 'Severe'},
    'severe stage': {'mr': 'गंभीर टप्पा', 'hi': 'गंभीर चरण', 'en': 'Severe Stage'},
    'critical': {'mr': 'अत्यंत गंभीर (Critical)', 'hi': 'अत्यंत गंभीर (Critical)', 'en': 'Critical'},
    'unknown': {'mr': 'अज्ञात तीव्रता', 'hi': 'अज्ञात गंभीरता', 'en': 'Unknown'}
}

# =====================================================================
# DYNAMIC URGENCY TRANSLATION MAP
# =====================================================================
URGENCY_MAP = {
    'critical': {'mr': 'अत्यंत गंभीर (Critical)', 'hi': 'अत्यंत गंभीर (Critical)', 'en': 'Critical'},
    'high': {'mr': 'उच्च तातडी (High)', 'hi': 'उच्च प्राथमिकता (High)', 'en': 'High'},
    'moderate': {'mr': 'मध्यम (Moderate)', 'hi': 'मध्यम (Moderate)', 'en': 'Moderate'},
    'low': {'mr': 'कमी / सामान्य (Low)', 'hi': 'सामान्य / कम (Low)', 'en': 'Low'},
    'unknown': {'mr': 'अज्ञात (Unknown)', 'hi': 'अज्ञात (Unknown)', 'en': 'Unknown'}
}

# =====================================================================
# DYNAMIC CONFIDENCE LEVEL TRANSLATION MAP
# =====================================================================
CONFIDENCE_LEVEL_MAP = {
    'very high': {'mr': 'अत्यंत उच्च (Very High)', 'hi': 'अत्यंत उच्च (Very High)', 'en': 'Very High'},
    'high': {'mr': 'उच्च (High)', 'hi': 'उच्च (High)', 'en': 'High'},
    'moderate': {'mr': 'मध्यम (Moderate)', 'hi': 'मध्यम (Moderate)', 'en': 'Moderate'},
    'low': {'mr': 'कमी (Low)', 'hi': 'कम (Low)', 'en': 'Low'},
    'medium': {'mr': 'मध्यम (Medium)', 'hi': 'मध्यम (Medium)', 'en': 'Medium'}
}


# =====================================================================
# TRANSLATION HELPER FUNCTIONS
# =====================================================================

def get_translation(key, lang='en'):
    """Fetch translated string for a given key and language with English fallback."""
    lang_code = (lang or 'en').lower()
    if lang_code not in TRANSLATIONS:
        lang_code = 'en'
    return TRANSLATIONS[lang_code].get(key) or TRANSLATIONS['en'].get(key, key)


def translate_crop_name(crop_name, lang='en'):
    """Translate crop common name into Marathi or Hindi."""
    if not crop_name:
        return crop_name
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return crop_name
    norm_key = str(crop_name).strip().lower()
    if norm_key in CROP_NAME_MAP:
        return CROP_NAME_MAP[norm_key].get(lang_code, crop_name)
    # Check partial contains
    for key, trans in CROP_NAME_MAP.items():
        if key in norm_key:
            return trans.get(lang_code, crop_name)
    return crop_name


def translate_disease_name(disease_name, lang='en'):
    """Translate disease name into Marathi or Hindi."""
    if not disease_name:
        return disease_name
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return disease_name
    norm_key = str(disease_name).strip().lower()
    if norm_key in DISEASE_NAME_MAP:
        return DISEASE_NAME_MAP[norm_key].get(lang_code, disease_name)
    # Partial search
    for key, trans in DISEASE_NAME_MAP.items():
        if key == norm_key or key in norm_key:
            return trans.get(lang_code, disease_name)
    return disease_name


def translate_category(category, lang='en'):
    """Translate disease category (Fungal, Bacterial, Viral, etc.)."""
    if not category:
        return category
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return category
    norm_key = str(category).strip().lower()
    if norm_key in CATEGORY_MAP:
        return CATEGORY_MAP[norm_key].get(lang_code, category)
    for key, trans in CATEGORY_MAP.items():
        if key in norm_key:
            return trans.get(lang_code, category)
    return category


def translate_health_status(status, lang='en'):
    """Translate health status (HEALTHY, DISEASED, PEST_DAMAGE, etc.)."""
    if not status:
        return status
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return status
    norm_key = str(status).strip().lower()
    if norm_key in HEALTH_STATUS_MAP:
        return HEALTH_STATUS_MAP[norm_key].get(lang_code, status)
    for key, trans in HEALTH_STATUS_MAP.items():
        if key in norm_key:
            return trans.get(lang_code, status)
    return status


def translate_severity(severity, lang='en'):
    """Translate severity rating (HEALTHY, EARLY, MODERATE, SEVERE, CRITICAL)."""
    if not severity:
        return severity
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return severity
    norm_key = str(severity).strip().lower()
    if norm_key in SEVERITY_MAP:
        return SEVERITY_MAP[norm_key].get(lang_code, severity)
    for key, trans in SEVERITY_MAP.items():
        if key in norm_key:
            return trans.get(lang_code, severity)
    return severity


def translate_urgency(urgency, lang='en'):
    """Translate action urgency level (LOW, MODERATE, HIGH, CRITICAL)."""
    if not urgency:
        return urgency
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return urgency
    norm_key = str(urgency).strip().lower()
    if norm_key in URGENCY_MAP:
        return URGENCY_MAP[norm_key].get(lang_code, urgency)
    for key, trans in URGENCY_MAP.items():
        if key in norm_key:
            return trans.get(lang_code, urgency)
    return urgency


def translate_confidence_level(level, lang='en'):
    """Translate confidence level string (Very High, High, Moderate, Low)."""
    if not level:
        return level
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return level
    norm_key = str(level).strip().lower()
    if norm_key in CONFIDENCE_LEVEL_MAP:
        return CONFIDENCE_LEVEL_MAP[norm_key].get(lang_code, level)
    for key, trans in CONFIDENCE_LEVEL_MAP.items():
        if key in norm_key:
            return trans.get(lang_code, level)
    return level


def translate_text(text, lang='en'):
    """Fallback text translator for common agricultural phrases and responses."""
    if not text:
        return text
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return text
    norm = str(text).strip()
    # Check direct dictionary translations
    for dict_key, trans_val in TRANSLATIONS['en'].items():
        if trans_val == norm:
            return TRANSLATIONS.get(lang_code, {}).get(dict_key, text)
    return text
