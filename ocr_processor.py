# ocr_processor_log.py

import os
import sys
import base64
import argparse
import logging
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_mistral_client() -> Mistral:
    """Initializes and returns the Mistral client."""
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY environment variable not set.")
    return Mistral(api_key=api_key)

def process_pdf_ocr(client: Mistral, file_path: str):
    """
    Reads a PDF, sends it to Mistral OCR, and prints the extracted markdown.
    """
    logging.info(f"Reading PDF file: {file_path}...")
    try:
        with open(file_path, "rb") as f:
            pdf_bytes = f.read()
        logging.info("PDF file read successfully.")
    except FileNotFoundError:
        logging.error(f"File not found at '{file_path}'.")
        sys.exit(1)

    b64_string = base64.b64encode(pdf_bytes).decode('utf-8')
    document_url = f"data:application/pdf;base64,{b64_string}"

    logging.info("Sending request to Mistral OCR API...")
    try:
        resp = client.ocr.process(
            model="mistral-ocr-latest",
            document={"type": "document_url", "document_url": document_url}
        )
        logging.info("Received response from Mistral.")

        if resp.pages:
            logging.info(f"Found {len(resp.pages)} page(s). Printing content.")
            for page in resp.pages:
                # Print the final result to standard output
                print(page.markdown)
        else:
            logging.warning("No text content found in the API response.")
            
    except Exception as e:
        logging.error(f"An issue occurred with the Mistral API: {e}")
        sys.exit(1)

def main():
    """Main function to parse arguments, configure logging, and run the OCR process."""
    parser = argparse.ArgumentParser(description="Extract text from a PDF using Mistral OCR API.")
    parser.add_argument("pdf_file", type=str, help="The path to the PDF file.")
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging to see step-by-step progress."
    )
    args = parser.parse_args()

    # Configure logging
    log_level = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(level=log_level, format='%(levelname)s: %(message)s')
    
    try:
        logging.info("Initializing Mistral client...")
        client = get_mistral_client()
        process_pdf_ocr(client, args.pdf_file)
        logging.info("Script finished successfully.")
    except ValueError as e:
        logging.critical(f"Configuration Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
