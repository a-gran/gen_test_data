# Импортируем список комментариев для генерации случайного комментария.
from procedural_version.data.names_data import COMMENTS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует комментарий любой заданной длины.
def generate_comment(length=100, seed=None):
    # Проверяем, что длина комментария не отрицательная.
    if length < 0:
        # Сообщаем понятную ошибку, если длина меньше нуля.
        raise ValueError("length не должен быть меньше 0")
    # Создаем генератор случайности для выбора основы комментария.
    randomizer = create_random(seed)
    # Выбираем базовый текст, чтобы комментарий был похож на человеческую фразу.
    base_comment = randomizer.choice(COMMENTS)
    # Повторяем базовый текст с пробелом, чтобы точно набрать нужную длину.
    repeated_comment = (base_comment + " ") * ((length // (len(base_comment) + 1)) + 2)
    # Обрезаем повторенный текст ровно до нужного количества символов.
    return repeated_comment[:length]
