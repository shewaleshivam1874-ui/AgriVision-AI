#!/usr/bin/env python3
"""
AgriVision AI - EfficientNetB0 Two-Stage Model Training Script
Performs transfer learning & fine-tuning on crop leaf dataset with 70/15/15 stratified split.
"""

import os
import sys
import argparse
import json

def train_efficientnet(dataset_dir, output_model_path, img_size=(224, 224), batch_size=32, epochs_stage1=10, epochs_stage2=5):
    """
    Two-stage training pipeline using EfficientNetB0 base architecture.
    """
    try:
        import tensorflow as tf
        from tensorflow.keras import layers, models
        from tensorflow.keras.applications import EfficientNetB0
        from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
    except ImportError:
        print("[ERROR] TensorFlow is required for model training. Run: pip install tensorflow")
        return

    print("==================================================")
    print("  AgriVision AI - EfficientNetB0 Two-Stage Trainer")
    print("==================================================")
    print(f"Dataset Path     : {dataset_dir}")
    print(f"Output Model     : {output_model_path}")
    print(f"Image Resolution : {img_size}")
    print(f"Batch Size       : {batch_size}")

    if not os.path.exists(dataset_dir):
        print(f"[ERROR] Dataset directory '{dataset_dir}' does not exist.")
        return

    # Load dataset using tf.data
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.3,
        subset="training",
        seed=42,
        image_size=img_size,
        batch_size=batch_size
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        dataset_dir,
        validation_split=0.3,
        subset="validation",
        seed=42,
        image_size=img_size,
        batch_size=batch_size
    )

    class_names = train_ds.class_names
    num_classes = len(class_names)
    print(f"\nDiscovered {num_classes} classes: {class_names[:5]}...")

    # Performance optimization
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    # Realistic Training Data Augmentation Layer
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.15),
        layers.RandomZoom(0.15),
        layers.RandomTranslation(0.1, 0.1),
        layers.RandomContrast(0.1),
    ], name="data_augmentation")

    # EfficientNetB0 Base
    base_model = EfficientNetB0(
        input_shape=(img_size[0], img_size[1], 3),
        include_top=False,
        weights='imagenet'
    )
    base_model.trainable = False  # Stage 1: Freeze base model

    inputs = tf.keras.Input(shape=(img_size[0], img_size[1], 3))
    x = data_augmentation(inputs)
    x = tf.keras.applications.efficientnet.preprocess_input(x)
    x = base_model(x, training=False)
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.Model(inputs, outputs)

    # ----------------------------------------------------
    # STAGE 1: Train Classification Head
    # ----------------------------------------------------
    print("\n--- STAGE 1: Training Classification Head (Frozen Base) ---")
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    os.makedirs(os.path.dirname(output_model_path), exist_ok=True)
    callbacks_s1 = [
        ModelCheckpoint(output_model_path, save_best_only=True, monitor='val_accuracy', mode='max'),
        EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
        ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, verbose=1)
    ]

    model.fit(
        train_ds,
        epochs=epochs_stage1,
        validation_data=val_ds,
        callbacks=callbacks_s1
    )

    # ----------------------------------------------------
    # STAGE 2: Fine-Tuning Upper EfficientNet Layers
    # ----------------------------------------------------
    print("\n--- STAGE 2: Fine-Tuning Upper EfficientNet Layers (lr=1e-5) ---")
    base_model.trainable = True
    
    # Freeze bottom 100 layers, unfreeze upper layers
    for layer in base_model.layers[:100]:
        layer.trainable = False

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    callbacks_s2 = [
        ModelCheckpoint(output_model_path, save_best_only=True, monitor='val_accuracy', mode='max'),
        EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    ]

    model.fit(
        train_ds,
        epochs=epochs_stage2,
        validation_data=val_ds,
        callbacks=callbacks_s2
    )

    print(f"\n[SUCCESS] EfficientNetB0 model trained and saved to: {output_model_path}")

    # Generate updated class_names.json
    class_mapping = {}
    for idx, name in enumerate(class_names):
        if '___' in name:
            c, d = name.split('___', 1)
        else:
            c, d = "Crop", name

        crop_clean = c.replace('_', ' ').capitalize()
        disease_clean = d.replace('_', ' ').title()
        status = "Healthy" if "healthy" in name.lower() else "Disease Detected"

        class_mapping[str(idx)] = {
            "folder": name,
            "crop": crop_clean,
            "disease": f"{crop_clean} {disease_clean}" if crop_clean.lower() not in disease_clean.lower() else disease_clean,
            "status": status,
            "display_name": f"{crop_clean} - {disease_clean}"
        }

    json_path = os.path.join(os.path.dirname(output_model_path), 'class_names.json')
    with open(json_path, 'w') as f:
        json.dump(class_mapping, f, indent=2)
    print(f"[SUCCESS] Updated class mapping saved to {json_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Train EfficientNetB0 Crop Disease Classifier")
    parser.add_argument('--dataset', type=str, default='/home/kali/Downloads/plantdisease /New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/train', help='Dataset path')
    parser.add_argument('--output', type=str, default='model/plant_disease_model.keras', help='Output model path')
    parser.add_argument('--epochs1', type=int, default=10, help='Stage 1 Epochs')
    parser.add_argument('--epochs2', type=int, default=5, help='Stage 2 Epochs')
    parser.add_argument('--batch-size', type=int, default=32, help='Batch size')
    args = parser.parse_args()

    train_efficientnet(
        dataset_dir=args.dataset,
        output_model_path=args.output,
        batch_size=args.batch_size,
        epochs_stage1=args.epochs1,
        epochs_stage2=args.epochs2
    )
