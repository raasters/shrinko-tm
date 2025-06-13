import ffmpeg
import os
from datetime import datetime

def compress_video(input_path, output_folder):
    """
    Compress video file using ffmpeg
    """
    try:
        # Create output filename
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{name}_compressed_{timestamp}{ext}"
        output_path = os.path.join(output_folder, output_filename)
        
        # Get video information
        probe = ffmpeg.probe(input_path)
        video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
        width = int(video_info['width'])
        height = int(video_info['height'])
        
        # Calculate new dimensions (reduce by 50% if original is larger than 720p)
        if height > 720:
            new_height = 720
            new_width = int(width * (new_height / height))
        else:
            new_height = height
            new_width = width
        
        # Compress video
        stream = ffmpeg.input(input_path)
        stream = ffmpeg.filter(stream, 'scale', new_width, new_height)
        stream = ffmpeg.output(stream, output_path,
                             **{'c:v': 'libx264',
                                'crf': '28',  # Constant Rate Factor (18-28 is good, higher means more compression)
                                'preset': 'medium',
                                'c:a': 'aac',
                                'b:a': '128k'})
        ffmpeg.run(stream, overwrite_output=True)
        
        return output_path
        
    except Exception as e:
        print(f"Error compressing video: {str(e)}")
        return None 