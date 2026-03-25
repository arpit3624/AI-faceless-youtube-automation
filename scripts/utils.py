import os
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_config(config_path):
    """Load JSON configuration from a file."""
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
            logging.info('Configuration loaded successfully.')
            return config
    except FileNotFoundError:
        logging.error(f'Config file not found: {config_path}')
    except json.JSONDecodeError:
        logging.error('Error decoding JSON from the config file.')
    return None


def create_directory(directory_path):
    """Create a directory if it does not exist."""
    try:
        os.makedirs(directory_path, exist_ok=True)
        logging.info(f'Directory created or already exists: {directory_path}')
    except Exception as e:
        logging.error(f'Error creating directory {directory_path}: {str(e)}')


def log_message(message):
    """Log a message to the console."""
    logging.info(message)