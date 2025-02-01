import streamlit as st
from src.services.weather_service import WeatherService
from src.ui.weather_ui import WeatherUI

def main():
    # Initialize services
    weather_service = WeatherService()
    
    # Initialize UI
    weather_ui = WeatherUI(weather_service)
    
    # Render UI
    weather_ui.render()

if __name__ == "__main__":
    main() 