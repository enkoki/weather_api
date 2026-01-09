import requests
import os
from dotenv import load_dotenv
from colorama import Fore,Style

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city, units="metric"):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": units
        }
        response = requests.get(url, params=params, timeout=5)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print(f"{Fore.RED}Invalid API key. Check your .env file.{Style.RESET_ALL}")
        elif response.status_code == 404:
            print(f"{Fore.YELLOW}City '{city}' not found.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Failed to retrieve data for '{city}'. Error code: {response.status_code}{Style.RESET_ALL}")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Network error for '{city}': {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error for '{city}': {e}{Style.RESET_ALL}")

    return None
