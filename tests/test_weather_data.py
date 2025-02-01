import pytest
from src.models.weather_data import WeatherData, ForecastData
from datetime import datetime

def test_weather_data_creation():
    data = {
        'main': {
            'temp': 20.5,
            'humidity': 65
        },
        'wind': {
            'speed': 5.2
        },
        'weather': [{
            'description': 'clear sky',
            'icon': '01d'
        }],
        'name': 'London'
    }
    
    weather = WeatherData.from_api_response(data)
    
    assert weather.temperature == 20.5
    assert weather.humidity == 65
    assert weather.wind_speed == 5.2
    assert weather.description == 'clear sky'
    assert weather.icon == '01d'
    assert weather.city == 'London'

def test_forecast_data_creation():
    data = {
        'main': {
            'temp': 22.5,
            'humidity': 70
        },
        'wind': {
            'speed': 4.8
        },
        'weather': [{
            'description': 'scattered clouds',
            'icon': '03d'
        }],
        'dt': 1625097600
    }
    
    forecast = ForecastData.from_api_response(data)
    
    assert forecast.temperature == 22.5
    assert forecast.humidity == 70
    assert forecast.wind_speed == 4.8
    assert forecast.description == 'scattered clouds'
    assert forecast.icon == '03d'
    assert isinstance(forecast.datetime, datetime) 