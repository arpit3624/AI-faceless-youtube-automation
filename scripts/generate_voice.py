import requests

class VoiceGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'https://api.elevenlabs.io/generate'

    def generate_voiceover(self, text):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'text': text,
            'voice': 'default'
        }
        response = requests.post(self.api_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()['voiceover_url']
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')
