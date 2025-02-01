# Weather App

A Streamlit-based weather application that provides current weather information, forecasts, and an interactive map interface.

## Features

- Current weather display for any city
- 5-day weather forecast with visual representation
- Interactive map interface
- Temperature, humidity, and wind speed information
- Weather condition icons and descriptions
- Metric unit system support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

## Running the App

```bash
streamlit run main.py
```

## Running Tests

```bash
pytest tests/
```

## Project Structure

- `src/`: Source code directory
  - `api/`: API integration code
  - `models/`: Data models
  - `ui/`: User interface components
- `tests/`: Test files
- `main.py`: Main Streamlit application file

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

MIT License