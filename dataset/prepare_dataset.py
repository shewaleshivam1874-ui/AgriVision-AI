#!/usr/bin/env python3
"""
AgriVision AI - Dataset Preparation Script
Splits raw leaf image folders into 70% Training, 15% Validation, and 15% Testing.
Resizes, normalizes, and validates image integrity.
"""

import os
import shutil
import random
import argparse
from PIL import Image

def prepare_dataset(source_dir, output_dir, train_ratio=0.70, val_ratio=0.15, test_ratio=0.15, target_size=(224, 224)):
    """
    Scan source_dir for class subfolders, sanitize images, and copy into train/val/test splits.
    """
    assert abs((train_ratio + val_ratio + test_ratio) - 1.0) < 1e-5, "Splits must sum to 1.0"
    
    if not os.path.exists(source_dir):
        print(f"[ERROR] Source directory '{source_dir}' does not exist.")
        return

    print(f"==================================================")
    print(f"  AgriVision AI - Dataset Preparation & Splitter")
    print(f"==================================================")
    print(f"Source Folder : {source_dir}")
    print(f"Output Folder : {output_dir}")
    print(f"Split Ratio   : {int(train_ratio*100)}% Train / {int(val_ratio*100)}% Val / {int(test_ratio*100)}% Test")

    class_folders = [f for f in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, f))]
    if not class_folders:
        print(f"[ERROR] No class subdirectories found in {source_dir}.")
        return

    print(f"Found {len(class_folders)} class categories: {class_folders}\n")

    for split in ['train', 'val', 'test']:
        for cls in class_folders:
            os.makedirs(os.path.join(output_dir, split, cls), exist_ok=True)

    total_processed = 0

    for cls in class_folders:
        cls_path = os.path.join(source_dir, cls)
        images = [img for img in os.listdir(cls_path) if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
        random.seed(42)
        random.shuffle(images)

        num_images = len(images)
        num_train = int(num_images * train_ratio)
        num_val = int(num_images * val_ratio)

        train_imgs = images[:num_train]
        val_imgs = images[num_train:num_train + num_val]
        test_imgs = images[num_train + num_val:]

        splits = {
            'train': train_imgs,
            'val': val_imgs,
            'test': test_imgs
        }

        print(f"Processing '{cls}' ({num_images} images) -> {len(train_imgs)} train | {len(val_imgs)} val | {len(test_imgs)} test")

        for split_name, split_files in splits.items():
            for fname in split_files:
                src_file = os.path.join(cls_path, fname)
                dst_file = os.path.join(output_dir, split_name, cls, fname)
                
                try:
                    # Validate and resize image during copying
                    with Image.open(src_file) as img:
                        img = img.convert('RGB')
                        img = img.resize(target_size, Image.Resampling.LANCZOS)
                        img.save(dst_file, quality=95)
                        total_processed += 1
                except Exception as e:
                    print(f"  [Skipped] Error processing {src_file}: {e}")

    print(f"\n[SUCCESS] Dataset preparation complete. Processed {total_processed} images into {output_dir}.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Prepare and split crop disease dataset into Train/Val/Test sets")
    parser.add_argument('--source', type=str, default='dataset/raw', help='Path to raw dataset folder')
    parser.add_argument('--output', type=str, default='dataset/processed', help='Path for organized dataset output')
    parser.add_argument('--train-ratio', type=float, default=0.70, help='Train set ratio')
    parser.add_argument('--val-ratio', type=float, default=0.15, help='Validation set ratio')
    parser.add_argument('--test-ratio', type=float, default=0.15, help='Test set ratio')
    args = parser.parse_args()

    prepare_dataset(
        source_dir=args.source,
        output_dir=args.output,
        train_ratio=args.train_ratio,
        val_ratio=args.val_ratio,
        test_ratio=args.test_ratio
    )
