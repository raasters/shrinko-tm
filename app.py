from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
import logging
from compress.pdf_compressor import compress_pdf
from compress.image_compressor import compress_image
from compress.video_compressor import compress_video
from compress.docx_compressor import compress_docx

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Configuration
UPLOAD_FOLDER = 'static/uploads'
COMPRESSED_FOLDER = 'static/compressed'
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'jpg', 'jpeg', 'png', 'mp4'}
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['COMPRESSED_FOLDER'] = COMPRESSED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create necessary folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            logger.warning('No file part in request')
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            logger.warning('No selected file')
            flash('No file selected')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            try:
                file.save(file_path)
                logger.info(f'File saved successfully at {file_path}')
                
                # Process file based on extension
                file_ext = filename.rsplit('.', 1)[1].lower()
                compressed_path = None
                
                logger.info(f'Processing file with extension: {file_ext}')
                
                try:
                    if file_ext in ['pdf']:
                        logger.info('Attempting PDF compression')
                        compressed_path = compress_pdf(file_path, app.config['COMPRESSED_FOLDER'])
                    elif file_ext in ['docx']:
                        logger.info('Attempting DOCX compression')
                        compressed_path = compress_docx(file_path, app.config['COMPRESSED_FOLDER'])
                    elif file_ext in ['jpg', 'jpeg', 'png']:
                        logger.info('Attempting image compression')
                        compressed_path = compress_image(file_path, app.config['COMPRESSED_FOLDER'])
                    elif file_ext in ['mp4']:
                        logger.info('Attempting video compression')
                        compressed_path = compress_video(file_path, app.config['COMPRESSED_FOLDER'])
                    
                    if compressed_path:
                        logger.info(f'Compression successful. Output file: {compressed_path}')
                        return render_template('download.html', 
                                            filename=os.path.basename(compressed_path),
                                            compressed_path=compressed_path)
                    else:
                        logger.error('Compression failed - no output path returned')
                        flash('Compression failed - please try again')
                        return redirect(request.url)
                        
                except Exception as e:
                    logger.error(f'Error during compression: {str(e)}', exc_info=True)
                    flash(f'Error during compression: {str(e)}')
                    return redirect(request.url)
                    
            except Exception as e:
                logger.error(f'Error saving file: {str(e)}', exc_info=True)
                flash(f'Error saving file: {str(e)}')
                return redirect(request.url)
                
        else:
            logger.warning(f'Invalid file type: {file.filename}')
            flash('File type not allowed')
            return redirect(request.url)
            
    return render_template('upload.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download/<filename>')
def download_file(filename):
    try:
        file_path = os.path.join(app.config['COMPRESSED_FOLDER'], filename)
        logger.info(f'Attempting to download file: {file_path}')
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        logger.error(f'Error downloading file: {str(e)}', exc_info=True)
        flash('Error downloading file')
        return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(debug=True) 