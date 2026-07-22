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
    # Можно вызвать full_name() и получить имя и фамилию через пробел.
    # Можно вызвать full_name(max_total_length=10) и получить результат до 10 символов.
    # Можно вызвать full_name(seed=1) два раза и получить один и тот же результат.
    # Пример вызова: full_name(max_total_length=10, seed=1) должен вернуть строку длиной 10 или меньше.
    # Документация: docs/function_specifications.md, раздел full_name.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py full_name
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: без ограничения в строке должен быть пробел между именем и фамилией.
    # Что вернуть: строку с именем, пробелом и фамилией.
    # Тесты: test_full_name_max_len, test_full_name_basic.
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Проверяем, передано ли ограничение общей длины.
    if max_total_length is not None:
        # Собираем все пары имени и фамилии, которые помещаются в ограничение.
        available_full_names = [f"{name} {surname}" for name in FIRST_NAMES for surname in LAST_NAMES if len(f"{name} {surname}") <= max_total_length]
        # Проверяем, что подходящая пара нашлась.
        if not available_full_names:
            # Сообщаем ошибку, если полное имя не помещается в ограничение.
            raise ValueError("Нет полного имени с такой общей длиной")
        # Возвращаем случайное полное имя из подходящего списка.
        return randomizer.choice(available_full_names)
    # Выбираем случайное имя из общего списка.
    name = choose_item(FIRST_NAMES, randomizer=randomizer)
    # Выбираем случайную фамилию из общего списка.
    surname = choose_item(LAST_NAMES, randomizer=randomizer)
    # Возвращаем имя и фамилию через пробел.
    return f"{name} {surname}"
