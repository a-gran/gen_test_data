# Файл нужен для функции full_name.
# Функция full_name должна собирать имя и фамилию пользователя в одну строку.
# В тестировании ПО такую функцию можно использовать, чтобы проверять отображение полного имени в профиле и документах.

# Импортируем список имен.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random
# Импортируем помощник для выбора случайного элемента.
from procedural_version.utils.random_utils import choose_item

# Объявляем функцию, которая должна вернуть имя и фамилию вместе.
def full_name(max_total_length=None, seed=None):
    # Что делает функция: возвращает строку вроде "Анна Иванова".
    # max_total_length=None значит полное имя можно не обрезать.
    # max_total_length=10 значит результат должен быть не длиннее 10 символов.
    # seed - число для random: с одним и тем же seed random выбирает одно и то же имя и фамилию.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.full_name import full_name
    # from procedural_version.generators.age import age
    #
    # full_name_result = full_name(max_total_length=10, seed=1)
    # print(full_name_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = full_name()
    # Вызов с ограничением длины: result = full_name(max_total_length=10)
    # Вызов с seed: result = full_name(seed=1)
    # Пример результата: полное имя должно быть строкой длиной 10 или меньше.
    # Документация: docs/function_specifications.md, раздел full_name.
    # Шаги реализации:
    # 1. Создать random через create_random(seed).
    # 2. Выбрать имя из FIRST_NAMES.
    # 3. Выбрать фамилию из LAST_NAMES.
    # 4. Собрать строку в формате "Имя Фамилия".
    # 5. Если max_total_length передан, подобрать или обрезать результат до нужной длины.
    # 6. Вернуть готовое полное имя.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py full_name
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: без ограничения в строке должен быть пробел между именем и фамилией.
    # Что вернуть: строку с именем, пробелом и фамилией.
    # Тесты: test_full_name_max_len, test_full_name_basic.
    pass
