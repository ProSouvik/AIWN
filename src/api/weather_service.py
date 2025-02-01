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
    
    def get_current_weather(self, city: str) -> WeatherData:
        url = f"{self.base_url}/weather"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch weather data: {response.json()['message']}")
            
        data = response.json()
        return WeatherData.from_api_response(data)
    
    def get_forecast(self, city: str) -> List[ForecastData]:
        url = f"{self.base_url}/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch forecast data: {response.json()['message']}")
            
        data = response.json()
        return [ForecastData.from_api_response(item) for item in data['list']] 