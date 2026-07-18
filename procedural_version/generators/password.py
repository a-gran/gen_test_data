# Импортируем список слов для генерации учебного пароля.
from procedural_version.data.names_data import PASSWORD_WORDS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует учебный пароль.
def generate_password(length=12, use_digits=True, use_symbols=True, seed=None):
    # Проверяем, что длина пароля положительная.
    if length <= 0:
        # Сообщаем понятную ошибку, если длина меньше или равна нулю.
        raise ValueError("length должен быть больше 0")
    # Создаем один генератор случайности для всех частей пароля.
    randomizer = create_random(seed)
    # Создаем строку с буквами, которые можно использовать в пароле.
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Создаем строку с цифрами, которые можно добавить в пароль.
    digits = "0123456789"
    # Создаем строку со специальными символами, которые можно добавить в пароль.
    symbols = "!@#$%^&*"
    # Начинаем пароль со случайного учебного слова.
    password_parts = [randomizer.choice(PASSWORD_WORDS)]
    # Добавляем обязательную цифру, если цифры включены.
    if use_digits:
        # Кладем одну случайную цифру в список частей пароля.
        password_parts.append(randomizer.choice(digits))
    # Добавляем обязательный спецсимвол, если спецсимволы включены.
    if use_symbols:
        # Кладем один случайный спецсимвол в список частей пароля.
        password_parts.append(randomizer.choice(symbols))
    # Собираем алфавит из букв.
    alphabet = letters
    # Добавляем цифры в алфавит, если они разрешены.
    if use_digits:
        # Расширяем алфавит цифрами.
        alphabet += digits
    # Добавляем спецсимволы в алфавит, если они разрешены.
    if use_symbols:
        # Расширяем алфавит спецсимволами.
        alphabet += symbols
    # Склеиваем обязательные части в одну строку.
    raw_password = "".join(password_parts)
    # Добавляем случайные символы, пока строка короче нужной длины.
    while len(raw_password) < length:
        # Добавляем один случайный символ из разрешенного алфавита.
        raw_password += randomizer.choice(alphabet)
    # Возвращаем пароль ровно нужной длины.
    return raw_password[:length]
