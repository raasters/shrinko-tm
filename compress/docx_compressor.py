from docx2pdf import convert
import os
from datetime import datetime

def compress_docx(input_path, output_folder):
    """
    Convert DOCX to PDF and compress it
    """
    try:
        # Create output filename
        filename = os.path.basename(input_path)
        name, _ = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{name}_converted_{timestamp}.pdf"
        output_path = os.path.join(output_folder, output_filename)
        
        # Convert DOCX to PDF
        convert(input_path, output_path)
        
        # Now compress the PDF
        from .pdf_compressor import compress_pdf
        compressed_path = compress_pdf(output_path, output_folder)
        
        # Remove the intermediate PDF if compression was successful
        if compressed_path and os.path.exists(output_path):
            os.remove(output_path)
            
        return compressed_path
        
    except Exception as e:
        print(f"Error converting DOCX: {str(e)}")
        return None 