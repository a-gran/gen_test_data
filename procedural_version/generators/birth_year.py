# Файл нужен для функции birth_year.
# Функция birth_year должна генерировать год рождения пользователя.
# В тестировании ПО такую функцию можно использовать, чтобы проверять формы, отчеты и фильтры по году рождения.

# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть год рождения пользователя.
def birth_year(min_year=1950, max_year=2008, boundary=None, seed=None):
    # Что делает функция: возвращает число-год рождения.
    # min_year - самый маленький год, например 1950.
    # max_year - самый большой год, например 2008.
    # boundary - это режим для специальных проверок в тестах.
    # boundary="min" значит вернуть min_year, например 1950.
    # boundary="max" значит вернуть max_year, например 2008.
    # boundary="below_min" значит вернуть год меньше минимума, например 1949.
    # boundary="above_max" значит вернуть год больше максимума, например 2009.
    # boundary=None значит выбрать случайный год от min_year до max_year.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же год.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.birth_year import birth_year
    # from procedural_version.generators.age import age
    #
    # birth_year_result = birth_year(boundary="max", seed=1)
    # print(birth_year_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = birth_year()
    # Вызов с boundary: result = birth_year(boundary="max")
    # Вызов со своим диапазоном: result = birth_year(min_year=2000, max_year=2010)
    # Вызов с seed: result = birth_year(seed=1)
    # Пример результата: год должен быть числом от 1950 до 2008.
    # Документация: docs/function_specifications.md, раздел birth_year.
    # Шаги реализации:
    # 1. Проверить, что min_year не больше max_year.
    # 2. Если boundary равен "min", вернуть min_year.
    # 3. Если boundary равен "max", вернуть max_year.
    # 4. Если boundary равен "below_min", вернуть min_year - 1.
    # 5. Если boundary равен "above_max", вернуть max_year + 1.
    # 6. Создать random через create_random(seed).
    # 7. Вернуть случайный год от min_year до max_year.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py birth_year
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если min_year больше max_year, нужно вызвать ValueError.
    # Что вернуть: целое число.
    # Тесты: test_birth_year_bounds, test_birth_year_range.

    ## Проверяем, что нижняя граница не больше верхней.
    if min_year > max_year:
        # Сообщаем ошибку, если диапазон написан наоборот.
        raise ValueError("min_year не должен быть больше max_year")
    # Возвращаем нижнюю границу года.
    if boundary == "min":
        # Возвращаем min_year.
        return min_year
    # Возвращаем верхнюю границу года.
    if boundary == "max":
        # Возвращаем max_year.
        return max_year
    # Возвращаем год ниже нижней границы.
    if boundary == "below_min":
        # Возвращаем min_year минус 1.
        return min_year - 1
    # Возвращаем год выше верхней границы.
    if boundary == "above_max":
        # Возвращаем max_year плюс 1.
        return max_year + 1
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Возвращаем случайный год внутри диапазона.
    return randomizer.randint(min_year, max_year)



    # Борис
    # if min_year > max_year:
    #     raise ValueError()
    # if seed is not None:
    #     random.seed(seed)
    # if boundary == "min":
    #     return min_year
    # elif boundary == "max":
    #     return max_year
    # elif boundary == "b_min":
    #     return min_year - 1
    # elif boundary == "a_min":
    #     return max_year + 1
    # elif boundary is None:
    #     return random.randint(min_year, max_year)
    # else:
    #     raise ValueError()
