import random
import time

import requests

from src.exceptions import BadRequest, BadResponce, CityNotFound, retryFailed
from src.logger import logger_API

URL = "https://geocoding-api.open-meteo.com/v1/search"
MAX_ATTEMPTS = 3


def get_geo(name: str):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
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
            elif response.json().get("results") is None:
                raise CityNotFound("Введенный город не найден")

            response.raise_for_status()
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
    print(get_geo(input()))
