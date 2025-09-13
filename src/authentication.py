from parameters.allowed_ids import ALLOWED_IDS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def authenticate(document_number):
    """
    Checks if the provided document number is in the allowed list.
    Returns True if authenticated, False otherwise.
    """
    logging.info(f"Attempting authentication for document number: {document_number}")
    result = document_number in ALLOWED_IDS
    if result:
        logging.info(f"Authentication successful for document number: {document_number}")
    else:
        logging.warning(f"Authentication failed for document number: {document_number}")
    return result
