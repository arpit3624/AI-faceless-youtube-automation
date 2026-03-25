## Setup Guide

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/arpit3624/ai-faceless-youtube-automation.git
cd ai-faceless-youtube-automation
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Copy `.env.example` to `.env` and fill in your API keys:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
- OpenAI API Key
- ElevenLabs API Key
- YouTube API Key

### Step 5: Run the Automation
```bash
python scripts/main.py
```

## Troubleshooting

### Import Errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt --upgrade
```

### API Key Issues
Verify your API keys are correctly set in the `.env` file.

### FFmpeg Not Found
Install FFmpeg:
- **Ubuntu/Debian:** `sudo apt-get install ffmpeg`
- **Mac:** `brew install ffmpeg`
- **Windows:** Download from https://ffmpeg.org/download.html

## Support
For issues, please create a GitHub issue or contact the maintainer.