# Подсказка ученику: create_random(seed) помогает получить одинаковый True или False при одинаковом seed.
from procedural_version.utils.random_utils import create_random

# Задание: реализуй генератор признака активности пользователя и проверь тип результата тестом.
def generate_is_active(seed=None):
    # Шаг 1. Создай генератор случайности через create_random(seed).
    randomizer = create_random(seed)
    # Шаг 2. Выбери одно значение из списка [True, False].
    # Шаг 3. Верни выбранное значение.
    # Проверка тестом: результат должен иметь тип bool.
    # Дополнительная проверка: при одинаковом seed результат должен повторяться.
    return randomizer.choice([True, False])
