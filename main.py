from api import get_weather
from display import display_weather

def main():
    city = input("Enter the name of a city: ").strip()
    units = input("Choose units \n1.Metric \n2.Imperial \n3.Standard\nDefault: Metric\nYour chosen unit (leave blank to use default): ").strip().lower() or "metric"

    weather = get_weather(city, units)
    if weather:
        display_weather(weather)

if __name__ == "__main__":
    main()
