# Импортируем список имен для генерации случайного имени.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует случайное имя.
def generate_first_name(min_length=None, max_length=None, seed=None):
    # Шаг 1. Создай randomizer через create_random(seed), чтобы выбор имени можно было повторить.
    # Шаг 2. Возьми полный список имен FIRST_NAMES и сохрани его в отдельную переменную.
    # Шаг 3. Если min_length передан, оставь только имена не короче этого значения.
    # Шаг 4. Если max_length передан, оставь только имена не длиннее этого значения.
    # Шаг 5. Если после фильтрации список пустой, вызови понятную ошибку ValueError.
    # Шаг 6. Верни случайное имя из подходящего списка.
    # Проверка после реализации: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_first_name_respects_length_filter
    # Если все хорошо, в конце вывода unittest будет написано OK.
    # Если тест упал, проверь, что имя взято из FIRST_NAMES и подходит под ограничения длины.
    pass
