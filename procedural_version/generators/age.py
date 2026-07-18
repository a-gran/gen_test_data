# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует возраст пользователя.
def generate_age(min_age=18, max_age=80, boundary=None, seed=None):
    # Шаг 1. Проверь, что min_age не больше max_age, потому что нижняя граница не может быть выше верхней.
    # Шаг 2. Если boundary равен "min", верни самый маленький разрешенный возраст.
    # Шаг 3. Если boundary равен "max", верни самый большой разрешенный возраст.
    # Шаг 4. Если boundary равен "below_min", верни возраст на 1 меньше минимума для негативного теста.
    # Шаг 5. Если boundary равен "above_max", верни возраст на 1 больше максимума для негативного теста.
    # Шаг 6. Если boundary не передан, создай randomizer через create_random(seed).
    # Шаг 7. Верни случайный возраст от min_age до max_age включительно.
    # Проверка после реализации: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_age_returns_boundary_values
    # Если все хорошо, в конце вывода unittest будет написано OK.
    # Если тест упал, прочитай строку с AssertionError и проверь, какое значение ожидалось для каждого boundary.
    pass
