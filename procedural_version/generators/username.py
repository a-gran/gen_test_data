# Импортируем учебные слова, с которых можно начать username.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть username.
def username(length=10, seed=None):
    # Что делает функция: возвращает строку username ровно из length символов.
    # length=12 значит username должен быть длиной ровно 12 символов.
    # Username можно собрать из маленьких английских букв, цифр и нижнего подчеркивания "_".
    # seed - число для random: с одним и тем же seed random собирает один и тот же username.
    # Пример вызова: username(length=12, seed=1) должен вернуть строку длиной 12.
    # Документация: docs/function_specifications.md, раздел username.
    # Команда для проверки: python check.py username
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_username_len, test_username_bad_len.
    pass
