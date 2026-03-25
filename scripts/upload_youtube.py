import os
import logging
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.urllib3 import Request as UrllibRequest
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class YouTubeUploader:
    def __init__(self):
        self.api_key = os.getenv("YOUTUBE_API_KEY")
        self.scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    
    def authenticate(self):
        """Authenticate with YouTube API."""
        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', self.scopes)
            credentials = flow.run_local_server(port=0)
            return build('youtube', 'v3', credentials=credentials)
        except Exception as e:
            logger.error(f"Authentication error: {str(e)}")
            raise
    
    def upload_video(self, video_path: str, title: str, description: str) -> str:
        """Upload video to YouTube."""
        try:
            youtube = self.authenticate()
            
            request_body = {
                'snippet': {
                    'title': title,
                    'description': description,
                    'tags': ['automation', 'AI'],
                    'categoryId': '28'
                },
                'status': {
                    'privacyStatus': 'public'
                }
            }
            
            media_file = MediaFileUpload(video_path, chunksize=1024*1024, resumable=True)
            request = youtube.videos().insert(
                part='snippet,status',
                body=request_body,
                media_body=media_file
            )
            
            response = request.execute()
            video_id = response['id']
            logger.info(f"✓ Video uploaded successfully. ID: {video_id}")
            return video_id
        except Exception as e:
            logger.error(f"Upload error: {str(e)}")
            raise

if __name__ == "__main__":
    uploader = YouTubeUploader()
    print("YouTube uploader ready")