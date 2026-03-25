## Getting API Keys

### OpenAI API Key

1. Go to https://platform.openai.com/
2. Sign up or log in to your account
3. Navigate to "API keys" section
4. Click "Create new secret key"
5. Copy and save the key in your `.env` file

### ElevenLabs API Key

1. Visit https://elevenlabs.io/
2. Sign up or log in
3. Go to "Profile" → "API Key"
4. Copy your API key
5. Add it to your `.env` file

### YouTube API Key

1. Go to https://console.developers.google.com/
2. Create a new project
3. Enable YouTube Data API v3
4. Create OAuth 2.0 credentials (Desktop application)
5. Download the credentials JSON
6. Copy the API key to `.env` file

### Getting YouTube Channel ID

1. Sign in to YouTube
2. Click your profile icon
3. Select "Create a channel" or go to channel settings
4. Your Channel ID is displayed in the "Basic info" section
5. Add it to `.env` file

## Security Notes

- Never commit `.env` file to Git
- Keep your API keys confidential
- Rotate keys regularly for security
- Use environment variables in production