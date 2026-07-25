# Файл нужен для функции user_id.
# Функция user_id должна генерировать строковый ID пользователя.
# В тестировании ПО такую функцию можно использовать, чтобы создавать уникальные идентификаторы тестовых пользователей.

# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть ID пользователя.
def user_id(length=6, only_digits=True, seed=None):
    # Что делает функция: возвращает строку-ID ровно из length символов.
    # length=8 значит ID должен быть длиной ровно 8 символов.
    # only_digits=True значит ID состоит только из цифр, например "123456".
    # only_digits=False значит можно использовать цифры и английские буквы.
    # seed - число для random: с одним и тем же seed random собирает один и тот же ID.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.user_id import user_id
    # from procedural_version.generators.age import age
    #
    # user_id_result = user_id(length=8, only_digits=True, seed=1)
    # print(user_id_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = user_id()
    # Вызов с длиной: result = user_id(length=8)
    # Вызов с буквами и цифрами: result = user_id(only_digits=False)
    # Вызов с seed: result = user_id(length=8, only_digits=True, seed=1)
    # Пример результата: ID должен быть строкой длиной 8.
    # Документация: docs/function_specifications.md, раздел user_id.
    # Шаги реализации:
    # 1. Проверить, что length больше 0.
    # 2. Создать random через create_random(seed).
    # 3. Если only_digits=True, подготовить символы только из цифр.
    # 4. Если only_digits=False, подготовить символы из цифр и английских букв.
    # 5. Выбрать length случайных символов из подготовленного набора.
    # 6. Склеить выбранные символы в одну строку.
    # 7. Вернуть готовый ID.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py user_id
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_id_digits, test_id_alnum.
    # Проверяем, что длина ID больше нуля.
    if length <= 0:
        # Сообщаем ошибку, если длина неправильная.
        raise ValueError("length должен быть больше 0")
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Подготавливаем строку с цифрами для цифрового ID.
    digits = "0123456789"
    # Подготавливаем строку с английскими буквами и цифрами для смешанного ID.
    letters_and_digits = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Выбираем набор символов по параметру only_digits.
    characters = digits if only_digits else letters_and_digits
    # Собираем список случайных символов нужной длины.
    result_characters = [randomizer.choice(characters) for _ in range(length)]
    # Склеиваем выбранные символы в одну строку.
    result = "".join(result_characters)
    # Возвращаем готовый ID.
    return result
