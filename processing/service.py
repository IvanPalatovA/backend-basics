from processing.preprocessing import get_struct_rate, get_struct_weather
from src.models import weather_info


def build_city_summary(city: str, currency: str) -> str:
    weather_struct: weather_info = get_struct_weather(city)
    rates_struct = get_struct_rate(currency)
    answer = f"""Город: {city}
Погода: {weather_struct.temp_c}°C, {weather_struct.desctiption}
Тёплая одежда: {"Да" if weather_struct.warm_clothes else "Нет"}
{currency}->RUB: {rates_struct.rates_to_rub}
Дорогой курс: {rates_struct.espensive}"""
    return answer


# print(build_city_summary("Moscow", "usd"))
