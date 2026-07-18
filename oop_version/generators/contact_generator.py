# Импортируем базовый генератор, чтобы использовать общую логику.
from oop_version.generators.base_generator import BaseGenerator

# Объявляем класс для генерации контактных данных.
class ContactGenerator(BaseGenerator):
    # Объявляем метод, который генерирует адрес электронной почты.
    def generate_email(self, valid=True, username_length=8):
        # Проверяем, что длина имени почтового ящика положительная.
        if username_length <= 0:
            # Сообщаем понятную ошибку, если длина меньше или равна нулю.
            raise ValueError("username_length должен быть больше 0")
        # Выбираем слово для части email до знака собаки.
        username_word = self.choose_item(self.data_provider.username_words)
        # Создаем алфавит из маленьких букв, цифр и нижнего подчеркивания.
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789_"
        # Берем начало username из слова и нижнего подчеркивания.
        username = f"{username_word}_"
        # Добавляем случайные символы, пока username короче нужной длины.
        while len(username) < username_length:
            # Добавляем один случайный символ из разрешенного алфавита.
            username += self.randomizer.choice(alphabet)
        # Обрезаем username ровно до нужной длины.
        username = username[:username_length]
        # Выбираем домен для части email после знака собаки.
        domain = self.choose_item(self.data_provider.email_domains)
        # Проверяем, нужно ли вернуть невалидный email для негативного теста.
        if not valid:
            # Возвращаем строку без знака собаки, чтобы формат был намеренно неправильным.
            return f"{username}.{domain}"
        # Склеиваем части email и возвращаем готовую строку.
        return f"{username}@{domain}"

    # Объявляем метод, который генерирует номер телефона как словарь.
    def generate_phone(self, valid=True):
        # Проверяем, нужно ли вернуть невалидный телефон для негативного теста.
        if not valid:
            # Возвращаем номер с неправильным кодом страны и слишком коротким номером.
            return {
                # Записываем неправильный код страны.
                "country_code": "7",
                # Генерируем слишком маленький код оператора.
                "operator_code": self.randomizer.randint(10, 99),
                # Генерируем слишком короткую основную часть номера.
                "number": self.randomizer.randint(1000, 9999),
            }
        # Возвращаем номер телефона в виде словаря с простыми значениями.
        return {
            # Записываем код страны отдельным значением.
            "country_code": "+7",
            # Генерируем код оператора как целое число.
            "operator_code": self.randomizer.randint(900, 999),
            # Генерируем основную часть номера как целое число.
            "number": self.randomizer.randint(1000000, 9999999),
        }
