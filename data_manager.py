from PIL import Image
import os
import shutil
from math import ceil


def rename(name, path):
    # Rename the images in the specified directory
    for i, filename in enumerate(os.listdir(path)):
        os.rename(f"{path}/{filename}", f"{path}/{name}.{i}.png")


def image_resize(size, path):
    # Iterate through all images in the specified directory
    for filename in os.listdir(path):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            img_path = os.path.join(path, filename)

            # Open the image
            img = Image.open(img_path)

            # Check if the image needs to be resized
            if img.size != (size, size):
                # Resize the image
                img = img.resize((size, size))

                # Save the resized image back to the file as PNG
                base_filename = os.path.splitext(filename)[0]
                img.save(os.path.join(path, f"{base_filename}.png"))

                # Delete the original image if it's not a PNG
                if not filename.endswith(".png"):
                    os.remove(img_path)


def add_data(name, src_path):
    # Call image_resize function
    image_resize(100, src_path)

    # Get list of all files in src_path
    files = os.listdir(src_path)

    # Calculate the number of files to move for training (80%)
    num_train_files = ceil(len(files) * 0.8)

    # Create directories if they don't exist
    train_dir = f'datasets/train/{name}'
    test_dir = f'datasets/test/{name}'
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Clear existing files in train_dir and test_dir
    for filename in os.listdir(train_dir):
        os.remove(os.path.join(train_dir, filename))
    for filename in os.listdir(test_dir):
        os.remove(os.path.join(test_dir, filename))

    # Move files to train directory and rename them
    for i in range(num_train_files):
        shutil.move(f'{src_path}/{files[i]}', f'{train_dir}/{files[i]}')
    rename(name, train_dir)

    # Move remaining files to test directory and rename them
    for i in range(num_train_files, len(files)):
        shutil.move(f'{src_path}/{files[i]}', f'{test_dir}/{files[i]}')
    rename(name, test_dir)
