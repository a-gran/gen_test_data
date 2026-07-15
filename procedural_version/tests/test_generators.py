# Импортируем модуль unittest, чтобы писать автоматические тесты.
import unittest
# Импортируем список имен для простой проверки.
from procedural_version.data.names_data import FIRST_NAMES
# Импортируем список фамилий для простой проверки.
from procedural_version.data.names_data import LAST_NAMES
# Импортируем список городов для простой проверки.
from procedural_version.data.names_data import CITY_NAMES
# Импортируем список тегов для простой проверки.
from procedural_version.data.names_data import TAGS
# Импортируем функцию генерации возраста.
from procedural_version.generators.age import generate_age
# Импортируем функцию генерации года рождения.
from procedural_version.generators.birth_year import generate_birth_year
# Импортируем функцию генерации города.
from procedural_version.generators.city import generate_city
# Импортируем функцию генерации комментария.
from procedural_version.generators.comment import generate_comment
# Импортируем функцию генерации email.
from procedural_version.generators.email import generate_email
# Импортируем функцию генерации имени.
from procedural_version.generators.first_name import generate_first_name
# Импортируем функцию генерации полного имени.
from procedural_version.generators.full_name import generate_full_name
# Импортируем функцию генерации активности.
from procedural_version.generators.is_active import generate_is_active
# Импортируем функцию генерации фамилии.
from procedural_version.generators.last_name import generate_last_name
# Импортируем функцию генерации пароля.
from procedural_version.generators.password import generate_password
# Импортируем функцию генерации телефона.
from procedural_version.generators.phone import generate_phone
# Импортируем функцию генерации даты регистрации.
from procedural_version.generators.registration_date import generate_registration_date
# Импортируем функцию генерации балла.
from procedural_version.generators.score import generate_score
# Импортируем функцию генерации тарифа.
from procedural_version.generators.subscription_plan import generate_subscription_plan
# Импортируем функцию генерации тегов.
from procedural_version.generators.tags import generate_tags
# Импортируем функцию генерации ID.
from procedural_version.generators.user_id import generate_user_id
# Импортируем функцию генерации профиля.
from procedural_version.generators.user_profile import generate_user_profile
# Импортируем функцию генерации username.
from procedural_version.generators.username import generate_username

