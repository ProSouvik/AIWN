import pytest
from src.api.weather_service import WeatherService
from src.models.weather_data import WeatherData, ForecastData

def test_weather_service_initialization():
    service = WeatherService(api_key="test_key")
    assert service.api_key == "test_key"

def test_get_weather_invalid_city():
    service = WeatherService(api_key="test_key")
    result = service.get_weather("NonExistentCity123456789")
    assert result is None

def test_get_current_weather(mocker):
    # Mock API response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "main": {
            "temp": 20.5,
            "humidity": 65
        },
        "wind": {
            "speed": 5.2
        },
        "weather": [{
            "description": "clear sky",
            "icon": "01d"
        }],
        "name": "London"
    }
    
    mocker.patch('requests.get', return_value=mock_response)
    
    weather_service = WeatherService("fake_api_key")
    result = weather_service.get_current_weather("London")
    
    assert isinstance(result, WeatherData)
    assert result.temperature == 20.5
    assert result.city == "London"

def test_get_forecast(mocker):
    # Mock API response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "list": [{
            "main": {
                "temp": 22.5,
                "humidity": 70
            },
            "wind": {
                "speed": 4.8
            },
            "weather": [{
                "description": "scattered clouds",
                "icon": "03d"
            }],
            "dt": 1625097600
        }]
    }
    
    mocker.patch('requests.get', return_value=mock_response)
    
    weather_service = WeatherService("fake_api_key")
    result = weather_service.get_forecast("London")
    
    assert isinstance(result, list)
    assert isinstance(result[0], ForecastData)
    assert result[0].temperature == 22.5

def test_api_error_handling(mocker):
    # Mock failed API response
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.json.return_value = {"message": "Invalid API key"}
    
    mocker.patch('requests.get', return_value=mock_response)
    
    weather_service = WeatherService("invalid_api_key")
    with pytest.raises(Exception) as exc_info:
        weather_service.get_current_weather("London")
    
    assert "Failed to fetch weather data" in str(exc_info.value) 