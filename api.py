import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city, units="metric"):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": units
    }
    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        print("Invalid API key. Check your .env file.")
    elif response.status_code == 404:
        print(f"City '{city}' not found.")
    else:
        print(f"Failed to retrieve data. Error code: {response.status_code}")
    return None
