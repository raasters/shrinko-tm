try:
    from PIL import Image
except ImportError:
    import Image

import os
from datetime import datetime

def compress_image(input_path, output_folder):
    """
    Compress image file using Pillow
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Create output filename
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{name}_compressed_{timestamp}{ext}"
        output_path = os.path.join(output_folder, output_filename)
        
        # Convert to RGB if necessary
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Save with compression
        if ext.lower() in ['.jpg', '.jpeg']:
            img.save(output_path, 'JPEG', quality=60, optimize=True)
        elif ext.lower() == '.png':
            img.save(output_path, 'PNG', optimize=True)
        else:
            img.save(output_path)
            
        return output_path
        
    except Exception as e:
        print(f"Error compressing image: {str(e)}")
        return None 