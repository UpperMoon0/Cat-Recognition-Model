import tensorflow as tf
import os
from keras.src.utils import load_img, img_to_array

model = tf.keras.models.load_model('computer_vision_model.keras')

test_data_dir = 'datasets/test'

# Manually specify class names or retrieve from model training
class_names = ['car', 'cat', 'food']

# Initialize counters
total_counts = {class_name: 0 for class_name in class_names}
correct_counts = {class_name: 0 for class_name in class_names}

for category in os.listdir(test_data_dir):
    category_dir = os.path.join(test_data_dir, category)
    for image_file in os.listdir(category_dir):
        image_path = os.path.join(category_dir, image_file)
        img = load_img(image_path, target_size=(100, 100))
        img_array = img_to_array(img) / 255.0
        img_array = tf.expand_dims(img_array, 0)

        predictions = model.predict(img_array)
        probabilities = predictions[0]
        predicted_class_index = int(tf.argmax(probabilities))
        predicted_class = class_names[predicted_class_index]

        # Extract actual class from the image file name
        actual_class = image_file.split('.')[0]

        # Update counters
        total_counts[actual_class] += 1
        if predicted_class == actual_class:
            correct_counts[actual_class] += 1

        print(f"Image: {image_file}")
        for i, prob in enumerate(probabilities):
            print(f"Class: {class_names[i]} | Probability: {prob:.4f}")
        print(f"Predicted Class: {predicted_class}")
        print("-" * 30)

for class_name in class_names:
    percentage = (correct_counts[class_name] / total_counts[class_name]) * 100 if total_counts[class_name] > 0 else 0
    print(f"Accuracy for {class_name}: {correct_counts[class_name]} / {total_counts[class_name]} ({percentage:.2f}%)")