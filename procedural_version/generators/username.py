# Импортируем список слов для генерации имени пользователя.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует username пользователя.
def generate_username(length=10, seed=None):
    # Шаг 1. Проверь, что length больше 0, потому что username должен содержать хотя бы один символ.
    # Шаг 2. Создай randomizer через create_random(seed), чтобы username можно было повторить.
    # Шаг 3. Выбери учебное слово из USERNAME_WORDS для начала username.
    # Шаг 4. Подготовь разрешенные символы: маленькие буквы, цифры и нижнее подчеркивание.
    # Шаг 5. Добавляй случайные символы, пока username не станет нужной длины.
    # Шаг 6. Обрежь username ровно до length символов.
    # Шаг 7. Верни готовый username.
    pass
