# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует цифровой ID пользователя.
def generate_user_id(length=6, only_digits=True, seed=None):
    # Проверяем, что длина ID положительная.
    if length <= 0:
        # Сообщаем понятную ошибку, если длина меньше или равна нулю.
        raise ValueError("length должен быть больше 0")
    # Создаем генератор случайности для ID пользователя.
    randomizer = create_random(seed)
    # Создаем алфавит только из цифр.
    alphabet = "0123456789"
    # Проверяем, можно ли использовать не только цифры.
    if not only_digits:
        # Добавляем английские буквы для буквенно-цифрового ID.
        alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Собираем ID из нужного количества случайных символов.
    user_id = "".join(randomizer.choice(alphabet) for _ in range(length))
    # Возвращаем ID ровно нужной длины.
    return user_id
