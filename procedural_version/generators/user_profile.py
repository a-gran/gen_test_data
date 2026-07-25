# Файл нужен для функции user_profile.
# Функция user_profile должна собирать полный словарь с данными пользователя.
# В тестировании ПО такую функцию можно использовать, чтобы быстро собирать полный набор тестовых данных пользователя.

# Импортируем список имен.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем список городов.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем список планов подписки.
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Импортируем пример готовой функции даты регистрации.
from procedural_version.generators.reg_date_example import reg_date_example
# Импортируем функцию generate_email.
from procedural_version.generators.generate_email import generate_email
# Импортируем функцию пароля.
from procedural_version.generators.password import password
# Импортируем функцию тегов.
from procedural_version.generators.tags import tags
# Импортируем функцию username.
from procedural_version.generators.username import username
# Импортируем функцию ID.
from procedural_version.generators.user_id import user_id
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random
# Импортируем помощник для выбора случайного элемента.
from procedural_version.utils.random_utils import choose_item

# Объявляем функцию, которая должна вернуть полный профиль пользователя.
def user_profile(valid=True, seed=None):
    # Что делает функция: собирает один большой словарь с данными пользователя.
    # valid=True значит email внутри профиля должен быть правильным и содержать @.
    # valid=False значит email внутри профиля должен быть специально неправильным.
    # seed - число для random: с одним и тем же seed random собирает один и тот же профиль.
    # В словаре должны быть ключи: user_id, first_name, last_name, age, city, is_active.
    # В словаре также должны быть ключи: username, email, password, tags, registration_date, subscription_plan.
    # user_id должен быть строкой длиной 6.
    # username должен быть строкой длиной 10.
    # password должен быть строкой длиной 12.
    # tags должен быть списком из 3 уникальных тегов.
    # subscription_plan - это план подписки, например "free" или "premium".
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.user_profile import user_profile
    # from procedural_version.generators.age import age
    #
    # user_profile_result = user_profile(valid=False, seed=1)
    # print(user_profile_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = user_profile()
    # Вызов неправильного email: result = user_profile(valid=False)
    # Вызов с seed: result = user_profile(seed=1)
    # Пример результата: профиль должен быть словарем с данными пользователя.
    # Документация: docs/function_specifications.md, раздел user_profile.
    # Шаги реализации:
    # 1. Создать random через create_random(seed).
    # 2. Сгенерировать user_id длиной 6.
    # 3. Выбрать first_name, last_name, age, city и is_active.
    # 4. Сгенерировать username длиной 10.
    # 5. Сгенерировать email с учетом параметра valid.
    # 6. Сгенерировать password длиной 12.
    # 7. Сгенерировать 3 уникальных тега.
    # 8. Сгенерировать дату регистрации.
    # 9. Выбрать subscription_plan из SUBSCRIPTION_PLANS.
    # 10. Собрать все значения в один словарь и вернуть его.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py user_profile
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: словарь dict.
    # Тесты: test_user_profile_fields, test_user_profile_invalid_email.
    pass
