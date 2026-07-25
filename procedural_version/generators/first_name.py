# Файл нужен для функции first_name.
# Функция first_name должна выбирать имя пользователя из учебного списка.
# В тестировании ПО такую функцию можно использовать, чтобы заполнять формы регистрации тестовыми именами.

# Импортируем список имен, из которого нужно выбирать результат.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть имя.
def first_name(min_length=None, max_length=None, seed=None):
    # Что делает функция: выбирает одно имя из FIRST_NAMES.
    # min_length=None значит нет ограничения снизу.
    # min_length=5 значит имя должно быть длиной 5 символов или больше.
    # max_length=None значит нет ограничения сверху.
    # max_length=4 значит имя должно быть длиной 4 символа или меньше.
    # seed - число для random: с одним и тем же seed random выбирает одно и то же имя.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.first_name import first_name
    # from procedural_version.generators.age import age
    #
    # first_name_result = first_name(min_length=5, seed=1)
    # print(first_name_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = first_name()
    # Вызов с минимальной длиной: result = first_name(min_length=5)
    # Вызов с максимальной длиной: result = first_name(max_length=4)
    # Вызов с seed: result = first_name(min_length=5, seed=1)
    # Пример результата: имя должно быть длиной 5 символов или больше.
    # Документация: docs/function_specifications.md, раздел first_name.
    # Шаги реализации:
    # 1. Начать со всего списка FIRST_NAMES.
    # 2. Если min_length передан, оставить только имена не короче min_length.
    # 3. Если max_length передан, оставить только имена не длиннее max_length.
    # 4. Проверить, что после фильтрации список не пустой.
    # 5. Создать random через create_random(seed).
    # 6. Вернуть случайное имя из подходящего списка.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py first_name
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если подходящих имен нет, нужно вызвать ValueError.
    # Что вернуть: строку с именем.
    # Тесты: test_first_name_min_len, test_first_name_max_len.
    pass
