#!/usr/bin/env python3
"""
AgriVision AI - Dataset Analysis & Automated Mapping Generator
Scans dataset directory, inspects class balance, dimensions, corrupt/duplicate images,
and generates model/class_names.json and model/crop_disease_mapping.json.
"""

import os
import json
import hashlib
from PIL import Image

def find_dataset_root():
    """Find the root dataset directory containing train/valid or class folders."""
    possible_paths = [
        '/home/kali/Downloads/plantdisease /New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/train',
        '/home/kali/Downloads/plantdisease /New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)',
        '/home/kali/Downloads/plantdisease',
        'dataset/raw',
        'dataset/processed/train'
    ]
    for path in possible_paths:
        if os.path.exists(path):
            # Check if it has class subdirectories
            subdirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
            if subdirs:
                print(f"[DatasetAnalysis] Found dataset root at: {path}")
                return path
    print("[DatasetAnalysis] Warning: Standard dataset path not found.")
    return None

def calculate_image_hash(image_path):
    """Calculate MD5 hash of image to detect duplicate images."""
    try:
        with open(image_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return None

def analyze_dataset(dataset_dir=None):
    """Comprehensive dataset inspection and class mapping generation."""
    if not dataset_dir:
        dataset_dir = find_dataset_root()

    if not dataset_dir or not os.path.exists(dataset_dir):
        print("[ERROR] Dataset directory not found.")
        return None

    print("==================================================")
    print("  AgriVision AI - Dataset Inspection Report")
    print("==================================================")
    print(f"Dataset Path: {dataset_dir}\n")

    class_folders = sorted([d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d))])
    
    total_classes = len(class_folders)
    total_images = 0
    corrupt_count = 0
    duplicate_count = 0
    
    seen_hashes = set()
    class_stats = {}
    class_mapping = {}
    crop_disease_mapping = {}
    image_sizes = set()

    for idx, folder in enumerate(class_folders):
        folder_path = os.path.join(dataset_dir, folder)
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        
        count = len(image_files)
        total_images += count
        class_stats[folder] = count

        # Automated parsing of Crop and Disease from folder name
        # e.g., Tomato___Early_blight -> Crop: Tomato, Disease: Early Blight
        if '___' in folder:
            crop_part, disease_part = folder.split('___', 1)
        elif '_' in folder:
            parts = folder.split('_', 1)
            crop_part, disease_part = parts[0], parts[1]
        else:
            crop_part, disease_part = "General", folder

        crop_name = crop_part.replace('_', ' ').replace(',', '').strip().capitalize()
        disease_name = disease_part.replace('_', ' ').strip().title()
        
        if "Healthy" in disease_name:
            status = "Healthy"
            display_name = f"{crop_name} - Healthy"
        else:
            status = "Disease Detected"
            display_name = f"{crop_name} - {disease_name}"

        # Populate class_names.json mapping
        class_mapping[str(idx)] = {
            "folder": folder,
            "crop": crop_name,
            "disease": f"{crop_name} {disease_name}" if crop_name.lower() not in disease_name.lower() else disease_name,
            "status": status,
            "display_name": display_name
        }

        # Populate crop_disease_mapping.json
        if crop_name not in crop_disease_mapping:
            crop_disease_mapping[crop_name] = []
        
        crop_disease_mapping[crop_name].append({
            "class_id": idx,
            "disease_name": disease_name,
            "full_name": display_name,
            "folder_name": folder
        })

        # Sample inspection of first 5 images for corruption and duplicates
        for fname in image_files[:10]:
            img_path = os.path.join(folder_path, fname)
            try:
                with Image.open(img_path) as img:
                    image_sizes.add(img.size)
                
                img_hash = calculate_image_hash(img_path)
                if img_hash:
                    if img_hash in seen_hashes:
                        duplicate_count += 1
                    else:
                        seen_hashes.add(img_hash)
            except Exception:
                corrupt_count += 1

    print(f"Total Disease Classes : {total_classes}")
    print(f"Total Images Inspected : {total_images}")
    print(f"Corrupt Images Found   : {corrupt_count}")
    print(f"Duplicate Hashes Found : {duplicate_count}")
    print(f"Image Resolutions Seen : {list(image_sizes)[:5]}\n")

    print("Class Distribution Summary (Top 10):")
    for k, v in list(class_stats.items())[:10]:
        print(f"  - {k}: {v} images")

    # Save class_names.json
    output_class_json = 'model/class_names.json'
    os.makedirs('model', exist_ok=True)
    with open(output_class_json, 'w') as f:
        json.dump(class_mapping, f, indent=2)
    print(f"\n[SUCCESS] Generated class mapping: {output_class_json}")

    # Save crop_disease_mapping.json
    output_crop_json = 'model/crop_disease_mapping.json'
    with open(output_crop_json, 'w') as f:
        json.dump(crop_disease_mapping, f, indent=2)
    print(f"[SUCCESS] Generated crop-disease mapping: {output_crop_json}")

    return class_mapping

if __name__ == '__main__':
    analyze_dataset()
