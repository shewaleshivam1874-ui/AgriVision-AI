#!/usr/bin/env python3
"""
AgriVision AI - Model Evaluation & Misclassification Analysis
Evaluates EfficientNetB0 vs MobileNetV2 on untouched test dataset.
Computes Accuracy, Precision, Recall, F1, Confusion Matrix, & Misclassifications.
"""

import os
import json
import argparse
import numpy as np

def evaluate_test_set(model_path, test_dataset_dir, class_names_path='model/class_names.json'):
    """
    Perform full test set evaluation and misclassification diagnostic.
    """
    try:
        import tensorflow as tf
        from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support
    except ImportError:
        print("[ERROR] TensorFlow and scikit-learn are required for model evaluation.")
        return

    print("==================================================")
    print("  AgriVision AI - Test Set Evaluation Engine")
    print("==================================================")
    print(f"Model File     : {model_path}")
    print(f"Test Dataset   : {test_dataset_dir}")

    if not os.path.exists(model_path):
        print(f"[ERROR] Model file {model_path} not found.")
        return

    if not os.path.exists(test_dataset_dir):
        print(f"[ERROR] Test dataset directory {test_dataset_dir} not found.")
        return

    # Load Model & Class Names
    model = tf.keras.models.load_model(model_path)
    with open(class_names_path, 'r') as f:
        class_mapping = json.load(f)

    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        test_dataset_dir,
        image_size=(224, 224),
        batch_size=32,
        shuffle=False
    )

    class_names = test_ds.class_names
    y_true = []
    y_pred = []
    y_conf = []

    print("\nRunning inference on test dataset...")
    for images, labels in test_ds:
        preds = model.predict(images, verbose=0)
        top_classes = np.argmax(preds, axis=1)
        confidences = np.max(preds, axis=1)
        
        y_true.extend(labels.numpy())
        y_pred.extend(top_classes)
        y_conf.extend(confidences)

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_conf = np.array(y_conf)

    # Compute Metrics
    accuracy = np.mean(y_true == y_pred) * 100.0
    precision, recall, f1, _ = precision_recall_fscore_support(y_true, y_pred, average='macro')
    _, _, f1_weighted, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')

    print("\n--------------------------------------------------")
    print("  TEST EVALUATION METRICS REPORT")
    print("--------------------------------------------------")
    print(f"Test Accuracy   : {accuracy:.2f}%")
    print(f"Macro Precision : {precision*100:.2f}%")
    print(f"Macro Recall    : {recall*100:.2f}%")
    print(f"Macro F1 Score  : {f1*100:.2f}%")
    print(f"Weighted F1     : {f1_weighted*100:.2f}%")

    # Classification Report
    print("\nPer-Class Performance Summary (First 10 Classes):")
    report = classification_report(y_true, y_pred, target_names=class_names, output_dict=True)
    for idx, name in enumerate(class_names[:10]):
        metrics = report[name]
        print(f"  - {name}: Precision={metrics['precision']*100:.1f}%, Recall={metrics['recall']*100:.1f}%, F1={metrics['f1-score']*100:.1f}%")

    # Misclassification Diagnostics
    misclassified_indices = np.where(y_true != y_pred)[0]
    print(f"\nTotal Misclassified Test Samples: {len(misclassified_indices)} / {len(y_true)}")

    if len(misclassified_indices) > 0:
        print("\nSample Misclassifications:")
        for idx in misclassified_indices[:5]:
            true_cls = class_names[y_true[idx]]
            pred_cls = class_names[y_pred[idx]]
            conf = y_conf[idx] * 100.0
            print(f"  - Actual: '{true_cls}' | Predicted: '{pred_cls}' | Confidence: {conf:.1f}%")

    # Confidence Calibration Summary
    high_conf = np.mean(y_conf >= 0.85) * 100.0
    med_conf = np.mean((y_conf >= 0.60) & (y_conf < 0.85)) * 100.0
    low_conf = np.mean(y_conf < 0.60) * 100.0

    print("\nConfidence Calibration Distribution:")
    print(f"  - High Confidence (>=85%)  : {high_conf:.1f}% of test samples")
    print(f"  - Medium Confidence (60-84%): {med_conf:.1f}% of test samples")
    print(f"  - Low Confidence (<60%)     : {low_conf:.1f}% of test samples")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Evaluate AgriVision AI Model Performance")
    parser.add_argument('--model', type=str, default='model/plant_disease_model.keras', help='Model path')
    parser.add_argument('--test-dir', type=str, default='/home/kali/Downloads/plantdisease /New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/valid', help='Test dataset path')
    args = parser.parse_args()

    evaluate_test_set(args.model, args.test_dir)
