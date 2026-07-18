# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует признак активности.
def generate_is_active(seed=None):
    # Создаем генератор случайности для выбора активности.
    randomizer = create_random(seed)
    # Возвращаем случайное булево значение.
    return randomizer.choice([True, False])
