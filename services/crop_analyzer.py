import os
import json
import re
import io
import time
from PIL import Image
from config import Config

# Attempt importing google.genai (new SDK) and google.generativeai (legacy SDK)
GENAI_SDK_AVAILABLE = False
GENAI_SDK_TYPE = None

try:
    from google import genai
    from google.genai import types
    GENAI_SDK_AVAILABLE = True
    GENAI_SDK_TYPE = 'google-genai'
except ImportError:
    try:
        import google.generativeai as legacy_genai
        GENAI_SDK_AVAILABLE = True
        GENAI_SDK_TYPE = 'google-generativeai'
    except ImportError:
        GENAI_SDK_AVAILABLE = False
        GENAI_SDK_TYPE = None


class CropAnalyzerService:
    """
    Decoupled Agricultural Vision Analysis Service utilizing Google Gemini AI.
    Analyzes crop leaf images and produces structured pathology reports.
    """

    SUPPORTED_MIME_TYPES = {
        'image/jpeg': 'jpeg',
        'image/jpg': 'jpeg',
        'image/png': 'png',
        'image/webp': 'webp'
    }

    SUPPORTED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}

    def __init__(self):
        self.api_key = Config.GEMINI_API_KEY
        self.model_name = Config.GEMINI_MODEL or 'gemini-3.6-flash'


    def is_configured(self):
        """Check if Gemini API key and SDK are properly configured."""
        key = self.api_key or os.environ.get('GEMINI_API_KEY', '')
        return bool(key and key.strip() and key != 'your_api_key_here' and GENAI_SDK_AVAILABLE)

    def validate_image(self, file_bytes, filename=""):
        """
        Server-side validation for image format, non-emptiness, and PIL openability.
        """
        if not file_bytes or len(file_bytes) == 0:
            return False, "Uploaded file is empty."

        if len(file_bytes) > Config.MAX_CONTENT_LENGTH:
            max_mb = Config.MAX_CONTENT_LENGTH // (1024 * 1024)
            return False, f"File size exceeds maximum permitted limit of {max_mb} MB."

        if filename:
            ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
            if ext not in self.SUPPORTED_EXTENSIONS:
                return False, f"Unsupported file extension '.{ext}'. Please upload JPG, JPEG, PNG, or WEBP image."

        try:
            img = Image.open(io.BytesIO(file_bytes))
            img.verify()
            return True, ""
        except Exception as e:
            return False, f"Corrupted or invalid image file format: {str(e)}"

    def _build_prompt(self, lang="en"):
        """Construct AgriVision AI system prompt and structured JSON request."""
        lang_names = {
            'hi': 'Hindi (हिंदी)',
            'mr': 'Marathi (मराठी)',
            'en': 'English'
        }
        target_lang = lang_names.get(lang.lower(), 'English')

        prompt = f"""You are the visual-analysis component of AgriVision AI, an agricultural crop-health assistance system.
Carefully inspect the supplied crop/leaf image.
Your job is to identify visible plant-health symptoms and provide a cautious preliminary assessment.

CRITICAL FIRST CHECK:
First determine whether the image contains a clear, usable crop/plant leaf.
If the image does NOT contain a plant leaf, or if it is unusable (e.g. extremely blurry, extremely dark, severely overexposed, extremely distant, unrelated object, person, animal, vehicle, document, or non-plant item), set "valid_image" to false.

Language Requirement:
All human-readable explanations (symptoms, treatment options, prevention, immediate actions, reasons, recommendations, limitations) MUST be written in {target_lang}.
Keep plant scientific names, pathogen taxonomy, and chemical active ingredient names accurate in standard scientific terminology.

Analysis Guidelines:
1. Distinguish clearly between direct visual observations and diagnostic inferences.
2. Do not claim certainty when visual evidence is insufficient.
3. Do not invent laboratory results or exact confidence percentages. Use confidence labels: HIGH, MEDIUM, LOW.
4. If the condition cannot be determined reliably, return UNKNOWN rather than guessing.
5. For pesticide/fungicide recommendations, do not invent exact dosages or brand names. Prefer active ingredients or treatment categories. Direct the user to follow locally approved product labels and agricultural authority guidelines.
6. Do not automatically recommend fertilizer simply because a plant appears diseased. Only provide nutrient correction when symptoms reasonably indicate deficiency.

Return ONLY a single valid JSON object matching EXACTLY this JSON structure without any additional commentary:
{{
  "valid_image": true,
  "plant": {{
    "common_name": "Common crop name",
    "scientific_name": "Scientific botanical name",
    "confidence": "HIGH"
  }},
  "health": {{
    "status": "HEALTHY"
  }},
  "diagnosis": {{
    "primary_condition": "Identified disease or condition name",
    "alternative_conditions": ["Alternative condition 1", "Alternative condition 2"],
    "category": "Fungal | Bacterial | Viral | Pest | Nutrient | Environmental | Healthy",
    "confidence": "HIGH"
  }},
  "symptoms": ["Visible symptom 1", "Visible symptom 2"],
  "severity": {{
    "level": "HEALTHY",
    "reason": "Explanation of visible foliage damage"
  }},
  "possible_causes": ["Cause 1", "Cause 2"],
  "pest_analysis": {{
    "suspected": false,
    "possible_pest": "Pest name if applicable",
    "evidence": "Visible signs of insect damage or pest activity"
  }},
  "nutrient_analysis": {{
    "deficiency_suspected": false,
    "possible_deficiency": "Nutrient name if applicable (e.g., Nitrogen, Potassium, Iron)",
    "visible_evidence": "Chlorosis pattern or interveinal yellowing signs"
  }},
  "environmental_stress": ["Stress factor if applicable"],
  "organic_treatment": ["Organic management step 1", "Organic management step 2"],
  "conventional_treatment": ["Conventional chemical/active ingredient treatment option"],
  "fertilizer_guidance": {{
    "needed": false,
    "recommendation": "Fertilizer guidance text",
    "organic_option": "Organic soil amendment option",
    "conventional_option": "Conventional fertilizer option"
  }},
  "prevention": ["Preventive practice 1", "Preventive practice 2"],
  "immediate_actions": [
    "Prioritized Action Step 1",
    "Prioritized Action Step 2",
    "Prioritized Action Step 3",
    "Prioritized Action Step 4"
  ],
  "urgency": "LOW",
  "expert_consultation": false,
  "limitations": "Visual identification limitations notice"
}}

Health status MUST be one of: HEALTHY, POSSIBLY_DISEASED, DISEASED, PEST_DAMAGE, NUTRIENT_DEFICIENCY, ENVIRONMENTAL_STRESS, UNKNOWN.
Severity level MUST be one of: HEALTHY, EARLY, MODERATE, SEVERE, UNKNOWN.
Urgency MUST be one of: LOW, MEDIUM, HIGH.
Confidence MUST be one of: HIGH, MEDIUM, LOW.
"""
        return prompt

    def analyze_leaf(self, file_bytes, filename="", lang="en"):
        """
        Master leaf image analysis method using Gemini Vision API.
        Returns dictionary with success boolean and payload or error details.
        """
        api_key = self.api_key or os.environ.get('GEMINI_API_KEY', '')
        if not api_key or api_key.strip() == 'your_api_key_here':
            return {
                "success": False,
                "error": "GEMINI_API_KEY_MISSING",
                "message": "Gemini API key is not configured. Please set GEMINI_API_KEY in your environment or .env file."
            }

        # 1. Validate image
        is_valid, err_msg = self.validate_image(file_bytes, filename)
        if not is_valid:
            return {
                "success": False,
                "error": "IMAGE_NOT_SUITABLE",
                "message": f"Image validation failed: {err_msg}"
            }

        # Load image with PIL
        try:
            pil_img = Image.open(io.BytesIO(file_bytes))
            # Convert RGBA/Palette to RGB
            if pil_img.mode != 'RGB':
                pil_img = pil_img.convert('RGB')
        except Exception as e:
            return {
                "success": False,
                "error": "IMAGE_NOT_SUITABLE",
                "message": f"Unable to process image file: {str(e)}"
            }

        prompt = self._build_prompt(lang=lang)

        # 2. Call Gemini API
        raw_text = None
        start_time = time.time()

        try:
            raw_text = self._call_gemini_api(api_key, pil_img, prompt)
        except Exception as e:
            err_str = str(e)
            print(f"[Gemini API Exception]: {err_str}")
            if "429" in err_str or "quota" in err_str.lower() or "rate" in err_str.lower():
                return {
                    "success": False,
                    "error": "RATE_LIMIT_EXCEEDED",
                    "message": "Gemini API quota or rate limit exceeded. Please wait a moment and try again."
                }
            elif "401" in err_str or "API_KEY_INVALID" in err_str or ("invalid" in err_str.lower() and "key" in err_str.lower()):
                return {
                    "success": False,
                    "error": "INVALID_API_KEY",
                    "message": "Invalid Gemini API key provided. Please check your GEMINI_API_KEY configuration."
                }
            elif "timeout" in err_str.lower():
                return {
                    "success": False,
                    "error": "REQUEST_TIMEOUT",
                    "message": "Gemini API request timed out. Please try again with a smaller clear leaf image."
                }
            else:
                return {
                    "success": False,
                    "error": "GEMINI_API_ERROR",
                    "message": f"Gemini vision analysis service error: {err_str}"
                }

        if not raw_text:
            return {
                "success": False,
                "error": "EMPTY_RESPONSE",
                "message": "Gemini returned an empty response."
            }

        # 3. Parse JSON Response
        parsed_json = self._parse_json_response(raw_text)
        if not parsed_json:
            return {
                "success": False,
                "error": "MALFORMED_RESPONSE",
                "message": "Could not parse structured analysis from Gemini response."
            }

        # 4. Check whether image was identified as a usable crop leaf
        if not parsed_json.get('valid_image', True):
            return {
                "success": False,
                "error": "IMAGE_NOT_SUITABLE",
                "message": "Please upload a clear close-up image of the affected crop leaf."
            }

        # 5. Normalize and validate fields
        normalized = self._normalize_analysis_response(parsed_json)
        normalized['elapsed_time'] = round(time.time() - start_time, 2)

        return {
            "success": True,
            "data": normalized
        }

    def _call_gemini_api(self, api_key, pil_img, prompt):
        """Invoke Gemini API using new google-genai or legacy google-generativeai SDK."""
        model_name = self.model_name or 'gemini-2.5-flash'

        # Modern google-genai SDK
        if GENAI_SDK_TYPE == 'google-genai':
            client = genai.Client(api_key=api_key)
            
            # Save PIL image to BytesIO jpeg buffer
            buf = io.BytesIO()
            pil_img.save(buf, format='JPEG')
            img_bytes = buf.getvalue()

            image_part = types.Part.from_bytes(
                data=img_bytes,
                mime_type='image/jpeg'
            )

            # Try generating content with model
            config = types.GenerateContentConfig(
                temperature=0.2,
                response_mime_type="application/json"
            )

            response = client.models.generate_content(
                model=model_name,
                contents=[prompt, image_part],
                config=config
            )
            return response.text

        # Legacy google-generativeai SDK
        elif GENAI_SDK_TYPE == 'google-generativeai':
            import google.generativeai as legacy_genai
            legacy_genai.configure(api_key=api_key)
            model = legacy_genai.GenerativeModel(model_name)
            
            generation_config = {
                "temperature": 0.2,
                "response_mime_type": "application/json"
            }
            
            response = model.generate_content(
                [prompt, pil_img],
                generation_config=generation_config
            )
            return response.text
        else:
            raise RuntimeError("No compatible Google GenAI SDK found installed in environment.")

    def _parse_json_response(self, text):
        """Clean markdown wrapping and parse raw string into JSON object."""
        if not text:
            return None

        clean_text = text.strip()
        # Remove ```json ... ``` code blocks
        if clean_text.startswith("```"):
            clean_text = re.sub(r"^```(?:json)?\s*", "", clean_text, flags=re.IGNORECASE)
            clean_text = re.sub(r"\s*```$", "", clean_text)
            clean_text = clean_text.strip()

        try:
            return json.loads(clean_text)
        except json.JSONDecodeError:
            # Fallback regex extraction of outermost { ... }
            match = re.search(r"(\{.*\})", clean_text, re.DOTALL)
            if match:
                try:
                    return json.loads(match.group(1))
                except json.JSONDecodeError:
                    pass
            return None

    def _normalize_analysis_response(self, data):
        """Ensure all required fields exist and adhere to standard formatting."""
        return {
            "valid_image": data.get("valid_image", True),
            "plant": {
                "common_name": data.get("plant", {}).get("common_name", "Unknown Crop"),
                "scientific_name": data.get("plant", {}).get("scientific_name", "Unspecified species"),
                "confidence": data.get("plant", {}).get("confidence", "MEDIUM")
            },
            "health": {
                "status": data.get("health", {}).get("status", "DISEASED")
            },
            "diagnosis": {
                "primary_condition": data.get("diagnosis", {}).get("primary_condition", "Crop Pathology Identified"),
                "alternative_conditions": data.get("diagnosis", {}).get("alternative_conditions", []),
                "category": data.get("diagnosis", {}).get("category", "General Crop Disease"),
                "confidence": data.get("diagnosis", {}).get("confidence", "MEDIUM")
            },
            "symptoms": data.get("symptoms", []),
            "severity": {
                "level": data.get("severity", {}).get("level", "MODERATE"),
                "reason": data.get("severity", {}).get("reason", "Visible foliage pathology observed.")
            },
            "possible_causes": data.get("possible_causes", []),
            "pest_analysis": {
                "suspected": data.get("pest_analysis", {}).get("suspected", False),
                "possible_pest": data.get("pest_analysis", {}).get("possible_pest", ""),
                "evidence": data.get("pest_analysis", {}).get("evidence", "")
            },
            "nutrient_analysis": {
                "deficiency_suspected": data.get("nutrient_analysis", {}).get("deficiency_suspected", False),
                "possible_deficiency": data.get("nutrient_analysis", {}).get("possible_deficiency", ""),
                "visible_evidence": data.get("nutrient_analysis", {}).get("visible_evidence", "")
            },
            "environmental_stress": data.get("environmental_stress", []),
            "organic_treatment": data.get("organic_treatment", []),
            "conventional_treatment": data.get("conventional_treatment", []),
            "fertilizer_guidance": {
                "needed": data.get("fertilizer_guidance", {}).get("needed", False),
                "recommendation": data.get("fertilizer_guidance", {}).get("recommendation", ""),
                "organic_option": data.get("fertilizer_guidance", {}).get("organic_option", ""),
                "conventional_option": data.get("fertilizer_guidance", {}).get("conventional_option", "")
            },
            "prevention": data.get("prevention", []),
            "immediate_actions": data.get("immediate_actions", []),
            "urgency": data.get("urgency", "MEDIUM"),
            "expert_consultation": data.get("expert_consultation", False),
            "limitations": data.get("limitations", "AgriVision AI provides AI-assisted preliminary crop health information based on visible symptoms.")
        }


# Singleton service instance
crop_analyzer = CropAnalyzerService()
