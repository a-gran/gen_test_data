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
    # Шаг 1. Создай randomizer через create_random(seed), чтобы профиль можно было повторить.
    # Шаг 2. Сгенерируй или выбери user_id, first_name, last_name, age и city.
    # Шаг 3. Сгенерируй is_active, username, email и password.
    # Шаг 4. Для email передай параметр valid, чтобы профиль мог быть валидным или невалидным.
    # Шаг 5. Сгенерируй tags, registration_date и subscription_plan.
    # Шаг 6. Собери все поля в один словарь с понятными ключами.
    # Шаг 7. Верни готовый словарь профиля пользователя.
    pass
