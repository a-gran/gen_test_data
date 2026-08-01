# Файл нужен для функции username.
# Функция username должна генерировать имя пользователя для аккаунта.
# В тестировании ПО такую функцию можно использовать, чтобы проверять регистрацию, профиль и отображение имени аккаунта.

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
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.username import username
    # from procedural_version.generators.age import age
    #
    # username_result = username(length=12, seed=1)
    # print(username_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = username()
    # Вызов с длиной: result = username(length=12)
    # Вызов с seed: result = username(length=12, seed=1)
    # Пример результата: username должен быть строкой длиной 12.
    # Документация: docs/function_specifications.md, раздел username.
    # Шаги реализации:
    # 1. Проверить, что length больше 0.
    # 2. Создать random через create_random(seed).
    # 3. Подготовить символы из маленьких английских букв, цифр и "_".
    # 4. Выбрать length случайных символов.
    # 5. Склеить выбранные символы в одну строку.
    # 6. Вернуть username ровно нужной длины.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py username
    # Или на Windows: py check.py username
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
    # Подготавливаем символы, из которых можно собирать username.
    characters = "abcdefghijklmnopqrstuvwxyz0123456789_"
    # Собираем список случайных символов нужной длины.
    result_characters = [randomizer.choice(characters) for _ in range(length)]
    # Склеиваем выбранные символы в одну строку.
    result = "".join(result_characters)
    # Возвращаем готовый username.
    return result
