import pytest
from src.models.weather_data import WeatherData

def test_weather_data_creation():
    sample_api_response = {
        'main': {
            'temp': 20.5,
            'humidity': 65,
            'feels_like': 21.0
        },
        'weather': [{'description': 'clear sky', 'icon': '01d'}],
        'name': 'London',
        'sys': {'country': 'GB'},
        'wind': {'speed': 5.2}
    }
    
    weather_data = WeatherData.from_api_response(sample_api_response)
    
    assert weather_data.temperature == 20.5
    assert weather_data.humidity == 65
    assert weather_data.city == 'London' 