# Импортируем список имен для генерации случайного имени.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий для генерации случайной фамилии.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random
# Импортируем функцию выбора случайного элемента.
from procedural_version.utils.random_utils import choose_item

# Объявляем функцию, которая генерирует полное имя.
def generate_full_name(max_total_length=None, seed=None):
    # Создаем один генератор случайности, чтобы имя и фамилия выбирались в одной последовательности.
    randomizer = create_random(seed)
    # Выбираем случайное имя с помощью общего генератора случайности.
    first_name = choose_item(FIRST_NAMES, randomizer=randomizer)
    # Выбираем случайную фамилию с помощью того же генератора случайности.
    last_name = choose_item(LAST_NAMES, randomizer=randomizer)
    # Склеиваем имя и фамилию через пробел и возвращаем результат.
    full_name = f"{first_name} {last_name}"
    # Проверяем, задана ли максимальная общая длина.
    if max_total_length is not None and len(full_name) > max_total_length:
        # Обрезаем полное имя до максимальной длины для проверки ограничений интерфейса.
        return full_name[:max_total_length]
    # Возвращаем полное имя без обрезки.
    return full_name
