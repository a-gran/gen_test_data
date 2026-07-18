# Импортируем список городов для генерации случайного города.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует случайный город.
def generate_city(starts_with=None, seed=None):
    # Создаем генератор случайности для выбора города.
    randomizer = create_random(seed)
    # Начинаем с полного списка городов.
    filtered_cities = CITY_NAMES
    # Проверяем, передана ли первая буква или начало города.
    if starts_with is not None:
        # Оставляем только города, которые начинаются с переданного текста.
        filtered_cities = [city for city in filtered_cities if city.startswith(starts_with)]
    # Проверяем, остались ли города после фильтрации.
    if not filtered_cities:
        # Сообщаем понятную ошибку, если подходящих городов нет.
        raise ValueError("Нет городов, которые подходят под starts_with")
    # Возвращаем случайный город из отфильтрованного списка.
    return randomizer.choice(filtered_cities)
