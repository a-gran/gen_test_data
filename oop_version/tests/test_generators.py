# Импортируем модуль unittest, чтобы писать автоматические тесты.
import unittest
# Импортируем генератор данных человека.
from oop_version.generators.person_generator import PersonGenerator
# Импортируем генератор контактных данных.
from oop_version.generators.contact_generator import ContactGenerator
# Импортируем генератор текстовых данных.
from oop_version.generators.text_generator import TextGenerator
# Импортируем генератор профиля пользователя.
from oop_version.generators.profile_generator import ProfileGenerator
# Импортируем процедурную функцию генерации возраста для сравнения.
from procedural_version.generators.age import generate_age
# Импортируем процедурную функцию генерации года рождения для сравнения.
from procedural_version.generators.birth_year import generate_birth_year
# Импортируем процедурную функцию генерации города для сравнения.
from procedural_version.generators.city import generate_city
# Импортируем процедурную функцию генерации комментария для сравнения.
from procedural_version.generators.comment import generate_comment
# Импортируем процедурную функцию генерации email для сравнения.
from procedural_version.generators.email import generate_email
# Импортируем процедурную функцию генерации имени для сравнения.
from procedural_version.generators.first_name import generate_first_name
# Импортируем процедурную функцию генерации полного имени для сравнения.
from procedural_version.generators.full_name import generate_full_name
# Импортируем процедурную функцию генерации активности для сравнения.
from procedural_version.generators.is_active import generate_is_active
# Импортируем процедурную функцию генерации фамилии для сравнения.
from procedural_version.generators.last_name import generate_last_name
# Импортируем процедурную функцию генерации пароля для сравнения.
from procedural_version.generators.password import generate_password
# Импортируем процедурную функцию генерации телефона для сравнения.
from procedural_version.generators.phone import generate_phone
# Импортируем процедурную функцию генерации даты регистрации для сравнения.
from procedural_version.generators.registration_date import generate_registration_date
# Импортируем процедурную функцию генерации балла для сравнения.
from procedural_version.generators.score import generate_score
# Импортируем процедурную функцию генерации тарифа для сравнения.
from procedural_version.generators.subscription_plan import generate_subscription_plan
# Импортируем процедурную функцию генерации тегов для сравнения.
from procedural_version.generators.tags import generate_tags
# Импортируем процедурную функцию генерации ID для сравнения.
from procedural_version.generators.user_id import generate_user_id
# Импортируем процедурную функцию генерации профиля для сравнения.
from procedural_version.generators.user_profile import generate_user_profile
# Импортируем процедурную функцию генерации username для сравнения.
from procedural_version.generators.username import generate_username

# Объявляем класс с тестами ООП-версии.
class OopGeneratorsTest(unittest.TestCase):
    # Объявляем тест ID пользователя.
    def test_generate_user_id_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_user_id(length=8), generate_user_id(length=8, seed=1))

    # Объявляем тест имени.
    def test_generate_first_name_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_first_name(min_length=5), generate_first_name(min_length=5, seed=1))

    # Объявляем тест фамилии.
    def test_generate_last_name_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_last_name(max_length=7), generate_last_name(max_length=7, seed=1))

    # Объявляем тест полного имени.
    def test_generate_full_name_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_full_name(max_total_length=10), generate_full_name(max_total_length=10, seed=1))

    # Объявляем тест возраста.
    def test_generate_age_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии на верхней границе.
        self.assertEqual(generator.generate_age(boundary="max"), generate_age(boundary="max", seed=1))

    # Объявляем тест года рождения.
    def test_generate_birth_year_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии на нижней границе.
        self.assertEqual(generator.generate_birth_year(boundary="min"), generate_birth_year(boundary="min", seed=1))

    # Объявляем тест города.
    def test_generate_city_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии с фильтром.
        self.assertEqual(generator.generate_city(starts_with="М"), generate_city(starts_with="М", seed=1))

    # Объявляем тест учебного балла.
    def test_generate_score_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии на нижней границе.
        self.assertEqual(generator.generate_score(boundary="min"), generate_score(boundary="min", seed=1))

    # Объявляем тест активности.
    def test_generate_is_active_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_is_active(), generate_is_active(seed=1))

    # Объявляем тест username.
    def test_generate_username_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_username(length=12), generate_username(length=12, seed=1))

    # Объявляем тест email.
    def test_generate_email_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ContactGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_email(valid=True, username_length=8), generate_email(valid=True, username_length=8, seed=1))

    # Объявляем тест телефона.
    def test_generate_phone_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ContactGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_phone(valid=False), generate_phone(valid=False, seed=1))

    # Объявляем тест комментария.
    def test_generate_comment_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = TextGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_comment(length=255), generate_comment(length=255, seed=1))

    # Объявляем тест пароля.
    def test_generate_password_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = TextGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_password(length=16), generate_password(length=16, seed=1))

    # Объявляем тест тегов.
    def test_generate_tags_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = TextGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_tags(count=5, unique=True), generate_tags(count=5, unique=True, seed=1))

    # Объявляем тест даты регистрации.
    def test_generate_registration_date_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ProfileGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_registration_date(boundary="max"), generate_registration_date(boundary="max", seed=1))

    # Объявляем тест тарифа.
    def test_generate_subscription_plan_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ProfileGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_subscription_plan(allowed_plans=["free", "premium"]), generate_subscription_plan(allowed_plans=["free", "premium"], seed=1))

    # Объявляем тест профиля пользователя.
    def test_generate_user_profile_matches_procedural_version(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ProfileGenerator(seed=1)
        # Проверяем совпадение ООП и процедурной версии.
        self.assertEqual(generator.generate_user_profile(valid=False), generate_user_profile(valid=False, seed=1))

# Проверяем, что файл тестов запущен напрямую.
if __name__ == "__main__":
    # Запускаем тесты из этого файла.
    unittest.main()
