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
        'disclaimer_point_1': 'AI-assisted preliminary screening based on visible foliar symptoms only.',
        'disclaimer_point_2': 'Does not replace certified laboratory diagnosis or advice from a qualified agricultural professional.',
        'disclaimer_point_3': 'Always follow locally approved agricultural product labels, dosage, and regulatory guidelines.',
        'btn_analyze_another': '📷 Analyze Another Leaf Image',

        # Disease Library Page (/diseases & /disease/<id>)
        'knowledge_base_tag': 'Agricultural Knowledge Base',
        'disease_library_title': 'Crop Disease Library',
        'disease_library_subtitle': 'Search, filter, and explore symptoms, causes, and prevention strategies across supported crops.',
        'all_crops': 'All Crops',
        'view_details': 'View Details',
        'no_diseases_found': 'No diseases found matching your search.',
        'no_diseases_desc': 'Try searching for a different keyword or crop filter.',
        'nav_diseases': 'Disease Library',
        'back_to_library': '← Back to Disease Library',

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
        'opt_moderate': '🟠 Moderate Severity',
        'opt_high': '🔴 High Severity',
        'opt_critical': '🚨 Critical',
        'btn_filter': 'Search / Filter',
        'btn_reset': 'Reset',
        'col_date': 'Date & Time',
        'col_image': 'Leaf Image',
        'col_crop': 'Crop',
        'col_condition': 'Condition Identified',
        'col_confidence': 'Confidence',
        'col_severity': 'Severity',
        'col_actions': 'Actions',
        'btn_view_report': 'View Full Report →',
        'delete_record': 'Delete',
        'tooltip_delete': 'Delete Record',
        'confirm_delete_record': 'Are you sure you want to delete this diagnostic record?',
        'empty_history': 'No records found in your diagnostic history.',
        'empty_history_desc': 'Upload a crop leaf image to initiate AI disease detection and save records.',

        # About Page (/about)
        'about_tag': 'About AgriVision AI',
        'about_title': 'Explainable & Accessible AI for Precision Agriculture',
        'about_subtitle': 'Bridging deep-learning computer vision with transparent crop-care guidance.',
        'platform_overview_tag': 'Platform Overview',
        'platform_overview_title': 'About AgriVision AI',
        'platform_overview_desc': 'AgriVision AI is an explainable agricultural intelligence system designed to support farmers, agronomists, and extension officers with early crop disease identification, visual validation, and structured management steps.',
        'core_objective_tag': 'Core Objective',
        'our_mission': 'Our Mission',
        'our_mission_desc': 'To empower farmers with accessible, trustworthy AI technology that reduces diagnostic delays, optimizes chemical use, and promotes sustainable agricultural crop protection.',
        'how_ai_helps': 'How AI Helps Farming',
        'how_ai_helps_desc': 'Computer vision models analyze microscopic foliage patterns, chlorosis halos, and necrotic lesions, identifying conditions before extensive field spread occurs.',
        'xai_title': 'Transparent & Explainable AI (XAI)',
        'xai_desc': 'Rather than offering black-box classifications, AgriVision AI utilizes Grad-CAM visual heatmaps to highlight exact leaf regions that influenced the model prediction.',
        'tech_stack_tag': 'Technical Architecture',
        'tech_stack_title': 'Technologies Used',
        'tech_python_title': 'Python 3',
        'tech_python_desc': 'Core language powering data processing, inference pipelines, and API services.',
        'tech_flask_title': 'Flask Framework',
        'tech_flask_desc': 'Lightweight and scalable WSGI web application server managing routes and APIs.',
        'tech_gemini_title': 'Google Gemini Vision AI',
        'tech_gemini_desc': 'Multimodal visual analysis producing structured diagnostic pathology reports.',
        'tech_opencv_title': 'OpenCV & Pillow',
        'tech_vision_desc': 'Computer vision libraries for validation, normalization, and image processing.',
        'tech_gradcam_title': 'Grad-CAM XAI',
        'tech_gradcam_desc': 'Gradient-weighted class activation mapping producing visual leaf heatmaps.',
        'tech_db_title': 'MySQL / SQLite',
        'tech_db_desc': 'Relational database storing prediction histories, pathology records, and libraries.',
        'tech_frontend_title': 'HTML5, CSS3, & JavaScript',
        'tech_frontend_desc': 'Responsive interface with fluid typography and instant internationalization.',
        'system_works_title': 'How the System Works',
        'pipe_1_title': '1. Leaf Capture',
        'pipe_1_desc': 'The user takes or uploads a clear crop leaf photo through the responsive portal.',
        'pipe_2_title': '2. Preprocessing',
        'pipe_2_desc': 'The image is verified, checked for format and resolution, and normalized.',
        'pipe_3_title': '3. AI Inference',
        'pipe_3_desc': 'Gemini Vision AI and neural networks identify disease class and severity stage.',
        'pipe_4_title': '4. XAI Heatmap',
        'pipe_4_desc': 'Grad-CAM visual overlays highlight active disease symptom spots.',
        'pipe_5_title': '5. Disease Insights',
        'pipe_5_desc': 'Structured knowledge base provides symptoms, pathogen types, and causes.',
        'pipe_6_title': '6. Field Guidance',
        'pipe_6_desc': 'Transforms predictions into 4 practical action steps, organic, and conventional treatments.',
        'limitations_title': 'Important System Limitations',
        'limitations_intro': 'AgriVision AI is an assistive decision-support tool. Users should note the following boundaries:',
        'limit_1': 'AI analysis relies on visible surface symptoms and image quality.',
        'limit_2': 'Different pathogens may present overlapping early chlorosis or spot patterns.',
        'limit_3': 'Abiotic physical damage, scorch, or wind bruising may mimic disease lesions.',
        'limit_4': 'Visual images cannot measure soil chemistry, root health, or internal vascular wilts.',
        'limit_5': 'Predictions do not replace certified laboratory testing or on-site agronomist inspections.',

        # Contact Page (/contact)
        'contact_tag': 'Get in Touch',
        'contact_title': 'Contact & Support',
        'contact_subtitle': 'Have questions, feedback, or agricultural inquiries? Send us a message.',
        'form_name': 'Your Full Name *',
        'form_name_placeholder': 'Enter your full name',
        'form_email': 'Email Address *',
        'form_email_placeholder': 'name@example.com',
        'form_subject': 'Subject',
        'form_subject_placeholder': 'e.g. Model feedback or general inquiry',
        'form_message': 'Your Message *',
        'form_message_placeholder': 'Write your message or inquiry here...',
        'send_btn': '✉️ Send Message',
        'toast_form_required': 'Please fill in all required fields before submitting.',
        'toast_valid_email': 'Please enter a valid email address.',
        'toast_copied': 'Diagnostic summary copied to clipboard!',
        'toast_copy_failed': 'Failed to copy summary to clipboard.'
    },

    'mr': {
        # Navigation & Header
        'app_name': 'एग्रीव्हिजन एआय',
        'app_subtitle': 'पारदर्शक पीक रोग निदान प्रणाली',
        'home': 'मुख्यपृष्ठ',
        'detect_disease': 'पान तपासा',
        'history': 'निदान इतिहास',
        'about': 'माहिती',
        'contact': 'संपर्क',
        'language': 'भाषा',
        'english': 'English',
        'marathi': 'मराठी',
        'hindi': 'हिंदी',
        'analyze_crop': '🔍 पीक तपासा',
        'toggle_theme': 'लाईट/डार्क मोड बदला',
        'menu_toggle': 'मेन्यू उघडा',

        # Footer
        'footer_brand_desc': 'पिकांवरील रोगांची वेळेवर ओळख, दृश्य हीटमॅप, तीव्रतेचा अंदाज आणि शेतकऱ्यांसाठी कृषी मार्गदर्शनासाठी डिझाइन केलेले पारदर्शक एआय ॲप्लिकेशन.',
        'footer_nav_heading': 'मार्गदर्शन',
        'footer_cap_heading': 'वैशिष्ट्ये',
        'footer_tech_heading': 'तंत्रज्ञान',
        'footer_rights': 'सर्व हक्क राखीव. अचूक व पारदर्शक शेतीसाठी विकसित.',
        'cap_leaf_analysis': 'थेट एआय पान विश्लेषण',
        'cap_severity_est': 'रोग तीव्रतेचा अंदाज',
        'cap_heatmaps': 'ग्रॅड-कॅम व्हिज्युअल हीटमॅप',
        'cap_guidance': 'सेंद्रिय व रासायनिक उपाययोजना',
        'tech_gemini': 'गूगल जेमिनी व्हिजन एआय',
        'tech_vision_scanner': 'कॉम्प्युटर व्हिजन लीफ स्कॅनर',
        'tech_flask': 'पायथन फ्लास्क बॅकएंड',
        'tech_xai': 'पारदर्शक एआय मार्गदर्शन',

        # Hero & Home Page
        'hero_badge': '🤖 गूगल जेमिनी व्हिजन एआय व ३D तंत्रज्ञान',
        'hero_title_1': 'पिकांचे रोग वेळीच ओळखा ',
        'hero_title_2': 'एआय तंत्रज्ञानाने',
        'hero_subtitle': 'पिकाच्या पानाचे छायाचित्र अपलोड करा आणि संभाव्य रोग, दृश्य लक्षणे, रोगाची तीव्रता आणि शेतकऱ्यांसाठी आवश्यक उपाययोजनांची माहिती मिळवा.',
        'btn_analyze_leaf': '🔍 पानाची तपासणी करा',
        'trust_realtime_ai': '✓ तात्काळ एआय विश्लेषण',
        'trust_explainable': '✓ पारदर्शक व स्पष्ट मार्गदर्शन',
        'trust_solutions': '✓ सेंद्रिय व रासायनिक उपाय',
        'floating_condition_val': 'करपा रोग',
        'floating_severity_val': 'मध्यम',

        # How AgriVision AI Works
        'how_tag': 'कार्यपद्धती',
        'how_title': 'एग्रीव्हिजन एआय कसे कार्य करते',
        'how_subtitle': 'छायाचित्र घेण्यापासून ते प्रत्यक्ष शेतातील उपायांपर्यंत, एग्रीव्हिजन एआय सोप्या भाषेत मार्गदर्शन प्रदान करते.',
        'step_01_title': 'पानाचे छायाचित्र अपलोड करा',
        'step_01_desc': 'बाधित पिकाच्या पानाचे स्पष्ट छायाचित्र मोबाईल किंवा संगणकावरून अपलोड करा.',
        'step_02_title': 'एआय पानाचे परीक्षण करते',
        'step_02_desc': 'संगणकीय दृष्टी मॉडेल पानाचे डाग, पिवळेपणा आणि ऊतींमधील बदल तपासते.',
        'step_03_title': 'संभाव्य रोग ओळखणे',
        'step_03_desc': 'प्रशिक्षित एआय मॉडेल संभाव्य रोग, त्याची अचूकता व तीव्रतेचा टप्पा निश्चित करते.',
        'step_04_title': 'कृषी मार्गदर्शन मिळवा',
        'step_04_desc': 'शेतकऱ्यांसाठी तातडीच्या उपाययोजना, सेंद्रिय व रासायनिक फवारणी आणि खत व्यवस्थापनाचा सल्ला मिळतो.',
        'chip_formats': 'JPG, PNG, WEBP',
        'chip_lighting': 'चांगला प्रकाश',
        'chip_drag_drop': 'ड्रॅग व ड्रॉप',
        'chip_processing': 'छायाचित्र प्रक्रिया सुरू आहे...',
        'chip_symptoms': 'लक्षणे तपासली जात आहेत...',
        'chip_disease_name': 'करपा रोग',
        'chip_confidence': '९४% विश्वास पातळी',
        'chip_moderate': 'मध्यम टप्पा',
        'workflow_cta_title': 'तुमचे पीक तपासायचे आहे का?',
        'workflow_cta_desc': 'तात्काळ रोग निदान आणि सेंद्रिय व्यवस्थापनाचे मार्गदर्शन मिळवा.',
        'workflow_cta_btn': 'पानाची तपासणी सुरू करा →',

        # Platform Capabilities / 10 Feature Cards
        'features_tag': 'प्लॅटफॉर्म वैशिष्ट्ये',
        'features_title': 'एग्रीव्हिजन एआय ची प्रमुख वैशिष्ट्ये',
        'features_subtitle': 'शेतकऱ्यांना समजेल अशी सोपी भाषा, पारदर्शकता आणि प्रत्यक्ष उपयुक्त कृषी सल्ला.',
        'feat_1_title': 'एआय रोग ओळख',
        'feat_1_desc': 'डीप लर्निंग तंत्रज्ञानाने पिकांवरील विविध रोगांची जलद ओळख करा.',
        'feat_2_title': 'विश्वास पातळी विश्लेषण',
        'feat_2_desc': 'मॉडेलच्या अचूकतेची टक्केवारी व विश्वास पातळी स्पष्टपणे पहा.',
        'feat_3_title': 'पारदर्शक एआय (Grad-CAM)',
        'feat_3_desc': 'पानाच्या कोणत्या भागामुळे निर्णय घेतला गेला हे रंगीत हीटमॅपद्वारे पहा.',
        'feat_4_title': 'रोग टप्पा अंदाज',
        'feat_4_desc': 'रोगाचा नेमका टप्पा (सुरुवातीचा, मध्यम, प्रगत, गंभीर) समजून घ्या.',
        'feat_5_title': 'बाधित क्षेत्राचे प्रमाण',
        'feat_5_desc': 'पानावर डागांचे टक्केवारी प्रमाण व नुकसान पातळी मोजा.',
        'feat_6_title': 'सविस्तर रोग माहिती',
        'feat_6_desc': 'रोगाची लक्षणे, बुरशी/जिवाणूचे प्रकार आणि प्रसाराची कारणे जाणून घ्या.',
        'feat_7_title': 'सेंद्रिय व्यवस्थापन',
        'feat_7_desc': 'पर्यावरणपूरक सेंद्रिय औषधे, ताक-अर्क आणि जैविक बुरशीनाशकांचे मार्गदर्शन.',
        'feat_8_title': 'रासायनिक फवारणी सल्ला',
        'feat_8_desc': 'लेबलवरील सूचनांसह सुरक्षित रासायनिक फवारणी व प्रतिबंधात्मक उपाय.',
        'feat_9_title': 'अन्नद्रव्य व खत मार्गदर्शन',
        'feat_9_desc': 'पिकांना आवश्यक असणाऱ्या नत्र, स्फुरद व पालाश खतांचे योग्य संतुलन.',
        'feat_10_title': 'प्रतिबंध व शेती व्यवस्थापन',
        'feat_10_desc': 'रोग पुन्हा न येण्यासाठी योग्य पीक फेरपालट आणि स्वच्छता पद्धती.',

        # Upload Portal (/detect)
        'upload_portal_tag': 'एआय निदान केंद्र',
        'upload_portal_title': 'रोग तपासणीसाठी पानाचे छायाचित्र अपलोड करा',
        'upload_portal_subtitle': 'लक्षणे दिसणाऱ्या एका पानाचे स्पष्ट व चांगल्या प्रकाशातील छायाचित्र निवडा.',
        'quick_tips_title': 'उत्तम परिणामांसाठी महत्त्वाच्या टिप्स',
        'quick_tip_1': 'एकाच पानाचे स्पष्ट आणि स्वच्छ छायाचित्र वापरा.',
        'quick_tip_2': 'छायाचित्र अस्पष्ट किंवा अंधुक होणार नाही याची काळजी घ्या.',
        'quick_tip_3': 'नैसर्गिक उजेडात छायाचित्र काढा, सावली टाळा.',
        'quick_tip_4': 'रोगाचे डाग व लक्षणे छायाचित्रात स्पष्ट दिसू द्या.',
        'quick_tip_5': 'पानावर बोटे, सावली किंवा अनावश्यक वस्तू येणार नाहीत याची काळजी घ्या.',
        'drag_drop_text': 'पानाचे छायाचित्र येथे ड्रॅग करून टाका किंवा',
        'browse_files': '📁 फाईल निवडा',
        'take_photo': '📷 फोटो काढा',
        'change_image': '🔄 फोटो बदला',
        'remove_image': 'फोटो काढा',
        'supported_formats': 'समर्थित फॉरमॅट: JPG, JPEG, PNG, WEBP (कमाल १० MB)',
        'quick_test_leaves': 'चाचणीसाठी नमुना पाने:',
        'sample_1_name': 'टोमॅटो करपा रोग',
        'sample_1_sub': 'नमुना पान १',
        'sample_2_name': 'टोमॅटो निरोगी',
        'sample_2_sub': 'नमुना पान २',
        'sample_3_name': 'बटाटा पछेती तांबेरा',
        'sample_3_sub': 'नमुना पान ३',
        'sample_4_name': 'सफरचंद खपल्या रोग',
        'sample_4_sub': 'नमुना पान ४',
        'btn_start_analysis': '🔬 पानाची तपासणी सुरू करा',
        'analyzing_img': 'पानाची तपासणी सुरू आहे...',
        'processing_msg': 'छायाचित्र प्रक्रिया सुरू आहे...',
        'analyzing_symptoms': 'दिसणाऱ्या लक्षणांचे विश्लेषण सुरू आहे...',
        'identifying_disease': 'संभाव्य रोगाची ओळख पटवली जात आहे...',
        'preparing_guidance': 'कृषी सल्ला तयार केला जात आहे...',
        'selected_file_label': 'निवडलेली फाईल: ',
        'err_select_image': 'कृपया आधी पिकाच्या पानाचे छायाचित्र निवडा.',
        'err_unsupported_format': 'असमर्थित फॉरमॅट. कृपया JPG, JPEG, PNG किंवा WEBP छायाचित्र अपलोड करा.',
        'err_file_too_large': 'फाईलचा आकार १० MB मर्यादेपेक्षा जास्त आहे. कृपया लहान छायाचित्र निवडा.',
        'err_analysis_failed': 'पीक विश्लेषण पूर्ण करण्यात अडचण आली.',
        'err_network_error': 'छायाचित्र प्रक्रियेदरम्यान नेटवर्क त्रुटी आली.',

        # Diagnostic Result Report (/result & /gemini-result)
        'report_title': 'पीक आरोग्य तपासणी अहवाल',
        'report_subtitle': 'थेट दृश्य पॅथॉलॉजी व अचूक कृषी मार्गदर्शन',
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
        'card_confidence': 'विश्वास पातळी',
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
        'what_do_now_title': 'आता मी काय करावे? (तातडीच्या उपाययोजना)',
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
        'standard_gap_rec': 'चांगल्या कृषी पद्धतींचे नियमित पालन करा.',
        'analysis_notes_title': 'निदान टीप व मर्यादा',
        'none_specified': 'कोणतीही विशिष्ट नोंद नाही.',

        # Disclaimer & CTA
        'disclaimer_heading': '📢 महत्त्वाची कृषी सूचना (Disclaimer):',
        'disclaimer_notice': 'एग्रीव्हिजन एआय दृश्य लक्षणांवर आधारित प्राथमिक माहिती प्रदान करते. अंतिम प्रमाणीकरणासाठी व औषध फवारणीच्या योग्य प्रमाणासाठी स्थानिक कृषी तज्ज्ञांचा किंवा कृषी विद्यापीठाचा सल्ला घ्या. औषध फवारताना पाकिटावरील सूचनांचे काटेकोर पालन करा.',
        'disclaimer_point_1': 'केवळ पानावरील दृश्य लक्षणांवर आधारित एआय प्राथमिक तपासणी.',
        'disclaimer_point_2': 'प्रयोगशाळा चाचणी किंवा अधिकृत कृषी तज्ज्ञांच्या सल्ल्याचा हा पर्याय नाही.',
        'disclaimer_point_3': 'औषध फवारताना पाकिटावरील सूचना, योग्य प्रमाण व स्थानिक कृषी शिफारसींचे पालन करा.',
        'btn_analyze_another': '📷 दुसऱ्या पानाचे छायाचित्र तपासा',

        # Disease Library Page (/diseases & /disease/<id>)
        'knowledge_base_tag': 'कृषी ज्ञानकोश',
        'disease_library_title': 'पीक रोग माहिती दालन',
        'disease_library_subtitle': 'पिकांचे रोग, लक्षणे, कारणे आणि प्रतिबंधात्मक उपाययोजना शोधा व माहिती मिळवा.',
        'all_crops': 'सर्व पिके',
        'view_details': 'सविस्तर माहिती पहा',
        'no_diseases_found': 'तुमच्या शोधाशी जुळणारा कोणताही रोग आढळला नाही.',
        'no_diseases_desc': 'कृपया वेगळा शब्द किंवा पिकाचे नाव निवडून पुन्हा शोधा.',
        'nav_diseases': 'रोग माहिती दालन',
        'back_to_library': '← रोग माहिती दालनाकडे परत जा',

        # History Page (/history)
        'history_tag': 'जतन केलेले निदान नोंदी',
        'history_title': 'पिकांच्या निदानांचा इतिहास',
        'history_subtitle': 'पूर्वीच्या पीक आरोग्य निदानांची नोंद, रोगाची तीव्रता आणि अहवाल पहा.',
        'stat_total_analyzed': 'एकूण तपासण्या',
        'stat_healthy_leaf': 'निरोगी पाने',
        'stat_moderate_watch': 'मध्यम / देखरेख',
        'stat_urgent_priority': 'तातडीचे प्राधान्य',
        'search_placeholder': '🔍 पीक किंवा रोगाच्या नावाने शोधा...',
        'severity_filter_label': 'तीव्रता:',
        'opt_all_severities': 'सर्व तीव्रता स्तर',
        'opt_healthy': '🟢 निरोगी',
        'opt_low': '🟡 कमी तीव्रता',
        'opt_moderate': '🟠 मध्यम तीव्रता',
        'opt_high': '🔴 उच्च तीव्रता',
        'opt_critical': '🚨 अत्यंत गंभीर',
        'btn_filter': 'शोधा / फिल्टर',
        'btn_reset': 'रीसेट करा',
        'col_date': 'तारीख व वेळ',
        'col_image': 'पानाचे छायाचित्र',
        'col_crop': 'पीक',
        'col_condition': 'आढळलेला रोग',
        'col_confidence': 'विश्वास पातळी',
        'col_severity': 'तीव्रता',
        'col_actions': 'कृती',
        'btn_view_report': 'पूर्ण अहवाल पहा →',
        'delete_record': 'हटवा',
        'tooltip_delete': 'नोंद हटवा',
        'confirm_delete_record': 'तुम्हाला खात्री आहे का की ही निदान नोंद हटवायची आहे?',
        'empty_history': 'तुमच्या इतिहासात सध्या कोणत्याही नोंदी उपलब्ध नाहीत.',
        'empty_history_desc': 'पिकाच्या पानाचा फोटो अपलोड करून एआय रोग तपासणी सुरू करा आणि नोंदी जतन करा.',

        # About Page (/about)
        'about_tag': 'एग्रीव्हिजन एआय बद्दल',
        'about_title': 'अचूक शेतीसाठी पारदर्शक व सुलभ एआय तंत्रज्ञान',
        'about_subtitle': 'डीप लर्निंग कॉम्प्युटर व्हिजन आणि पारदर्शक पीक मार्गदर्शनाचा संगम.',
        'platform_overview_tag': 'प्लॅटफॉर्म परिचय',
        'platform_overview_title': 'एग्रीव्हिजन एआय बद्दल',
        'platform_overview_desc': 'एग्रीव्हिजन एआय ही एक प्रगत कृषी सहाय्यक प्रणाली आहे, जी शेतकऱ्यांना पिकांवरील रोगांची वेळेवर ओळख, दृश्य विश्लेषण आणि प्रत्यक्ष कृती मार्गदर्शन प्रदान करते.',
        'core_objective_tag': 'मुख्य उद्दिष्ट',
        'our_mission': 'आमचे ध्येय',
        'our_mission_desc': 'शेतकऱ्यांना व कृषी कार्यकर्त्यांना सुलभ एआय तंत्रज्ञानाने सक्षम करणे, पिकांचे नुकसान वेळीच रोखणे आणि अनावश्यक रासायनिक कीटकनाशकांचा वापर कमी करणे.',
        'how_ai_helps': 'एआय शेतीत कशी मदत करते',
        'how_ai_helps_desc': 'कॉम्प्युटर व्हिजन मॉडेल्स पानावरील करपा, डाग आणि पिवळेपणाचे सूक्ष्म विश्लेषण करून रोग पसरण्यापूर्वीच अचूक माहिती देतात.',
        'xai_title': 'पारदर्शक व स्पष्ट एआय (XAI)',
        'xai_desc': 'केवळ निकाल देण्याऐवजी, एग्रीव्हिजन एआय Grad-CAM हीटमॅपद्वारे पानाच्या कोणत्या भागावरून निष्कर्ष काढला हे स्पष्टपणे दाखवते.',
        'tech_stack_tag': 'तांत्रिक रचना',
        'tech_stack_title': 'वापरलेले तंत्रज्ञान',
        'tech_python_title': 'पायथन ३',
        'tech_python_desc': 'डेटा प्रक्रिया, मॉडेल इन्फरन्स आणि बॅकएंड सेवांचे संचालन करणारी मुख्य भाषा.',
        'tech_flask_title': 'फ्लास्क फ्रेमवर्क',
        'tech_flask_desc': 'रेस्ट एपीआय आणि वेब टेम्पलेट्स वेगाने व्यवस्थापित करणारे हलके फ्रेमवर्क.',
        'tech_gemini_title': 'गूगल जेमिनी व्हिजन एआय',
        'tech_gemini_desc': 'थेट पानांचे दृश्य पॅथॉलॉजी विश्लेषण करणारे प्रगत मल्टीमॉडेल व्हिजन मॉडेल.',
        'tech_opencv_title': 'ओपनसीव्ही व पिलो',
        'tech_vision_desc': 'फाईल पडताळणी, आकारमान आणि पानाची स्पष्टता तपासण्यासाठी कॉम्प्युटर व्हिजन साधने.',
        'tech_gradcam_title': 'ग्रॅड-कॅम एक्सएआई',
        'tech_gradcam_desc': 'एआयच्या विश्लेषणाचे रंगीत हीटमॅप तयार करणारे पारदर्शक तंत्रज्ञान.',
        'tech_db_title': 'मायएसक्यूएल / एसक्यूलाइट',
        'tech_db_desc': 'निदान इतिहास आणि कृषी माहिती सुरक्षित साठवणारी डेटाबेस प्रणाली.',
        'tech_frontend_title': 'एचटीएमएल, सीएसएस आणि जावास्क्रिप्ट',
        'tech_frontend_desc': 'सर्व मोबाईल व संगणकावर सुरळीत चालणारी आधुनिक डिझाइन प्रणाली.',
        'system_works_title': 'प्रणाली कशी कार्य करते',
        'pipe_1_title': '१. छायाचित्र अपलोड करा',
        'pipe_1_desc': 'शेतकरी बाधित पानाचे स्पष्ट छायाचित्र अपलोड करतात.',
        'pipe_2_title': '२. पूर्वप्रक्रिया',
        'pipe_2_desc': 'सर्व्हर छायाचित्राचा आकार, गुणवत्ता व स्पष्टतेची तपासणी करतो.',
        'pipe_3_title': '३. एआय विश्लेषण',
        'pipe_3_desc': 'जेमिनी मॉडेल पिकाची जात, रोग व तीव्रतेचा टप्पा ओळखते.',
        'pipe_4_title': '४. व्हिज्युअल हीटमॅप',
        'pipe_4_desc': 'पानावरील बाधित डाग व रोग क्षेत्र रंगीत हायलाइट केले जाते.',
        'pipe_5_title': '५. सविस्तर माहिती',
        'pipe_5_desc': 'रोगाची लक्षणे, संभाव्य कारणे व कीटकांचे विश्लेषण दाखवले जाते.',
        'pipe_6_title': '६. प्रत्यक्ष कृती सल्ला',
        'pipe_6_desc': 'शेतकऱ्यांसाठी ४ तातडीची पावले, सेंद्रिय उपाय व फवारणी सल्ला दिला जातो.',
        'limitations_title': 'महत्त्वाच्या एआय मर्यादा',
        'limitations_intro': 'एग्रीव्हिजन एआय हे निर्णय-सहाय्यक साधन आहे. वापरकर्त्यांनी खालील मर्यादा लक्षात ठेवाव्यात:',
        'limit_1': 'एआय निदान पानावरील दृश्य लक्षणांवर आणि छायाचित्राच्या गुणवत्तेवर अवलंबून असते.',
        'limit_2': 'वेगवेगळ्या रोगांमध्ये पानांवर एकाच प्रकारचा पिवळेपणा किंवा डाग दिसू शकतात.',
        'limit_3': 'उन्हामुळे करपणे किंवा वाऱ्यामुळे होणारे नुकसान रोगाच्या डागांसारखे वाटू शकते.',
        'limit_4': 'छायाचित्रावरून जमिनीतील घटकांची अचूक कमतरता किंवा मुळांमधील रोग मोजता येत नाही.',
        'limit_5': 'एआय सल्ला हा अधिकृत प्रयोगशाळा चाचणी किंवा कृषी तज्ज्ञांच्या प्रत्यक्ष भेटीचा पर्याय नाही.',

        # Contact Page (/contact)
        'contact_tag': 'संपर्क साधा',
        'contact_title': 'संपर्क व अभिप्राय',
        'contact_subtitle': 'आपल्या काही शंका, अभिप्राय किंवा कृषीविषयक प्रश्न असल्यास आम्हाला नक्की कळवा.',
        'form_name': 'तुमचे पूर्ण नाव *',
        'form_name_placeholder': 'तुमचे पूर्ण नाव प्रविष्ट करा',
        'form_email': 'ईमेल पत्ता *',
        'form_email_placeholder': 'name@example.com',
        'form_subject': 'विषय',
        'form_subject_placeholder': 'उदा. मॉडेलबद्दल अभिप्राय किंवा विचारणा',
        'form_message': 'तुमचा संदेश *',
        'form_message_placeholder': 'तुमचा प्रश्न किंवा संदेश येथे लिहा...',
        'send_btn': '✉️ संदेश पाठवा',
        'toast_form_required': 'कृपया संदेश पाठवण्यापूर्वी सर्व आवश्यक रकाने भरा.',
        'toast_valid_email': 'कृपया एक वैध ईमेल पत्ता प्रविष्ट करा.',
        'toast_copied': 'निदान सारांश क्लिपबोर्डवर कॉपी झाला!',
        'toast_copy_failed': 'सारांश कॉपी करण्यात अडचण आली.'
    },

    'hi': {
        # Navigation & Header
        'app_name': 'एग्रीविज़न एआई',
        'app_subtitle': 'पारदर्शी फसल रोग पहचान प्रणाली',
        'home': 'मुखपृष्ठ',
        'detect_disease': 'पत्ती जांचें',
        'history': 'निदान इतिहास',
        'about': 'जानकारी',
        'contact': 'संपर्क',
        'language': 'भाषा',
        'english': 'English',
        'marathi': 'मराठी',
        'hindi': 'हिंदी',
        'analyze_crop': '🔍 फसल जांचें',
        'toggle_theme': 'लाइट/डार्क मोड बदलें',
        'menu_toggle': 'मेनू खोलें',

        # Footer
        'footer_brand_desc': 'फसल रोगों की प्रारंभिक पहचान, विज़ुअल हीटमैप, रोग गंभीरता का अनुमान और किसानों के लिए उपयोगी कृषि मार्गदर्शन हेतु विकसित पारदर्शी एआई तकनीक।',
        'footer_nav_heading': 'मार्गदर्शन',
        'footer_cap_heading': 'क्षमताएं',
        'footer_tech_heading': 'तकनीक',
        'footer_rights': 'सर्वाधिकार सुरक्षित। सटीक एवं पारदर्शी कृषि के लिए निर्मित।',
        'cap_leaf_analysis': 'रियल-टाइम एआई पत्ती विश्लेषण',
        'cap_severity_est': 'रोग गंभीरता का अनुमान',
        'cap_heatmaps': 'ग्रैड-कैम विज़ुअल हीटमैप',
        'cap_guidance': 'जैविक एवं रासायनिक उपाय',
        'tech_gemini': 'गूगल जेमिनी विज़न एआई',
        'tech_vision_scanner': 'कंप्यूटर विज़न लीफ स्कैनर',
        'tech_flask': 'पायथन फ्लास्क बैकएंड',
        'tech_xai': 'पारदर्शी एआई मार्गदर्शन',

        # Hero & Home Page
        'hero_badge': '🤖 गूगल जेमिनी विज़न एआई एवं ३D तकनीक',
        'hero_title_1': 'फसल रोगों की समय पर पहचान करें ',
        'hero_title_2': 'एआई तकनीक से',
        'hero_subtitle': 'फसल की पत्ती की तस्वीर अपलोड करें और संभावित रोग, दृश्य लक्षण, रोग गंभीरता और किसानों के लिए आवश्यक प्रबंधन प्रक्रियाओं की जानकारी पाएं।',
        'btn_analyze_leaf': '🔍 पत्ती की जांच करें',
        'trust_realtime_ai': '✓ तत्काल एआई विश्लेषण',
        'trust_explainable': '✓ पारदर्शी एवं स्पष्ट मार्गदर्शन',
        'trust_solutions': '✓ जैविक एवं रासायनिक समाधान',
        'floating_condition_val': 'अगेती झुलसा',
        'floating_severity_val': 'मध्यम',

        # How AgriVision AI Works
        'how_tag': 'कार्यप्रणाली',
        'how_title': 'एग्रीविज़न एआई कैसे काम करता है',
        'how_subtitle': 'तस्वीर लेने से लेकर खेत में व्यावहारिक उपायों तक, एग्रीविज़न एआई सरल भाषा में सटीक मार्गदर्शन देता है।',
        'step_01_title': 'पत्ती की तस्वीर अपलोड करें',
        'step_01_desc': 'प्रभावित फसल की पत्ती की साफ तस्वीर मोबाइल या कंप्यूटर से अपलोड करें।',
        'step_02_title': 'एआई पत्ती का परीक्षण करता है',
        'step_02_desc': 'कंप्यूटर विज़न मॉडल पत्ती के धब्बों, पीलेपन और प्रभावित क्षेत्रों का विश्लेषण करता है।',
        'step_03_title': 'संभावित रोग की पहचान',
        'step_03_desc': 'प्रशिक्षित एआई मॉडल रोग, उसकी सटीकता और गंभीरता का चरण निर्धारित करता है।',
        'step_04_title': 'कृषि मार्गदर्शन प्राप्त करें',
        'step_04_desc': 'किसानों के लिए आवश्यक कदम, जैविक व रासायनिक छिड़काव और खाद प्रबंधन की सलाह मिलती है।',
        'chip_formats': 'JPG, PNG, WEBP',
        'chip_lighting': 'स्पष्ट प्रकाश',
        'chip_drag_drop': 'ड्रैग व ड्रॉप',
        'chip_processing': 'तस्वीर प्रसंस्करण जारी है...',
        'chip_symptoms': 'लक्षणों का विश्लेषण हो रहा है...',
        'chip_disease_name': 'अगेती झुलसा',
        'chip_confidence': '९४% विश्वास स्तर',
        'chip_moderate': 'मध्यम चरण',
        'workflow_cta_title': 'क्या आप अपनी फसल जांचना चाहते हैं?',
        'workflow_cta_desc': 'तत्काल रोग निदान और जैविक प्रबंधन के निर्देश प्राप्त करें।',
        'workflow_cta_btn': 'पत्ती की जांच शुरू करें →',

        # Platform Capabilities / 10 Feature Cards
        'features_tag': 'मंच की क्षमताएं',
        'features_title': 'एग्रीविज़न एआई की मुख्य विशेषताएं',
        'features_subtitle': 'किसानों के लिए सरल भाषा, पूर्ण पारदर्शिता और उपयोगी कृषि सलाह।',
        'feat_1_title': 'एआई रोग पहचान',
        'feat_1_desc': 'डीप लर्निंग तकनीक से फसलों के विभिन्न रोगों की त्वरित पहचान करें।',
        'feat_2_title': 'विश्वास स्तर विश्लेषण',
        'feat_2_desc': 'मॉडल की भविष्यवाणी का विश्वास स्तर और सटीकता स्पष्ट रूप से देखें।',
        'feat_3_title': 'पारदर्शी एआई (Grad-CAM)',
        'feat_3_desc': 'पत्ती के किन हिस्सों के आधार पर निर्णय लिया गया, यह रंगीन हीटमैप से देखें।',
        'feat_4_title': 'रोग चरण अनुमान',
        'feat_4_desc': 'रोग का सही चरण (प्रारंभिक, मध्यम, उन्नत, गंभीर) समझें।',
        'feat_5_title': 'प्रभावित क्षेत्र का प्रतिशत',
        'feat_5_desc': 'पत्ती पर धब्बों का प्रतिशत और नुकसान का स्तर मापें।',
        'feat_6_title': 'विस्तृत रोग जानकारी',
        'feat_6_desc': 'रोग के लक्षण, कवक/जीवाणु के प्रकार और फैलाव के कारण जानें।',
        'feat_7_title': 'जैविक प्रबंधन',
        'feat_7_desc': 'पर्यावरण-अनुकूल जैविक दवाएं, नीम अर्क और जैव-कवकनाशी का मार्गदर्शन।',
        'feat_8_title': 'रासायनिक छिड़काव निर्देश',
        'feat_8_desc': 'पैकेट पर दिए सुरक्षा निर्देशों के साथ सुरक्षित रासायनिक छिड़काव सलाह।',
        'feat_9_title': 'उर्वरक एवं पोषण प्रबंधन',
        'feat_9_desc': 'फसलों के लिए आवश्यक नाइट्रोजन, फास्फोरस और पोटाश का उचित संतुलन।',
        'feat_10_title': 'रोकथाम एवं सुरक्षा',
        'feat_10_desc': 'रोग की पुनरावृत्ति रोकने के लिए उचित फसल चक्र और खेत की स्वच्छता।',

        # Upload Portal (/detect)
        'upload_portal_tag': 'एआई निदान केंद्र',
        'upload_portal_title': 'रोग जांच के लिए पत्ती की तस्वीर अपलोड करें',
        'upload_portal_subtitle': 'लक्षण दिखाई देने वाली एक पत्ती की स्पष्ट और अच्छे प्रकाश वाली तस्वीर चुनें।',
        'quick_tips_title': 'उत्कृष्ट परिणामों के लिए उपयोगी सुझाव',
        'quick_tip_1': 'एक ही पत्ती की स्पष्ट और सीधी तस्वीर लें।',
        'quick_tip_2': 'तस्वीर धुंधली या अस्पष्ट न हो इसका ध्यान रखें।',
        'quick_tip_3': 'प्राकृतिक रोशनी में फोटो खींचें, गहरी छाया से बचें।',
        'quick_tip_4': 'रोग के धब्बे और लक्षण तस्वीर में साफ दिखने चाहिए।',
        'quick_tip_5': 'पत्ती पर उंगलियां, औजार या अन्य वस्तुएं न आने दें।',
        'drag_drop_text': 'पत्ती की तस्वीर यहां ड्रैग करके छोड़ें या',
        'browse_files': '📁 फ़ाइल चुनें',
        'take_photo': '📷 फोटो खींचें',
        'change_image': '🔄 फोटो बदलें',
        'remove_image': 'फोटो हटाएं',
        'supported_formats': 'समर्थित प्रारूप: JPG, JPEG, PNG, WEBP (अधिकतम 10 MB)',
        'quick_test_leaves': 'परीक्षण के लिए नमूना पत्तियां:',
        'sample_1_name': 'टमाटर अगेती झुलसा',
        'sample_1_sub': 'नमूना पत्ती 1',
        'sample_2_name': 'टमाटर स्वस्थ',
        'sample_2_sub': 'नमूना पत्ती 2',
        'sample_3_name': 'आलू पछेती झुलसा',
        'sample_3_sub': 'नमूना पत्ती 3',
        'sample_4_name': 'सेब पपड़ी रोग',
        'sample_4_sub': 'नमूना पत्ती 4',
        'btn_start_analysis': '🔬 पत्ती की जांच शुरू करें',
        'analyzing_img': 'पत्ती का विश्लेषण किया जा रहा है…',
        'processing_msg': 'तस्वीर संसाधित हो रही है...',
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
        'report_title': 'फसल स्वास्थ्य निदान रिपोर्ट',
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
        'card_confidence': 'विश्वास स्तर',
        'card_health_status': 'स्वास्थ्य स्थिति',
        'card_action_urgency': 'कार्रवाई की गंभीरता',
        'plant_id_label': 'पौधे की पहचान:',
        'category_label': 'रोग श्रेणी:',
        'diagnostic_status_label': 'निदान स्थिति',

        # Photo & Severity Card
        'analyzed_leaf_photo': 'जांची गई पत्ती की फोटो',
        'leaf_sample_placeholder': 'अपलोड की गई पत्ती का नमूना',
        'pathology_severity_title': 'रोग गंभीरता का स्तर',
        'severity_assessment_label': 'गंभीरता का विवरण:',

        # Actionable Guidance Section
        'actionable_guidance_title': '⚡ किसानों के लिए प्रत्यक्ष कार्रवाई मार्गदर्शन',
        'actionable_guidance_sub': 'फसल स्वास्थ्य विश्लेषण के आधार पर अनुशंसित अगले कदम',
        'ai_guided_actions_badge': 'एआई निर्देशित कदम',
        'what_do_now_title': 'अब मुझे क्या करना चाहिए? (तत्काल उपाय)',
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
        'standard_gap_rec': 'उत्कृष्ट कृषि पद्धतियों का नियमित पालन करें।',
        'analysis_notes_title': 'निदान टिप्पणी एवं सीमाएं',
        'none_specified': 'कोई विशेष उल्लेख नहीं।',

        # Disclaimer & CTA
        'disclaimer_heading': '📢 महत्वपूर्ण कृषि सूचना (Disclaimer):',
        'disclaimer_notice': 'एग्रीविज़न एआई दृश्य लक्षणों पर आधारित प्राथमिक जानकारी प्रदान करता है। अंतिम पुष्टि एवं दवा छिड़काव की सटीक मात्रा के लिए स्थानीय कृषि विशेषज्ञ या अनुसंधान केंद्र से सलाह लें। हमेशा स्थानीय रूप से स्वीकृत कृषि उत्पाद लेबल के निर्देशों का पालन करें।',
        'disclaimer_point_1': 'केवल पत्तियों पर दृश्य लक्षणों पर आधारित एआई प्रारंभिक जांच।',
        'disclaimer_point_2': 'यह प्रयोगशाला परीक्षण या प्रमाणित कृषि विशेषज्ञ की सलाह का विकल्प नहीं है।',
        'disclaimer_point_3': 'दवा छिड़काव के लिए हमेशा स्थानीय रूप से अनुमोदित उत्पाद लेबल और निर्देशों का पालन करें।',
        'btn_analyze_another': '📷 किसी अन्य पत्ती की जांच करें',

        # Disease Library Page (/diseases & /disease/<id>)
        'knowledge_base_tag': 'कृषि ज्ञानकोश',
        'disease_library_title': 'फसल रोग ज्ञानकोश',
        'disease_library_subtitle': 'फसलों के रोग, लक्षण, कारण और निवारक रणनीतियों को खोजें और समझें।',
        'all_crops': 'सभी फसलें',
        'view_details': 'विस्तृत जानकारी देखें',
        'no_diseases_found': 'आपकी खोज से मेल खाता कोई रोग नहीं मिला।',
        'no_diseases_desc': 'कृपया कोई अन्य शब्द या फसल चुनकर पुनः प्रयास करें।',
        'nav_diseases': 'रोग ज्ञानकोश',
        'back_to_library': '← रोग ज्ञानकोश पर वापस जाएं',

        # History Page (/history)
        'history_tag': 'सुरक्षित निदान रिकॉर्ड',
        'history_title': 'निदान इतिहास लॉग',
        'history_subtitle': 'पिछली फसल जांच रिपोर्ट, बीमारी की गंभीरता और हीटमैप देखें।',
        'stat_total_analyzed': 'कुल जांचें',
        'stat_healthy_leaf': 'स्वस्थ पत्तियां',
        'stat_moderate_watch': 'मध्यम / निगरानी',
        'stat_urgent_priority': 'तत्काल प्राथमिकता',
        'search_placeholder': '🔍 फसल या रोग के नाम से खोजें...',
        'severity_filter_label': 'गंभीरता:',
        'opt_all_severities': 'सभी गंभीरता स्तर',
        'opt_healthy': '🟢 स्वस्थ',
        'opt_low': '🟡 कम गंभीरता',
        'opt_moderate': '🟠 मध्यम गंभीरता',
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
        'tech_python_title': 'पायथन ३',
        'tech_python_desc': 'डेटा प्रोसेसिंग, एपीआई और कंप्यूटर विज़न पाइपलाइन को संचालित करने वाली मुख्य भाषा।',
        'tech_flask_title': 'फ्लास्क फ्रेमवर्क',
        'tech_flask_desc': 'हल्का और तेज़ WSGI वेब फ्रेमवर्क, जो रेस्ट एपीआई और टेम्पलेट्स का प्रबंधन करता है।',
        'tech_gemini_title': 'गूगल जेमिनी विज़न एआई',
        'tech_gemini_desc': 'आधिकारिक गूगल जेमिनी विज़न मॉडल, जो रियल-टाइम विज़ुअल पैथोलॉजी की पहचान करता है।',
        'tech_opencv_title': 'ओपनसीवी और पिलो',
        'tech_vision_desc': 'फ़ाइल सत्यापन, स्केलिंग और पत्ती की गुणवत्ता जांच के लिए कंप्यूटर विज़न टूल।',
        'tech_gradcam_title': 'ग्रैड-कैम एक्सएआई',
        'tech_gradcam_desc': 'एआई के निर्णय की विज़ुअल व्याख्या करने वाली अत्याधुनिक हीटमैप तकनीक।',
        'tech_db_title': 'मायएसक्यूएल / एसक्यूलाइट',
        'tech_db_desc': 'निदान इतिहास और कृषि अभिलेखों को सुरक्षित रखने वाली रिलेशनल डेटाबेस प्रणाली।',
        'tech_frontend_title': 'एचटीएमएल, सीएसएस और जावास्क्रिप्ट',
        'tech_frontend_desc': 'सभी उपकरणों पर सुचारू रूप से चलने वाली आधुनिक सीएसएस और जावास्क्रिप्ट डिज़ाइन प्रणाली।',
        'system_works_title': 'प्रणाली कैसे काम करती है',
        'pipe_1_title': '१. तस्वीर अपलोड करें',
        'pipe_1_desc': 'प्रभावित फसल की पत्ती की साफ और नजदीकी तस्वीर अपलोड करें।',
        'pipe_2_title': '२. तस्वीर प्रसंस्करण',
        'pipe_2_desc': 'सर्वर फ़ाइल प्रारूप, रिज़ॉल्यूशन और पत्ती की स्पष्टता की जांच करता है।',
        'pipe_3_title': '३. एआई निदान',
        'pipe_3_desc': 'जेमिनी विज़न मॉडल फसल की किस्म, बीमारी और उसकी गंभीरता की पहचान करता है।',
        'pipe_4_title': '४. पारदर्शी विज़ुअल व्याख्या',
        'pipe_4_desc': 'पत्ती पर धब्बों का प्रतिशत और विज़ुअल हीटमैप तैयार करता है।',
        'pipe_5_title': '५. रोग की विस्तृत जानकारी',
        'pipe_5_desc': 'बीमारी के लक्षण, संभावित कारण और कीट विश्लेषण प्रदर्शित करता है।',
        'pipe_6_title': '६. प्रबंधन मार्गदर्शन',
        'pipe_6_desc': 'किसानों के लिए प्राथमिकता वाले कदम, जैविक उपाय और छिड़काव सलाह देता है।',
        'limitations_title': 'महत्वपूर्ण एआई सीमाएं',
        'limitations_intro': 'एग्रीविज़न एआई एक निर्णय-सहायक उपकरण है। उपयोगकर्ताओं को निम्नलिखित सीमाओं का ध्यान रखना चाहिए:',
        'limit_1': 'एआई निदान तस्वीर में दिखाई देने वाले लक्षणों और फोटो की गुणवत्ता पर निर्भर करता है।',
        'limit_2': 'कुछ अलग-अलग बीमारियों में पत्तियों पर एक जैसे ही धब्बे या पीलापन दिखाई दे सकता है।',
        'limit_3': 'धूप से झुलसना या हवा से होने वाली क्षति भी बीमारी के धब्बों जैसी प्रतीत हो सकती है।',
        'limit_4': 'तस्वीर से मिट्टी का पीएच, पोषक तत्वों की सटीक मात्रा या जड़ों की सड़न नहीं मापी जा सकती।',
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
# DYNAMIC CROP NAME TRANSLATION MAP (Pure, Clean Translations)
# =====================================================================
CROP_NAME_MAP = {
    'tomato': {'mr': 'टोमॅटो', 'hi': 'टमाटर', 'en': 'Tomato'},
    'potato': {'mr': 'बटाटा', 'hi': 'आलू', 'en': 'Potato'},
    'pepper': {'mr': 'शिमला मिरची', 'hi': 'शिमला मिर्च', 'en': 'Pepper'},
    'pepper bell': {'mr': 'शिमला मिरची', 'hi': 'शिमला मिर्च', 'en': 'Pepper bell'},
    'pepper, bell': {'mr': 'शिमला मिरची', 'hi': 'शिमला मिर्च', 'en': 'Pepper bell'},
    'apple': {'mr': 'सफरचंद', 'hi': 'सेब', 'en': 'Apple'},
    'corn': {'mr': 'मका', 'hi': 'मक्का', 'en': 'Corn'},
    'corn (maize)': {'mr': 'मका', 'hi': 'मक्का', 'en': 'Corn (maize)'},
    'corn_(maize)': {'mr': 'मका', 'hi': 'मक्का', 'en': 'Corn (maize)'},
    'grape': {'mr': 'द्राक्षे', 'hi': 'अंगूर', 'en': 'Grape'},
    'orange': {'mr': 'संत्रे', 'hi': 'संतरा', 'en': 'Orange'},
    'peach': {'mr': 'पीच', 'hi': 'आड़ू', 'en': 'Peach'},
    'blueberry': {'mr': 'ब्लूबेरी', 'hi': 'ब्लूबेरी', 'en': 'Blueberry'},
    'cherry': {'mr': 'चेरी', 'hi': 'चेरी', 'en': 'Cherry'},
    'cherry (including sour)': {'mr': 'चेरी', 'hi': 'चेरी', 'en': 'Cherry (including sour)'},
    'raspberry': {'mr': 'रासबेरी', 'hi': 'रास्पबेरी', 'en': 'Raspberry'},
    'soybean': {'mr': 'सोयाबीन', 'hi': 'सोयाबीन', 'en': 'Soybean'},
    'squash': {'mr': 'भोपळा', 'hi': 'कद्दू', 'en': 'Squash'},
    'strawberry': {'mr': 'स्ट्रॉबेरी', 'hi': 'स्ट्रॉबेरी', 'en': 'Strawberry'},
    'unknown crop': {'mr': 'अज्ञात पीक', 'hi': 'अज्ञात फसल', 'en': 'Unknown Crop'},
    'crop': {'mr': 'पीक', 'hi': 'फसल', 'en': 'Crop'}
}

# =====================================================================
# DYNAMIC DISEASE NAME TRANSLATION MAP (Pure, Clean Translations)
# =====================================================================
DISEASE_NAME_MAP = {
    # Tomato Diseases
    'tomato healthy': {'mr': 'टोमॅटो - निरोगी', 'hi': 'टमाटर - स्वस्थ', 'en': 'Tomato Healthy'},
    'tomato early blight': {'mr': 'टोमॅटो - करपा रोग', 'hi': 'टमाटर - अगेती झुलसा', 'en': 'Tomato Early Blight'},
    'early blight': {'mr': 'करपा रोग', 'hi': 'अगेती झुलसा', 'en': 'Early Blight'},
    'tomato late blight': {'mr': 'टोमॅटो - तांबेरा / पछेती करपा', 'hi': 'टमाटर - पछेती झुलसा', 'en': 'Tomato Late Blight'},
    'late blight': {'mr': 'तांबेरा / पछेती करपा', 'hi': 'पछेती झुलसा', 'en': 'Late Blight'},
    'tomato bacterial spot': {'mr': 'टोमॅटो - जिवाणूजन्य डाग', 'hi': 'टमाटर - जीवाणु धब्बा', 'en': 'Tomato Bacterial Spot'},
    'bacterial spot': {'mr': 'जिवाणूजन्य डाग', 'hi': 'जीवाणु धब्बा', 'en': 'Bacterial Spot'},
    'tomato septoria leaf spot': {'mr': 'टोमॅटो - सेप्टोरिया पानावरील डाग', 'hi': 'टमाटर - सेप्टोरिया पत्ती धब्बा', 'en': 'Tomato Septoria Leaf Spot'},
    'septoria leaf spot': {'mr': 'सेप्टोरिया पानावरील डाग', 'hi': 'सेप्टोरिया पत्ती धब्बा', 'en': 'Septoria Leaf Spot'},
    'tomato spider mites': {'mr': 'टोमॅटो - लाल कोळी कीड', 'hi': 'टमाटर - लाल मकड़ी कीट', 'en': 'Tomato Spider Mites'},
    'tomato spider mites two-spotted spider mite': {'mr': 'टोमॅटो - दोन ठिपक्यांची लाल कोळी कीड', 'hi': 'टमाटर - दो धब्बों वाली लाल मकड़ी कीट', 'en': 'Tomato Spider Mites'},
    'tomato target spot': {'mr': 'टोमॅटो - टार्गेट स्पॉट बुरशी', 'hi': 'टमाटर - टारगेट स्पॉट कवक', 'en': 'Tomato Target Spot'},
    'target spot': {'mr': 'टार्गेट स्पॉट बुरशी', 'hi': 'टारगेट स्पॉट कवक', 'en': 'Target Spot'},
    'tomato yellow leaf curl virus': {'mr': 'टोमॅटो - पिवळा पाने मुरडणारा विषाणू', 'hi': 'टमाटर - पीली पत्ती मरोड़ विषाणु', 'en': 'Tomato Yellow Leaf Curl Virus'},
    'yellow leaf curl virus': {'mr': 'पिवळा पाने मुरडणारा विषाणू', 'hi': 'पीली पत्ती मरोड़ विषाणु', 'en': 'Yellow Leaf Curl Virus'},
    'tomato mosaic virus': {'mr': 'टोमॅटो - मोझॅक विषाणू', 'hi': 'टमाटर - मोज़ेक विषाणु', 'en': 'Tomato Mosaic Virus'},
    'mosaic virus': {'mr': 'मोझॅक विषाणू', 'hi': 'मोज़ेक विषाणु', 'en': 'Mosaic Virus'},
    'tomato leaf mold': {'mr': 'टोमॅटो - पानावरील बुरशी', 'hi': 'टमाटर - पत्ती फफूंद', 'en': 'Tomato Leaf Mold'},
    'leaf mold': {'mr': 'पानावरील बुरशी', 'hi': 'पत्ती फफूंद', 'en': 'Leaf Mold'},

    # Potato Diseases
    'potato healthy': {'mr': 'बटाटा - निरोगी', 'hi': 'आलू - स्वस्थ', 'en': 'Potato Healthy'},
    'potato early blight': {'mr': 'बटाटा - करपा रोग', 'hi': 'आलू - अगेती झुलसा', 'en': 'Potato Early Blight'},
    'potato late blight': {'mr': 'बटाटा - पछेती तांबेरा', 'hi': 'आलू - पछेती झुलसा', 'en': 'Potato Late Blight'},

    # Pepper Diseases
    'pepper healthy': {'mr': 'शिमला मिरची - निरोगी', 'hi': 'शिमला मिर्च - स्वस्थ', 'en': 'Pepper Healthy'},
    'pepper bell healthy': {'mr': 'शिमला मिरची - निरोगी', 'hi': 'शिमला मिर्च - स्वस्थ', 'en': 'Pepper bell Healthy'},
    'pepper bacterial spot': {'mr': 'शिमला मिरची - जिवाणूजन्य डाग', 'hi': 'शिमला मिर्च - जीवाणु धब्बा', 'en': 'Pepper Bacterial Spot'},
    'pepper bell bacterial spot': {'mr': 'शिमला मिरची - जिवाणूजन्य डाग', 'hi': 'शिमला मिर्च - जीवाणु धब्बा', 'en': 'Pepper bell Bacterial Spot'},

    # Apple Diseases
    'apple healthy': {'mr': 'सफरचंद - निरोगी', 'hi': 'सेब - स्वस्थ', 'en': 'Apple Healthy'},
    'apple scab': {'mr': 'सफरचंद - खपल्या रोग', 'hi': 'सेब - पपड़ी रोग', 'en': 'Apple Scab'},
    'apple black rot': {'mr': 'सफरचंद - काळी कूज', 'hi': 'सेब - काला सड़न रोग', 'en': 'Apple Black Rot'},
    'cedar apple rust': {'mr': 'सफरचंद - तांबेरा बुरशी', 'hi': 'सेब - रतुआ कवक', 'en': 'Cedar Apple Rust'},

    # Corn Diseases
    'corn healthy': {'mr': 'मका - निरोगी', 'hi': 'मक्का - स्वस्थ', 'en': 'Corn Healthy'},
    'corn (maize) healthy': {'mr': 'मका - निरोगी', 'hi': 'मक्का - स्वस्थ', 'en': 'Corn (maize) Healthy'},
    'corn common rust': {'mr': 'मका - तांबेरा रोग', 'hi': 'मक्का - सामान्य रतुआ', 'en': 'Corn Common Rust'},
    'corn cercospora leaf spot gray leaf spot': {'mr': 'मका - करडा पानावरील डाग', 'hi': 'मक्का - धूसर पत्ती धब्बा', 'en': 'Corn Gray Leaf Spot'},
    'corn northern leaf blight': {'mr': 'मका - उत्तरेकडील करपा', 'hi': 'मक्का - उत्तरी पत्ती झुलसा', 'en': 'Corn Northern Leaf Blight'},

    # Grape Diseases
    'grape healthy': {'mr': 'द्राक्षे - निरोगी', 'hi': 'अंगूर - स्वस्थ', 'en': 'Grape Healthy'},
    'grape black rot': {'mr': 'द्राक्षे - काळी कूज', 'hi': 'अंगूर - काला सड़न', 'en': 'Grape Black Rot'},
    'grape esca (black measles)': {'mr': 'द्राक्षे - एस्का रोग', 'hi': 'अंगूर - एस्का रोग', 'en': 'Grape Esca (Black Measles)'},
    'grape leaf blight (isariopsis leaf spot)': {'mr': 'द्राक्षे - पानावरील करपा', 'hi': 'अंगूर - पत्ती झुलसा', 'en': 'Grape Leaf Blight'},

    # Orange / Citrus
    'orange haunglongbing (citrus greening)': {'mr': 'संत्रे - सिट्रस ग्रीनिंग', 'hi': 'संतरा - सिट्रस ग्रीनिंग', 'en': 'Orange Haunglongbing (Citrus Greening)'},
    'citrus greening': {'mr': 'सिट्रस ग्रीनिंग', 'hi': 'सिट्रस ग्रीनिंग', 'en': 'Citrus Greening'},

    # Peach Diseases
    'peach healthy': {'mr': 'पीच - निरोगी', 'hi': 'आड़ू - स्वस्थ', 'en': 'Peach Healthy'},
    'peach bacterial spot': {'mr': 'पीच - जिवाणूजन्य डाग', 'hi': 'आड़ू - जीवाणु धब्बा', 'en': 'Peach Bacterial Spot'},

    # Blueberry, Cherry, Raspberry, Soybean, Squash, Strawberry
    'blueberry healthy': {'mr': 'ब्लूबेरी - निरोगी', 'hi': 'ब्लूबेरी - स्वस्थ', 'en': 'Blueberry Healthy'},
    'cherry healthy': {'mr': 'चेरी - निरोगी', 'hi': 'चेरी - स्वस्थ', 'en': 'Cherry Healthy'},
    'cherry powdery mildew': {'mr': 'चेरी - भुरी रोग', 'hi': 'चेरी - चूर्णिल फफूंद', 'en': 'Cherry Powdery Mildew'},
    'raspberry healthy': {'mr': 'रासबेरी - निरोगी', 'hi': 'रास्पबेरी - स्वस्थ', 'en': 'Raspberry Healthy'},
    'soybean healthy': {'mr': 'सोयाबीन - निरोगी', 'hi': 'सोयाबीन - स्वस्थ', 'en': 'Soybean Healthy'},
    'squash powdery mildew': {'mr': 'भोपळा - भुरी रोग', 'hi': 'कद्दू - चूर्णिल फफूंद', 'en': 'Squash Powdery Mildew'},
    'powdery mildew': {'mr': 'भुरी रोग', 'hi': 'चूर्णिल फफूंद', 'en': 'Powdery Mildew'},
    'strawberry healthy': {'mr': 'स्ट्रॉबेरी - निरोगी', 'hi': 'स्ट्रॉबेरी - स्वस्थ', 'en': 'Strawberry Healthy'},
    'strawberry leaf scorch': {'mr': 'स्ट्रॉबेरी - पान करपा', 'hi': 'स्ट्रॉबेरी - पत्ती झुलसा', 'en': 'Strawberry Leaf Scorch'},

    # Generic
    'crop pathology': {'mr': 'पिकाचा रोग', 'hi': 'फसल रोग', 'en': 'Crop Pathology'},
    'crop pathology identified': {'mr': 'पिकाचा रोग आढळला', 'hi': 'फसल रोग पाया गया', 'en': 'Crop Pathology Identified'},
    'healthy': {'mr': 'निरोगी', 'hi': 'स्वस्थ', 'en': 'Healthy'},
    'disease detected': {'mr': 'रोग आढळला', 'hi': 'रोग पाया गया', 'en': 'Disease Detected'}
}

# =====================================================================
# DYNAMIC CATEGORY TRANSLATION MAP
# =====================================================================
CATEGORY_MAP = {
    'fungal': {'mr': 'बुरशीजन्य रोग', 'hi': 'फफूंदजन्य रोग', 'en': 'Fungal'},
    'bacterial': {'mr': 'जिवाणूजन्य रोग', 'hi': 'जीवाणुजन्य रोग', 'en': 'Bacterial'},
    'viral': {'mr': 'विषाणूजन्य रोग', 'hi': 'विषाणुजन्य रोग', 'en': 'Viral'},
    'pest': {'mr': 'कीड / कीटक प्रादुर्भाव', 'hi': 'कीट प्रकोप', 'en': 'Pest'},
    'nutrient': {'mr': 'अन्नद्रव्यांची कमतरता', 'hi': 'पोषक तत्वों की कमी', 'en': 'Nutrient'},
    'environmental': {'mr': 'वातावरणाचा ताण', 'hi': 'वातावरणीय तनाव', 'en': 'Environmental'},
    'healthy': {'mr': 'निरोगी पीक', 'hi': 'स्वस्थ फसल', 'en': 'Healthy'},
    'general crop disease': {'mr': 'सामान्य पीक रोग', 'hi': 'सामान्य फसल रोग', 'en': 'General Crop Disease'}
}

# =====================================================================
# DYNAMIC HEALTH STATUS TRANSLATION MAP
# =====================================================================
HEALTH_STATUS_MAP = {
    'healthy': {'mr': 'निरोगी', 'hi': 'स्वस्थ', 'en': 'Healthy'},
    'diseased': {'mr': 'रोगग्रस्त', 'hi': 'रोगग्रस्त', 'en': 'Diseased'},
    'possibly_diseased': {'mr': 'संभाव्य रोगग्रस्त', 'hi': 'संभावित रोगग्रस्त', 'en': 'Possibly Diseased'},
    'pest_damage': {'mr': 'किडीचा प्रादुर्भाव', 'hi': 'कीट प्रकोप', 'en': 'Pest Damage'},
    'nutrient_deficiency': {'mr': 'अन्नद्रव्यांची कमतरता', 'hi': 'पोषक तत्वों की कमी', 'en': 'Nutrient Deficiency'},
    'environmental_stress': {'mr': 'वातावरणाचा ताण', 'hi': 'वातावरणीय तनाव', 'en': 'Environmental Stress'},
    'unknown': {'mr': 'अज्ञात स्थिती', 'hi': 'अज्ञात स्थिति', 'en': 'Unknown'}
}

# =====================================================================
# DYNAMIC SEVERITY TRANSLATION MAP
# =====================================================================
SEVERITY_MAP = {
    'healthy': {'mr': 'निरोगी', 'hi': 'स्वस्थ', 'en': 'Healthy'},
    'healthy leaf': {'mr': 'निरोगी पान', 'hi': 'स्वस्थ पत्ती', 'en': 'Healthy Leaf'},
    'very early': {'mr': 'अतिशय सुरुवातीचा टप्पा', 'hi': 'अत्यंत प्रारंभिक चरण', 'en': 'Very Early'},
    'early': {'mr': 'सुरुवातीचा टप्पा', 'hi': 'प्रारंभिक चरण', 'en': 'Early'},
    'early stage': {'mr': 'सुरुवातीचा टप्पा', 'hi': 'प्रारंभिक चरण', 'en': 'Early Stage'},
    'moderate': {'mr': 'मध्यम टप्पा', 'hi': 'मध्यम चरण', 'en': 'Moderate'},
    'moderate stage': {'mr': 'मध्यम टप्पा', 'hi': 'मध्यम चरण', 'en': 'Moderate Stage'},
    'developing': {'mr': 'वाढणारा टप्पा', 'hi': 'विकासशील चरण', 'en': 'Developing'},
    'advanced': {'mr': 'प्रगत टप्पा', 'hi': 'उन्नत चरण', 'en': 'Advanced'},
    'advanced stage': {'mr': 'प्रगत टप्पा', 'hi': 'उन्नत चरण', 'en': 'Advanced Stage'},
    'severe': {'mr': 'गंभीर टप्पा', 'hi': 'गंभीर चरण', 'en': 'Severe'},
    'severe stage': {'mr': 'गंभीर टप्पा', 'hi': 'गंभीर चरण', 'en': 'Severe Stage'},
    'critical': {'mr': 'अत्यंत गंभीर', 'hi': 'अत्यंत गंभीर', 'en': 'Critical'},
    'unknown': {'mr': 'अज्ञात तीव्रता', 'hi': 'अज्ञात गंभीरता', 'en': 'Unknown'}
}

# =====================================================================
# DYNAMIC URGENCY TRANSLATION MAP
# =====================================================================
URGENCY_MAP = {
    'critical': {'mr': 'अत्यंत गंभीर', 'hi': 'अत्यंत गंभीर', 'en': 'Critical'},
    'high': {'mr': 'उच्च तातडी', 'hi': 'उच्च प्राथमिकता', 'en': 'High'},
    'moderate': {'mr': 'मध्यम', 'hi': 'मध्यम', 'en': 'Moderate'},
    'low': {'mr': 'कमी / सामान्य', 'hi': 'सामान्य / कम', 'en': 'Low'},
    'unknown': {'mr': 'अज्ञात', 'hi': 'अज्ञात', 'en': 'Unknown'}
}

# =====================================================================
# DYNAMIC CONFIDENCE LEVEL TRANSLATION MAP
# =====================================================================
CONFIDENCE_LEVEL_MAP = {
    'very high': {'mr': 'अत्यंत उच्च', 'hi': 'अत्यंत उच्च', 'en': 'Very High'},
    'high': {'mr': 'उच्च', 'hi': 'उच्च', 'en': 'High'},
    'moderate': {'mr': 'मध्यम', 'hi': 'मध्यम', 'en': 'Moderate'},
    'low': {'mr': 'कमी', 'hi': 'कम', 'en': 'Low'},
    'medium': {'mr': 'मध्यम', 'hi': 'मध्यम', 'en': 'Medium'}
}

# =====================================================================
# COMPREHENSIVE AGRICULTURAL PHRASE TRANSLATIONS (MR / HI / EN)
# =====================================================================
PHRASE_TRANSLATIONS = {
    # Severity reasons & assessments
    'visible foliage pathology observed.': {
        'mr': 'पानांवर दृश्य रोगाची लक्षणे व डाग स्पष्टपणे दिसत आहेत.',
        'hi': 'पत्तियों पर रोग के दृश्य लक्षण एवं धब्बे स्पष्ट रूप से दिखाई दे रहे हैं.',
        'en': 'Visible foliage pathology observed.'
    },
    'visible foliage pathology observed': {
        'mr': 'पानांवर दृश्य रोगाची लक्षणे व डाग स्पष्टपणे दिसत आहेत.',
        'hi': 'पत्तियों पर रोग के दृश्य लक्षण एवं धब्बे स्पष्ट रूप से दिखाई दे रहे हैं.',
        'en': 'Visible foliage pathology observed.'
    },
    'no disease symptoms observed - leaf appears healthy and vigorous': {
        'mr': 'कोणतीही रोग लक्षणे आढळली नाहीत - पान निरोगी व सशक्त दिसत आहे.',
        'hi': 'कोई रोग लक्षण नहीं दिखे - पत्ता स्वस्थ और मजबूत दिखाई देता है.',
        'en': 'No disease symptoms observed - leaf appears healthy and vigorous'
    },
    'no disease symptoms observed - leaf appears healthy and vigorous.': {
        'mr': 'कोणतीही रोग लक्षणे आढळली नाहीत - पान निरोगी व सशक्त दिसत आहे.',
        'hi': 'कोई रोग लक्षण नहीं दिखे - पत्ता स्वस्थ और मजबूत दिखाई देता है.',
        'en': 'No disease symptoms observed - leaf appears healthy and vigorous.'
    },
    'leaf appears healthy with no visible lesions': {
        'mr': 'कोणतेही डाग नसून पान पूर्णपणे निरोगी दिसत आहे.',
        'hi': 'बिना किसी धब्बे के पत्ती पूरी तरह स्वस्थ दिखाई दे रही है.',
        'en': 'Leaf appears healthy with no visible lesions'
    },

    # Immediate actions
    'prune and dispose of infected leaves.': {
        'mr': 'रोगट पाने कापून शेतातून दूर नष्ट करा.',
        'hi': 'संक्रमित पत्तियों को काटकर खेत से दूर नष्ट करें.',
        'en': 'Prune and dispose of infected leaves.'
    },
    'prune and dispose of infected leaves': {
        'mr': 'रोगट पाने कापून शेतातून दूर नष्ट करा.',
        'hi': 'संक्रमित पत्तियों को काटकर खेत से दूर नष्ट करें.',
        'en': 'Prune and dispose of infected leaves.'
    },
    'apply copper-based organic bio-fungicide.': {
        'mr': 'तांबायुक्त सेंद्रिय बुरशीनाशकाची (कॉपर) फवारणी करा.',
        'hi': 'कॉपर युक्त जैविक कवकनाशी का छिड़काव करें.',
        'en': 'Apply copper-based organic bio-fungicide.'
    },
    'apply copper-based organic bio-fungicide': {
        'mr': 'तांबायुक्त सेंद्रिय बुरशीनाशकाची (कॉपर) फवारणी करा.',
        'hi': 'कॉपर युक्त जैविक कवकनाशी का छिड़काव करें.',
        'en': 'Apply copper-based organic bio-fungicide.'
    },
    'avoid overhead foliar sprinkler irrigation.': {
        'mr': 'तुषार सिंचन टाळा आणि झाडांच्या मुळाशी पाणी द्या.',
        'hi': 'फव्वारा सिंचाई से बचें और पौधों की जड़ों में पानी दें.',
        'en': 'Avoid overhead foliar sprinkler irrigation.'
    },
    'avoid overhead foliar sprinkler irrigation': {
        'mr': 'तुषार सिंचन टाळा आणि झाडांच्या मुळाशी पाणी द्या.',
        'hi': 'फव्वारा सिंचाई से बचें और पौधों की जड़ों में पानी दें.',
        'en': 'Avoid overhead foliar sprinkler irrigation.'
    },
    'inspect nearby crop rows for chlorosis.': {
        'mr': 'लगतच्या ओळींमधील झाडांवर पिवळेपणा किंवा डाग तपासा.',
        'hi': 'पास की पंक्तियों के पौधों पर पीलापन या धब्बे जांचें.',
        'en': 'Inspect nearby crop rows for chlorosis.'
    },
    'inspect nearby crop rows for chlorosis': {
        'mr': 'लगतच्या ओळींमधील झाडांवर पिवळेपणा किंवा डाग तपासा.',
        'hi': 'पास की पंक्तियों के पौधों पर पीलापन या धब्बे जांचें.',
        'en': 'Inspect nearby crop rows for chlorosis.'
    },
    'check surrounding leaves and plants in the same crop row for similar visible spot lesions or chlorosis.': {
        'mr': 'त्याच ओळीतील लगतच्या झाडांवर व पानांवर असे डाग किंवा पिवळेपणा आला आहे का ते तपासा.',
        'hi': 'उसी पंक्ति के आस-पास के पौधों और पत्तियों पर ऐसे धब्बे या पीलापन जांचें.',
        'en': 'Check surrounding leaves and plants in the same crop row for similar visible spot lesions or chlorosis.'
    },
    'observe whether spot lesions, concentric ring marks, or foliage discoloration expand over the next 24 to 48 hours.': {
        'mr': 'पुढील २४ ते ४८ तासांत डाग किंवा पिवळेपणा वाढत आहे का याचे निरीक्षण करा.',
        'hi': 'अगले २४ से ४८ घंटों में देखें कि धब्बे या पीलापन और बढ़ तो नहीं रहा.',
        'en': 'Observe whether spot lesions, concentric ring marks, or foliage discoloration expand over the next 24 to 48 hours.'
    },
    'remove heavily diseased lower foliage, avoid overhead foliar irrigation, and apply copper-based organic bio-fungicides if appropriate.': {
        'mr': 'जास्त बाधित पाने काढून नष्ट करा, तुषार सिंचन टाळा आणि तांबायुक्त सेंद्रिय बुरशीनाशक वापरा.',
        'hi': 'अधिक संक्रमित निचली पत्तियां हटा दें, फव्वारा सिंचाई से बचें और कॉपर युक्त जैविक कवकनाशी का प्रयोग करें.',
        'en': 'Remove heavily diseased lower foliage, avoid overhead foliar irrigation, and apply copper-based organic bio-fungicides if appropriate.'
    },
    'consult an agricultural extension officer or agronomist if symptoms spread rapidly or severe defoliation occurs.': {
        'mr': 'लक्षणे वेगाने पसरत असल्यास किंवा पाने गळत असल्यास जवळच्या कृषी विस्तार अधिकाऱ्यांशी संपर्क साधा.',
        'hi': 'यदि लक्षण तेजी से फैल रहे हों या पत्ते झड़ रहे हों तो नजदीकी कृषि प्रसार अधिकारी से संपर्क करें.',
        'en': 'Consult an agricultural extension officer or agronomist if symptoms spread rapidly or severe defoliation occurs.'
    },

    # Treatments
    'apply mancozeb or chlorothalonil fungicide.': {
        'mr': 'मॅनकोझेब किंवा क्लोरोथॅलोनील बुरशीनाशकाची फवारणी करा.',
        'hi': 'मैनकोजेब या क्लोरोथैलोनिल कवकनाशी का छिड़काव करें.',
        'en': 'Apply Mancozeb or Chlorothalonil fungicide.'
    },
    'apply chlorothalonil according to package safety instructions.': {
        'mr': 'पाकिटावरील सुरक्षा सूचनांनुसार क्लोरोथॅलोनीलची फवारणी करा.',
        'hi': 'पैकेट पर दिए सुरक्षा निर्देशों के अनुसार क्लोरोथैलोनिल का छिड़काव करें.',
        'en': 'Apply Chlorothalonil according to package safety instructions.'
    },
    'apply neem oil spray (0.5%) or bacillus subtilis bio-fungicide.': {
        'mr': 'कडुलिंबाचे तेल (०.५%) किंवा बॅसिलस सबटिलिस जैविक बुरशीनाशक फवारा.',
        'hi': 'नीम का तेल (०.५%) या बैसिलस सबटिलिस जैविक कवकनाशी का छिड़काव करें.',
        'en': 'Apply neem oil spray (0.5%) or Bacillus subtilis bio-fungicide.'
    },
    'spray neem oil extract (0.5-1%) or botanical bio-pesticide every 7-10 days': {
        'mr': 'कडुलिंबाचे तेल (०.५-१%) किंवा जैविक कीटकनाशक दर ७-१० दिवसांनी फवारा.',
        'hi': 'नीम का तेल (०.५-१%) या जैविक कीटनाशक हर ७-१० दिन में छिड़कें.',
        'en': 'Spray neem oil extract (0.5-1%) or botanical bio-pesticide every 7-10 days'
    },
    'apply trichoderma viride or pseudomonas fluorescens as bio-fungicide foliar spray': {
        'mr': 'ट्रायकोडर्मा विरिडी किंवा स्यूडोमोनास फ्लुओरेसेन्सची जैविक फवारणी करा.',
        'hi': 'ट्राइकोडर्मा विरिडी या स्यूडोमोनास फ्लोरेसेंस का जैविक छिड़काव करें.',
        'en': 'Apply Trichoderma viride or Pseudomonas fluorescens as bio-fungicide foliar spray'
    },
    'apply protective fungicide containing chlorothalonil, mancozeb, or copper hydroxide according to label': {
        'mr': 'लेबलच्या निर्देशानुसार मॅनकोझेब, कॉपर किंवा क्लोरोथॅलोनीलची फवारणी करा.',
        'hi': 'लेबल निर्देशों के अनुसार मैनकोजेब, कॉपर या क्लोरोथैलोनिल का छिड़काव करें.',
        'en': 'Apply protective fungicide containing Chlorothalonil, Mancozeb, or Copper Hydroxide according to label'
    },
    'for active expanding infections, apply systemic fungicides such as azoxystrobin, difenoconazole, or boscalid': {
        'mr': 'वाढणाऱ्या रोगासाठी अझोक्सीस्ट्रोबिन किंवा डायफेनोकोनाझोल आंतरप्रवाही बुरशीनाशक वापरा.',
        'hi': 'फैलते संक्रमण के लिए एज़ोक्सीस्ट्रोबिन या डाइफेनोकोनाज़ोल कवकनाशी का प्रयोग करें.',
        'en': 'For active expanding infections, apply systemic fungicides such as Azoxystrobin, Difenoconazole, or Boscalid'
    },

    # Nutrient Guidance
    'maintain standard good agricultural practices.': {
        'mr': 'चांगल्या कृषी पद्धतींचे नियमित पालन करा.',
        'hi': 'उत्कृष्ट कृषि पद्धतियों का नियमित पालन करें.',
        'en': 'Maintain standard good agricultural practices.'
    },
    'ensure balanced nitrogen and adequate potassium.': {
        'mr': 'योग्य प्रमाणात नत्र आणि पुरेसे पालाश (पोटॅश) द्या.',
        'hi': 'संतुलित नाइट्रोजन और पर्याप्त पोटाश प्रदान करें.',
        'en': 'Ensure balanced nitrogen and adequate potassium.'
    },
    'apply well-decomposed organic compost or farmyard manure (fym)': {
        'mr': 'चांगले कुजलेले शेणखत किंवा गांडूळ खत जमिनीत मिसळा.',
        'hi': 'अच्छी सड़ी हुई गोबर की खाद या केंचुआ खाद मिट्टी में मिलाएं.',
        'en': 'Apply well-decomposed organic compost or farmyard manure (FYM)'
    },
    'apply balanced n-p-k fertilizer based on soil test': {
        'mr': 'माती परीक्षणानुसार संतुलित एन-पी-के (N-P-K) खतांचा वापर करा.',
        'hi': 'मिट्टी परीक्षण के आधार पर संतुलित एन-पी-के (N-P-K) खाद का प्रयोग करें.',
        'en': 'Apply balanced N-P-K fertilizer based on soil test'
    },
    'apply organic vermicompost and foliar seaweed extract': {
        'mr': 'गांडूळ खत आणि समुद्री शैवाल अर्काची फवारणी करा.',
        'hi': 'केंचुआ खाद और समुद्री शैवाल अर्क का छिड़काव करें.',
        'en': 'Apply organic vermicompost and foliar seaweed extract'
    },
    'apply balanced 19:19:19 water-soluble foliar spray': {
        'mr': '१९:१९:१९ विद्राव्य खताची फवारणी करा.',
        'hi': '१९:१९:१९ घुलनशील खाद का पर्णीय छिड़काव करें.',
        'en': 'Apply balanced 19:19:19 water-soluble foliar spray'
    },

    # Symptoms
    'target concentric spot lesions on lower leaves': {
        'mr': 'खालच्या पानांवर गोलाकार वलय असलेले करपा डाग',
        'hi': 'निचली पत्तियों पर गोल छल्लों वाले झुलसा धब्बे',
        'en': 'Target concentric spot lesions on lower leaves'
    },
    'concentric dark brown rings on lower foliage (target spot lesions)': {
        'mr': 'खालच्या पानांवर गडद तपकिरी वर्तुळाकार वलय (टार्गेट स्पॉट डाग)',
        'hi': 'निचली पत्तियों पर गहरे भूरे गोल छल्ले (टारगेट स्पॉट धब्बे)',
        'en': 'Concentric dark brown rings on lower foliage (target spot lesions)'
    },
    'chlorosis halo surrounding necrotic lesions': {
        'mr': 'वाळलेल्या डागांभोवती पिवळसर वलय (क्लोरोसिस)',
        'hi': 'सूखे धब्बों के चारों ओर पीला छल्ला (क्लोरोसिस)',
        'en': 'Chlorosis halo surrounding necrotic lesions'
    },
    'lower leaf yellowing and premature defoliation': {
        'mr': 'खालची पाने पिवळी पडून वेळेआधी गळणे',
        'hi': 'निचली पत्तियों का पीला पड़ना और समय से पहले गिरना',
        'en': 'Lower leaf yellowing and premature defoliation'
    },

    # Causes
    'fungal spore propagation in humid conditions': {
        'mr': 'दमट व उबदार हवामानात बुरशीच्या बीजाणूंचा प्रसार',
        'hi': 'नमी और गर्म मौसम में फफूंद बीजाणुओं का फैलाव',
        'en': 'Fungal spore propagation in humid conditions'
    },
    'alternaria solani fungal infection favored by warm, humid weather (24-29°c)': {
        'mr': 'उबदार व दमट हवामानामुळे अल्टरनेरिया सोलानी बुरशीचा प्रादुर्भाव (२४-२९°C)',
        'hi': 'गर्म और नम मौसम के कारण अल्टरनेरिया सोलानी कवक संक्रमण (२४-२९°C)',
        'en': 'Alternaria solani fungal infection favored by warm, humid weather (24-29°C)'
    },
    'overhead irrigation or rainfall splashing spores from soil onto lower leaves': {
        'mr': 'पावसामुळे किंवा तुषार सिंचनामुळे मातीतील बुरशी पानांवर उडणे',
        'hi': 'बारिश या फव्वारा सिंचाई से मिट्टी के कवक छींटों द्वारा पत्तियों पर पहुंचना',
        'en': 'Overhead irrigation or rainfall splashing spores from soil onto lower leaves'
    },
    'dense canopy reducing air circulation and prolonging leaf wetness': {
        'mr': 'दाट झाडांमुळे हवा न खेळणे आणि पानांवर जास्त वेळ ओलावा राहणे',
        'hi': 'घने पौधों के कारण हवा का प्रवाह रुकना और पत्तियों पर देर तक नमी रहना',
        'en': 'Dense canopy reducing air circulation and prolonging leaf wetness'
    },

    # Pest Analysis
    'spider mites or thrips not detected': {
        'mr': 'लाल कोळी किंवा थ्रिप्स किडीचा प्रादुर्भाव दिसत नाही',
        'hi': 'लाल मकड़ी या थ्रिप्स कीट का प्रकोप नहीं दिख रहा है',
        'en': 'Spider mites or thrips not detected'
    },
    'no active pest damage or insect activity visible on foliage.': {
        'mr': 'पानावर कोणताही कीटक प्रादुर्भाव किंवा नुकसान दिसत नाही.',
        'hi': 'पत्ती पर किसी सक्रिय कीट या कीड़े का नुकसान नहीं दिख रहा है.',
        'en': 'No active pest damage or insect activity visible on foliage.'
    },

    # Environmental stress
    'high humidity or wet foliage stress': {
        'mr': 'हवेतील अति आर्द्रता आणि पानांवरील सततचा ओलावा',
        'hi': 'अत्यधिक नमी और पत्तियों पर निरंतर गीलापन',
        'en': 'High humidity or wet foliage stress'
    },
    'no severe environmental stress visible.': {
        'mr': 'वातावरणाचा कोणताही गंभीर ताण दिसत नाही.',
        'hi': 'कोई गंभीर वातावरणीय तनाव दिखाई नहीं देता.',
        'en': 'No severe environmental stress visible.'
    },

    # Prevention
    'rotate crops with non-solanaceous species': {
        'mr': 'टोमॅटो/बटाटा व्यतिरिक्त इतर पिकांची फेरपालट करा',
        'hi': 'टमाटर/आलू के अलावा अन्य फसलों की हेर-फेर करें',
        'en': 'Rotate crops with non-solanaceous species'
    },
    'practice 2-3 year crop rotation with non-host crops': {
        'mr': '२-३ वर्षे इतर कुळातील पिकांची फेरपालट करा',
        'hi': '२-३ साल अन्य गैर-पोषक फसलों की हेर-फेर करें',
        'en': 'Practice 2-3 year crop rotation with non-host crops'
    },
    'ensure proper plant spacing for air circulation': {
        'mr': 'हवा खेळती राहण्यासाठी झाडांमध्ये योग्य अंतर ठेवा',
        'hi': 'हवा के आवागमन के लिए पौधों के बीच उचित दूरी रखें',
        'en': 'Ensure proper plant spacing for air circulation'
    },
    'water at the soil base using drip irrigation': {
        'mr': 'ठिबक सिंचनाचा वापर करून थेट मुळाशी पाणी द्या',
        'hi': 'ड्रिप सिंचाई द्वारा सीधे पौधों की जड़ों में पानी दें',
        'en': 'Water at the soil base using drip irrigation'
    },
    'apply organic mulch around plant bases to prevent soil splashing': {
        'mr': 'माती उडणे रोखण्यासाठी झाडांच्या बुंध्याभोवती आच्छादन (मल्चिंग) करा',
        'hi': 'मिट्टी के छींटों को रोकने के लिए पौधों के चारों ओर मल्चिंग करें',
        'en': 'Apply organic mulch around plant bases to prevent soil splashing'
    },

    # Limitations
    'agrivision ai provides ai-assisted preliminary crop health information based on visible symptoms.': {
        'mr': 'एग्रीव्हिजन एआय दृश्य लक्षणांवर आधारित प्राथमिक माहिती प्रदान करते. अंतिम निदानासाठी कृषी तज्ज्ञांचा सल्ला घ्या.',
        'hi': 'एग्रीविज़न एआई दृश्य लक्षणों पर आधारित प्राथमिक जानकारी प्रदान करता है. अंतिम पुष्टि के लिए कृषि विशेषज्ञ की सलाह लें.',
        'en': 'AgriVision AI provides AI-assisted preliminary crop health information based on visible symptoms.'
    },
    'agrivision ai provides ai-assisted preliminary crop-health information based on visible symptoms. results may be inaccurate and should not replace laboratory diagnosis or advice from a qualified agricultural professional. always follow locally approved agricultural product labels and recommendations.': {
        'mr': 'एग्रीव्हिजन एआय दृश्य लक्षणांवर आधारित प्राथमिक माहिती प्रदान करते. अंतिम प्रमाणीकरणासाठी व औषध फवारणीच्या योग्य प्रमाणासाठी स्थानिक कृषी तज्ज्ञांचा किंवा कृषी विद्यापीठाचा सल्ला घ्या. औषध फवारताना पाकिटावरील सूचनांचे काटेकोर पालन करा.',
        'hi': 'एग्रीविज़न एआई दृश्य लक्षणों पर आधारित प्राथमिक जानकारी प्रदान करता है। अंतिम पुष्टि एवं दवा छिड़काव की सटीक मात्रा के लिए स्थानीय कृषि विशेषज्ञ या अनुसंधान केंद्र से सलाह लें। हमेशा स्थानीय रूप से स्वीकृत कृषि उत्पाद लेबल के निर्देशों का पालन करें।',
        'en': 'AgriVision AI provides AI-assisted preliminary crop-health information based on visible symptoms. Results may be inaccurate and should not replace laboratory diagnosis or advice from a qualified agricultural professional. Always follow locally approved agricultural product labels and recommendations.'
    }
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
    """Comprehensive text and phrase translator for agricultural recommendations, causes, and symptoms."""
    if not text:
        return text
    lang_code = (lang or 'en').lower()
    if lang_code == 'en':
        return text
    
    norm = str(text).strip()
    norm_lower = norm.lower()

    # 1. Exact or lowercase match in PHRASE_TRANSLATIONS
    if norm_lower in PHRASE_TRANSLATIONS:
        return PHRASE_TRANSLATIONS[norm_lower].get(lang_code, text)

    # 2. Match in TRANSLATIONS dictionary values
    for dict_key, trans_val in TRANSLATIONS.get('en', {}).items():
        if str(trans_val).strip().lower() == norm_lower:
            return TRANSLATIONS.get(lang_code, {}).get(dict_key, text)

    # 3. Partial / substring matches in PHRASE_TRANSLATIONS
    for phrase_key, phrase_data in PHRASE_TRANSLATIONS.items():
        if phrase_key in norm_lower or norm_lower in phrase_key:
            return phrase_data.get(lang_code, text)

    # 4. Check disease / crop / status maps
    if norm_lower in DISEASE_NAME_MAP:
        return DISEASE_NAME_MAP[norm_lower].get(lang_code, text)
    if norm_lower in CROP_NAME_MAP:
        return CROP_NAME_MAP[norm_lower].get(lang_code, text)
    if norm_lower in CATEGORY_MAP:
        return CATEGORY_MAP[norm_lower].get(lang_code, text)
    if norm_lower in HEALTH_STATUS_MAP:
        return HEALTH_STATUS_MAP[norm_lower].get(lang_code, text)
    if norm_lower in SEVERITY_MAP:
        return SEVERITY_MAP[norm_lower].get(lang_code, text)
    if norm_lower in URGENCY_MAP:
        return URGENCY_MAP[norm_lower].get(lang_code, text)

    return text
