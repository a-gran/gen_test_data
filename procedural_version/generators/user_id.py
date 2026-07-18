# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть ID пользователя.
def user_id(length=6, only_digits=True, seed=None):
    # Что делает функция: возвращает строку-ID ровно из length символов.
    # length=8 значит ID должен быть длиной ровно 8 символов.
    # only_digits=True значит ID состоит только из цифр, например "123456".
    # only_digits=False значит можно использовать цифры и английские буквы.
    # seed - число для random: с одним и тем же seed random собирает один и тот же ID.
    # Пример вызова: user_id(length=8, only_digits=True, seed=1).
    # Документация: docs/function_specifications.md, раздел user_id.
    # Команда для проверки: python check.py id
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_id_digits, test_id_alnum.
    pass
