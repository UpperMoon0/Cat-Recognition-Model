from PIL import Image
import os


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
