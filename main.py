import pytesseract
from PIL import ImageGrab
import keyboard

# Set the path to the tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def take_screenshot():
    """
    Captures the entire screen.
    """
    print("Taking screenshot...")
    screenshot = ImageGrab.grab()
    return screenshot

def extract_text_from_image(image):
    """
    Extracts text from a given image using pytesseract.
    """
    print("Extracting text from image...")
    try:
        text = pytesseract.image_to_string(image)
        return text
    except pytesseract.TesseractNotFoundError:
        return "Tesseract is not installed or not in your PATH. Please install Tesseract OCR."

def screenshot_and_ocr():
    """
    Takes a screenshot and performs OCR on it.
    """
    # 1. Capture the screenshot
    captured_image = take_screenshot()
    
    # 2. Extract text from the screenshot
    extracted_text = extract_text_from_image(captured_image)
    
    # 3. Print the extracted text
    print("\n--- Extracted Text ---")
    print(extracted_text)
    print("----------------------")

if __name__ == "__main__":
    print("Press 'Shift + S' to take a screenshot and extract text.")
    print("Press 'esc' to stop.")
    
    # Set up the hotkey
    keyboard.add_hotkey('shift+s', screenshot_and_ocr)
    
    # Keep the script running to listen for the hotkey
    keyboard.wait('esc')