# Объявляем класс с тестами процедурной версии.
class ProceduralGeneratorsTest(unittest.TestCase):
    # Объявляем тест ID заданной длины.
    def test_generate_user_id_returns_digits_with_exact_length(self):
        # Генерируем ID длиной 8 символов.
        user_id = generate_user_id(length=8, seed=1)
        # Проверяем, что ID является строкой.
        self.assertIsInstance(user_id, str)
        # Проверяем, что ID имеет ровно 8 символов.
        self.assertEqual(len(user_id), 8)
        # Проверяем, что ID состоит только из цифр.
        self.assertTrue(user_id.isdigit())

    # Объявляем тест ID с буквами и цифрами.
    def test_generate_user_id_can_return_letters_and_digits(self):
        # Генерируем буквенно-цифровой ID.
        user_id = generate_user_id(length=10, only_digits=False, seed=1)
        # Проверяем, что ID имеет ровно 10 символов.
        self.assertEqual(len(user_id), 10)
        # Проверяем, что ID состоит из букв и цифр.
        self.assertTrue(user_id.isalnum())

    # Объявляем тест имени с ограничением длины.
    def test_generate_first_name_respects_length_filter(self):
        # Генерируем имя не короче 5 символов.
        first_name = generate_first_name(min_length=5, seed=1)
        # Проверяем, что имя взято из учебного списка.
        self.assertIn(first_name, FIRST_NAMES)
        # Проверяем, что имя не короче 5 символов.
        self.assertGreaterEqual(len(first_name), 5)

    # Объявляем тест фамилии с ограничением длины.
    def test_generate_last_name_respects_length_filter(self):
        # Генерируем фамилию не длиннее 7 символов.
        last_name = generate_last_name(max_length=7, seed=1)
        # Проверяем, что фамилия взята из учебного списка.
        self.assertIn(last_name, LAST_NAMES)
        # Проверяем, что фамилия не длиннее 7 символов.
        self.assertLessEqual(len(last_name), 7)

    # Объявляем тест полного имени с максимальной длиной.
    def test_generate_full_name_respects_max_total_length(self):
        # Генерируем полное имя с ограничением общей длины.
        full_name = generate_full_name(max_total_length=10, seed=1)
        # Проверяем, что полное имя не длиннее 10 символов.
        self.assertLessEqual(len(full_name), 10)

    # Объявляем тест возраста на границах.
    def test_generate_age_returns_boundary_values(self):
        # Проверяем нижнюю границу возраста.
        self.assertEqual(generate_age(min_age=18, max_age=80, boundary="min"), 18)
        # Проверяем верхнюю границу возраста.
        self.assertEqual(generate_age(min_age=18, max_age=80, boundary="max"), 80)
        # Проверяем значение ниже нижней границы.
        self.assertEqual(generate_age(min_age=18, max_age=80, boundary="below_min"), 17)
        # Проверяем значение выше верхней границы.
        self.assertEqual(generate_age(min_age=18, max_age=80, boundary="above_max"), 81)

    # Объявляем тест года рождения на границах.
    def test_generate_birth_year_returns_boundary_values(self):
        # Проверяем нижнюю границу года рождения.
        self.assertEqual(generate_birth_year(min_year=1950, max_year=2008, boundary="min"), 1950)
        # Проверяем верхнюю границу года рождения.
        self.assertEqual(generate_birth_year(min_year=1950, max_year=2008, boundary="max"), 2008)

    # Объявляем тест города с фильтром по началу строки.
    def test_generate_city_respects_starts_with_filter(self):
        # Генерируем город, который начинается с буквы М.
        city = generate_city(starts_with="М", seed=1)
        # Проверяем, что город взят из учебного списка.
        self.assertIn(city, CITY_NAMES)
        # Проверяем, что город начинается с нужной буквы.
        self.assertTrue(city.startswith("М"))

    # Объявляем тест комментария точной длины.
    def test_generate_comment_returns_exact_length(self):
        # Генерируем комментарий длиной 255 символов.
        comment = generate_comment(length=255, seed=1)
        # Проверяем, что комментарий является строкой.
        self.assertIsInstance(comment, str)
        # Проверяем, что длина комментария ровно 255 символов.
        self.assertEqual(len(comment), 255)

    # Объявляем тест комментариев разной длины.
    def test_generate_comment_returns_any_requested_length(self):
        # Проверяем комментарий нулевой длины.
        self.assertEqual(len(generate_comment(length=0, seed=1)), 0)
        # Проверяем комментарий длиной 1 символ.
        self.assertEqual(len(generate_comment(length=1, seed=1)), 1)
        # Проверяем комментарий большой длины.
        self.assertEqual(len(generate_comment(length=1000, seed=1)), 1000)

    # Объявляем тест email в валидном и невалидном режиме.
    def test_generate_email_can_return_valid_and_invalid_values(self):
        # Генерируем валидный email.
        valid_email = generate_email(valid=True, username_length=8, seed=1)
        # Генерируем невалидный email.
        invalid_email = generate_email(valid=False, username_length=8, seed=1)
        # Проверяем, что в валидном email есть знак собаки.
        self.assertIn("@", valid_email)
        # Проверяем, что в невалидном email нет знака собаки.
        self.assertNotIn("@", invalid_email)
        # Проверяем, что часть до знака собаки имеет нужную длину.
        self.assertEqual(len(valid_email.split("@")[0]), 8)

    # Объявляем тест username точной длины.
    def test_generate_username_returns_exact_length(self):
        # Генерируем username длиной 12 символов.
        username = generate_username(length=12, seed=1)
        # Проверяем, что username имеет ровно 12 символов.
        self.assertEqual(len(username), 12)

    # Объявляем тест пароля с цифрами и спецсимволами.
    def test_generate_password_respects_required_parts(self):
        # Генерируем пароль длиной 16 символов.
        password = generate_password(length=16, use_digits=True, use_symbols=True, seed=1)
        # Проверяем, что пароль имеет ровно 16 символов.
        self.assertEqual(len(password), 16)
        # Проверяем, что в пароле есть хотя бы одна цифра.
        self.assertTrue(any(symbol.isdigit() for symbol in password))
        # Проверяем, что в пароле есть хотя бы один спецсимвол.
        self.assertTrue(any(symbol in "!@#$%^&*" for symbol in password))

    # Объявляем тест телефона в валидном и невалидном режиме.
    def test_generate_phone_can_return_valid_and_invalid_values(self):
        # Генерируем валидный телефон.
        valid_phone = generate_phone(valid=True, seed=1)
        # Генерируем невалидный телефон.
        invalid_phone = generate_phone(valid=False, seed=1)
        # Проверяем правильный код страны валидного телефона.
        self.assertEqual(valid_phone["country_code"], "+7")
        # Проверяем неправильный код страны невалидного телефона.
        self.assertNotEqual(invalid_phone["country_code"], "+7")
        # Проверяем длину основной части валидного телефона.
        self.assertGreaterEqual(valid_phone["number"], 1000000)
        # Проверяем короткую основную часть невалидного телефона.
        self.assertLess(invalid_phone["number"], 1000000)

    # Объявляем тест даты регистрации на границах.
    def test_generate_registration_date_returns_boundary_values(self):
        # Проверяем нижнюю границу даты.
        self.assertEqual(generate_registration_date(start_year=2020, end_year=2026, boundary="min"), "2020-01-01")
        # Проверяем верхнюю границу даты.
        self.assertEqual(generate_registration_date(start_year=2020, end_year=2026, boundary="max"), "2026-12-28")

    # Объявляем тест учебного балла на границах.
    def test_generate_score_returns_boundary_values(self):
        # Проверяем нижнюю границу балла.
        self.assertEqual(generate_score(min_score=1, max_score=100, boundary="min"), 1)
        # Проверяем верхнюю границу балла.
        self.assertEqual(generate_score(min_score=1, max_score=100, boundary="max"), 100)

    # Объявляем тест признака активности.
    def test_generate_is_active_returns_boolean(self):
        # Генерируем признак активности.
        is_active = generate_is_active(seed=1)
        # Проверяем, что результат является булевым значением.
        self.assertIsInstance(is_active, bool)

    # Объявляем тест тегов с точным количеством и уникальностью.
    def test_generate_tags_respects_count_and_unique(self):
        # Генерируем 5 уникальных тегов.
        tags = generate_tags(count=5, unique=True, seed=1)
        # Проверяем, что тегов ровно 5.
        self.assertEqual(len(tags), 5)
        # Проверяем, что все теги уникальны.
        self.assertEqual(len(tags), len(set(tags)))
        # Проверяем каждый тег из списка.
        for tag in tags:
            # Проверяем, что тег взят из учебного списка.
            self.assertIn(tag, TAGS)

    # Объявляем тест тарифа из разрешенного списка.
    def test_generate_subscription_plan_respects_allowed_plans(self):
        # Генерируем тариф только из двух разрешенных вариантов.
        plan = generate_subscription_plan(allowed_plans=["free", "premium"], seed=1)
        # Проверяем, что тариф входит в разрешенный список.
        self.assertIn(plan, ["free", "premium"])

    # Объявляем тест профиля пользователя.
    def test_generate_user_profile_returns_rich_dictionary(self):
        # Генерируем валидный профиль.
        profile = generate_user_profile(valid=True, seed=1)
        # Проверяем, что профиль является словарем.
        self.assertIsInstance(profile, dict)
        # Проверяем, что ID имеет длину 6 символов.
        self.assertEqual(len(profile["user_id"]), 6)
        # Проверяем, что email валидного профиля содержит знак собаки.
        self.assertIn("@", profile["email"])
        # Проверяем, что пароль имеет длину 12 символов.
        self.assertEqual(len(profile["password"]), 12)
        # Проверяем, что в профиле ровно 3 тега.
        self.assertEqual(len(profile["tags"]), 3)

    # Объявляем тест невалидного профиля пользователя.
    def test_generate_user_profile_can_return_invalid_email(self):
        # Генерируем профиль с невалидным email.
        profile = generate_user_profile(valid=False, seed=1)
        # Проверяем, что email намеренно не содержит знак собаки.
        self.assertNotIn("@", profile["email"])

# Проверяем, что файл тестов запущен напрямую.
if __name__ == "__main__":
    # Запускаем тесты из этого файла.
    unittest.main()
