import os
import sys
import glob

# Auto-detect workspace virtual environment site-packages if running outside venv
project_root = os.path.abspath(os.path.dirname(__file__))
venv_site_packages = glob.glob(os.path.join(project_root, 'venv', 'lib', 'python*', 'site-packages'))
for p in venv_site_packages:
    if p not in sys.path:
        sys.path.insert(0, p)

import cv2
import numpy as np

class ImageQualityAnalyzer:
    """
    Evaluates image quality metrics (blur, brightness, contrast, resolution)
    and checks for Out-of-Distribution / Non-leaf uploads.
    """
    def __init__(self, blur_threshold=80.0, low_bright=40.0, high_bright=220.0, min_resolution=150):
        self.blur_threshold = blur_threshold
        self.low_bright = low_bright
        self.high_bright = high_bright
        self.min_resolution = min_resolution

    def analyze_quality(self, cv_bgr_image):
        """
        Analyze input BGR image array.
        Returns dictionary with:
        - quality_grade: 'Good', 'Moderate', or 'Poor'
        - is_usable: boolean
        - blur_score: float (Laplacian variance)
        - brightness_mean: float (0-255)
        - contrast_std: float
        - resolution: tuple (width, height)
        - warnings: list of warnings
        - is_leaf_like: boolean
        """
        if cv_bgr_image is None or cv_bgr_image.size == 0:
            return {
                "quality_grade": "Poor",
                "is_usable": False,
                "warnings": ["Invalid or corrupted image format."],
                "is_leaf_like": False
            }

        h, w = cv_bgr_image.shape[:2]
        warnings = []
        is_usable = True

        # 1. Resolution Check
        if h < self.min_resolution or w < self.min_resolution:
            warnings.append(f"Low image resolution ({w}x{h}). High-resolution photos yield higher AI accuracy.")
            is_usable = False

        # 2. Blur Check (Variance of Laplacian)
        gray = cv2.cvtColor(cv_bgr_image, cv2.COLOR_BGR2GRAY)
        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        if laplacian_var < self.blur_threshold:
            warnings.append("Image appears blurry. Please upload a clear, focused leaf photo.")
            is_usable = False

        # 3. Brightness Check (HSV V-Channel Mean)
        hsv = cv2.cvtColor(cv_bgr_image, cv2.COLOR_BGR2HSV)
        v_channel = hsv[:, :, 2]
        brightness_mean = float(np.mean(v_channel))

        if brightness_mean < self.low_bright:
            warnings.append("Image is under-exposed or dark. Use good lighting for better leaf analysis.")
        elif brightness_mean > self.high_bright:
            warnings.append("Image is over-exposed or washed out by harsh glare.")

        # 4. Contrast Check (Standard Deviation of Grayscale)
        contrast_std = float(np.std(gray))
        if contrast_std < 25.0:
            warnings.append("Low image contrast detected.")

        # 5. Leaf-like Saliency / Greenness Ratio (OOD Detection)
        lower_green = np.array([20, 30, 30])
        upper_green = np.array([90, 255, 255])
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        green_ratio = (np.count_nonzero(green_mask) / (w * h + 1e-5)) * 100.0

        # Also check for brown/yellow foliage spots
        lower_brown = np.array([10, 30, 30])
        upper_brown = np.array([30, 255, 255])
        brown_mask = cv2.inRange(hsv, lower_brown, upper_brown)
        foliage_ratio = green_ratio + (np.count_nonzero(brown_mask) / (w * h + 1e-5)) * 100.0

        is_leaf_like = foliage_ratio > 8.0

        if not is_leaf_like:
            warnings.append("The uploaded image does not appear to contain a recognizable plant leaf.")
            is_usable = False

        # Assign Overall Quality Grade
        if len(warnings) == 0 and laplacian_var > 150.0:
            quality_grade = "Good"
        elif is_usable and len(warnings) <= 1:
            quality_grade = "Moderate"
        else:
            quality_grade = "Poor"

        return {
            "quality_grade": quality_grade,
            "is_usable": is_usable,
            "blur_score": round(laplacian_var, 1),
            "brightness_mean": round(brightness_mean, 1),
            "contrast_std": round(contrast_std, 1),
            "resolution": (w, h),
            "warnings": warnings,
            "is_leaf_like": is_leaf_like,
            "foliage_ratio": round(foliage_ratio, 1)
        }

quality_analyzer = ImageQualityAnalyzer()
