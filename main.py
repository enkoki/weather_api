from api import get_weather
from display import display_weather
from colorama import Style, Fore
def main():
    try:
        city_input = input("Enter name of cities (separated by commas)\n").strip()
        if not city_input:
            print("No cities entered. Exiting.")
            return

        cities = [city.strip() for city in city_input.split(",") if city.strip()]

        units_map = {"1": "metric", "2": "imperial", "3": "standard"}
        unit_choice = input("Choose units \n1.Metric(C) \n2.Imperial(F) \n3.Standard(K)\nDefault: Metric\nYour choice: ").strip()
        units = units_map.get(unit_choice, "metric")

        weather_results = []
        for city in cities:
            weather = get_weather(city, units)
            if weather:
                weather_results.append(weather)

        for weather in weather_results:
            display_weather(weather, units)

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")


if __name__ == '__main__':
    main()
