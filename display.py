from datetime import datetime
from extras import WEATHER_EMOJIS
from colorama import init, Fore, Style

init(autoreset=True)

def display_weather(weather, units):
    try:
        unit_symbol = "°C" if units == "metric" else "°F" if units == "imperial" else "K"
        name = weather["name"]
        main = weather["main"]
        wind = weather["wind"]
        weather_main = weather["weather"][0]["main"]
        description = weather["weather"][0]["description"].capitalize()
        emoji = WEATHER_EMOJIS.get(weather_main, "")

        sunrise = datetime.fromtimestamp(weather["sys"]["sunrise"] + weather["timezone"]).strftime("%H:%M")
        sunset = datetime.fromtimestamp(weather["sys"]["sunset"] + weather["timezone"]).strftime("%H:%M")

        temp = main['temp']
        if temp >= 30:
            temp_color = Fore.RED
        elif temp <= 10:
            temp_color = Fore.BLUE
        else:
            temp_color = Fore.YELLOW

        feels_like = main['feels_like']
        feels_color = temp_color

        weather_info = f"""
            {Fore.CYAN}Weather in {name} {emoji}:{Style.RESET_ALL}
            {temp_color}Temperature: {temp}{unit_symbol}{Style.RESET_ALL} (feels like {feels_color}{feels_like}{unit_symbol}{Style.RESET_ALL})
            {Fore.BLUE}Humidity: {main['humidity']}%{Style.RESET_ALL}
            {Fore.YELLOW}Condition: {description}{Style.RESET_ALL}
            {Fore.MAGENTA}Wind Speed: {wind['speed']} m/s{Style.RESET_ALL}
            {Fore.GREEN}Sunrise: {sunrise} | Sunset: {sunset}{Style.RESET_ALL}
        """
        
        print(weather_info)
        print("─" * 50)

    except Exception as e:
        print(f"{Fore.RED}Error displaying weather for '{weather.get('name', 'Unknown')}': {e}{Style.RESET_ALL}")
