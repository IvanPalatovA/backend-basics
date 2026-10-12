import requests

from src.logger import logger_API

URL = "https://api.open-meteo.com/v1/forecast"
# ?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m" "


def get_weather(latitude: float, longitude: float):
    logger_API.info("Req for Weather")
    response = requests.get(
        URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "weather_code"],
        },
        headers={"User-Agent": "PY_app/v1"},
        timeout=(3, 10),
    )
    response.raise_for_status()
    return response.json()


# print(get_weather(float(input()), float(input())))
