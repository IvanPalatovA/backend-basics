from dataclasses import dataclass
from datetime import date
from typing import Literal


@dataclass
class weather_info:
    temp_c: float
    desctiption: str
    warm_clothes: bool


@dataclass
class rates_info:
    currency: str
    rates_to_rub: float
    espensive: bool


@dataclass
class struct_response:
    city: str
    weather: weather_info
    rates: rates_info


@dataclass
class exit_code:
    code: Literal[1, 2, 3, 4]


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: date
