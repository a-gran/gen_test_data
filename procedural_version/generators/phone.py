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
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Проверяем, нужен ли правильный телефон.
    if valid:
        # Выбираем правильный код оператора.
        operator_code = randomizer.randint(900, 999)
        # Выбираем правильную основную часть номера.
        number = randomizer.randint(1000000, 9999999)
        # Возвращаем словарь с правильными телефонными данными.
        return {
            # Записываем правильный код страны.
            "country_code": "+7",
            # Записываем код оператора.
            "operator_code": operator_code,
            # Записываем основную часть номера.
            "number": number,
        }
    # Выбираем неправильный код оператора ниже разрешенного диапазона.
    operator_code = randomizer.randint(100, 899)
    # Выбираем слишком короткую основную часть номера.
    number = randomizer.randint(1, 999999)
    # Возвращаем словарь со специально неправильными телефонными данными.
    return {
        # Записываем неправильный код страны.
        "country_code": "+1",
        # Записываем неправильный код оператора.
        "operator_code": operator_code,
        # Записываем слишком короткую основную часть номера.
        "number": number,
    }
