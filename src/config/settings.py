import os
from dotenv import load_dotenv

class Settings:
    """Configuration settings for the weather app"""
    
    def __init__(self):
        load_dotenv()
        self.OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
        if not self.OPENWEATHER_API_KEY:
            raise ValueError("OpenWeatherMap API key not found. Please set OPENWEATHER_API_KEY in .env file") 