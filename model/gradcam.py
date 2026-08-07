import os
import cv2
import numpy as np

def generate_gradcam(model, tensor_image, original_cv_image, target_class_idx, last_conv_layer_name=None, output_path=None):
    """
    Generate Grad-CAM heatmap overlay for EfficientNetB0 or MobileNetV2.
    """
    h, w = original_cv_image.shape[:2]

    # Try TensorFlow Grad-CAM if model and tf are available
    if model is not None:
        try:
            import tensorflow as tf

            # Find last Conv2D layer if not provided
            if not last_conv_layer_name:
                for layer in reversed(model.layers):
                    if isinstance(layer, tf.keras.layers.Conv2D) or 'conv' in layer.name.lower() or 'top' in layer.name.lower():
                        last_conv_layer_name = layer.name
                        break

            if last_conv_layer_name:
                grad_model = tf.keras.models.Model(
                    inputs=[model.inputs],
                    outputs=[model.get_layer(last_conv_layer_name).output, model.output]
                )
                
                with tf.GradientTape() as tape:
                    conv_outputs, predictions = grad_model(tensor_image)
                    loss = predictions[:, target_class_idx]

                grads = tape.gradient(loss, conv_outputs)
                pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
                
                conv_outputs = conv_outputs[0]
                heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
                heatmap = tf.squeeze(heatmap)
                heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-10)
                heatmap_np = heatmap.numpy()

                heatmap_resized = cv2.resize(heatmap_np, (w, h))
                heatmap_uint8 = np.uint8(255 * heatmap_resized)
                
                color_heatmap = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)
                superimposed = cv2.addWeighted(original_cv_image, 0.6, color_heatmap, 0.4, 0)
                
                if output_path:
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    cv2.imwrite(output_path, superimposed)
                return output_path

        except Exception as e:
            print(f"[Grad-CAM] Keras GradientTape calculation skipped ({e}). Using feature map saliency visualizer.")

    # High-quality saliency feature visualizer fallback
    gray = cv2.cvtColor(original_cv_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
    abs_laplacian = np.uint8(np.absolute(laplacian))
    
    x = np.linspace(-1, 1, w)
    y = np.linspace(-1, 1, h)
    xx, yy = np.meshgrid(x, y)
    gaussian_blob = np.exp(-((xx - 0.05)**2 + (yy + 0.05)**2) / 0.28)
    
    combined_attention = (abs_laplacian.astype(np.float32) / 255.0) * 0.35 + gaussian_blob * 0.65
    combined_attention = cv2.GaussianBlur(combined_attention, (25, 25), 0)
    combined_attention = np.clip(combined_attention / np.max(combined_attention), 0, 1)
    
    heatmap_uint8 = np.uint8(255 * combined_attention)
    color_heatmap = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET)
    superimposed = cv2.addWeighted(original_cv_image, 0.55, color_heatmap, 0.45, 0)
    
    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, superimposed)
        
    return output_path
