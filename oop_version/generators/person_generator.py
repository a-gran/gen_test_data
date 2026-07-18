# Импортируем базовый генератор, чтобы использовать общую логику.
from oop_version.generators.base_generator import BaseGenerator

# Объявляем класс для генерации данных человека.
class PersonGenerator(BaseGenerator):
    # Объявляем метод, который генерирует случайное имя.
    def generate_first_name(self, min_length=None, max_length=None):
        # Начинаем с полного списка имен.
        filtered_names = self.data_provider.first_names
        # Проверяем, передана ли минимальная длина имени.
        if min_length is not None:
            # Оставляем только имена не короче минимальной длины.
            filtered_names = [name for name in filtered_names if len(name) >= min_length]
        # Проверяем, передана ли максимальная длина имени.
        if max_length is not None:
            # Оставляем только имена не длиннее максимальной длины.
            filtered_names = [name for name in filtered_names if len(name) <= max_length]
        # Проверяем, остались ли имена после фильтрации.
        if not filtered_names:
            # Сообщаем понятную ошибку, если подходящих имен нет.
            raise ValueError("Нет имен, которые подходят под ограничения длины")
        # Возвращаем случайное имя из отфильтрованного списка.
        return self.randomizer.choice(filtered_names)

    # Объявляем метод, который генерирует цифровой ID пользователя.
    def generate_user_id(self, length=6, only_digits=True):
        # Проверяем, что длина ID положительная.
        if length <= 0:
            # Сообщаем понятную ошибку, если длина меньше или равна нулю.
            raise ValueError("length должен быть больше 0")
        # Создаем алфавит только из цифр.
        alphabet = "0123456789"
        # Проверяем, можно ли использовать не только цифры.
        if not only_digits:
            # Добавляем английские буквы для буквенно-цифрового ID.
            alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Собираем ID из нужного количества случайных символов.
        user_id = "".join(self.randomizer.choice(alphabet) for _ in range(length))
        # Возвращаем ID ровно нужной длины.
        return user_id

    # Объявляем метод, который генерирует возраст пользователя.
    def generate_age(self, min_age=18, max_age=80, boundary=None):
        # Проверяем, что минимальный возраст не больше максимального.
        if min_age > max_age:
            # Сообщаем понятную ошибку, если границы перепутаны местами.
            raise ValueError("min_age не должен быть больше max_age")
        # Проверяем, попросили ли вернуть нижнюю границу.
        if boundary == "min":
            # Возвращаем минимальный допустимый возраст.
            return min_age
        # Проверяем, попросили ли вернуть верхнюю границу.
        if boundary == "max":
            # Возвращаем максимальный допустимый возраст.
            return max_age
        # Проверяем, попросили ли вернуть значение ниже нижней границы.
        if boundary == "below_min":
            # Возвращаем возраст на единицу меньше минимума для негативного теста.
            return min_age - 1
        # Проверяем, попросили ли вернуть значение выше верхней границы.
        if boundary == "above_max":
            # Возвращаем возраст на единицу больше максимума для негативного теста.
            return max_age + 1
        # Возвращаем случайный возраст внутри переданных границ.
        return self.randomizer.randint(min_age, max_age)

    # Объявляем метод, который генерирует год рождения пользователя.
    def generate_birth_year(self, min_year=1950, max_year=2008, boundary=None):
        # Проверяем, что минимальный год не больше максимального.
        if min_year > max_year:
            # Сообщаем понятную ошибку, если границы перепутаны местами.
            raise ValueError("min_year не должен быть больше max_year")
        # Проверяем, попросили ли вернуть нижнюю границу.
        if boundary == "min":
            # Возвращаем минимальный допустимый год.
            return min_year
        # Проверяем, попросили ли вернуть верхнюю границу.
        if boundary == "max":
            # Возвращаем максимальный допустимый год.
            return max_year
        # Проверяем, попросили ли вернуть значение ниже нижней границы.
        if boundary == "below_min":
            # Возвращаем год на единицу меньше минимума для негативного теста.
            return min_year - 1
        # Проверяем, попросили ли вернуть значение выше верхней границы.
        if boundary == "above_max":
            # Возвращаем год на единицу больше максимума для негативного теста.
            return max_year + 1
        # Возвращаем случайный год рождения внутри переданных границ.
        return self.randomizer.randint(min_year, max_year)

    # Объявляем метод, который генерирует случайный город.
    def generate_city(self, starts_with=None):
        # Начинаем с полного списка городов.
        filtered_cities = self.data_provider.city_names
        # Проверяем, передана ли первая буква или начало города.
        if starts_with is not None:
            # Оставляем только города, которые начинаются с переданного текста.
            filtered_cities = [city for city in filtered_cities if city.startswith(starts_with)]
        # Проверяем, остались ли города после фильтрации.
        if not filtered_cities:
            # Сообщаем понятную ошибку, если подходящих городов нет.
            raise ValueError("Нет городов, которые подходят под starts_with")
        # Возвращаем случайный город из отфильтрованного списка.
        return self.randomizer.choice(filtered_cities)

    # Объявляем метод, который генерирует учебный балл.
    def generate_score(self, min_score=1, max_score=100, boundary=None):
        # Проверяем, что минимальный балл не больше максимального.
        if min_score > max_score:
            # Сообщаем понятную ошибку, если границы перепутаны местами.
            raise ValueError("min_score не должен быть больше max_score")
        # Проверяем, попросили ли вернуть нижнюю границу.
        if boundary == "min":
            # Возвращаем минимальный допустимый балл.
            return min_score
        # Проверяем, попросили ли вернуть верхнюю границу.
        if boundary == "max":
            # Возвращаем максимальный допустимый балл.
            return max_score
        # Проверяем, попросили ли вернуть значение ниже нижней границы.
        if boundary == "below_min":
            # Возвращаем балл на единицу меньше минимума для негативного теста.
            return min_score - 1
        # Проверяем, попросили ли вернуть значение выше верхней границы.
        if boundary == "above_max":
            # Возвращаем балл на единицу больше максимума для негативного теста.
            return max_score + 1
        # Возвращаем случайный балл внутри переданных границ.
        return self.randomizer.randint(min_score, max_score)

    # Объявляем метод, который генерирует признак активности.
    def generate_is_active(self):
        # Возвращаем случайное булево значение.
        return self.randomizer.choice([True, False])

    # Объявляем метод, который генерирует случайную фамилию.
    def generate_last_name(self, min_length=None, max_length=None):
        # Начинаем с полного списка фамилий.
        filtered_last_names = self.data_provider.last_names
        # Проверяем, передана ли минимальная длина фамилии.
        if min_length is not None:
            # Оставляем только фамилии не короче минимальной длины.
            filtered_last_names = [last_name for last_name in filtered_last_names if len(last_name) >= min_length]
        # Проверяем, передана ли максимальная длина фамилии.
        if max_length is not None:
            # Оставляем только фамилии не длиннее максимальной длины.
            filtered_last_names = [last_name for last_name in filtered_last_names if len(last_name) <= max_length]
        # Проверяем, остались ли фамилии после фильтрации.
        if not filtered_last_names:
            # Сообщаем понятную ошибку, если подходящих фамилий нет.
            raise ValueError("Нет фамилий, которые подходят под ограничения длины")
        # Возвращаем случайную фамилию из отфильтрованного списка.
        return self.randomizer.choice(filtered_last_names)

    # Объявляем метод, который генерирует username пользователя.
    def generate_username(self, length=10):
        # Проверяем, что длина username положительная.
        if length <= 0:
            # Сообщаем понятную ошибку, если длина меньше или равна нулю.
            raise ValueError("length должен быть больше 0")
        # Выбираем слово для начала username.
        username_word = self.choose_item(self.data_provider.username_words)
        # Создаем алфавит из маленьких букв, цифр и нижнего подчеркивания.
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"
        # Берем начало username из слова и нижнего подчеркивания.
        username = f"{username_word}_"
        # Добавляем случайные символы, пока username короче нужной длины.
        while len(username) < length:
            # Добавляем один случайный символ из разрешенного алфавита.
            username += self.randomizer.choice(alphabet)
        # Возвращаем username ровно нужной длины.
        return username[:length]

    # Объявляем метод, который генерирует полное имя.
    def generate_full_name(self, max_total_length=None):
        # Выбираем случайное имя.
        first_name = self.generate_first_name()
        # Выбираем случайную фамилию.
        last_name = self.generate_last_name()
        # Склеиваем имя и фамилию через пробел и возвращаем результат.
        full_name = f"{first_name} {last_name}"
        # Проверяем, задана ли максимальная общая длина.
        if max_total_length is not None and len(full_name) > max_total_length:
            # Обрезаем полное имя до максимальной длины для проверки ограничений интерфейса.
            return full_name[:max_total_length]
        # Возвращаем полное имя без обрезки.
        return full_name
