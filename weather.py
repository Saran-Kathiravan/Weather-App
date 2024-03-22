from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import geocoder


load_dotenv()

def get_current_weather(city):
    request_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric"

    weather_data=requests.get(request_url).json()

    return weather_data

def get_current_city():
    # Get the device's current location coordinates (latitude and longitude)
    location = geocoder.ip('me')

    # Check if location retrieval was successful
    if location.ok:
        # Get the city name using reverse geocoding
        city = location.city
        print("Current city:", city)
    else:
        print("Chennai")


if __name__ == "__main__":
    print("\nGet Current weather Conditions\n")

    city=input("\nPlease enter a city name: ")

    if not bool(city.strip()):
        city=get_current_city()

    weather_data=get_current_weather(city)
    
    print("\n")
    pprint(weather_data)