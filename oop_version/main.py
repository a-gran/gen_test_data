# Импортируем генератор данных человека.
from oop_version.generators.person_generator import PersonGenerator

# Импортируем генератор контактных данных.
from oop_version.generators.contact_generator import ContactGenerator

# Импортируем генератор текстовых данных.
from oop_version.generators.text_generator import TextGenerator

# Импортируем генератор профиля пользователя.
from oop_version.generators.profile_generator import ProfileGenerator

# Проверяем, что файл запущен напрямую, а не импортирован как модуль.
if __name__ == "__main__":
    # Создаем генератор данных человека.
    person_generator = PersonGenerator(seed=1)
    # Создаем генератор контактных данных.
    contact_generator = ContactGenerator(seed=1)
    # Создаем генератор текстовых данных.
    text_generator = TextGenerator(seed=1)
    # Создаем генератор профиля пользователя.
    profile_generator = ProfileGenerator(seed=1)
    # Печатаем пример цифрового ID пользователя.
    print(person_generator.generate_user_id())
    # Печатаем пример возраста пользователя.
    print(person_generator.generate_age())
    # Печатаем пример года рождения пользователя.
    print(person_generator.generate_birth_year())
    # Печатаем пример длинного комментария.
    print(text_generator.generate_comment())
    # Печатаем пример адреса электронной почты.
    print(contact_generator.generate_email())
    # Печатаем пример номера телефона.
    print(contact_generator.generate_phone())
    # Печатаем пример учебного пароля.
    print(text_generator.generate_password())
    # Печатаем пример города.
    print(person_generator.generate_city())
    # Печатаем пример даты регистрации пользователя.
    print(profile_generator.generate_registration_date())
    # Печатаем пример учебного балла.
    print(person_generator.generate_score())
    # Печатаем пример признака активности.
    print(person_generator.generate_is_active())
    # Печатаем пример тарифа пользователя.
    print(profile_generator.generate_subscription_plan())
    # Печатаем пример списка тегов.
    print(text_generator.generate_tags())
    # Печатаем пример username пользователя.
    print(person_generator.generate_username())
    # Печатаем пример профиля пользователя.
    print(profile_generator.generate_user_profile())
    # Печатаем пример полного имени.
    print(person_generator.generate_full_name())

# Сохраняем простую строку для учебного примера работы с переменной.
letter = 'Привет мир'
