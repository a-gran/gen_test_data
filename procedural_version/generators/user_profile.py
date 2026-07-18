# Импортируем список имен для генерации случайного имени.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий для генерации случайной фамилии.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем список городов для генерации случайного города.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем список планов подписки для генерации варианта аккаунта пользователя.
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Импортируем функцию генерации даты регистрации.
from procedural_version.generators.registration_date import generate_registration_date
# Импортируем функцию генерации email.
from procedural_version.generators.email import generate_email
# Импортируем функцию генерации пароля.
from procedural_version.generators.password import generate_password
# Импортируем функцию генерации тегов.
from procedural_version.generators.tags import generate_tags
# Импортируем функцию генерации username.
from procedural_version.generators.username import generate_username
# Импортируем функцию генерации user_id.
from procedural_version.generators.user_id import generate_user_id
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random
# Импортируем функцию выбора случайного элемента.
from procedural_version.utils.random_utils import choose_item

# Объявляем функцию, которая генерирует словарь профиля пользователя.
def generate_user_profile(valid=True, seed=None):
    # Что такое seed: это подсказка для random, чтобы случайный результат можно было повторить.
    # Например, если два раза вызвать функцию с seed=1, результат должен получиться одинаковым.
    # Входные данные - это значения в скобках функции.
    # Входные данные: valid - если True, email в профиле должен быть правильным; если False, email должен быть с ошибкой.
    # Входные данные: seed - значение для повторяемой генерации.
    # Переменные внутри функции можно называть по-своему.
    # Тесты проверяют результат функции, а не названия переменных.
    # Ниже перечислены примеры понятных названий переменных.
    # Внутренние переменные: randomizer - генератор случайности, который создается через create_random(seed).
    # Внутренние переменные: user_id - ID пользователя.
    # Внутренние переменные: first_name - имя пользователя.
    # Внутренние переменные: last_name - фамилия пользователя.
    # Внутренние переменные: age - возраст пользователя.
    # Внутренние переменные: city - город пользователя.
    # Внутренние переменные: is_active - признак активности пользователя.
    # Внутренние переменные: username - username пользователя.
    # Внутренние переменные: email - email пользователя.
    # Внутренние переменные: password - пароль пользователя.
    # Внутренние переменные: tags - список тегов пользователя.
    # Внутренние переменные: registration_date - дата регистрации пользователя.
    # Внутренние переменные: subscription_plan - план подписки пользователя, то есть вариант его аккаунта.
    # Выходные данные - это значение, которое функция отдает с помощью return.
    # Выходные данные: функция должна вернуть словарь с полным профилем пользователя.
    # Шаг 1. Создай randomizer через create_random(seed), чтобы профиль можно было повторить.
    # Шаг 2. Сгенерируй или выбери user_id, first_name, last_name, age и city.
    # Шаг 3. Сгенерируй is_active, username, email и password.
    # Шаг 4. Для email передай параметр valid, чтобы профиль мог быть валидным или невалидным.
    # Шаг 5. Сгенерируй tags, registration_date и subscription_plan.
    # Шаг 6. Собери все поля в один словарь с понятными ключами.
    # Шаг 7. Верни готовый словарь профиля пользователя.
    # Как проверить работу: запусти в терминале python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_user_profile_returns_rich_dictionary
    # Дополнительная проверка: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_user_profile_can_return_invalid_email
    # Если все правильно, в самом конце появится слово OK.
    # Если вместо OK появилась ошибка, проверь ключи словаря и email для valid=True или valid=False.
    pass
