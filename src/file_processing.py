from PIL import Image
import streamlit as st
import logging
from datetime import datetime
import pytz
import fitz

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_file(uploaded_file):
    """
    Processes the uploaded file. Converts PDFs or images to JPG format, saves the image, and converts it to a PDF.
    """
    logging.info(f"Processing uploaded file: {uploaded_file.name}")
    try:
        # Convert to JPG if not already
        if uploaded_file.type == "application/pdf":
            image = process_pdf_with_pymupdf(uploaded_file.getbuffer())
        else:
            image = Image.open(uploaded_file)
            image = image.convert("RGB")

        # Save the image as JPG
        jpg_path = save_image(image)


        logging.info(f"Image saved as {jpg_path}.")
        return jpg_path, uploaded_file.name
    except Exception as e:
        logging.error(f"Error processing file: {e}")
        raise

def process_pdf_with_pymupdf(pdf_bytes):
    """Converts the first page of a PDF (provided as bytes) to an image using PyMuPDF."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    page = doc[0]  # Get the first page
    pix = page.get_pixmap()  # Render page to an image
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return image

def save_image(image):
    """Saves an image as a JPG file with a timestamp."""
    colombia_tz = pytz.timezone('America/Bogota')
    datetim = datetime.now(colombia_tz).strftime("%Y%m%d_%H%M%S")
    jpg_path = f"{datetim}.jpg"
    image.save(jpg_path, "JPEG")
    return jpg_path
