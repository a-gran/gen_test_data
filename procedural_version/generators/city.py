# Импортируем список городов для генерации случайного города.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует случайный город.
def generate_city(starts_with=None, seed=None):
    # Шаг 1. Создай randomizer через create_random(seed), чтобы выбор города можно было повторить.
    # Шаг 2. Возьми полный список городов CITY_NAMES и сохрани его в отдельную переменную.
    # Шаг 3. Если starts_with передан, оставь только города, которые начинаются с этого текста.
    # Шаг 4. Если после фильтрации список пустой, вызови понятную ошибку ValueError.
    # Шаг 5. Верни случайный город из подходящего списка.
    pass
