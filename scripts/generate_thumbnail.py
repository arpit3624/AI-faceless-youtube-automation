import os
import logging
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ThumbnailGenerator:
    def __init__(self):
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_thumbnail(self, title: str, output_path: str = "output/thumbnail.png") -> str:
        """Generate YouTube thumbnail image."""
        try:
            # Create image
            img = Image.new('RGB', (1280, 720), color='red')
            draw = ImageDraw.Draw(img)
            
            # Add title text
            text_color = 'white'
            draw.text((640, 360), title, fill=text_color, anchor='mm')
            
            # Save
            img.save(output_path)
            logger.info(f"✓ Thumbnail generated: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Error generating thumbnail: {str(e)}")
            raise

if __name__ == "__main__":
    generator = ThumbnailGenerator()
    print("Thumbnail generator ready")