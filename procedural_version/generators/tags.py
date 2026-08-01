# Файл нужен для функции tags.
# Функция tags должна генерировать список тегов пользователя.
# В тестировании ПО такую функцию можно использовать, чтобы проверять поиск, фильтрацию и отображение тегов.

# Импортируем список тегов, из которого нужно выбирать результат.
from procedural_version.data.names_data import TAGS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть список тегов.
def tags(count=None, unique=True, seed=None):
    # Что делает функция: возвращает список строк-тегов.
    # count=None значит выбрать случайное количество тегов от 1 до 3.
    # count=5 значит вернуть ровно 5 тегов.
    # unique=True значит теги не должны повторяться.
    # unique=False значит повторы разрешены.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же список тегов.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.tags import tags
    # from procedural_version.generators.age import age
    #
    # tags_result = tags(count=5, unique=True, seed=1)
    # print(tags_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = tags()
    # Вызов с количеством: result = tags(count=5)
    # Вызов с повторами: result = tags(count=5, unique=False)
    # Вызов с seed: result = tags(count=5, unique=True, seed=1)
    # Пример результата: список должен содержать 5 разных тегов.
    # Документация: docs/function_specifications.md, раздел tags.
    # Шаги реализации:
    # 1. Проверить, что count не меньше 0, если count передан.
    # 2. Создать random через create_random(seed).
    # 3. Если count=None, выбрать случайное количество тегов от 1 до 3.
    # 4. Если unique=True, выбрать теги без повторов.
    # 5. Если unique=False, выбрать теги с возможными повторами.
    # 6. Вернуть список выбранных тегов.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py tags
    # Или на Windows: py check.py tags
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если count меньше 0, нужно вызвать ValueError.
    # Что вернуть: список строк.
    # Тесты: test_tags_unique, test_tags_dupes.
    # Проверяем, что count не отрицательный, если он передан.
    if count is not None and count < 0:
        # Сообщаем ошибку, если количество тегов неправильное.
        raise ValueError("count не должен быть меньше 0")
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Если count не передан, выбираем случайное количество тегов от 1 до 3.
    selected_count = count if count is not None else randomizer.randint(1, 3)
    # Проверяем, нужны ли уникальные теги.
    if unique:
        # Проверяем, что уникальных тегов в списке хватает.
        if selected_count > len(TAGS):
            # Сообщаем ошибку, если невозможно выбрать столько уникальных тегов.
            raise ValueError("count больше количества доступных уникальных тегов")
        # Возвращаем случайные теги без повторов.
        return randomizer.sample(TAGS, selected_count)
    # Создаем пустой список для тегов с возможными повторами.
    selected_tags = []
    # Добавляем теги, пока не получим нужное количество.
    for _ in range(selected_count):
        # Добавляем один случайный тег из учебного списка.
        selected_tags.append(randomizer.choice(TAGS))
    # Возвращаем готовый список тегов.
    return selected_tags
