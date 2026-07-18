# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем готовый пример функции активности.
def active_example(seed=None):
    # Что делает функция: возвращает True или False.
    # True значит пользователь активен.
    # False значит пользователь не активен.
    # seed - число для random: с одним и тем же seed random выбирает одно и то же True или False.
    # Пример вызова: active_example(seed=1) должен вернуть булево значение.
    # Документация: docs/function_specifications.md, раздел active.
    # Команда для проверки: python check.py active
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: только True или False, не строку "True" и не число 1.
    # Проверка тестами: python check.py active
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Выбираем True или False и сразу возвращаем результат.
    return randomizer.choice([True, False])
