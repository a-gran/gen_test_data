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
    # Можно вызвать first_name() и получить любое имя из списка.
    # Можно вызвать first_name(min_length=5) и получить имя длиной 5 символов или больше.
    # Можно вызвать first_name(max_length=4) и получить имя длиной 4 символа или меньше.
    # Можно вызвать first_name(min_length=4, max_length=6, seed=1) и сочетать ограничения.
    # Пример вызова: first_name(min_length=5, seed=1) должен вернуть имя длиной 5 или больше.
    # Документация: docs/function_specifications.md, раздел first_name.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py first_name
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если подходящих имен нет, нужно вызвать ValueError.
    # Что вернуть: строку с именем.
    # Тесты: test_first_name_min_len, test_first_name_max_len.
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Начинаем со всего списка имен.
    available_names = FIRST_NAMES
    # Проверяем, есть ли ограничение минимальной длины.
    if min_length is not None:
        # Оставляем только имена не короче min_length.
        available_names = [name for name in available_names if len(name) >= min_length]
    # Проверяем, есть ли ограничение максимальной длины.
    if max_length is not None:
        # Оставляем только имена не длиннее max_length.
        available_names = [name for name in available_names if len(name) <= max_length]
    # Проверяем, что после фильтров осталось хотя бы одно имя.
    if not available_names:
        # Сообщаем ошибку, если подходящих имен нет.
        raise ValueError("Нет имен с такой длиной")
    # Возвращаем случайное имя из подходящего списка.
    return randomizer.choice(available_names)
