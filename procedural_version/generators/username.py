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
    # Можно вызвать username() и получить username длиной 10 символов.
    # Можно вызвать username(length=12) и получить username длиной 12 символов.
    # Можно вызвать username(length=12, seed=1) два раза и получить одинаковый username.
    # Пример вызова: username(length=12, seed=1) должен вернуть строку длиной 12.
    # Документация: docs/function_specifications.md, раздел username.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py username
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_username_len, test_username_bad_len.
    # Проверяем, что длина username больше нуля.
    if length <= 0:
        # Сообщаем ошибку, если длина неправильная.
        raise ValueError("length должен быть больше 0")
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Выбираем слово, с которого начнется username.
    base_word = randomizer.choice(USERNAME_WORDS)
    # Задаем символы, которыми можно дополнить username.
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"
    # Добавляем случайные символы, чтобы строки точно хватило.
    extra_symbols = "".join(randomizer.choice(alphabet) for _ in range(length))
    # Возвращаем username ровно нужной длины.
    return (base_word + extra_symbols)[:length]
