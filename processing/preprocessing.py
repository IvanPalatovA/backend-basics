from clients.geo import get_geo
from clients.rates import get_raw_rates
from clients.weather import get_weather
from src.logger import logger_API
from src.models import rates_info, weather_info

code_weather_intepret = {
    "0": "Clear sky",
    "1": "Mainly clear",
    "2": "Partly cloudy",
    "3": "Overcast",
    "45": "Fog",
    "48": "Depositing rime fog",
    "51": "Light drizzle",
    "53": "Moderate drizzle",
    "55": "Dense drizzle",
    "56": "Light freezing drizzle",
    "57": "Dense freezing drizzle",
    "61": "Slight rain",
    "63": "Moderate rain",
    "65": "Heavy rain",
    "66": "Light freezing rain",
    "67": "Heavy freezing rain",
    "71": "Slight snowfall",
    "73": "Moderate snowfall",
    "75": "Heavy snowfall",
    "77": "Snow grains",
    "80": "Slight rain showers",
    "81": "Moderate rain showers",
    "82": "Violent rain showers",
    "85": "Slight snow showers",
    "86": "Heavy snow showers",
    "95": "Thunderstorm",
    "96": "Thunderstorm with slight hail",
    "97": "Heavy thunderstorm",
    "99": "Thunderstorm with heavy hail",
}


def get_struct_weather(city: str) -> weather_info:
    raw_geo = get_geo(city)

    geo_lat: float = raw_geo["results"][0]["latitude"]
    geo_long: float = raw_geo["results"][0]["longitude"]

    raw_weather = get_weather(geo_lat, geo_long)
    temp: float = raw_weather["current"]["temperature_2m"]
    condition: str = code_weather_intepret[str(raw_weather["current"]["weather_code"])]
    if temp < 0:
        warm_clothes = True
    else:
        warm_clothes = False
    response = weather_info(
        temp_c=temp, desctiption=condition, warm_clothes=warm_clothes
    )
    logger_API.info("preprocesing корректно обработал погоду")
    return response


def get_struct_rate(curr: str) -> rates_info:
    raw_ans = get_raw_rates(curr)
    rate: float = raw_ans["rate"]
    ans = rates_info(
        currency=curr, rates_to_rub=rate, espensive=(True if rate > 100 else False)
    )
    logger_API.info("preprocessing корректно обработал курс валют")
    return ans


# print(get_struct_weather(input()))
# print(get_struct_rate(input()))
