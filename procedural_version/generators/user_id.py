# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует цифровой ID пользователя.
def generate_user_id(length=6, only_digits=True, seed=None):
    # Что такое seed: это значение, которое делает случайный ID повторяемым для тестов.
    # Если вызвать функцию два раза с одинаковым seed, случайный результат должен быть одинаковым.
    # Входные данные: length - точное количество символов в ID.
    # Входные данные: only_digits - если True, ID состоит только из цифр; если False, можно добавить буквы.
    # Входные данные: seed - значение для повторяемой генерации.
    # Внутренние переменные: randomizer - генератор случайности, который создается через create_random(seed).
    # Внутренние переменные: alphabet - строка символов, из которых можно собирать ID.
    # Внутренние переменные: user_id - готовая строка ID.
    # Выходные данные: функция должна вернуть строку длиной ровно length символов.
    # Шаг 1. Проверь, что length больше 0, потому что ID должен содержать хотя бы один символ.
    # Шаг 2. Создай randomizer через create_random(seed), чтобы ID можно было повторить.
    # Шаг 3. Подготовь строку с цифрами, которые можно использовать в ID.
    # Шаг 4. Если only_digits равен False, добавь к цифрам английские буквы.
    # Шаг 5. Собери строку из length случайных символов.
    # Шаг 6. Верни готовый ID.
    # Проверка после реализации: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_user_id_returns_digits_with_exact_length
    # Дополнительная проверка: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_user_id_can_return_letters_and_digits
    # Если все хорошо, в конце вывода unittest будет написано OK.
    # Если тест упал, проверь длину ID и набор разрешенных символов.
    pass
