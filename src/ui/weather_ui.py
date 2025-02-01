import streamlit as st
import folium
from streamlit_folium import folium_static
from src.models.weather_data import WeatherData, ForecastData
from typing import List

class WeatherUI:
    """Class to handle the Streamlit UI components"""
    
    def __init__(self, weather_service):
        self.weather_service = weather_service
    
    def render(self):
        """Render the main UI components"""
        st.title("☁️ Weather App")
        
        # Location input with example
        st.write("Enter location (e.g., 'Bhanjipur,Tarakeswar' or 'London,UK')")
        city = st.text_input("Location", "London")
        
        if st.button("Get Weather") or city:  # Auto-update when city changes
            with st.spinner("Fetching weather data..."):
                try:
                    # Get current weather
                    current_weather = self.weather_service.get_current_weather(city)
                    self.display_weather(current_weather)
                    
                    # Get and display forecast
                    forecast = self.weather_service.get_forecast(city)
                    self.display_forecast(forecast)
                    
                    # Update map with the new location
                    self.create_map(current_weather)
                except Exception as e:
                    st.error(str(e))
    
    def display_weather(self, weather: WeatherData):
        """Display current weather information"""
        st.subheader(f"Current Weather in {weather.city}")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            icon_url = f"http://openweathermap.org/img/wn/{weather.icon}@2x.png"
            st.image(icon_url, width=100)
            st.write(weather.description.capitalize())
        
        with col2:
            st.metric("Temperature", f"{weather.temperature:.1f}°C")
            st.metric("Humidity", f"{weather.humidity}%")
        
        with col3:
            st.metric("Wind Speed", f"{weather.wind_speed} m/s")

    def display_forecast(self, forecast_data: List[ForecastData]):
        """Display 5-day weather forecast"""
        st.subheader("5-Day Forecast")
        
        # Group forecast by day and get the first forecast for each day
        daily_forecasts = {}
        for forecast in forecast_data:
            date = forecast.datetime.date()
            if date not in daily_forecasts:
                daily_forecasts[date] = forecast
        
        # Display forecasts
        cols = st.columns(min(len(daily_forecasts), 5))  # Limit to 5 days
        for col, (date, forecast) in zip(cols, list(daily_forecasts.items())[:5]):
            with col:
                st.write(date.strftime("%A"))
                icon_url = f"http://openweathermap.org/img/wn/{forecast.icon}@2x.png"
                st.image(icon_url, width=50)
                st.write(f"{forecast.temperature:.1f}°C")

    def create_map(self, weather: WeatherData = None):
        """Create and display an interactive map"""
        st.subheader("Location Map")
        
        # Default to London coordinates if no weather data
        lat, lon = 51.5074, -0.1278
        
        # If we have weather data, update the coordinates
        if weather and hasattr(weather, 'lat') and hasattr(weather, 'lon'):
            lat, lon = weather.lat, weather.lon
        
        m = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker(
            [lat, lon],
            popup=weather.city if weather else "Selected Location",
            icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(m)
        
        folium_static(m) 