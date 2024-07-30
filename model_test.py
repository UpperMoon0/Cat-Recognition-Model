import tensorflow as tf
import os

from keras.src.utils import load_img, img_to_array


def test_model():
    # Load the trained model
    model = tf.keras.models.load_model('cat_recognition_model.keras')

    # Set your test data directory
    test_data_dir = 'datasets/test'

    # Iterate through test images
    for category in os.listdir(test_data_dir):
        category_dir = os.path.join(test_data_dir, category)
        for image_file in os.listdir(category_dir):
            image_path = os.path.join(category_dir, image_file)
            img = load_img(image_path, target_size=(100, 100))
            img_array = img_to_array(img) / 255.0  # Normalize pixel values
            img_array = tf.expand_dims(img_array, 0)  # Add batch dimension

            # Make predictions
            prediction = model.predict(img_array)
            if prediction[0][0] >= 0.5:
                result = "cat"
            else:
                result = "dog"

            print(f"Image: {image_file} | Prediction: {result}")
