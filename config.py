import os
from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your-secret-key'
    DEEP_SEEK_API_KEY = os.getenv('DEEP_SEEK_API_KEY')
    PROXY_USERNAME = os.getenv('PROXY_USERNAME')
    PROXY_PASSWORD = os.getenv('PROXY_PASSWORD')