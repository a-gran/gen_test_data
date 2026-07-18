# Импортируем список имен для генерации случайного имени.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий для генерации случайной фамилии.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем список городов для генерации случайного города.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем список тарифов для генерации тарифа пользователя.
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
    # Создаем один генератор случайности для всех полей профиля.
    randomizer = create_random(seed)
    # Возвращаем профиль пользователя в виде словаря.
    return {
        # Добавляем цифровой ID пользователя.
        "user_id": generate_user_id(length=6, seed=seed),
        # Добавляем случайное имя пользователя.
        "first_name": choose_item(FIRST_NAMES, randomizer=randomizer),
        # Добавляем случайную фамилию пользователя.
        "last_name": choose_item(LAST_NAMES, randomizer=randomizer),
        # Добавляем случайный возраст пользователя.
        "age": randomizer.randint(18, 80),
        # Добавляем случайный город пользователя.
        "city": choose_item(CITY_NAMES, randomizer=randomizer),
        # Добавляем случайный признак активности пользователя.
        "is_active": randomizer.choice([True, False]),
        # Добавляем username пользователя заданной длины.
        "username": generate_username(length=10, seed=seed),
        # Добавляем email, который может быть валидным или невалидным.
        "email": generate_email(valid=valid, username_length=8, seed=seed),
        # Добавляем учебный пароль заданной длины.
        "password": generate_password(length=12, seed=seed),
        # Добавляем список из трех уникальных тегов.
        "tags": generate_tags(count=3, unique=True, seed=seed),
        # Добавляем случайную дату регистрации пользователя.
        "registration_date": generate_registration_date(seed=seed),
        # Добавляем случайный тариф пользователя.
        "subscription_plan": choose_item(SUBSCRIPTION_PLANS, randomizer=randomizer),
    }
