import os
import requests
from pprint import pprint
from datetime import datetime

# Minneapolis
lat = 44.97
lon = -93.26
units = 'imperial'  # change to 'imperial' for quantities in Fahrenheit, miles per hour etc.

api_key = os.environ['05ab7c2c11ebf476301cf655794d76c2']  # Set this environment variable on your computer

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}'



response = requests.get(url)
weather_forecast = response.json()
pprint(weather_forecast.json())
for updated_forcast in weather_forecast:
    timestamp = datetime
    temperature = updated_forcast
    description = updated_forcast
    speed = updated_forcast

    print(f'Timestamp: {timestamp}')
    print(f'Temperature: {temperature}')
    print(f'Weather: {description}')
    print(f'Wind Speed: {speed}')


