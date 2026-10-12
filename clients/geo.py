import requests

from src.logger import logger_API

URL = "https://geocoding-api.open-meteo.com/v1/search"


def get_geo(name: str):
    logger_API.info(f"Req for GeoPosition of {name}")
    response = requests.get(
        URL,
        params={
            "name": name,
            "count": 1,
        },
        headers={
            "User-Agent": "PY_app/1.0",
        },
        timeout=(3, 10),
    )
    response.raise_for_status()
    return response.json()


# print(get_geo(input()))
