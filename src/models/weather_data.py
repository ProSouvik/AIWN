from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class WeatherData:
    """Data class to store weather information"""
    temperature: float
    humidity: int
    wind_speed: float
    description: str
    icon: str
    city: str
    lat: float = 51.5074  # Default to London
    lon: float = -0.1278
    
    @classmethod
    def from_api_response(cls, data: dict) -> 'WeatherData':
        """Create WeatherData instance from API response"""
        return cls(
            temperature=data['main']['temp'],
            humidity=data['main']['humidity'],
            wind_speed=data['wind']['speed'],
            description=data['weather'][0]['description'],
            icon=data['weather'][0]['icon'],
            city=data['name'],
            lat=data['coord']['lat'],
            lon=data['coord']['lon']
        )

@dataclass
class ForecastData:
    temperature: float
    humidity: int
    wind_speed: float
    description: str
    icon: str
    datetime: datetime
    
    @classmethod
    def from_api_response(cls, data: dict) -> 'ForecastData':
        return cls(
            temperature=data['main']['temp'],
            humidity=data['main']['humidity'],
            wind_speed=data['wind']['speed'],
            description=data['weather'][0]['description'],
            icon=data['weather'][0]['icon'],
            datetime=datetime.fromtimestamp(data['dt'])
        ) 