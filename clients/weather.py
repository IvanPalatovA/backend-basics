import random
import time

import requests

from src.exceptions import BadRequest, BadResponce, retryFailed
from src.logger import logger_API

URL = "https://api.open-meteo.com/v1/forecast"
MAX_ATTEMPTS = 3


def get_weather(latitude: float, longitude: float):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
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
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                if retry_after is not None:
                    retry_after = float(retry_after)
                else:
                    raise BadResponce(
                        "Сработал time rate но сервер не вернул retry-after"
                    )
                logger_API.warning("Сработал Time-limit подождать {retry_after} секунд")
                time.sleep(retry_after)
                response.raise_for_status()
            elif response.status_code < 500 and response.status_code >= 400:
                raise BadRequest("Ошибка 4xx на стороне клиента")

            response.raise_for_status()
            logger_API.debug("get_raw_rates закончил работу")
            return response.json()

        except (
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
        ):
            logger_API.warning("Попытка №{attempt} провалена")
            delay = 2 ** (attempt - 1) + random.uniform(0, 0.5)
            if attempt > MAX_ATTEMPTS:
                logger_API.error("!!Последняя попытка №{attempt} провалена!!")
                raise retryFailed
            time.sleep(delay)


if __name__ == "__main__":
    print(get_weather(float(input()), float(input())))
