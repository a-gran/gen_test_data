# Импортируем список имен для генерации случайного имени.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий для генерации случайной фамилии.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random
# Импортируем функцию выбора случайного элемента.
from procedural_version.utils.random_utils import choose_item

# Объявляем функцию, которая генерирует полное имя.
def generate_full_name(max_total_length=None, seed=None):
    # Шаг 1. Создай randomizer через create_random(seed), чтобы имя и фамилия выбирались повторяемо.
    # Шаг 2. Выбери случайное имя из FIRST_NAMES.
    # Шаг 3. Выбери случайную фамилию из LAST_NAMES.
    # Шаг 4. Склей имя и фамилию через пробел.
    # Шаг 5. Если max_total_length передан и строка слишком длинная, обрежь ее до нужной длины.
    # Шаг 6. Верни готовое полное имя.
    pass
