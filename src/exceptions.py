class retryFailed(Exception):
    """Провалены все попытки достучаться"""


class BadRequest(Exception):
    """Запрос неверный"""


class BadResponce(Exception):
    """Получин сломанный ответ от сервера"""


class CityNotFound(Exception):
    """внешний API не нашел похожих городов"""


class СurrencyNotFound(Exception):
    """внешний API не нашел похожих городов"""
