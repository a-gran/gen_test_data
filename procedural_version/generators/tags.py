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
    # Можно вызвать tags() и получить от 1 до 3 разных тегов.
    # Можно вызвать tags(count=5) и получить ровно 5 разных тегов.
    # Можно вызвать tags(count=5, unique=False) и разрешить одинаковые теги.
    # Можно вызвать tags(count=5, unique=True, seed=1) и сочетать настройки.
    # Пример вызова: tags(count=5, unique=True, seed=1) должен вернуть 5 разных тегов.
    # Документация: docs/function_specifications.md, раздел tags.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py tags
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если count меньше 0, нужно вызвать ValueError.
    # Что вернуть: список строк.
    # Тесты: test_tags_unique, test_tags_dupes.
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Проверяем, нужно ли выбрать случайное количество тегов.
    if count is None:
        # Выбираем количество тегов от 1 до 3.
        count = randomizer.randint(1, 3)
    # Проверяем, что количество тегов не отрицательное.
    if count < 0:
        # Сообщаем ошибку, если количество меньше нуля.
        raise ValueError("count не должен быть меньше 0")
    # Проверяем, нужны ли уникальные теги.
    if unique:
        # Проверяем, что уникальных тегов хватит.
        if count > len(TAGS):
            # Сообщаем ошибку, если запросили слишком много уникальных тегов.
            raise ValueError("count больше количества доступных тегов")
        # Возвращаем список уникальных тегов.
        return randomizer.sample(TAGS, count)
    # Возвращаем список тегов, где повторы разрешены.
    return [randomizer.choice(TAGS) for _ in range(count)]
