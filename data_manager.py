import os


def rename(path):
    # Rename the images in the specified directory
    for i, filename in enumerate(os.listdir(path)):
        os.rename(f"{path}/{filename}", f"{path}/{i}.png")
