# Файл нужен для функции password.
# Функция password должна генерировать пароль с нужными правилами.
# В тестировании ПО такую функцию можно использовать, чтобы проверять правила создания и проверки паролей.

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
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.password import password
    # from procedural_version.generators.age import age
    #
    # password_result = password(length=16, use_digits=True, use_symbols=True, seed=1)
    # print(password_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = password()
    # Вызов с длиной: result = password(length=16)
    # Вызов без цифр: result = password(use_digits=False)
    # Вызов с seed: result = password(length=16, use_digits=True, use_symbols=True, seed=1)
    # Пример результата: пароль должен быть строкой длиной 16.
    # Документация: docs/function_specifications.md, раздел password.
    # Шаги реализации:
    # 1. Проверить, что length больше 0.
    # 2. Создать random через create_random(seed).
    # 3. Собрать набор символов для пароля.
    # 4. Если use_digits=True, добавить в пароль хотя бы одну цифру.
    # 5. Если use_symbols=True, добавить в пароль хотя бы один спецсимвол.
    # 6. Дополнить пароль случайными символами до длины length.
    # 7. Перемешать символы, чтобы обязательные символы не всегда стояли на одном месте.
    # 8. Вернуть пароль строкой ровно из length символов.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py password
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку с паролем.
    # Тесты: test_password_parts, test_password_bad_len.
    pass
