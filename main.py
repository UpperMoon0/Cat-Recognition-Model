import pytesseract
from PIL import ImageGrab
import keyboard
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Set the path to the tesseract executable if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

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

def extract_info_with_gemini(text):
    """
    Uses Gemini to extract relevant information from text.
    """
    print("Sending text to Gemini API...")
    try:
        response = model.generate_content(f"Extract the most relevant information from this text:\n\n{text}")
        return response.text
    except Exception as e:
        return f"An error occurred with the Gemini API: {e}"

def screenshot_and_process():
    """
    Takes a screenshot, performs OCR, and extracts info with Gemini.
    """
    # 1. Capture the screenshot
    captured_image = take_screenshot()
    
    # 2. Extract text from the screenshot
    extracted_text = extract_text_from_image(captured_image)
    
    if "Tesseract is not installed" in extracted_text:
        print(extracted_text)
        return

    print("\n--- Extracted Text ---")
    print(extracted_text)
    print("----------------------")

    # 3. Extract relevant information using Gemini
    gemini_extraction = extract_info_with_gemini(extracted_text)

    print("\n--- Gemini Extraction ---")
    print(gemini_extraction)
    print("-------------------------")


if __name__ == "__main__":
    print("Press 'Alt + S' to take a screenshot and extract text.")
    print("Press 'esc' to stop.")
    
    # Set up the hotkey
    keyboard.add_hotkey('alt+s', screenshot_and_process)
    
    # Keep the script running to listen for the hotkey
    keyboard.wait('esc')
