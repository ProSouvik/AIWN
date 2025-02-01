import requests
from typing import Optional
from ..models.weather_data import WeatherData
from ..config import WEATHER_API_KEY

class WeatherService:
    """Service class to handle weather API interactions"""
    
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key: str = WEATHER_API_KEY):
        self.api_key = api_key
    
    def get_weather(self, city: str, units: str = 'metric') -> Optional[WeatherData]:
        """Fetch weather data for a given city"""
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': units
            }
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            
            return WeatherData.from_api_response(response.json())
        except requests.RequestException:
            return None 