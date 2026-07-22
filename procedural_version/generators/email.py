# Импортируем домены, которые можно ставить после знака @.
from procedural_version.data.names_data import EMAIL_DOMAINS
# Импортируем слова, из которых можно начать имя почтового ящика.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть email.
def email(valid=True, username_length=8, seed=None):
    # Проверяем, что длина имени почтового ящика больше нуля.
    if username_length <= 0:
        # Сообщаем ошибку, если длина неправильная.
        raise ValueError("username_length must be greater than 0")
    # Создаем random с переданным seed.
    rnd = create_random(seed)
    # Собираем запас символов из учебных слов.
    raw_words = "".join(rnd.choices(USERNAME_WORDS, k=int(username_length) + 5))
    # Обрезаем имя почтового ящика до нужной длины.
    username = raw_words[:username_length]
    # Выбираем домен из учебного списка.
    domain = rnd.choice(EMAIL_DOMAINS)
    # Проверяем, нужен ли правильный email.
    if valid:
        # Возвращаем правильный email со знаком @.
        return f"{username}@{domain}"
    # Возвращаем специально неправильный email без знака @.
    return f"{username}{domain}"
