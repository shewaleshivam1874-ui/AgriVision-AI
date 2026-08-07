# AgriVision AI - Dataset Guidelines

AgriVision AI uses high-resolution leaf image datasets to train computer vision models for early crop disease detection.

## Recommended Public Datasets
- **PlantVillage Dataset**: Contains 54,303 healthy and diseased crop leaf images across 38 categories (Tomato, Potato, Pepper, Apple, Grape, Corn, etc.).
- **Kaggle Plant Pathology**: Fine-grained apple and crop foliage leaf disease annotations.

## Organization & Directory Structure

Raw dataset files should be placed inside `dataset/raw/` organized by disease class folders:

```
dataset/
├── raw/
│   ├── Tomato_Healthy/
│   │   ├── image1.jpg
│   │   └── image2.jpg
│   ├── Tomato_Early_Blight/
│   ├── Tomato_Late_Blight/
│   ├── Potato_Healthy/
│   ├── Potato_Early_Blight/
│   ├── Potato_Late_Blight/
│   ├── Pepper_Healthy/
│   └── Pepper_Bacterial_Spot/
```

## Running Dataset Preparation

To split your raw images into 70% Training, 15% Validation, and 15% Testing:

```bash
python3 dataset/prepare_dataset.py --source dataset/raw --output dataset/processed
```

This generates `dataset/processed/train`, `dataset/processed/val`, and `dataset/processed/test`.
