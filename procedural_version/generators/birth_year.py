# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует год рождения пользователя.
def generate_birth_year(min_year=1950, max_year=2008, boundary=None, seed=None):
    # Шаг 1. Проверь, что min_year не больше max_year, потому что диапазон годов должен идти слева направо.
    # Шаг 2. Если boundary равен "min", верни самый маленький разрешенный год.
    # Шаг 3. Если boundary равен "max", верни самый большой разрешенный год.
    # Шаг 4. Если boundary равен "below_min", верни год на 1 меньше минимума для негативного теста.
    # Шаг 5. Если boundary равен "above_max", верни год на 1 больше максимума для негативного теста.
    # Шаг 6. Если boundary не передан, создай randomizer через create_random(seed).
    # Шаг 7. Верни случайный год от min_year до max_year включительно.
    pass
