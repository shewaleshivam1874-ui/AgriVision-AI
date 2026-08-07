import os
from dotenv import load_dotenv

# Load environment variables from .env file if available
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'agrivision_ai_default_secret_key_2026')
    
    # Gemini AI Configuration
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    GEMINI_MODEL = os.environ.get('GEMINI_MODEL', 'gemini-3.6-flash')


    # Upload Settings
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')

    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB limit
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp'}

    # MySQL Configuration
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = int(os.environ.get('DB_PORT', 3306))
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_NAME = os.environ.get('DB_NAME', 'agrivision_db')

    # SQLite Fallback DB Path
    SQLITE_DB_PATH = os.path.join(BASE_DIR, 'database', 'agrivision.db')

    # Model Configuration
    MODEL_PATH = os.path.join(BASE_DIR, 'model', 'plant_disease_model.keras')
    CLASS_NAMES_PATH = os.path.join(BASE_DIR, 'model', 'class_names.json')
    IMAGE_SIZE = (224, 224)
