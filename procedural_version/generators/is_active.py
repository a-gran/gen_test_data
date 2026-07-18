# Подсказка ученику: create_random(seed) помогает получить одинаковый True или False при одинаковом seed.
from procedural_version.utils.random_utils import create_random

# Задание: реализуй генератор признака активности пользователя и проверь тип результата тестом.
def generate_is_active(seed=None):
    # Что такое seed: это значение, которое делает случайный выбор True или False повторяемым для тестов.
    # Если вызвать функцию два раза с одинаковым seed, случайный результат должен быть одинаковым.
    # Входные данные: seed - значение для повторяемой генерации.
    # Внутренние переменные: randomizer - генератор случайности, который создается через create_random(seed).
    # Выходные данные: функция должна вернуть булево значение True или False.
    # Шаг 1. Создай генератор случайности через create_random(seed).
    randomizer = create_random(seed)
    # Шаг 2. Выбери одно значение из списка [True, False].
    # Шаг 3. Верни выбранное значение.
    # Проверка тестом: результат должен иметь тип bool.
    # Дополнительная проверка: при одинаковом seed результат должен повторяться.
    # Проверка после реализации: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_is_active_returns_boolean
    # Если все хорошо, в конце вывода unittest будет написано OK.
    # Если тест упал, проверь, что функция возвращает именно True или False, а не строку и не число.
    return randomizer.choice([True, False])
