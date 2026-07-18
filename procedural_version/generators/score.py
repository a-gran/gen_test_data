# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует учебный балл.
def generate_score(min_score=1, max_score=100, boundary=None, seed=None):
    # Проверяем, что минимальный балл не больше максимального.
    if min_score > max_score:
        # Сообщаем понятную ошибку, если границы перепутаны местами.
        raise ValueError("min_score не должен быть больше max_score")
    # Проверяем, попросили ли вернуть нижнюю границу.
    if boundary == "min":
        # Возвращаем минимальный допустимый балл.
        return min_score
    # Проверяем, попросили ли вернуть верхнюю границу.
    if boundary == "max":
        # Возвращаем максимальный допустимый балл.
        return max_score
    # Проверяем, попросили ли вернуть значение ниже нижней границы.
    if boundary == "below_min":
        # Возвращаем балл на единицу меньше минимума для негативного теста.
        return min_score - 1
    # Проверяем, попросили ли вернуть значение выше верхней границы.
    if boundary == "above_max":
        # Возвращаем балл на единицу больше максимума для негативного теста.
        return max_score + 1
    # Создаем генератор случайности для учебного балла.
    randomizer = create_random(seed)
    # Возвращаем случайный балл внутри переданных границ.
    return randomizer.randint(min_score, max_score)
