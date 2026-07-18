# Импортируем список готовых фраз для комментария.
from procedural_version.data.names_data import COMMENTS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть комментарий точной длины.
def comment(length=100, seed=None):
    # Что делает функция: возвращает строку ровно из length символов.
    # length=0 значит вернуть пустую строку "".
    # length=1 значит вернуть строку из одного символа.
    # length=255 значит вернуть строку длиной ровно 255 символов.
    # seed - число для random: с одним и тем же seed random выбирает одну и ту же фразу.
    # Пример вызова: len(comment(length=255, seed=1)) должен быть 255.
    # Документация: docs/function_specifications.md, раздел comment.
    # Команда для проверки: python check.py comment
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_comment_lengths, test_comment_bad_len.
    pass
