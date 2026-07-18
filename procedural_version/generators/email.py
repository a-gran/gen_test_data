# Импортируем список доменов для генерации адреса электронной почты.
from procedural_version.data.names_data import EMAIL_DOMAINS
# Импортируем список слов для генерации имени почтового ящика.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует адрес электронной почты.
def generate_email(valid=True, username_length=8, seed=None):
    # Что такое seed: это значение, которое делает случайный email повторяемым для тестов.
    # Если вызвать функцию два раза с одинаковым seed, случайный результат должен быть одинаковым.
    # Входные данные: valid - если True, email должен быть правильным; если False, email должен быть с ошибкой.
    # Входные данные: username_length - точная длина части email до знака @.
    # Входные данные: seed - значение для повторяемой генерации.
    # Внутренние переменные: randomizer - генератор случайности, который создается через create_random(seed).
    # Внутренние переменные: username_word - учебное слово для начала username.
    # Внутренние переменные: alphabet - строка разрешенных символов для username.
    # Внутренние переменные: username - готовая часть email до знака @.
    # Внутренние переменные: domain - домен email из EMAIL_DOMAINS.
    # Выходные данные: функция должна вернуть строку с email.
    # Шаг 1. Проверь, что username_length больше 0, потому что имя почтового ящика должно иметь длину.
    # Шаг 2. Создай randomizer через create_random(seed), чтобы email можно было повторить.
    # Шаг 3. Выбери учебное слово из USERNAME_WORDS для начала username.
    # Шаг 4. Добавляй разрешенные символы, пока username не станет нужной длины.
    # Шаг 5. Выбери домен из EMAIL_DOMAINS.
    # Шаг 6. Если valid равен False, верни email с намеренной ошибкой без знака @.
    # Шаг 7. Если valid равен True, верни email в формате username@domain.
    # Проверка после реализации: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_email_can_return_valid_and_invalid_values
    # Если все хорошо, в конце вывода unittest будет написано OK.
    # Если тест упал, проверь наличие знака @ в valid=True и его отсутствие в valid=False.
    pass
