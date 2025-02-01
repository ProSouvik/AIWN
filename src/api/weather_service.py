from abc import ABC, abstractmethod
import requests
from typing import Dict, List
from src.models.weather_data import WeatherData, ForecastData

class WeatherServiceInterface(ABC):
    @abstractmethod
    def get_current_weather(self, city: str) -> WeatherData:
        pass
    
    @abstractmethod
    def get_forecast(self, city: str) -> List[ForecastData]:
        pass

class WeatherService(WeatherServiceInterface):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def _format_location(self, location: str) -> str:
        """Format location string for API request"""
        # Replace spaces around comma with just comma
        return location.replace(" ,", ",").replace(", ", ",")
    
    def get_current_weather(self, city: str) -> WeatherData:
        url = f"{self.base_url}/weather"
        formatted_city = self._format_location(city)
        params = {
            "q": formatted_city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise exception for non-200 status codes
            data = response.json()
            return WeatherData.from_api_response(data)
        except requests.exceptions.RequestException as e:
            if response.status_code == 404:
                raise Exception(f"Location '{city}' not found. Please check the spelling and try again.")
            raise Exception(f"Failed to fetch weather data: {str(e)}")
    
    def get_forecast(self, city: str) -> List[ForecastData]:
        url = f"{self.base_url}/forecast"
        formatted_city = self._format_location(city)
        params = {
            "q": formatted_city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return [ForecastData.from_api_response(item) for item in data['list']]
        except requests.exceptions.RequestException as e:
            if response.status_code == 404:
                raise Exception(f"Location '{city}' not found. Please check the spelling and try again.")
            raise Exception(f"Failed to fetch forecast data: {str(e)}") 