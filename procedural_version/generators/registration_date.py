# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует дату регистрации пользователя.
def generate_registration_date(start_year=2020, end_year=2026, boundary=None, seed=None):
    # Проверяем, что начальный год не больше конечного.
    if start_year > end_year:
        # Сообщаем понятную ошибку, если годы перепутаны местами.
        raise ValueError("start_year не должен быть больше end_year")
    # Проверяем, попросили ли вернуть дату на нижней границе.
    if boundary == "min":
        # Возвращаем первое января начального года.
        return f"{start_year:04d}-01-01"
    # Проверяем, попросили ли вернуть дату на верхней границе.
    if boundary == "max":
        # Возвращаем двадцать восьмое декабря конечного года.
        return f"{end_year:04d}-12-28"
    # Проверяем, попросили ли вернуть дату ниже допустимого диапазона.
    if boundary == "below_min":
        # Возвращаем дату за год до начального года.
        return f"{start_year - 1:04d}-12-31"
    # Проверяем, попросили ли вернуть дату выше допустимого диапазона.
    if boundary == "above_max":
        # Возвращаем дату через год после конечного года.
        return f"{end_year + 1:04d}-01-01"
    # Создаем генератор случайности для даты регистрации.
    randomizer = create_random(seed)
    # Генерируем год регистрации.
    year = randomizer.randint(start_year, end_year)
    # Генерируем месяц регистрации.
    month = randomizer.randint(1, 12)
    # Генерируем день регистрации в безопасном диапазоне до 28.
    day = randomizer.randint(1, 28)
    # Возвращаем дату строкой в формате год-месяц-день.
    return f"{year:04d}-{month:02d}-{day:02d}"
