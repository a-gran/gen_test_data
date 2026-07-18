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
    # Что такое seed: это значение, которое делает случайный выбор имени и фамилии повторяемым для тестов.
    # Если вызвать функцию два раза с одинаковым seed, случайный результат должен быть одинаковым.
    # Входные данные: max_total_length - максимальная длина полного имени или None без ограничения.
    # Входные данные: seed - значение для повторяемой генерации.
    # Внутренние переменные: randomizer - генератор случайности, который создается через create_random(seed).
    # Внутренние переменные: first_name - выбранное имя из FIRST_NAMES.
    # Внутренние переменные: last_name - выбранная фамилия из LAST_NAMES.
    # Внутренние переменные: full_name - имя и фамилия, склеенные через пробел.
    # Выходные данные: функция должна вернуть строку с полным именем.
    # Шаг 1. Создай randomizer через create_random(seed), чтобы имя и фамилия выбирались повторяемо.
    # Шаг 2. Выбери случайное имя из FIRST_NAMES.
    # Шаг 3. Выбери случайную фамилию из LAST_NAMES.
    # Шаг 4. Склей имя и фамилию через пробел.
    # Шаг 5. Если max_total_length передан и строка слишком длинная, обрежь ее до нужной длины.
    # Шаг 6. Верни готовое полное имя.
    # Проверка после реализации: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_full_name_respects_max_total_length
    # Если все хорошо, в конце вывода unittest будет написано OK.
    # Если тест упал, проверь, что полное имя не длиннее max_total_length.
    pass
