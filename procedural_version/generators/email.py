# Файл нужен для функции email.
# Функция email генерирует правильный или специально неправильный email.
# В тестировании ПО такую функцию можно использовать, чтобы проверять регистрацию, вход и валидацию email.

# Импортируем домены, которые можно ставить после знака @.
from procedural_version.data.names_data import EMAIL_DOMAINS
# Импортируем слова, из которых можно начать имя почтового ящика.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть email.
def email(valid=True, username_length=8, seed=None):
    # Что делает функция: возвращает email строкой.
    # valid=True значит email должен быть правильным и содержать знак @.
    # valid=False значит email должен быть специально неправильным и без знака @.
    # username_length=8 значит часть до @ должна быть длиной 8 символов.
    # seed - число для random: с одним и тем же seed random собирает один и тот же email.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.email import email
    # from procedural_version.generators.age import age
    #
    # email_result = email(valid=True, username_length=8, seed=1)
    # print(email_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = email()
    # Вызов неправильного email: result = email(valid=False)
    # Вызов с длиной username: result = email(username_length=10)
    # Вызов с seed: result = email(valid=True, username_length=8, seed=1)
    # Пример результата: правильный email должен содержать знак @.
    # Документация: docs/function_specifications.md, раздел email.
    # Шаги реализации:
    # 1. Проверить, что username_length больше 0.
    # 2. Создать random через create_random(seed).
    # 3. Собрать имя почтового ящика нужной длины.
    # 4. Выбрать домен из EMAIL_DOMAINS.
    # 5. Если valid=True, вернуть email со знаком @.
    # 6. Если valid=False, вернуть email без знака @.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py email
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если username_length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку email.
    # Тесты: test_email_validity, test_email_bad_len.
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
