# Файл нужен для функции score_example.
# Функция score_example показывает готовый пример генератора учебного балла.
# В тестировании ПО такую функцию можно использовать, чтобы проверять рейтинги, оценки и числовые фильтры.

# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем готовый пример функции учебного балла.
def score_example(min_score=1, max_score=100, boundary=None, seed=None):
    # Что делает функция: возвращает число-балл.
    # min_score - самый маленький балл, например 1.
    # max_score - самый большой балл, например 100.
    # boundary - это режим для специальных проверок в тестах.
    # boundary="min" значит вернуть min_score, например 1.
    # boundary="max" значит вернуть max_score, например 100.
    # boundary="below_min" значит вернуть число меньше минимума, например 0.
    # boundary="above_max" значит вернуть число больше максимума, например 101.
    # boundary=None значит выбрать случайный балл от min_score до max_score.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же балл.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.score_example import score_example
    # from procedural_version.generators.age import age
    #
    # score_result = score_example(boundary="above_max", seed=1)
    # print(score_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = score_example()
    # Вызов с boundary: result = score_example(boundary="min")
    # Вызов со своим диапазоном: result = score_example(min_score=10, max_score=20)
    # Вызов с seed: result = score_example(min_score=10, max_score=20, seed=1)
    # Пример результата: балл должен быть целым числом.
    # Документация: docs/function_specifications.md, раздел score.
    # Шаги реализации:
    # 1. Проверить, что min_score не больше max_score.
    # 2. Если boundary равен "min", вернуть min_score.
    # 3. Если boundary равен "max", вернуть max_score.
    # 4. Если boundary равен "below_min", вернуть min_score - 1.
    # 5. Если boundary равен "above_max", вернуть max_score + 1.
    # 6. Создать random через create_random(seed).
    # 7. Вернуть случайный балл от min_score до max_score.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py score_example
    # Или на Windows: py check.py score_example
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: целое число.
    # Проверка тестами: python check.py score_example
    # Или на Windows: py check.py score_example
    # Проверяем, что нижняя граница не больше верхней.
    if min_score > max_score:
        # Сообщаем ошибку, если диапазон написан наоборот.
        raise ValueError("min_score не должен быть больше max_score")
    # Возвращаем нижнюю границу.
    if boundary == "min":
        # Возвращаем min_score.
        return min_score
    # Возвращаем верхнюю границу.
    if boundary == "max":
        # Возвращаем max_score.
        return max_score
    # Возвращаем число ниже нижней границы.
    if boundary == "below_min":
        # Возвращаем min_score минус 1.
        return min_score - 1
    # Возвращаем число выше верхней границы.
    if boundary == "above_max":
        # Возвращаем max_score плюс 1.
        return max_score + 1
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Возвращаем случайный балл внутри диапазона.
    return randomizer.randint(min_score, max_score)
