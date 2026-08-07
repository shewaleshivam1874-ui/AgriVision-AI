import os
import cv2
import numpy as np
from PIL import Image
from config import Config

def allowed_file(filename):
    """Check if the uploaded file has an allowed image extension."""
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in Config.ALLOWED_EXTENSIONS

def validate_image_file(file_path):
    """
    Validate that the file exists, is non-empty, and can be opened as a valid image by PIL.
    Returns (is_valid, error_message).
    """
    if not os.path.exists(file_path):
        return False, "Uploaded image file not found."
    
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        return False, "Uploaded image file is empty."
    
    if file_size > Config.MAX_CONTENT_LENGTH:
        return False, f"Image size exceeds maximum limit of {Config.MAX_CONTENT_LENGTH // (1024 * 1024)} MB."
    
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True, ""
    except Exception as e:
        return False, f"Corrupted or invalid image file: {str(e)}"

def preprocess_image_for_model(image_path, target_size=(224, 224)):
    """
    Load image, convert to RGB, resize according to target_size, 
    normalize pixels to [0, 1] range, and expand dimensions to tensor batch (1, H, W, 3).
    Returns (processed_numpy_array, original_cv2_bgr_image).
    """
    # Load image using OpenCV
    cv_img = cv2.imread(image_path)
    if cv_img is None:
        # Fallback load via Pillow if OpenCV fails with special paths
        pil_img = Image.open(image_path).convert('RGB')
        cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    # Convert BGR to RGB
    rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    
    # Resize image
    resized_img = cv2.resize(rgb_img, target_size, interpolation=cv2.INTER_AREA)
    
    # Normalize pixel values to [0, 1] range
    normalized_arr = resized_img.astype(np.float32) / 255.0
    
    # Expand dims to shape (1, 224, 224, 3)
    tensor_input = np.expand_dims(normalized_arr, axis=0)
    
    return tensor_input, cv_img
