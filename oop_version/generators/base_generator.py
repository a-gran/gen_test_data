# Импортируем класс с исходными данными для генераторов.
from oop_version.data.data_provider import DataProvider
# Импортируем функцию создания генератора случайности.
from oop_version.utils.random_utils import create_random

# Объявляем базовый класс для всех ООП-генераторов.
class BaseGenerator:
    # Объявляем метод, который запускается при создании объекта.
    def __init__(self, seed=None):
        # Сохраняем seed, чтобы вложенные генераторы могли повторить тот же результат.
        self.seed = seed
        # Сохраняем объект с исходными данными внутри генератора.
        self.data_provider = DataProvider()
        # Сохраняем генератор случайности внутри объекта.
        self.randomizer = create_random(seed)

    # Объявляем метод, который выбирает случайный элемент из списка.
    def choose_item(self, items):
        # Возвращаем случайный элемент с помощью генератора случайности объекта.
        return self.randomizer.choice(items)
