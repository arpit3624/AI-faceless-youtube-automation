import os
import logging
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip, AudioFileClip

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VideoGenerator:
    def __init__(self):
        self.output_dir = "output"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_video(self, voiceover_path: str, background_music_path: str = None, output_path: str = "output/video.mp4") -> str:
        """Create video from voiceover and background music."""
        try:
            audio = AudioFileClip(voiceover_path)
            duration = audio.duration
            
            # Create a simple background (black screen)
            background = ColorClip(size=(1920, 1080), color=(0, 0, 0), duration=duration)
            
            # Add text overlay
            txt_clip = TextClip("AI Generated Video", fontsize=70, color='white', duration=duration)
            txt_clip = txt_clip.set_position('center')
            
            # Compose video
            video = CompositeVideoClip([background, txt_clip])
            video = video.set_audio(audio)
            
            # Write output
            video.write_videofile(output_path, fps=30, codec='libx264', audio_codec='aac')
            logger.info(f"✓ Video created: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Error creating video: {str(e)}")
            raise

if __name__ == "__main__":
    generator = VideoGenerator()
    print("Video generator ready")
