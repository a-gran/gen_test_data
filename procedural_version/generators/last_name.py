# Импортируем список фамилий для генерации случайной фамилии.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует случайную фамилию.
def generate_last_name(min_length=None, max_length=None, seed=None):
    # Создаем генератор случайности для выбора фамилии.
    randomizer = create_random(seed)
    # Начинаем с полного списка фамилий.
    filtered_last_names = LAST_NAMES
    # Проверяем, передана ли минимальная длина фамилии.
    if min_length is not None:
        # Оставляем только фамилии не короче минимальной длины.
        filtered_last_names = [last_name for last_name in filtered_last_names if len(last_name) >= min_length]
    # Проверяем, передана ли максимальная длина фамилии.
    if max_length is not None:
        # Оставляем только фамилии не длиннее максимальной длины.
        filtered_last_names = [last_name for last_name in filtered_last_names if len(last_name) <= max_length]
    # Проверяем, остались ли фамилии после фильтрации.
    if not filtered_last_names:
        # Сообщаем понятную ошибку, если подходящих фамилий нет.
        raise ValueError("Нет фамилий, которые подходят под ограничения длины")
    # Возвращаем случайную фамилию из отфильтрованного списка.
    return randomizer.choice(filtered_last_names)
