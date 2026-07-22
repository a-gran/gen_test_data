'''
# Импортируем домены, которые можно ставить после знака @.
from procedural_version.data.names_data import EMAIL_DOMAINS
# Импортируем слова, из которых можно начать имя почтового ящика.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть email.
def email(valid=True, username_length=8, seed=None):
    # Что делает функция: возвращает строку email.
    # valid=True значит email должен быть правильным и содержать знак @.
    # valid=False значит email должен быть специально неправильным, например без @.
    # username_length=8 значит часть до @ должна быть ровно 8 символов.
    # seed - число для random: с одним и тем же seed random собирает один и тот же email.
    # Можно вызвать email() и получить правильный email с именем длиной 8 символов.
    # Можно вызвать email(valid=False) и получить специально неправильный email.
    # Можно вызвать email(username_length=12) и получить email с именем длиной 12 символов.
    # Можно вызвать email(valid=False, username_length=12, seed=1) и сочетать все настройки.
    # Пример вызова: email(valid=True, username_length=8, seed=1) должен вернуть строку с @.
    # Пример вызова: email(valid=False, username_length=8, seed=1) должен вернуть строку без @.
    # Документация: docs/function_specifications.md, раздел email.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py email
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если username_length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_email_validity, test_email_bad_len.
    # Проверяем, что длина имени почтового ящика больше нуля.
    if username_length <= 0:
        # Сообщаем ошибку, если длина неправильная.
        raise ValueError("username_length должен быть больше 0")
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Выбираем слово, с которого начнется имя почтового ящика.
    base_word = randomizer.choice(USERNAME_WORDS)
    # Задаем символы, которыми можно дополнить имя почтового ящика.
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    # Добавляем случайные символы, чтобы строки точно хватило.
    extra_symbols = "".join(randomizer.choice(alphabet) for _ in range(username_length))
    # Собираем имя почтового ящика нужной длины.
    email_username = (base_word + extra_symbols)[:username_length]
    # Выбираем домен для email.
    domain = randomizer.choice(EMAIL_DOMAINS)
    # Проверяем, нужен ли правильный email.
    if valid:
        # Возвращаем правильный email со знаком @.
        return f"{email_username}@{domain}"
    # Возвращаем специально неправильный email без знака @.
    return f"{email_username}.{domain}"
'''




from procedural_version.data.names_data import EMAIL_DOMAINS
# Импортируем слова, из которых можно начать имя почтового ящика.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть email.
def email(valid=True, username_length=8, seed=None):

    if username_length <= 0:
        raise ValueError("username_length must be greater than 0")

    rnd = create_random(seed)
    raw_words = "".join(rnd.choices(USERNAME_WORDS, k=int(username_length) + 5))
    username = raw_words[:username_length]
    domain = rnd.choice(EMAIL_DOMAINS)

    if valid:
        return f"{username}@{domain}"
    else:
        return f"{username}{domain}"

