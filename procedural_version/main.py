# Импортируем функцию генерации полного имени.
from procedural_version.generators.full_name import generate_full_name
# Импортируем функцию генерации цифрового ID пользователя.
from procedural_version.generators.user_id import generate_user_id
# Импортируем функцию генерации возраста пользователя.
from procedural_version.generators.age import generate_age
# Импортируем функцию генерации года рождения пользователя.
from procedural_version.generators.birth_year import generate_birth_year
# Импортируем функцию генерации длинного комментария.
from procedural_version.generators.comment import generate_comment
# Импортируем функцию генерации адреса электронной почты.
from procedural_version.generators.email import generate_email
# Импортируем функцию генерации номера телефона.
from procedural_version.generators.phone import generate_phone
# Импортируем функцию генерации учебного пароля.
from procedural_version.generators.password import generate_password
# Импортируем функцию генерации города.
from procedural_version.generators.city import generate_city
# Импортируем пример готовой функции генерации даты регистрации пользователя.
from procedural_version.generators.registration_date_example import generate_registration_date_example
# Импортируем пример готовой функции генерации учебного балла.
from procedural_version.generators.score_example import generate_score_example
# Импортируем пример готовой функции генерации признака активности.
from procedural_version.generators.is_active_example import generate_is_active_example
# Импортируем пример готовой функции генерации плана подписки пользователя.
from procedural_version.generators.subscription_plan_example import generate_subscription_plan_example
# Импортируем функцию генерации списка тегов.
from procedural_version.generators.tags import generate_tags
# Импортируем функцию генерации username пользователя.
from procedural_version.generators.username import generate_username
# Импортируем функцию генерации профиля пользователя.
from procedural_version.generators.user_profile import generate_user_profile

# Проверяем, что файл запущен напрямую, а не импортирован как модуль.
if __name__ == "__main__":
    # Печатаем пример цифрового ID пользователя.
    print(generate_user_id(seed=1))
    # Печатаем пример возраста пользователя.
    print(generate_age(seed=1))
    # Печатаем пример года рождения пользователя.
    print(generate_birth_year(seed=1))
    # Печатаем пример длинного комментария.
    print(generate_comment(seed=1))
    # Печатаем пример адреса электронной почты.
    print(generate_email(seed=1))
    # Печатаем пример номера телефона.
    print(generate_phone(seed=1))
    # Печатаем пример учебного пароля.
    print(generate_password(seed=1))
    # Печатаем пример города.
    print(generate_city(seed=1))
    # Печатаем пример даты регистрации пользователя.
    print(generate_registration_date_example(seed=1))
    # Печатаем пример учебного балла.
    print(generate_score_example(seed=1))
    # Печатаем пример признака активности.
    print(generate_is_active_example(seed=1))
    # Печатаем пример плана подписки пользователя.
    print(generate_subscription_plan_example(seed=1))
    # Печатаем пример списка тегов.
    print(generate_tags(seed=1))
    # Печатаем пример username пользователя.
    print(generate_username(seed=1))
    # Печатаем пример профиля пользователя.
    print(generate_user_profile(seed=1))
    # Печатаем пример полного имени.
    print(generate_full_name(seed=1))
