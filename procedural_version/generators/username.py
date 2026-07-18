# Импортируем список слов для генерации имени пользователя.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует username пользователя.
def generate_username(length=10, seed=None):
    # Проверяем, что длина username положительная.
    if length <= 0:
        # Сообщаем понятную ошибку, если длина меньше или равна нулю.
        raise ValueError("length должен быть больше 0")
    # Создаем один генератор случайности для всех частей username.
    randomizer = create_random(seed)
    # Выбираем слово для начала username.
    username_word = randomizer.choice(USERNAME_WORDS)
    # Создаем алфавит из маленьких букв, цифр и нижнего подчеркивания.
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"
    # Берем начало username из слова и нижнего подчеркивания.
    username = f"{username_word}_"
    # Добавляем случайные символы, пока username короче нужной длины.
    while len(username) < length:
        # Добавляем один случайный символ из разрешенного алфавита.
        username += randomizer.choice(alphabet)
    # Возвращаем username ровно нужной длины.
    return username[:length]
