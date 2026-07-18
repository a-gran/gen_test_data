# Подсказка ученику: create_random(seed) нужен, чтобы случайный результат можно было повторить в тестах.
from procedural_version.utils.random_utils import create_random

# Задание: реализуй генератор учебного балла и проверь его граничные значения тестами.
def generate_score(min_score=1, max_score=100, boundary=None, seed=None):
    # Шаг 1. Сначала проверь ошибочный случай: min_score не должен быть больше max_score.
    if min_score > max_score:
        # Шаг 2. Если границы перепутаны, выброси ValueError, чтобы тест мог проверить ошибку.
        raise ValueError("min_score не должен быть больше max_score")
    # Шаг 3. Проверь boundary="min": функция должна вернуть нижнюю границу.
    if boundary == "min":
        # Проверка тестом: generate_score(boundary="min") должен вернуть min_score.
        return min_score
    # Шаг 4. Проверь boundary="max": функция должна вернуть верхнюю границу.
    if boundary == "max":
        # Проверка тестом: generate_score(boundary="max") должен вернуть max_score.
        return max_score
    # Шаг 5. Проверь boundary="below_min": это значение нужно для негативного теста.
    if boundary == "below_min":
        # Проверка тестом: результат должен быть на 1 меньше min_score.
        return min_score - 1
    # Шаг 6. Проверь boundary="above_max": это значение тоже нужно для негативного теста.
    if boundary == "above_max":
        # Проверка тестом: результат должен быть на 1 больше max_score.
        return max_score + 1
    # Шаг 7. Если boundary не передан, создай генератор случайности.
    randomizer = create_random(seed)
    # Шаг 8. Верни случайный балл внутри диапазона; тест должен проверить, что min_score <= результат <= max_score.
    # Проверка после реализации: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_score_returns_boundary_values
    # Если все хорошо, в конце вывода unittest будет написано OK.
    # Если тест упал, прочитай строку с AssertionError и проверь значения для boundary="min" и boundary="max".
    return randomizer.randint(min_score, max_score)
