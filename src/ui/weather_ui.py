import streamlit as st
from ..services.weather_service import WeatherService
from ..models.weather_data import WeatherData, ForecastData
from typing import List
import folium
from streamlit_folium import folium_static

class WeatherUI:
    """Class to handle the Streamlit UI components"""
    
    def __init__(self, weather_service: WeatherService):
        self.weather_service = weather_service
    
    def render(self):
        """Render the main UI components"""
        st.title("☁️ Weather App")
        
        # City input
        city = st.text_input("Enter City Name", "London")
        
        if st.button("Get Weather"):
            self._display_weather(city)
    
    def _display_weather(self, city: str):
        """Display weather information for the given city"""
        with st.spinner("Fetching weather data..."):
            weather_data = self.weather_service.get_weather(city)
            
            if weather_data:
                self.display_weather(weather_data)
                self.display_forecast(self.weather_service.get_forecast(city))
                self.create_map()
            else:
                st.error("Unable to fetch weather data. Please try again.")

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
        
        # Group forecast by day
        daily_forecasts = {}
        for forecast in forecast_data:
            date = forecast.datetime.date()
            if date not in daily_forecasts:
                daily_forecasts[date] = forecast
        
        # Display forecasts
        cols = st.columns(len(daily_forecasts))
        for col, (date, forecast) in zip(cols, daily_forecasts.items()):
            with col:
                st.write(date.strftime("%A"))
                icon_url = f"http://openweathermap.org/img/wn/{forecast.icon}@2x.png"
                st.image(icon_url, width=50)
                st.write(f"{forecast.temperature:.1f}°C")

    def create_map(self):
        """Create and display an interactive map"""
        st.subheader("Interactive Weather Map")
        
        m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)
        folium.Marker(
            [51.5074, -0.1278],
            popup="Selected Location",
            icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(m)
        
        folium_static(m) 