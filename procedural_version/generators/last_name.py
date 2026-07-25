# Файл нужен для функции last_name.
# Функция last_name должна выбирать фамилию пользователя из учебного списка.
# В тестировании ПО такую функцию можно использовать, чтобы заполнять формы регистрации тестовыми фамилиями.

# Импортируем список фамилий, из которого нужно выбирать результат.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть фамилию.
def last_name(min_length=None, max_length=None, seed=None):
    # Что делает функция: выбирает одну фамилию из LAST_NAMES.
    # min_length=None значит нет ограничения снизу.
    # min_length=8 значит фамилия должна быть длиной 8 символов или больше.
    # max_length=None значит нет ограничения сверху.
    # max_length=7 значит фамилия должна быть длиной 7 символов или меньше.
    # seed - число для random: с одним и тем же seed random выбирает одну и ту же фамилию.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.last_name import last_name
    # from procedural_version.generators.age import age
    #
    # last_name_result = last_name(max_length=7, seed=1)
    # print(last_name_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = last_name()
    # Вызов с минимальной длиной: result = last_name(min_length=8)
    # Вызов с максимальной длиной: result = last_name(max_length=7)
    # Вызов с seed: result = last_name(max_length=7, seed=1)
    # Пример результата: фамилия должна быть длиной 7 символов или меньше.
    # Документация: docs/function_specifications.md, раздел last_name.
    # Шаги реализации:
    # 1. Начать со всего списка LAST_NAMES.
    # 2. Если min_length передан, оставить только фамилии не короче min_length.
    # 3. Если max_length передан, оставить только фамилии не длиннее max_length.
    # 4. Проверить, что после фильтрации список не пустой.
    # 5. Создать random через create_random(seed).
    # 6. Вернуть случайную фамилию из подходящего списка.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py last_name
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если подходящих фамилий нет, нужно вызвать ValueError.
    # Что вернуть: строку с фамилией.
    # Тесты: test_last_name_max_len, test_last_name_min_len.
    pass
