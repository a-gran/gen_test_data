# Файл нужен для функции user_profile.
# Функция user_profile должна собирать полный профиль пользователя в виде красивого текста.
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
    # Что делает функция: собирает данные пользователя и возвращает их текстом в столбик.
    # valid=True значит email внутри профиля должен быть правильным и содержать @.
    # valid=False значит email внутри профиля должен быть специально неправильным.
    # seed - число для random: с одним и тем же seed random собирает один и тот же профиль.
    # В тексте должны быть строки: user_id, first_name, last_name, age, city, is_active.
    # В тексте также должны быть строки: username, email, password, tags, registration_date, subscription_plan.
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
    # Пример результата: профиль должен быть текстом, где каждая строка имеет вид ключ: значение.
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
    # 10. Собрать все значения в красивый многострочный текст и вернуть его.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py user_profile
    # Или на Windows: py check.py user_profile
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: многострочную строку str.
    # Тесты: test_user_profile_fields, test_user_profile_invalid_email.
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Создаем отдельный seed для ID пользователя.
    user_id_seed = randomizer.randint(0, 1000000000)
    # Создаем отдельный seed для username.
    username_seed = randomizer.randint(0, 1000000000)
    # Создаем отдельный seed для email.
    email_seed = randomizer.randint(0, 1000000000)
    # Создаем отдельный seed для пароля.
    password_seed = randomizer.randint(0, 1000000000)
    # Создаем отдельный seed для тегов.
    tags_seed = randomizer.randint(0, 1000000000)
    # Создаем отдельный seed для даты регистрации.
    registration_date_seed = randomizer.randint(0, 1000000000)
    # Генерируем ID пользователя длиной 6.
    profile_user_id = user_id(length=6, only_digits=True, seed=user_id_seed)
    # Выбираем имя из учебного списка.
    profile_first_name = choose_item(FIRST_NAMES, randomizer=randomizer)
    # Выбираем фамилию из учебного списка.
    profile_last_name = choose_item(LAST_NAMES, randomizer=randomizer)
    # Выбираем возраст пользователя.
    profile_age = randomizer.randint(18, 80)
    # Выбираем город из учебного списка.
    profile_city = choose_item(CITY_NAMES, randomizer=randomizer)
    # Выбираем признак активности.
    profile_is_active = randomizer.choice([True, False])
    # Генерируем username длиной 10.
    profile_username = username(length=10, seed=username_seed)
    # Генерируем email с учетом параметра valid.
    profile_email = generate_email(valid=valid, username_length=8, seed=email_seed)
    # Генерируем пароль длиной 12.
    profile_password = password(length=12, seed=password_seed)
    # Генерируем 3 уникальных тега.
    profile_tags = tags(count=3, unique=True, seed=tags_seed)
    # Генерируем дату регистрации.
    profile_registration_date = reg_date_example(seed=registration_date_seed)
    # Выбираем план подписки из учебного списка.
    profile_subscription_plan = choose_item(SUBSCRIPTION_PLANS, randomizer=randomizer)
    # Собираем строки профиля пользователя в понятном порядке.
    profile_lines = [
        # Записываем ID пользователя.
        f"user_id: {profile_user_id}",
        # Записываем имя пользователя.
        f"first_name: {profile_first_name}",
        # Записываем фамилию пользователя.
        f"last_name: {profile_last_name}",
        # Записываем возраст пользователя.
        f"age: {profile_age}",
        # Записываем город пользователя.
        f"city: {profile_city}",
        # Записываем признак активности пользователя.
        f"is_active: {profile_is_active}",
        # Записываем username пользователя.
        f"username: {profile_username}",
        # Записываем email пользователя.
        f"email: {profile_email}",
        # Записываем пароль пользователя.
        f"password: {profile_password}",
        # Записываем теги пользователя через запятую.
        f"tags: {', '.join(profile_tags)}",
        # Записываем дату регистрации пользователя.
        f"registration_date: {profile_registration_date}",
        # Записываем план подписки пользователя.
        f"subscription_plan: {profile_subscription_plan}",
    ]
    # Склеиваем строки через перенос строки.
    profile_text = "\n".join(profile_lines)
    # Возвращаем готовый профиль пользователя красивым текстом.
    return profile_text
