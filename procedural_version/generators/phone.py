# Файл нужен для функции phone.
# Функция phone должна генерировать словарь с телефонными данными.
# В тестировании ПО такую функцию можно использовать, чтобы проверять формы с телефонными номерами.

# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть телефон.
def phone(valid=True, seed=None):
    # Что делает функция: возвращает словарь с телефоном.
    # valid=True значит телефон должен быть правильным.
    # Правильный country_code должен быть "+7".
    # Правильный operator_code должен быть числом от 900 до 999.
    # Правильный number должен быть числом от 1000000 до 9999999.
    # valid=False значит телефон должен быть специально неправильным для негативного теста.
    # seed - число для random: с одним и тем же seed random собирает один и тот же телефон.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.phone import phone
    # from procedural_version.generators.age import age
    #
    # phone_result = phone(valid=True, seed=1)
    # print(phone_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = phone()
    # Вызов неправильного телефона: result = phone(valid=False)
    # Вызов с seed: result = phone(seed=1)
    # Пример результата: телефон должен быть словарем.
    # Документация: docs/function_specifications.md, раздел phone.
    # Шаги реализации:
    # 1. Создать random через create_random(seed).
    # 2. Если valid=True, выбрать operator_code от 900 до 999.
    # 3. Если valid=True, выбрать number от 1000000 до 9999999.
    # 4. Если valid=True, вернуть словарь с country_code "+7".
    # 5. Если valid=False, специально собрать словарь с неправильными телефонными данными.
    # 6. Вернуть словарь с ключами country_code, operator_code и number.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py phone
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: словарь с ключами country_code, operator_code и number.
    # Тесты: test_phone_validity, test_phone_code.
    pass
