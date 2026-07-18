# Импортируем список тегов для генерации списка тегов.
from procedural_version.data.names_data import TAGS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует список тегов.
def generate_tags(count=None, unique=True, seed=None):
    # Шаг 1. Создай randomizer через create_random(seed), чтобы список тегов можно было повторить.
    # Шаг 2. Если count не передан, выбери случайное количество тегов от 1 до 3.
    # Шаг 3. Проверь, что итоговое количество тегов не меньше 0.
    # Шаг 4. Если unique равен True, выбери теги без повторов из списка TAGS.
    # Шаг 5. Если unique равен False, выбери теги из TAGS с возможными повторами.
    # Шаг 6. Верни готовый список тегов.
    pass
