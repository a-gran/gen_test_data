# Файл нужен для функции comment.
# Функция comment должна генерировать текстовый комментарий нужной длины.
# В тестировании ПО такую функцию можно использовать, чтобы проверять поля комментариев с разной длиной текста.

# Импортируем список готовых фраз для комментария.
from procedural_version.data.names_data import COMMENTS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть комментарий точной длины.
def comment(length=100, seed=None):
    # Что делает функция: возвращает строку ровно из length символов.
    # length=0 значит вернуть пустую строку "".
    # length=1 значит вернуть строку из одного символа.
    # length=255 значит вернуть строку длиной ровно 255 символов.
    # seed - число для random: с одним и тем же seed random выбирает одну и ту же фразу.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.comment import comment
    # from procedural_version.generators.age import age
    #
    # comment_result = comment(length=255, seed=1)
    # print(comment_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = comment()
    # Вызов с пустой строкой: result = comment(length=0)
    # Вызов с длиной и seed: result = comment(length=255, seed=1)
    # Пример результата: len(result) должен быть 255.
    # Документация: docs/function_specifications.md, раздел comment.
    # Шаги реализации:
    # 1. Проверить, что length не меньше 0.
    # 2. Если length равен 0, вернуть пустую строку.
    # 3. Создать random через create_random(seed).
    # 4. Выбрать одну или несколько фраз из COMMENTS.
    # 5. Собрать длинную строку из выбранных фраз.
    # 6. Обрезать строку так, чтобы ее длина стала ровно length.
    # 7. Вернуть готовый комментарий.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py comment
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше 0, нужно вызвать ValueError.
    # Что вернуть: строку.
    # Тесты: test_comment_lengths, test_comment_bad_len.
    # Проверяем, что длина комментария не отрицательная.
    if length < 0:
        # Сообщаем ошибку, если длина неправильная.
        raise ValueError("length не должен быть меньше 0")
    # Проверяем, нужен ли пустой комментарий.
    if length == 0:
        # Возвращаем пустую строку.
        return ""
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Создаем пустой список для частей комментария.
    comment_parts = []
    # Собираем текст, пока его длина меньше нужной.
    while len(" ".join(comment_parts)) < length:
        # Добавляем случайную фразу из учебного списка.
        comment_parts.append(randomizer.choice(COMMENTS))
    # Склеиваем выбранные фразы через пробел.
    result = " ".join(comment_parts)
    # Обрезаем текст до точной нужной длины.
    result = result[:length]
    # Возвращаем готовый комментарий.
    return result
