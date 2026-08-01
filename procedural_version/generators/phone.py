# Файл нужен для функции phone.
# Функция phone должна генерировать строку с полным номером телефона.
# В тестировании ПО такую функцию можно использовать, чтобы проверять формы с телефонными номерами.

# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть телефон.
def phone(valid=True, seed=None):
    # Что делает функция: возвращает строку с телефоном.
    # valid=True значит телефон должен быть правильным.
    # Правильный телефон должен начинаться с "+7".
    # Правильный код оператора должен быть числом от 900 до 999.
    # Правильная основная часть номера должна быть числом от 1000000 до 9999999.
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
    # Пример результата: телефон должен быть строкой, например "+79123456789".
    # Документация: docs/function_specifications.md, раздел phone.
    # Шаги реализации:
    # 1. Создать random через create_random(seed).
    # 2. Если valid=True, выбрать operator_code от 900 до 999.
    # 3. Если valid=True, выбрать number от 1000000 до 9999999.
    # 4. Если valid=True, вернуть строку с кодом страны "+7".
    # 5. Если valid=False, специально собрать строку с неправильным телефоном.
    # 6. Вернуть полный телефон одной строкой.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py phone
    # Или на Windows: py check.py phone
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: строку с полным номером телефона.
    # Тесты: test_phone_validity, test_phone_code.


    # Эталонное решение
    # Создаем random с переданным seed.
    # randomizer = create_random(seed)
    # # Проверяем, нужен ли правильный телефон.
    # if valid:
    #     # Выбираем правильный код оператора.
    #     operator_code = randomizer.randint(900, 999)
    #     # Выбираем правильную основную часть номера.
    #     number = randomizer.randint(1000000, 9999999)
    #     # Возвращаем словарь с правильными телефонными данными.
    #     return {
    #         # Записываем правильный код страны.
    #         "country_code": "+7",
    #         # Записываем код оператора.
    #         "operator_code": operator_code,
    #         # Записываем основную часть номера.
    #         "number": number,
    #     }
    # # Выбираем неправильный код оператора ниже разрешенного диапазона.
    # operator_code = randomizer.randint(100, 899)
    # # Выбираем слишком короткую основную часть номера.
    # number = randomizer.randint(1, 999999)
    # # Возвращаем словарь со специально неправильными телефонными данными.
    # return {
    #     # Записываем неправильный код страны.
    #     "country_code": "+1",
    #     # Записываем неправильный код оператора.
    #     "operator_code": operator_code,
    #     # Записываем слишком короткую основную часть номера.
    #     "number": number,
    # }


    # Боря
    # if valid:
    #     country_code = "+7"
    #     operator_code = rng.randint(900, 999)
    #     number = rng.randint(1000000, 9999999)
    # else:
    #     error_type = rng.randint(0, 2)
    #     if error_type == 0:
    #         country_code = rng.choice(["+1", "+44", "+49", "+39", "+380", "+86", "+91", "+61"])
    #         operator_code = rng.randint(900, 999)
    #         number = rng.randint(1000000, 9999999)
    #     elif error_type == 1:
    #         country_code = "+7"
    #         operator_code = rng.randint(900, 999)
    #         number = rng.randint(0, 9999999)
    #     return {
    #         "country_code": country_code
    #         "operator_code": operator_code
    #         "number": number
    #     }


    # Илья
    randomizer = create_random(seed)

    # Проверяем, нужен ли специально неправильный телефон.
    if not valid:
        # Генерируем неправильный код оператора ниже разрешенного диапазона.
        operator_code = randomizer.randint(100, 899)
        # Генерируем короткую основную часть номера.
        number = randomizer.randint(10000, 999999)
        # Возвращаем специально неправильный телефон строкой.
        return f"+0{operator_code}{number}"

    # Генерируем правильный код оператора.
    operator_code = randomizer.randint(900, 999)
    # Генерируем семь цифр основной части телефона.
    number = randomizer.randint(1000000, 9999999)
    # Возвращаем полный телефон одной строкой.
    return f"+7{operator_code}{number}"
