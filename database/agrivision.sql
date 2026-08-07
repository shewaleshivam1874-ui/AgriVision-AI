-- AgriVision AI Comprehensive Database Schema
-- Database Name: agrivision_db

CREATE DATABASE IF NOT EXISTS agrivision_db;
USE agrivision_db;

-- 1. Crops Table
CREATE TABLE IF NOT EXISTS crops (
    crop_id INT AUTO_INCREMENT PRIMARY KEY,
    crop_name VARCHAR(100) NOT NULL UNIQUE,
    scientific_name VARCHAR(150),
    description TEXT,
    image VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Diseases Master Table
CREATE TABLE IF NOT EXISTS diseases (
    disease_id INT AUTO_INCREMENT PRIMARY KEY,
    crop_id INT NOT NULL,
    disease_name VARCHAR(150) NOT NULL,
    pathogen_type VARCHAR(50), -- Fungal, Bacterial, Viral, Healthy
    description TEXT,
    reference_image VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (crop_id) REFERENCES crops(crop_id) ON DELETE CASCADE
);

-- 3. Disease Symptoms Table
CREATE TABLE IF NOT EXISTS disease_symptoms (
    symptom_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    primary_visual_symptoms TEXT,
    leaf_pattern TEXT,
    lesion_appearance TEXT,
    progression_notes TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 4. Disease Causes Table
CREATE TABLE IF NOT EXISTS disease_causes (
    cause_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    pathogen_name VARCHAR(150),
    primary_causes TEXT,
    conducive_factors TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 5. Disease Prevention Table
CREATE TABLE IF NOT EXISTS disease_prevention (
    prevention_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    cultural_practices TEXT,
    sanitation_guidelines TEXT,
    resistant_varieties TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 6. Disease Management Table
CREATE TABLE IF NOT EXISTS disease_management (
    management_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    immediate_precautions TEXT,
    field_actions TEXT,
    quarantine_advice TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 7. Organic Management Options Table
CREATE TABLE IF NOT EXISTS organic_options (
    organic_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    bio_control_agents TEXT,
    botanical_extracts TEXT,
    cultural_controls TEXT,
    advantages TEXT,
    limitations TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 8. Conventional Management Options Table
CREATE TABLE IF NOT EXISTS conventional_options (
    conventional_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    fungicide_bactericide_classes TEXT,
    application_timing TEXT,
    advantages TEXT,
    limitations TEXT,
    label_warning TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 9. Nutrient Information Table
CREATE TABLE IF NOT EXISTS nutrient_information (
    nutrient_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    key_nutrients TEXT,
    deficiency_susceptibility TEXT,
    foliar_support TEXT,
    disclaimer TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 10. Fertilizer Guidance Table
CREATE TABLE IF NOT EXISTS fertilizer_guidance (
    fertilizer_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    npk_ratio_advice TEXT,
    fertilizer_timing TEXT,
    soil_testing_recommendation TEXT,
    limitation_notice TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 11. Environmental Risk Factors Table
CREATE TABLE IF NOT EXISTS environmental_conditions (
    env_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    optimum_temp_c VARCHAR(50),
    humidity_requirement TEXT,
    moisture_risk TEXT,
    spread_risk VARCHAR(50), -- Low, Moderate, High
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 12. Monitoring Guidance Table
CREATE TABLE IF NOT EXISTS monitoring_guidance (
    monitoring_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    inspection_frequency TEXT,
    key_signs_to_watch TEXT,
    when_to_consult_expert TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);

-- 13. Prediction History Table
CREATE TABLE IF NOT EXISTS prediction_history (
    prediction_id INT AUTO_INCREMENT PRIMARY KEY,
    image_path VARCHAR(255) NOT NULL,
    crop_name VARCHAR(100) NOT NULL,
    disease_name VARCHAR(150) NOT NULL,
    confidence FLOAT NOT NULL,
    confidence_level VARCHAR(50),
    image_quality VARCHAR(50),
    affected_area_pct FLOAT,
    severity_band VARCHAR(50),
    heatmap_path VARCHAR(255),
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 14. References & Sources Table
CREATE TABLE IF NOT EXISTS references_sources (
    ref_id INT AUTO_INCREMENT PRIMARY KEY,
    disease_id INT NOT NULL,
    source_name VARCHAR(255),
    publisher VARCHAR(255),
    url TEXT,
    FOREIGN KEY (disease_id) REFERENCES diseases(disease_id) ON DELETE CASCADE
);
