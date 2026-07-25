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
    print(person_generator.user_id())
    # Печатаем пример возраста пользователя.
    print(person_generator.age())
    # Печатаем пример года рождения пользователя.
    print(person_generator.birth_year())
    # Печатаем пример длинного комментария.
    print(text_generator.comment())
    # Печатаем пример адреса электронной почты.
    print(contact_generator.email())
    # Печатаем пример номера телефона.
    print(contact_generator.phone())
    # Печатаем пример учебного пароля.
    print(text_generator.password())
    # Печатаем пример города.
    print(person_generator.city())
    # Печатаем пример даты регистрации пользователя.
    print(profile_generator.reg_date())
    # Печатаем пример учебного балла.
    print(person_generator.score())
    # Печатаем пример признака активности.
    print(person_generator.active())
    # Печатаем пример плана подписки пользователя.
    print(profile_generator.plan())
    # Печатаем пример списка тегов.
    print(text_generator.tags())
    # Печатаем пример username пользователя.
    print(person_generator.username())
    # Печатаем пример профиля пользователя.
    print(profile_generator.user_profile())
    # Печатаем пример полного имени.
    print(person_generator.full_name())

# Сохраняем простую строку для учебного примера работы с переменной.
letter = 'Привет мир'
