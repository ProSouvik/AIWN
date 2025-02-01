import streamlit as st
from src.api.weather_service import WeatherService
from src.config.settings import Settings
from src.ui.weather_ui import WeatherUI

def main():
    # Initialize settings and services
    settings = Settings()
    weather_service = WeatherService(settings.OPENWEATHER_API_KEY)
    
    # Initialize and render UI
    ui = WeatherUI(weather_service)
    ui.render()

if __name__ == "__main__":
    main() 