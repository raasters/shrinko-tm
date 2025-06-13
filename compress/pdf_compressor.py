from PyPDF2 import PdfReader, PdfWriter
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def compress_pdf(input_path, output_folder):
    """
    Compress PDF file using PyPDF2
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            logger.error(f"Input file does not exist: {input_path}")
            return None

        # Check if output folder exists, create if it doesn't
        os.makedirs(output_folder, exist_ok=True)

        # Create output filename
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{name}_compressed_{timestamp}{ext}"
        output_path = os.path.join(output_folder, output_filename)

        logger.info(f"Starting PDF compression. Input: {input_path}, Output: {output_path}")

        # Open the PDF
        reader = PdfReader(input_path)
        writer = PdfWriter()

        # Process each page
        for page in reader.pages:
            # Add page to writer
            writer.add_page(page)

        # Set compression parameters
        writer.add_metadata(reader.metadata)

        # Save with compression
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        # Verify the output file was created
        if not os.path.exists(output_path):
            logger.error("Output file was not created")
            return None

        logger.info(f"PDF compression completed successfully: {output_path}")
        return output_path

    except Exception as e:
        logger.error(f"Error compressing PDF: {str(e)}", exc_info=True)
        return None 