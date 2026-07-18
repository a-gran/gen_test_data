# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть возраст пользователя.
def age(min_age=18, max_age=80, boundary=None, seed=None):
    # Что делает функция: возвращает число-возраст.
    # min_age - самый маленький возраст, например 18.
    # max_age - самый большой возраст, например 80.
    # boundary - это режим для специальных проверок в тестах.
    # boundary="min" значит вернуть min_age, например 18.
    # boundary="max" значит вернуть max_age, например 80.
    # boundary="below_min" значит вернуть число меньше минимума, например 17.
    # boundary="above_max" значит вернуть число больше максимума, например 81.
    # boundary=None значит выбрать случайный возраст от min_age до max_age.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же возраст.
    # Пример вызова: age(min_age=18, max_age=80, boundary="min") должен вернуть 18.
    # Пример вызова: age(min_age=18, max_age=80, seed=1) должен вернуть число от 18 до 80.
    # Документация: docs/function_specifications.md, раздел age.
    # Команда для проверки: python check.py age
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если min_age больше max_age, нужно вызвать ValueError.
    # Что вернуть: целое число.
    # Тесты: test_age_bounds, test_age_range.
    pass
