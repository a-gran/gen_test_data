# Импортируем базовый генератор, чтобы использовать общую логику.
from oop_version.generators.base_generator import BaseGenerator
# Импортируем генератор контактных данных для сборки профиля.
from oop_version.generators.contact_generator import ContactGenerator
# Импортируем генератор данных человека для сборки профиля.
from oop_version.generators.person_generator import PersonGenerator
# Импортируем генератор текстовых данных для сборки профиля.
from oop_version.generators.text_generator import TextGenerator

# Объявляем класс для генерации профиля пользователя.
class ProfileGenerator(BaseGenerator):
    # Объявляем метод, который генерирует дату регистрации пользователя.
    def generate_registration_date(self, start_year=2020, end_year=2026, boundary=None):
        # Проверяем, что начальный год не больше конечного.
        if start_year > end_year:
            # Сообщаем понятную ошибку, если годы перепутаны местами.
            raise ValueError("start_year не должен быть больше end_year")
        # Проверяем, попросили ли вернуть дату на нижней границе.
        if boundary == "min":
            # Возвращаем первое января начального года.
            return f"{start_year:04d}-01-01"
        # Проверяем, попросили ли вернуть дату на верхней границе.
        if boundary == "max":
            # Возвращаем двадцать восьмое декабря конечного года.
            return f"{end_year:04d}-12-28"
        # Проверяем, попросили ли вернуть дату ниже допустимого диапазона.
        if boundary == "below_min":
            # Возвращаем дату за год до начального года.
            return f"{start_year - 1:04d}-12-31"
        # Проверяем, попросили ли вернуть дату выше допустимого диапазона.
        if boundary == "above_max":
            # Возвращаем дату через год после конечного года.
            return f"{end_year + 1:04d}-01-01"
        # Генерируем год регистрации.
        year = self.randomizer.randint(start_year, end_year)
        # Генерируем месяц регистрации.
        month = self.randomizer.randint(1, 12)
        # Генерируем день регистрации в безопасном диапазоне до 28.
        day = self.randomizer.randint(1, 28)
        # Возвращаем дату строкой в формате год-месяц-день.
        return f"{year:04d}-{month:02d}-{day:02d}"

    # Объявляем метод, который генерирует тариф пользователя.
    def generate_subscription_plan(self, allowed_plans=None):
        # Используем переданный список тарифов или общий учебный список.
        plans = allowed_plans if allowed_plans is not None else self.data_provider.subscription_plans
        # Проверяем, что список тарифов не пустой.
        if not plans:
            # Сообщаем понятную ошибку, если выбирать не из чего.
            raise ValueError("Список тарифов не должен быть пустым")
        # Возвращаем случайный тариф из выбранного списка тарифов.
        return self.randomizer.choice(plans)

    # Объявляем метод, который генерирует словарь профиля пользователя.
    def generate_user_profile(self, valid=True):
        # Создаем генератор данных человека для ID с тем же seed.
        id_generator = PersonGenerator(seed=self.seed)
        # Создаем генератор данных человека для username с тем же seed.
        username_generator = PersonGenerator(seed=self.seed)
        # Создаем генератор контактных данных с тем же seed для повторяемого результата.
        contact_generator = ContactGenerator(seed=self.seed)
        # Создаем генератор текстовых данных для пароля с тем же seed.
        password_generator = TextGenerator(seed=self.seed)
        # Создаем генератор текстовых данных для тегов с тем же seed.
        tags_generator = TextGenerator(seed=self.seed)
        # Создаем генератор профиля для даты с тем же seed.
        date_generator = ProfileGenerator(seed=self.seed)
        # Возвращаем профиль пользователя в виде словаря.
        return {
            # Добавляем цифровой ID пользователя.
            "user_id": id_generator.generate_user_id(length=6),
            # Добавляем случайное имя пользователя.
            "first_name": self.choose_item(self.data_provider.first_names),
            # Добавляем случайную фамилию пользователя.
            "last_name": self.choose_item(self.data_provider.last_names),
            # Добавляем случайный возраст пользователя.
            "age": self.randomizer.randint(18, 80),
            # Добавляем случайный город пользователя.
            "city": self.choose_item(self.data_provider.city_names),
            # Добавляем случайный признак активности пользователя.
            "is_active": self.randomizer.choice([True, False]),
            # Добавляем username пользователя заданной длины.
            "username": username_generator.generate_username(length=10),
            # Добавляем email, который может быть валидным или невалидным.
            "email": contact_generator.generate_email(valid=valid, username_length=8),
            # Добавляем учебный пароль заданной длины.
            "password": password_generator.generate_password(length=12),
            # Добавляем список из трех уникальных тегов.
            "tags": tags_generator.generate_tags(count=3, unique=True),
            # Добавляем случайную дату регистрации пользователя.
            "registration_date": date_generator.generate_registration_date(),
            # Добавляем случайный тариф пользователя.
            "subscription_plan": self.generate_subscription_plan(),
        }
