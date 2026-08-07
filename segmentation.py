import os
import numpy as np

try:
    import cv2
except ImportError:
    cv2 = None

def segment_leaf_and_lesions(cv_bgr_image, output_mask_path=None):
    """
    Perform leaf background isolation and affected lesion area segmentation.
    
    Returns dictionary with:
    - affected_percentage: float (0.0 to 100.0)
    - healthy_percentage: float
    - severity_band: 'Very Low', 'Low', 'Moderate', 'High', or 'Severe'
    - mask_path: path to saved visual segmentation overlay
    """
    if cv2 is None or cv_bgr_image is None or cv_bgr_image.size == 0:
        return {
            "affected_percentage": 0.0,
            "healthy_percentage": 100.0,
            "severity_band": "Unknown",
            "mask_path": None
        }


    h, w = cv_bgr_image.shape[:2]

    # Convert to HSV color space
    hsv = cv2.cvtColor(cv_bgr_image, cv2.COLOR_BGR2HSV)

    # 1. Segment Total Leaf Area (exclude white/grey neutral background)
    # Leaf encompasses green, yellow, brown, dark lesion shades
    lower_foliage = np.array([5, 20, 20])
    upper_foliage = np.array([95, 255, 255])
    leaf_mask = cv2.inRange(hsv, lower_foliage, upper_foliage)

    # Apply morphological operation to clean noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_CLOSE, kernel)
    leaf_mask = cv2.morphologyEx(leaf_mask, cv2.MORPH_OPEN, kernel)

    total_leaf_pixels = np.count_nonzero(leaf_mask)
    if total_leaf_pixels < 100:
        total_leaf_pixels = h * w  # Fallback to full frame if isolation threshold misses

    # 2. Segment Lesions / Affected Regions (Brown, dark yellow, chlorotic necrotic spots)
    lower_lesion = np.array([5, 40, 20])
    upper_lesion = np.array([32, 255, 220])
    lesion_mask_hsv = cv2.inRange(hsv, lower_lesion, upper_lesion)

    # Edge & Texture enhancement for dark necrotic spots
    gray = cv2.cvtColor(cv_bgr_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    # Intersect leaf area with lesion mask
    lesion_mask = cv2.bitwise_and(lesion_mask_hsv, leaf_mask)
    lesion_pixels = np.count_nonzero(lesion_mask)

    # Calculate affected percentage relative to leaf area
    affected_pct = round((lesion_pixels / float(total_leaf_pixels)) * 100.0, 1)
    affected_pct = min(100.0, max(0.0, affected_pct))
    healthy_pct = round(100.0 - affected_pct, 1)

    # Categorize Severity Band
    if affected_pct <= 10.0:
        severity_band = "Very Low"
    elif affected_pct <= 25.0:
        severity_band = "Low"
    elif affected_pct <= 50.0:
        severity_band = "Moderate"
    elif affected_pct <= 75.0:
        severity_band = "High"
    else:
        severity_band = "Severe"

    # Create visual segmentation mask overlay (red overlay over lesions)
    overlay = cv_bgr_image.copy()
    red_mask = np.zeros_like(cv_bgr_image)
    red_mask[:, :] = (0, 0, 235)  # Bright red for lesions
    
    # Apply red mask blend to lesion pixels
    blended = cv2.addWeighted(cv_bgr_image, 0.4, red_mask, 0.6, 0)
    lesion_3d = lesion_mask > 0
    overlay[lesion_3d] = blended[lesion_3d]

    # Draw contour outline around lesion areas
    contours, _ = cv2.findContours(lesion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(overlay, contours, -1, (0, 255, 255), 1)  # Yellow contour border


    if output_mask_path:
        os.makedirs(os.path.dirname(output_mask_path), exist_ok=True)
        cv2.imwrite(output_mask_path, overlay)

    return {
        "affected_percentage": affected_pct,
        "healthy_percentage": healthy_pct,
        "severity_band": severity_band,
        "mask_path": output_mask_path
    }
