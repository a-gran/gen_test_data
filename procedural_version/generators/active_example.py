# Файл нужен для функции active_example.
# Функция active_example показывает готовый пример генератора активности пользователя.
# В тестировании ПО такую функцию можно использовать, чтобы проверять сценарии для активных и неактивных пользователей.

# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем готовый пример функции активности.
def active_example(seed=None):
    # Что делает функция: возвращает True или False.
    # True значит пользователь активен.
    # False значит пользователь не активен.
    # seed - число для random: с одним и тем же seed random выбирает одно и то же True или False.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.active_example import active_example
    # from procedural_version.generators.age import age
    #
    # active_result = active_example(seed=1)
    # print(active_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = active_example()
    # Вызов с seed: result = active_example(seed=1)
    # Пример результата: функция должна вернуть True или False.
    # Документация: docs/function_specifications.md, раздел active.
    # Шаги реализации:
    # 1. Создать random через create_random(seed).
    # 2. Подготовить список из двух значений: True и False.
    # 3. Выбрать одно случайное значение из этого списка.
    # 4. Вернуть выбранное булево значение.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py active_example
    # Или на Windows: py check.py active_example
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: только True или False, не строку "True" и не число 1.
    # Проверка тестами: python check.py active_example
    # Или на Windows: py check.py active_example
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Выбираем True или False и сразу возвращаем результат.
    return randomizer.choice([True, False])
