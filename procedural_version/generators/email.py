# Импортируем список доменов для генерации адреса электронной почты.
from procedural_version.data.names_data import EMAIL_DOMAINS
# Импортируем список слов для генерации имени почтового ящика.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует адрес электронной почты.
def generate_email(valid=True, username_length=8, seed=None):
    # Проверяем, что длина имени почтового ящика положительная.
    if username_length <= 0:
        # Сообщаем понятную ошибку, если длина меньше или равна нулю.
        raise ValueError("username_length должен быть больше 0")
    # Создаем один генератор случайности для всех частей email.
    randomizer = create_random(seed)
    # Выбираем слово для части email до знака собаки.
    username_word = randomizer.choice(USERNAME_WORDS)
    # Создаем алфавит из маленьких букв, цифр и нижнего подчеркивания.
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"
    # Берем начало username из слова и нижнего подчеркивания.
    username = f"{username_word}_"
    # Добавляем случайные символы, пока username короче нужной длины.
    while len(username) < username_length:
        # Добавляем один случайный символ из разрешенного алфавита.
        username += randomizer.choice(alphabet)
    # Обрезаем username ровно до нужной длины.
    username = username[:username_length]
    # Выбираем домен для части email после знака собаки.
    domain = randomizer.choice(EMAIL_DOMAINS)
    # Проверяем, нужно ли вернуть невалидный email для негативного теста.
    if not valid:
        # Возвращаем строку без знака собаки, чтобы формат был намеренно неправильным.
        return f"{username}.{domain}"
    # Склеиваем части email и возвращаем готовую строку.
    return f"{username}@{domain}"
