"""
AgriVision AI - Multilingual Internationalization (i18n) Module
Supports English (en), Marathi (mr), and Hindi (hi).
"""

TRANSLATIONS = {
    'en': {
        # Navigation & Global
        'app_name': 'AgriVision AI',
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
        
        # Hero & Home
        'hero_badge': '🤖 Google Gemini Vision AI & Interactive 3D XAI',
        'hero_title_1': 'Detect Crop Diseases Early with ',
        'hero_title_2': 'AI',
        'hero_subtitle': 'Upload a crop leaf image and let AgriVision AI identify possible diseases, explain visible foliage symptoms, estimate disease severity, and provide structured crop management guidance.',
        'btn_analyze_leaf': '🔍 Analyze a Leaf',
        'trust_realtime_ai': '✓ Real-Time Vision AI',
        'trust_explainable': '✓ Explainable AI Guidance',
        'trust_solutions': '✓ Organic & Chemical Solutions',
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
        'workflow_cta_title': 'Ready to check your crop?',
        'workflow_cta_desc': 'Get instant diagnostic results and organic management protocols.',
        'workflow_cta_btn': 'Analyze a Crop Leaf →',
        
        # Upload Portal (/detect)
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
        'supported_formats': 'Supported formats: JPG, JPEG, PNG, WEBP (Max 10MB)',
        'quick_test_leaves': 'Quick Test Sample Leaves:',
        'btn_start_analysis': '🔬 Analyze Crop Image',
        'analyzing_img': 'Analyzing your crop image…',
        'processing_msg': 'Processing image...',
        'analyzing_symptoms': 'Analyzing visible symptoms...',
        'identifying_disease': 'Identifying possible disease...',
        'preparing_guidance': 'Preparing recommendations...',

        
        # Result Page (/gemini-result & /result)
        'report_title': 'AI Crop Health Analysis Report',
        'crop_heading': 'Crop Details',
        'condition_heading': 'Primary Condition',
        'confidence_heading': 'AI Confidence',
        'health_heading': 'Health Status',
        'action_urgency': 'Action Urgency',
        'action_now_title': 'What Should I Do Now?',
        'action_urgent_title': 'Action Urgency',
        'monitor_signs_title': 'Monitor For Warning Signs',
        'expert_help_title': 'When to Seek Expert Help',
        'organic_mgmt_title': 'Organic Management Options',
        'chemical_mgmt_title': 'Chemical Management Guidelines',
        'fertilizer_title': 'Nutrient & Soil Guidance',
        'preventive_title': 'Preventive Practices & Crop Rotation',
        'disclaimer_notice': '📢 Notice: AgriVision AI provides diagnostic assistance based on visual evidence. Consult local agricultural authorities for certified field confirmation.',
        
        # History Page (/history)
        'history_title': 'Prediction History Logs',
        'history_subtitle': 'View past crop diagnostic records, severity scores, and visual heatmaps.',
        'col_date': 'Date & Time',
        'col_image': 'Leaf Preview',
        'col_crop': 'Crop',
        'col_condition': 'Condition Identified',
        'col_confidence': 'Confidence',
        'col_severity': 'Severity',
        'col_actions': 'Actions',
        'view_report': 'View Report',
        'delete_record': 'Delete',
        'empty_history': 'No prediction records found in your history yet.',
        
        # About Page (/about)
        'about_title': 'About AgriVision AI',
        'about_subtitle': 'Empowering farmers and agricultural extension agents with explainable AI diagnostic intelligence.',
        'our_mission': 'Our Mission',
        'how_ai_helps': 'How AI Helps Agriculture',
        
        # Contact Page (/contact)
        'contact_title': 'Contact & Feedback',
        'contact_subtitle': 'Have questions, feedback, or feature requests for AgriVision AI? We would love to hear from you.',
        'form_name': 'Your Name',
        'form_email': 'Email Address',
        'form_message': 'Message',
        'send_btn': 'Send Message',
        
        # Footer
        'footer_tagline': 'AI-Powered Precision Crop Health Diagnostics & Explainable Agricultural Guidance.',
        'footer_rights': 'All rights reserved. Designed for explainable precision agriculture.'
    },
    'mr': {
        # Navigation & Global
        'app_name': 'एग्रीव्हिजन एआय',
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
        
        # Hero & Home
        'hero_badge': '🤖 गूगल जेमिनी व्हिजन एआय व एक्सएआय निदाने',
        'hero_title_1': 'एआय तंत्रज्ञानाने पिकांचे रोगांपासून ',
        'hero_title_2': 'रक्षण',
        'hero_subtitle': 'तुमच्या पिकाच्या पानाचा फोटो अपलोड करा आणि एआय द्वारे रोगाची अचूक ओळख, दिसणाऱ्या लक्षणांचे स्पष्टीकरण आणि सेंद्रिय व रासायनिक उपचार उपाय मिळवा.',
        'btn_analyze_leaf': '🔍 पिकाचे पान तपासा',
        'trust_realtime_ai': '✓ रीअल-टाइम व्हिजन एआय',
        'trust_explainable': '✓ सुलभ एआय मार्गदर्शन',
        'trust_solutions': '✓ सेंद्रिय व रासायनिक उपाय',
        'how_title': 'एग्रीव्हिजन एआय कसे कार्य करते',
        'how_subtitle': 'छायाचित्र घेण्यापासून ते पीक सुरक्षेच्या प्रत्यक्ष उपायांपर्यंत, एग्रीव्हिजन एआय पिकाचे सोप्या व सुलभ भाषेत आरोग्य विश्लेषण प्रदान करते.',
        'step_01_title': 'पिकाचे छायाचित्र अपलोड करा',
        'step_01_desc': 'बाधित पानाचे स्पष्ट छायाचित्र घ्या किंवा स्मार्टफोन अथवा संगणकावरून अपलोड करा.',
        'step_02_title': 'एआय पानाचे परीक्षण करते',
        'step_02_desc': 'एआय मॉडेल पिकाच्या पानातील डाग, पिवळेपणा, कर्पा आणि रचनेचे सखोल विश्लेषण करते.',
        'step_03_title': 'संभाव्य रोग ओळखा',
        'step_03_desc': 'प्रशिक्षित एआय प्रणाली रोगाची अचूक ओळख, विश्वास पातळी आणि तीव्रतेची श्रेणी निश्चित करते.',
        'step_04_title': 'पीक काळजी मार्गदर्शन मिळवा',
        'step_04_desc': 'शेतकऱ्यांसाठी प्रत्यक्ष कृती आराखडा, सेंद्रिय उपाय, रासायनिक फवारणी व खत व्यवस्थापन मार्गदर्शन मिळवा.',
        'workflow_cta_title': 'तुमच्या पिकाची तपासणी करण्यास तयार आहात?',
        'workflow_cta_desc': 'त्वरित रोग निदान आणि सेंद्रिय व्यवस्थापन उपाय मिळवा.',
        'workflow_cta_btn': 'पिकाचे पान तपासा →',
        
        # Upload Portal (/detect)
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
        'supported_formats': 'समर्थित फॉरमॅट: JPG, JPEG, PNG, WEBP (कमाल १० MB)',
        'quick_test_leaves': 'त्वरित चाचणीसाठी नमुना पाने:',
        'btn_start_analysis': '🔬 पिकाचे विश्लेषण करा',
        'analyzing_img': 'तुमच्या पिकाच्या पानाचे विश्लेषण सुरू आहे…',
        'processing_msg': 'छायाचित्र प्रक्रिया सुरू आहे...',
        'analyzing_symptoms': 'दिसणाऱ्या लक्षणांचे विश्लेषण सुरू आहे...',
        'identifying_disease': 'संभाव्य रोग ओळखला जात आहे...',
        'preparing_guidance': 'शिफारसी तयार केल्या जात आहेत...',

        
        # Result Page (/gemini-result & /result)
        'report_title': 'एआय पीक आरोग्य निदान अहवाल',
        'crop_heading': 'पिकाचा तपशील',
        'condition_heading': 'आढळलेला रोग',
        'confidence_heading': 'विश्वास पातळी (Confidence)',
        'health_heading': 'आरोग्य स्थिती',
        'action_urgency': 'कृतीची तातडी',
        'action_now_title': 'मी आता प्रथम काय करावे?',
        'action_urgent_title': 'उपचाराची तातडी',
        'monitor_signs_title': 'पुढील निरीक्षणासाठी धोक्याची लक्षणे',
        'expert_help_title': 'कृषी तज्ज्ञांचा सल्ला कधी घ्यावा?',
        'organic_mgmt_title': 'सेंद्रिय व्यवस्थापन पर्याय',
        'chemical_mgmt_title': 'रासायनिक फवारणी मार्गदर्शन',
        'fertilizer_title': 'खत व अन्नद्रव्य व्यवस्थापन',
        'preventive_title': 'प्रतिबंधात्मक उपाय व पीक फेरपालट',
        'disclaimer_notice': '📢 टीप: एआय निदान हे दृश्य लक्षणांवर आधारित प्राथमिक माहिती प्रदान करते. अंतिम प्रमाणीकरणासाठी स्थानिक कृषी तज्ज्ञांचा सल्ला घ्या.',
        
        # History Page (/history)
        'history_title': 'पिकांच्या निदानांचा इतिहास',
        'history_subtitle': 'पूर्वीच्या पीक आरोग्य निदानांची नोंद, रोगाची तीव्रता आणि अहवाल पहा.',
        'col_date': 'दिनांक व वेळ',
        'col_image': 'पानाचे छायाचित्र',
        'col_crop': 'पीक',
        'col_condition': 'ओळखलेला रोग',
        'col_confidence': 'विश्वास पातळी',
        'col_severity': 'तीव्रता',
        'col_actions': 'कृती',
        'view_report': 'अहवाल पहा',
        'delete_record': 'हटवा',
        'empty_history': 'तुमच्या इतिहासात अद्याप कोणत्याही निदानाची नोंद नाही.',
        
        # About Page (/about)
        'about_title': 'एग्रीव्हिजन एआय बद्दल',
        'about_subtitle': 'शेतकऱ्यांना आणि कृषी विस्तारकांना सुलभ एआय निदानाद्वारे सक्षम करणे.',
        'our_mission': 'आमचे ध्येय',
        'how_ai_helps': 'एआय शेतीला कशी मदत करते',
        
        # Contact Page (/contact)
        'contact_title': 'संपर्क व अभिप्राय',
        'contact_subtitle': 'तुमच्या काही शंका, अभिप्राय किंवा सूचना असल्यास आमच्याशी नक्की संपर्क साधा.',
        'form_name': 'तुमचे नाव',
        'form_email': 'ईमेल पत्ता',
        'form_message': 'संदेश',
        'send_btn': 'संदेश पाठवा',
        
        # Footer
        'footer_tagline': 'एआय-संचालित अचूक पीक आरोग्य निदान व सुलभ कृषी मार्गदर्शन.',
        'footer_rights': 'सर्व हक्क राखीव. अचूक व सुलभ शेती मार्गदर्शनासाठी तयार केलेले.'
    },
    'hi': {
        # Navigation & Global
        'app_name': 'एग्रीविज़न एआई',
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
        
        # Hero & Home
        'hero_badge': '🤖 गूगल जेमिनी विजन एआई एवं एक्सएआई',
        'hero_title_1': 'एआई तकनीक से अपनी फसलों को ',
        'hero_title_2': 'बीमारियों',
        'hero_subtitle': 'अपनी फसल की पत्ती की तस्वीर अपलोड करें और एआई द्वारा बीमारी की सटीक पहचान, लक्षणों का विश्लेषण तथा जैविक व रासायनिक उपचार पाएं।',
        'btn_analyze_leaf': '🔍 फसल की पत्ती जांचें',
        'trust_realtime_ai': '✓ रियल-टाइम विजन एआई',
        'trust_explainable': '✓ आसान एआई मार्गदर्शन',
        'trust_solutions': '✓ जैविक और रासायनिक उपाय',
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
        'workflow_cta_title': 'क्या आप अपनी फसल की जांच करने के लिए तैयार हैं?',
        'workflow_cta_desc': 'तुरंत बीमारी की पहचान और जैविक प्रबंधन के उपाय प्राप्त करें।',
        'workflow_cta_btn': 'फसल के पत्ते की जांच करें →',
        
        # Upload Portal (/detect)
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
        'supported_formats': 'समर्थित प्रारूप: JPG, JPEG, PNG, WEBP (अधिकतम 10MB)',
        'quick_test_leaves': 'त्वरित परीक्षण के लिए नमूना पत्तियां:',
        'btn_start_analysis': '🔬 फसल का विश्लेषण करें',
        'analyzing_img': 'आपकी फसल की पत्ती का विश्लेषण किया जा रहा है…',
        'processing_msg': 'तस्वीर संसाधित की जा रही है...',
        'analyzing_symptoms': 'दिखाई देने वाले लक्षणों का विश्लेषण किया जा रहा है...',
        'identifying_disease': 'संभावित रोग की पहचान की जा रही है...',
        'preparing_guidance': 'सुझाव तैयार किए जा रहे हैं...',

        
        # Result Page (/gemini-result & /result)
        'report_title': 'एआई फसल स्वास्थ्य निदान रिपोर्ट',
        'crop_heading': 'फसल की जानकारी',
        'condition_heading': 'पहचाना गया रोग',
        'confidence_heading': 'विश्वास स्तर (Confidence)',
        'health_heading': 'स्वास्थ्य स्थिति',
        'action_urgency': 'कार्रवाई की गंभीरता',
        'action_now_title': 'मुझे अभी पहले क्या करना चाहिए?',
        'action_urgent_title': 'उपचार की तात्कालिकता',
        'monitor_signs_title': 'आगे की निगरानी के लिए चेतावनी लक्षण',
        'expert_help_title': 'कृषि विशेषज्ञ की सलाह कब लें?',
        'organic_mgmt_title': 'जैविक प्रबंधन विकल्प',
        'chemical_mgmt_title': 'रासायनिक छिड़काव निर्देश',
        'fertilizer_title': 'उर्वरक एवं पोषण प्रबंधन',
        'preventive_title': 'निवारक उपाय और फसल चक्र',
        'disclaimer_notice': '📢 सूचना: एआई पूर्वानुमान प्रारंभिक पहचान के लिए हैं। अंतिम पुष्टि के लिए स्थानीय कृषि विशेषज्ञों की सलाह लें।',
        
        # History Page (/history)
        'history_title': 'निदान इतिहास लॉग',
        'history_subtitle': 'पिछली फसल जांच रिपोर्ट, बीमारी की गंभीरता और हीटमैप देखें।',
        'col_date': 'दिनांक व समय',
        'col_image': 'पत्ते की तस्वीर',
        'col_crop': 'फसल',
        'col_condition': 'पहचाना गया रोग',
        'col_confidence': 'विश्वास स्तर',
        'col_severity': 'गंभीरता',
        'col_actions': 'कार्रवाई',
        'view_report': 'रिपोर्ट देखें',
        'delete_record': 'हटाएं',
        'empty_history': 'आपके इतिहास में अभी कोई रिकॉर्ड मौजूद नहीं है।',
        
        # About Page (/about)
        'about_title': 'एग्रीविज़न एआई के बारे में',
        'about_subtitle': 'किसानों और कृषि कार्यकर्ताओं को आसान एआई निदान तकनीक द्वारा सशक्त बनाना।',
        'our_mission': 'हमारा लक्ष्य',
        'how_ai_helps': 'एआई खेती में कैसे मदद करता है',
        
        # Contact Page (/contact)
        'contact_title': 'संपर्क एवं प्रतिक्रिया',
        'contact_subtitle': 'यदि आपके पास कोई प्रश्न, सुझाव या प्रतिक्रिया है तो हमसे अवश्य संपर्क करें।',
        'form_name': 'आपका नाम',
        'form_email': 'ईमेल पता',
        'form_message': 'संदेश',
        'send_btn': 'संदेश भेजें',
        
        # Footer
        'footer_tagline': 'एआई-संचालित सटीक फसल स्वास्थ्य निदान और आसान कृषि मार्गदर्शन।',
        'footer_rights': 'सर्वाधिकार सुरक्षित। सटीक एवं आसान कृषि सलाह के लिए निर्मित।'
    }
}

def get_translation(key, lang='en'):
    """Fetch translated string for a given key and language with English fallback."""
    lang_code = (lang or 'en').lower()
    if lang_code not in TRANSLATIONS:
        lang_code = 'en'
    return TRANSLATIONS[lang_code].get(key) or TRANSLATIONS['en'].get(key, key)
