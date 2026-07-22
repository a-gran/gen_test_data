# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть год рождения пользователя.
def birth_year(min_year=1950, max_year=2008, boundary=None, seed=None):
    # Что делает функция: возвращает число-год рождения.
    # min_year - самый маленький год, например 1950.
    # max_year - самый большой год, например 2008.
    # boundary - это режим для специальных проверок в тестах.
    # boundary="min" значит вернуть min_year, например 1950.
    # boundary="max" значит вернуть max_year, например 2008.
    # boundary="below_min" значит вернуть год меньше минимума, например 1949.
    # boundary="above_max" значит вернуть год больше максимума, например 2009.
    # boundary=None значит выбрать случайный год от min_year до max_year.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же год.
    # Можно вызвать birth_year() и получить случайный год от 1950 до 2008.
    # Можно вызвать birth_year(boundary="max") и получить стандартный максимум 2008.
    # Можно вызвать birth_year(min_year=2000, max_year=2010) и получить год от 2000 до 2010.
    # Можно вызвать birth_year(min_year=2000, max_year=2010, boundary="min") и получить 2000.
    # Можно вызвать birth_year(seed=1) два раза и получить один и тот же год.
    # Пример вызова: birth_year(boundary="max") должен вернуть 2008.
    # Документация: docs/function_specifications.md, раздел birth_year.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py birth_year
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если min_year больше max_year, нужно вызвать ValueError.
    # Что вернуть: целое число.
    # Тесты: test_birth_year_bounds, test_birth_year_range.
    # Проверяем, что минимальный год не больше максимального.
    if min_year > max_year:
        # Сообщаем ошибку, если диапазон годов написан наоборот.
        raise ValueError("min_year не должен быть больше max_year")
    # Возвращаем нижнюю границу года рождения.
    if boundary == "min":
        # Возвращаем min_year.
        return min_year
    # Возвращаем верхнюю границу года рождения.
    if boundary == "max":
        # Возвращаем max_year.
        return max_year
    # Возвращаем год меньше нижней границы.
    if boundary == "below_min":
        # Возвращаем min_year минус 1.
        return min_year - 1
    # Возвращаем год больше верхней границы.
    if boundary == "above_max":
        # Возвращаем max_year плюс 1.
        return max_year + 1
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Возвращаем случайный год внутри диапазона.
    return randomizer.randint(min_year, max_year)
