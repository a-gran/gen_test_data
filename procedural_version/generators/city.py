# Импортируем список городов, из которого нужно выбирать результат.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть город.
def city(starts_with=None, seed=None):
    # Что делает функция: выбирает один город из CITY_NAMES.
    # starts_with=None значит можно выбрать любой город.
    # starts_with="М" значит можно выбрать только город, который начинается с буквы "М".
    # seed - число для random: с одним и тем же seed random выбирает один и тот же город.
    # Пример вызова: city(starts_with="М", seed=1) должен вернуть город на "М".
    # Документация: docs/function_specifications.md, раздел city.
    # Команда для проверки: python check.py city
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если подходящих городов нет, нужно вызвать ValueError.
    # Что вернуть: строку с названием города.
    # Тесты: test_city_prefix, test_city_list.
    pass
