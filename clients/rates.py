import requests

from src.logger import logger_API

URL = "https://api.frankfurter.dev/v2/rate"


def get_raw_rates(currency: str):
    logger_API.debug("get_raw_rates начал работу")
    responce = requests.get(
        f"{URL}/{currency}/rub",
        headers={
            "User-Agent": "PY_app/v1",
        },
        timeout=(3, 10),
    )
    responce.raise_for_status()
    logger_API.debug("get_raw_rates закончил работу")
    return responce.json()


# print(get_raw_rates(input()))
