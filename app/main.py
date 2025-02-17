import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    weather_info = data["current"]

    print("Current weather in Paris:")
    print(f"Temperature: {weather_info.get("temp_c")}°C")
    print(f"Condition: {weather_info["condition"]["text"]}")
    print(f"Wind: {weather_info.get("wind_kph")} kph")
    print(f"Humidity: {weather_info.get("humidity")}%")


if __name__ == "__main__":
    get_weather()
