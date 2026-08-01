# Файл нужен для функции age.
# Функция age должна генерировать возраст пользователя.
# В тестировании ПО такую функцию можно использовать, чтобы создавать тестовых пользователей разного возраста.

# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random


# Объявляем функцию, которая должна вернуть возраст пользователя.
def age(min_age=18, max_age=80, boundary=None, seed=None):
    # Что делает функция: возвращает число-возраст.
    # min_age - самый маленький возраст, например 18.
    # max_age - самый большой возраст, например 80.
    # boundary - это режим для специальных проверок в тестах.
    # boundary="min" значит вернуть min_age, например 18.
    # boundary="max" значит вернуть max_age, например 80.
    # boundary="below_min" значит вернуть число меньше минимума, например 17.
    # boundary="above_max" значит вернуть число больше максимума, например 81.
    # boundary=None значит выбрать случайный возраст от min_age до max_age.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же возраст.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.age import age
    # from procedural_version.generators.city import city
    #
    # age_result = age(min_age=18, max_age=80, seed=1)
    # print(age_result)
    #
    # city_result = city(starts_with="М", seed=1)
    # print(city_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = age()
    # Вызов с boundary: result = age(boundary="min")
    # Вызов со своим диапазоном: result = age(min_age=10, max_age=20)
    # Вызов с seed: result = age(min_age=18, max_age=80, seed=1)
    # Пример результата: возраст должен быть числом от 18 до 80.
    # Документация: docs/function_specifications.md, раздел age.
    # Шаги реализации:
    # 1. Проверить, что min_age не больше max_age.
    # 2. Если boundary равен "min", вернуть min_age.
    # 3. Если boundary равен "max", вернуть max_age.
    # 4. Если boundary равен "below_min", вернуть min_age - 1.
    # 5. Если boundary равен "above_max", вернуть max_age + 1.
    # 6. Создать random через create_random(seed).
    # 7. Вернуть случайное целое число от min_age до max_age.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py age
    # Или на Windows: py check.py age
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если min_age больше max_age, нужно вызвать ValueError.
    # Что вернуть: целое число.
    # Тесты: test_age_bounds, test_age_range.


    # Эталонное решение
    # Проверяем, что нижняя граница не больше верхней.
    # if min_age > max_age:
    #     # Сообщаем ошибку, если диапазон написан наоборот.
    #     raise ValueError("min_age не должен быть больше max_age")
    # # Возвращаем нижнюю границу.
    # if boundary == "min":
    #     # Возвращаем min_age.
    #     return min_age
    # # Возвращаем верхнюю границу.
    # if boundary == "max":
    #     # Возвращаем max_age.
    #     return max_age
    # # Возвращаем число ниже нижней границы.
    # if boundary == "below_min":
    #     # Возвращаем min_age минус 1.
    #     return min_age - 1
    # # Возвращаем число выше верхней границы.
    # if boundary == "above_max":
    #     # Возвращаем max_age плюс 1.
    #     return max_age + 1
    # # Создаем random с переданным seed.
    # randomizer = create_random(seed)
    # # Возвращаем случайный возраст внутри диапазона.
    # return randomizer.randint(min_age, max_age)


    # Артем
    # if min_age > max_age:
    #     raise ValueError("min_age не может быть больше max_age")
    # if boundary == "min":
    #     return min_age
    # elif boundary == "max":
    #     return max_age
    # elif boundary == "below_min":
    #     return min_age - 1
    # elif boundary == "above_max":
    #     return max_age + 1
    # randomizer = create_random(seed)
    # return randomizer.randint(min_age, max_age)


    # Илья
    if min_age > max_age:
        raise ValueError("min_age must not be greater than max_age")

    if boundary == "min":
        return min_age
    if boundary == "max":
        return max_age
    if boundary == "below_min":
        return min_age - 1
    if boundary == "above_max":
        return max_age + 1

    randomizer = create_random(seed)
    return randomizer.randint(min_age, max_age)

