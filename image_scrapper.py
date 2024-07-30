from selenium import webdriver
from PIL import Image
import urllib.request
import os

from selenium.webdriver.common.by import By


def download_images(keyword, n):
    path = f"downloaded_images/{keyword}"
    # Set up the webdriver and navigate to Google Images
    driver = webdriver.Firefox()
    driver.get(f"https://www.google.com/search?q={keyword}&source=lnms&tbm=isch")

    # Find the image elements and extract the source URLs
    img_urls = [img.get_attribute('src') for img in driver.find_elements(By.TAG_NAME, "img")]

    # Ensure the data directory exists
    if not os.path.exists(path):
        os.makedirs(path)

    # Download and save the images
    for i, url in enumerate(img_urls[:n]):
        try:
            # Skip if i < 2
            if i < 2:
                continue

            # Skip if the URL is None
            if url is None:
                print(f"Skipping image {i} due to missing URL")
                continue

            # Download the image
            urllib.request.urlretrieve(url, f"{path}/temp.png")

            # Open the image and resize it
            img = Image.open(f"{path}/temp.png")
            img = img.resize((100, 100))

            # Save the image to the specified location
            img.save(f"{path}/{keyword}_{i}.png")

        except Exception as e:
            print(f"Error downloading image {i}: {e}")

    # Delete the temporary image
    if os.path.exists(f"{path}/temp.png"):
        os.remove(f"{path}/temp.png")

    # Close the webdriver
    driver.close()
