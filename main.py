import argparse
import sys

from processing.service import build_city_summary
from src.exceptions import CityNotFound, СurrencyNotFound, retryFailed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True, help="Название города")
    parser.add_argument(
        "--currency",
        default="usd",
        help="Валюта по отношению к рублю",
    )
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as err:
        print(f"ошибка {err}")
        return 2
    try:
        text = build_city_summary(args.city, args.currency)
        print(text)
        return 0
    except (CityNotFound, СurrencyNotFound) as err:
        print(f"ошибка {err}")
        return 3
    except retryFailed as err:
        print(f"ошибка {err}")
        return 4


if __name__ == "__main__":
    sys.exit(main())
