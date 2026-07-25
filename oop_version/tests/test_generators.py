# Импортируем модуль unittest, чтобы писать автоматические тесты.
import unittest
# Импортируем источник учебных списков для проверок ООП-результатов.
from oop_version.data.data_provider import DataProvider
# Импортируем генератор контактных данных.
from oop_version.generators.contact_generator import ContactGenerator
# Импортируем генератор данных человека.
from oop_version.generators.person_generator import PersonGenerator
# Импортируем генератор профиля пользователя.
from oop_version.generators.profile_generator import ProfileGenerator
# Импортируем генератор текстовых данных.
from oop_version.generators.text_generator import TextGenerator

# Объявляем класс с тестами ООП-версии.
class OopGeneratorsTest(unittest.TestCase):
    # Объявляем тест ID пользователя.
    def test_id_digits(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Генерируем ID длиной 8 символов.
        user_id = generator.user_id(length=8)
        # Проверяем, что ID является строкой.
        self.assertIsInstance(user_id, str)
        # Проверяем, что ID имеет ровно 8 символов.
        self.assertEqual(len(user_id), 8)
        # Проверяем, что ID состоит только из цифр.
        self.assertTrue(user_id.isdigit())

    # Объявляем тест ID с буквами и цифрами.
    def test_id_alnum(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Генерируем ID из букв и цифр.
        user_id = generator.user_id(length=10, only_digits=False)
        # Проверяем, что ID имеет ровно 10 символов.
        self.assertEqual(len(user_id), 10)
        # Проверяем, что ID состоит только из букв и цифр.
        self.assertTrue(user_id.isalnum())

    # Объявляем тест имени с фильтром длины.
    def test_first_name_len(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Генерируем имя длиной 5 символов или больше.
        first_name = generator.first_name(min_length=5)
        # Проверяем, что имя взято из учебного списка.
        self.assertIn(first_name, DataProvider.first_names)
        # Проверяем, что имя не короче 5 символов.
        self.assertGreaterEqual(len(first_name), 5)

    # Объявляем тест фамилии с фильтром длины.
    def test_last_name_len(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Генерируем фамилию длиной 7 символов или меньше.
        last_name = generator.last_name(max_length=7)
        # Проверяем, что фамилия взята из учебного списка.
        self.assertIn(last_name, DataProvider.last_names)
        # Проверяем, что фамилия не длиннее 7 символов.
        self.assertLessEqual(len(last_name), 7)

    # Объявляем тест полного имени.
    def test_full_name_basic(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Генерируем полное имя.
        full_name = generator.full_name()
        # Проверяем, что в полном имени есть пробел между именем и фамилией.
        self.assertIn(" ", full_name)
        # Проверяем, что результат является строкой.
        self.assertIsInstance(full_name, str)

    # Объявляем тест возраста на специальных значениях.
    def test_age_bounds(self):
        # Создаем ООП-генератор.
        generator = PersonGenerator(seed=1)
        # Проверяем, что boundary="min" возвращает минимальный возраст.
        self.assertEqual(generator.age(min_age=18, max_age=80, boundary="min"), 18)
        # Проверяем, что boundary="max" возвращает максимальный возраст.
        self.assertEqual(generator.age(min_age=18, max_age=80, boundary="max"), 80)
        # Проверяем, что boundary="below_min" возвращает возраст ниже минимума.
        self.assertEqual(generator.age(min_age=18, max_age=80, boundary="below_min"), 17)
        # Проверяем, что boundary="above_max" возвращает возраст выше максимума.
        self.assertEqual(generator.age(min_age=18, max_age=80, boundary="above_max"), 81)

    # Объявляем тест года рождения на специальных значениях.
    def test_birth_year_bounds(self):
        # Создаем ООП-генератор.
        generator = PersonGenerator(seed=1)
        # Проверяем, что boundary="min" возвращает минимальный год.
        self.assertEqual(generator.birth_year(min_year=1950, max_year=2008, boundary="min"), 1950)
        # Проверяем, что boundary="max" возвращает максимальный год.
        self.assertEqual(generator.birth_year(min_year=1950, max_year=2008, boundary="max"), 2008)
        # Проверяем, что boundary="below_min" возвращает год ниже минимума.
        self.assertEqual(generator.birth_year(min_year=1950, max_year=2008, boundary="below_min"), 1949)
        # Проверяем, что boundary="above_max" возвращает год выше максимума.
        self.assertEqual(generator.birth_year(min_year=1950, max_year=2008, boundary="above_max"), 2009)

    # Объявляем тест города с фильтром по первой букве.
    def test_city_prefix(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Генерируем город на букву М.
        city = generator.city(starts_with="М")
        # Проверяем, что город взят из учебного списка.
        self.assertIn(city, DataProvider.city_names)
        # Проверяем, что город начинается с буквы М.
        self.assertTrue(city.startswith("М"))

    # Объявляем тест учебного балла на специальных значениях.
    def test_score_bounds(self):
        # Создаем ООП-генератор.
        generator = PersonGenerator(seed=1)
        # Проверяем, что boundary="min" возвращает минимальный балл.
        self.assertEqual(generator.score(min_score=1, max_score=100, boundary="min"), 1)
        # Проверяем, что boundary="max" возвращает максимальный балл.
        self.assertEqual(generator.score(min_score=1, max_score=100, boundary="max"), 100)
        # Проверяем, что boundary="below_min" возвращает балл ниже минимума.
        self.assertEqual(generator.score(min_score=1, max_score=100, boundary="below_min"), 0)
        # Проверяем, что boundary="above_max" возвращает балл выше максимума.
        self.assertEqual(generator.score(min_score=1, max_score=100, boundary="above_max"), 101)

    # Объявляем тест активности.
    def test_active_bool(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Генерируем признак активности.
        is_active = generator.active()
        # Проверяем, что результат является True или False.
        self.assertIsInstance(is_active, bool)

    # Объявляем тест username точной длины.
    def test_username_len(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = PersonGenerator(seed=1)
        # Генерируем username длиной 12 символов.
        username = generator.username(length=12)
        # Проверяем, что username является строкой.
        self.assertIsInstance(username, str)
        # Проверяем, что username имеет ровно 12 символов.
        self.assertEqual(len(username), 12)

    # Объявляем тест email в валидном режиме.
    def test_email_valid(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ContactGenerator(seed=1)
        # Генерируем валидный email.
        email = generator.email(valid=True, username_length=8)
        # Проверяем, что email содержит знак @.
        self.assertIn("@", email)
        # Проверяем, что часть до знака @ имеет длину 8.
        self.assertEqual(len(email.split("@")[0]), 8)

    # Объявляем тест телефона в невалидном режиме.
    def test_phone_invalid(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ContactGenerator(seed=1)
        # Генерируем специально неправильный телефон.
        phone = generator.phone(valid=False)
        # Проверяем, что телефон является словарем.
        self.assertIsInstance(phone, dict)
        # Проверяем, что неправильный телефон не начинается с +7.
        self.assertNotEqual(phone["country_code"], "+7")
        # Проверяем, что неправильный номер короткий.
        self.assertLess(phone["number"], 1000000)

    # Объявляем тест комментария точной длины.
    def test_comment_len(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = TextGenerator(seed=1)
        # Генерируем комментарий длиной 255 символов.
        comment = generator.comment(length=255)
        # Проверяем, что комментарий является строкой.
        self.assertIsInstance(comment, str)
        # Проверяем, что длина комментария ровно 255 символов.
        self.assertEqual(len(comment), 255)

    # Объявляем тест пароля.
    def test_password_parts(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = TextGenerator(seed=1)
        # Генерируем пароль длиной 16 символов.
        password = generator.password(length=16)
        # Проверяем, что пароль имеет ровно 16 символов.
        self.assertEqual(len(password), 16)
        # Проверяем, что в пароле есть хотя бы одна цифра.
        self.assertTrue(any(symbol.isdigit() for symbol in password))
        # Проверяем, что в пароле есть хотя бы один спецсимвол.
        self.assertTrue(any(symbol in "!@#$%^&*" for symbol in password))

    # Объявляем тест тегов.
    def test_tags_unique(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = TextGenerator(seed=1)
        # Генерируем 5 уникальных тегов.
        tags = generator.tags(count=5, unique=True)
        # Проверяем, что тегов ровно 5.
        self.assertEqual(len(tags), 5)
        # Проверяем, что все теги разные.
        self.assertEqual(len(tags), len(set(tags)))
        # Проверяем каждый тег из списка.
        for tag in tags:
            # Проверяем, что тег взят из учебного списка.
            self.assertIn(tag, DataProvider.tags)

    # Объявляем тест даты регистрации.
    def test_reg_date_range(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ProfileGenerator(seed=1)
        # Генерируем обычную дату регистрации.
        registration_date = generator.reg_date(start_year=2020, end_year=2026)
        # Разделяем дату на год, месяц и день.
        year_text, month_text, day_text = registration_date.split("-")
        # Проверяем, что год не меньше 2020.
        self.assertGreaterEqual(int(year_text), 2020)
        # Проверяем, что год не больше 2026.
        self.assertLessEqual(int(year_text), 2026)
        # Проверяем, что месяц не меньше 1.
        self.assertGreaterEqual(int(month_text), 1)
        # Проверяем, что месяц не больше 12.
        self.assertLessEqual(int(month_text), 12)
        # Проверяем, что день не меньше 1.
        self.assertGreaterEqual(int(day_text), 1)
        # Проверяем, что день не больше 28.
        self.assertLessEqual(int(day_text), 28)

    # Объявляем тест плана подписки.
    def test_plan_allowed(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ProfileGenerator(seed=1)
        # Генерируем план подписки только из двух разрешенных вариантов.
        plan = generator.plan(allowed_plans=["free", "premium"])
        # Проверяем, что план входит в разрешенный список.
        self.assertIn(plan, ["free", "premium"])

    # Объявляем тест профиля пользователя.
    def test_user_profile_fields(self):
        # Создаем ООП-генератор с фиксированным seed.
        generator = ProfileGenerator(seed=1)
        # Генерируем профиль с невалидным email.
        profile = generator.user_profile(valid=False)
        # Проверяем, что профиль является словарем.
        self.assertIsInstance(profile, dict)
        # Проверяем, что в профиле есть ID.
        self.assertIn("user_id", profile)
        # Проверяем, что в профиле есть имя.
        self.assertIn("first_name", profile)
        # Проверяем, что в профиле есть фамилия.
        self.assertIn("last_name", profile)
        # Проверяем, что в профиле есть возраст.
        self.assertIn("age", profile)
        # Проверяем, что в профиле есть город.
        self.assertIn("city", profile)
        # Проверяем, что в профиле есть активность.
        self.assertIn("is_active", profile)
        # Проверяем, что в профиле есть username.
        self.assertIn("username", profile)
        # Проверяем, что в профиле есть email.
        self.assertIn("email", profile)
        # Проверяем, что в профиле есть пароль.
        self.assertIn("password", profile)
        # Проверяем, что в профиле есть теги.
        self.assertIn("tags", profile)
        # Проверяем, что в профиле есть дата регистрации.
        self.assertIn("registration_date", profile)
        # Проверяем, что в профиле есть план подписки.
        self.assertIn("subscription_plan", profile)
        # Проверяем, что email специально не содержит @.
        self.assertNotIn("@", profile["email"])
        # Проверяем, что password имеет длину 12 символов.
        self.assertEqual(len(profile["password"]), 12)

# Проверяем, что файл тестов запущен напрямую.
if __name__ == "__main__":
    # Запускаем тесты из этого файла.
    unittest.main()
