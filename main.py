import argparse
import sys

from processing.service import build_city_summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True, help="Название города")
    parser.add_argument(
        "--currency",
        default="usd",
        help="Валюта по отношению к рублю",
    )
    args = parser.parse_args()
    try:
        text = build_city_summary(args.city, args.currency)
        print(text)
        return 0
    except Exception:
        return 1

    # tasks_by_id: dict[int, Task] = {}
    # task = create_task(
    #     tasks_by_id,
    #     title="Подготовить README",
    #     description="Добавить инструкцию запуска проекта",
    #     due_date=date(2027, 6, 30),
    # )
    # print(get_task(tasks_by_id, task.id))


if __name__ == "__main__":
    sys.exit(main())
