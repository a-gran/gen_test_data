# Импортируем учебные слова, с которых можно начать пароль.
from procedural_version.data.names_data import PASSWORD_WORDS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть пароль.
def password(length=12, use_digits=True, use_symbols=True, seed=None):
    # Что делает функция: возвращает строку-пароль ровно из length символов.
    # length=16 значит пароль должен быть длиной ровно 16 символов.
    # use_digits=True значит в пароле должна быть хотя бы одна цифра, например "5".
    # use_symbols=True значит в пароле должен быть хотя бы один спецсимвол, например "!".
    # seed - число для random: с одним и тем же seed random собирает один и тот же пароль.
    # Пример вызова: password(length=16, use_digits=True, use_symbols=True, seed=1).
    # Документация: docs/function_specifications.md, раздел password.
    # Команда для проверки: python check.py password
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку с паролем.
    # Тесты: test_password_parts, test_password_bad_len.
    pass
