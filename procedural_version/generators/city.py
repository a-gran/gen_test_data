# Файл нужен для функции city.
# Функция city должна выбирать город пользователя из учебного списка.
# В тестировании ПО такую функцию можно использовать, чтобы проверять доставку, регистрацию и фильтры по городам.

# Импортируем список городов, из которого нужно выбирать результат.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть город.
def city(starts_with=None, seed=None):
    # Что делает функция: выбирает один город из CITY_NAMES.
    # starts_with=None значит можно выбрать любой город.
    # starts_with="М" значит можно выбрать только город, который начинается с буквы "М".
    # seed - число для random: с одним и тем же seed random выбирает один и тот же город.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.city import city
    # from procedural_version.generators.age import age
    #
    # city_result = city(starts_with="М", seed=1)
    # print(city_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = city()
    # Вызов с фильтром: result = city(starts_with="М")
    # Вызов с seed: result = city(seed=1)
    # Пример результата: город должен начинаться на "М".
    # Документация: docs/function_specifications.md, раздел city.
    # Шаги реализации:
    # 1. Начать со всего списка CITY_NAMES.
    # 2. Если starts_with передан, оставить только города, которые начинаются с этого текста.
    # 3. Проверить, что после фильтрации список не пустой.
    # 4. Создать random через create_random(seed).
    # 5. Вернуть случайный город из подходящего списка.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py city
    # Или на Windows: py check.py city
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если подходящих городов нет, нужно вызвать ValueError.
    # Что вернуть: строку с названием города.
    # Тесты: test_city_prefix, test_city_list.


    # Давид
    # 1. Начать со всего списка CITY_NAMES.
    city = CITY_NAMES
    # 2. Если starts_with передан, оставить только города, которые начинаются с этого текста.
    if starts_with is not None:
        current_city = [i for i in city if i.startswith(starts_with)]
    else:
        current_city = city
    # 3. Проверить, что после фильтрации список не пустой.
    if not current_city:
        raise ValueError
    # 4. Создать random через create_random(seed).
    randomizer = create_random(seed)
    # 5. Вернуть случайный город из подходящего списка.
    return randomizer.choice(current_city)