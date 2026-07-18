# Импортируем список тегов для генерации списка тегов.
from procedural_version.data.names_data import TAGS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует список тегов.
def generate_tags(count=None, unique=True, seed=None):
    # Создаем генератор случайности для выбора тегов.
    randomizer = create_random(seed)
    # Выбираем случайное количество тегов от 1 до 3, если количество не передали.
    tags_count = count if count is not None else randomizer.randint(1, 3)
    # Проверяем, что количество тегов не отрицательное.
    if tags_count < 0:
        # Сообщаем понятную ошибку, если количество меньше нуля.
        raise ValueError("count не должен быть меньше 0")
    # Проверяем, нужны ли уникальные теги.
    if unique:
        # Ограничиваем количество размером списка, чтобы sample не упал.
        safe_count = min(tags_count, len(TAGS))
        # Возвращаем список случайных тегов без повторов.
        return randomizer.sample(TAGS, safe_count)
    # Возвращаем список тегов, где повторы разрешены.
    return [randomizer.choice(TAGS) for _ in range(tags_count)]
