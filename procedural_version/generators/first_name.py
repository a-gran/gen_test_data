# Импортируем список имен для генерации случайного имени.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует случайное имя.
def generate_first_name(min_length=None, max_length=None, seed=None):
    # Создаем генератор случайности для выбора имени.
    randomizer = create_random(seed)
    # Начинаем с полного списка имен.
    filtered_names = FIRST_NAMES
    # Проверяем, передана ли минимальная длина имени.
    if min_length is not None:
        # Оставляем только имена не короче минимальной длины.
        filtered_names = [name for name in filtered_names if len(name) >= min_length]
    # Проверяем, передана ли максимальная длина имени.
    if max_length is not None:
        # Оставляем только имена не длиннее максимальной длины.
        filtered_names = [name for name in filtered_names if len(name) <= max_length]
    # Проверяем, остались ли имена после фильтрации.
    if not filtered_names:
        # Сообщаем понятную ошибку, если подходящих имен нет.
        raise ValueError("Нет имен, которые подходят под ограничения длины")
    # Возвращаем случайное имя из отфильтрованного списка.
    return randomizer.choice(filtered_names)
