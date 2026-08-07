# AgriVision AI – An Explainable AI Web Application for Early Crop Disease Detection

AgriVision AI is a modern, responsive web application built with **Python Flask**, **TensorFlow / Keras**, **OpenCV**, **Explainable AI (Grad-CAM)**, and **MySQL**. It enables farmers, agronomists, and researchers to upload crop leaf images, detect crop diseases using deep learning, view confidence scores, visualize neural attention heatmaps using **Grad-CAM**, and retrieve structured management advice, organic remedies, and nutrient recommendations.

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3 (Modern Agriculture Palette with Emerald Green & White, Glassmorphism, Micro-animations), JavaScript (ES6+, Drag-and-Drop, AJAX Uploads)
- **Backend**: Python Flask
- **Machine Learning**: TensorFlow / Keras (MobileNetV2 Transfer Learning Architecture)
- **Image Processing**: OpenCV (`opencv-python-headless`) and Pillow
- **Explainable AI**: Grad-CAM (Gradient-weighted Class Activation Mapping)
- **Database**: MySQL (`agrivision_db`) with automatic SQLite fallback for instant testability
- **Environment**: Linux / Kali Linux / Ubuntu, Python 3.10+

---

## 📁 Project Folder Structure

```
AgriVisionAI/
├── app.py                      # Flask main server application & routes
├── config.py                   # Environment configuration & DB settings
├── requirements.txt            # Python dependencies
├── .env.example                # Template for environment variables
├── .gitignore                  # Git ignore rules
├── README.md                   # Complete documentation & setup instructions
├── static/
│   ├── css/
│   │   └── style.css           # Modern agriculture-themed CSS stylesheet
│   ├── js/
│   │   ├── main.js             # Navigation menu, search filter & form validation
│   │   └── upload.js           # Drag-and-drop file upload & AJAX predictor
│   └── uploads/                # User uploaded images & generated Grad-CAM heatmaps
├── templates/
│   ├── base.html               # Master layout with responsive navbar & footer
│   ├── index.html              # Hero section, 5-step process, feature cards
│   ├── detect.html             # Leaf image upload & analysis dashboard
│   ├── result.html             # Prediction result view with confidence gauge & Grad-CAM visualizer
│   ├── diseases.html           # Searchable & filterable Disease Library
│   ├── disease_details.html    # Detailed disease page (Symptoms, Causes, Organic, Nutrients)
│   ├── about.html              # About AgriVision AI, Tech Stack, XAI focus & project scope
│   └── contact.html            # Contact form
├── model/
│   ├── predict.py              # ML inference loader & fallback demo predictor
│   ├── gradcam.py              # Grad-CAM heatmap generator using OpenCV & TensorFlow
│   ├── train_model.py          # Transfer learning script (MobileNetV2 / 70-15-15 split)
│   ├── class_names.json        # Class index to disease mapping
│   └── plant_disease_model.keras # Saved trained model file
├── database/
│   ├── database.py             # DB connection manager (MySQL with SQLite auto-fallback)
│   └── agrivision.sql          # SQL schema & seed data for crops, diseases, history
├── dataset/
│   ├── README.md               # Dataset structure documentation
│   └── prepare_dataset.py      # Dataset splitter (70% train, 15% val, 15% test)
└── utils/
    └── image_processing.py     # Image validation, resizing & tensor normalization
```

---

## 🚀 Setup & Installation Guide (Linux / Kali Linux)

Follow these step-by-step commands in your terminal to set up and run AgriVision AI locally.

### Step 1: System Dependencies & Prerequisites
Open your terminal and ensure Python 3, `pip`, `venv`, and MySQL server are installed:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv mysql-server libgl1-mesa-glx
```

---

### Step 2: Navigate to Project & Create Virtual Environment

```bash
cd /home/kali/AgriVisionAI

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

---

### Step 3: Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Step 4: Configure Environment Variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

*(Optional)* Edit `.env` to update your MySQL credentials:
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=agrivision_db
```

---

### Step 5: Configure MySQL Database

Log into MySQL and run the database setup script:

```bash
# Start MySQL Service if not running
sudo systemctl start mysql

# Import Schema and Seed Data into MySQL
sudo mysql -u root < database/agrivision.sql
```

> **Note**: If MySQL server is not configured or running, AgriVision AI automatically falls back to an embedded SQLite database (`database/agrivision.db`) populated with identical seed data, allowing immediate testing out of the box!

---

### Step 6: Dataset Preparation & Model Training (Optional)

AgriVision AI includes scripts to prepare leaf datasets and train deep learning models.

1. **Prepare Dataset (70% Train, 15% Val, 15% Test)**:
   ```bash
   python3 dataset/prepare_dataset.py --source dataset/raw --output dataset/processed
   ```

2. **Train TensorFlow Transfer Learning Model (MobileNetV2)**:
   ```bash
   python3 model/train_model.py --dataset dataset/processed --output model/plant_disease_model.keras --epochs 15
   ```

*(Note: If `plant_disease_model.keras` is omitted, the web application runs in high-fidelity demo inference mode).*

---

### Step 7: Start the Flask Web Application

```bash
python3 app.py
```

The terminal will display:
```
==================================================
  Starting AgriVision AI Web Application Server
==================================================
 * Running on http://0.0.0.0:5000
```

---

### Step 8: Open in Browser

Open your web browser and visit:
👉 **`http://localhost:5000`** or **`http://127.0.0.1:5000`**

---

## 🔬 Primary Application Workflow

1. Open AgriVision AI Homepage (`/`).
2. Navigate to **Detect Disease** (`/detect`).
3. Drag & drop or browse a crop leaf image (`.jpg`, `.jpeg`, `.png`).
4. Click **Analyze Image**.
5. Flask backend validates the file, normalizes pixels, runs neural network inference, and generates a **Grad-CAM attention heatmap**.
6. View the **Result Dashboard** (`/result/<id>`) displaying:
   - Crop Name & Disease Name
   - Plant Health Status Badge (Healthy / Disease Detected / Low Confidence)
   - Confidence Progress Meter
   - Side-by-side **Original Image vs Grad-CAM Heatmap**
   - Symptoms, Causes, Prevention, Management, Organic Remedies, and Nutrient/Fertilizer Info fetched from MySQL.
7. Search and filter diseases in the **Disease Library** (`/diseases`).
