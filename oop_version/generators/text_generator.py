# Импортируем базовый генератор, чтобы использовать общую логику.
from oop_version.generators.base_generator import BaseGenerator

# Объявляем класс для генерации текстовых данных.
class TextGenerator(BaseGenerator):
    # Объявляем метод, который генерирует комментарий любой заданной длины.
    def generate_comment(self, length=100):
        # Проверяем, что длина комментария не отрицательная.
        if length < 0:
            # Сообщаем понятную ошибку, если длина меньше нуля.
            raise ValueError("length не должен быть меньше 0")
        # Выбираем базовый текст, чтобы комментарий был похож на человеческую фразу.
        base_comment = self.choose_item(self.data_provider.comments)
        # Повторяем базовый текст с пробелом, чтобы точно набрать нужную длину.
        repeated_comment = (base_comment + " ") * ((length // (len(base_comment) + 1)) + 2)
        # Обрезаем повторенный текст ровно до нужного количества символов.
        return repeated_comment[:length]

    # Объявляем метод, который генерирует учебный пароль.
    def generate_password(self, length=12, use_digits=True, use_symbols=True):
        # Проверяем, что длина пароля положительная.
        if length <= 0:
            # Сообщаем понятную ошибку, если длина меньше или равна нулю.
            raise ValueError("length должен быть больше 0")
        # Создаем строку с буквами, которые можно использовать в пароле.
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Создаем строку с цифрами, которые можно добавить в пароль.
        digits = "0123456789"
        # Создаем строку со специальными символами, которые можно добавить в пароль.
        symbols = "!@#$%^&*"
        # Начинаем пароль со случайного учебного слова.
        password_parts = [self.choose_item(self.data_provider.password_words)]
        # Добавляем обязательную цифру, если цифры включены.
        if use_digits:
            # Кладем одну случайную цифру в список частей пароля.
            password_parts.append(self.randomizer.choice(digits))
        # Добавляем обязательный спецсимвол, если спецсимволы включены.
        if use_symbols:
            # Кладем один случайный спецсимвол в список частей пароля.
            password_parts.append(self.randomizer.choice(symbols))
        # Собираем алфавит из букв.
        alphabet = letters
        # Добавляем цифры в алфавит, если они разрешены.
        if use_digits:
            # Расширяем алфавит цифрами.
            alphabet += digits
        # Добавляем спецсимволы в алфавит, если они разрешены.
        if use_symbols:
            # Расширяем алфавит спецсимволами.
            alphabet += symbols
        # Склеиваем обязательные части в одну строку.
        raw_password = "".join(password_parts)
        # Добавляем случайные символы, пока строка короче нужной длины.
        while len(raw_password) < length:
            # Добавляем один случайный символ из разрешенного алфавита.
            raw_password += self.randomizer.choice(alphabet)
        # Возвращаем пароль ровно нужной длины.
        return raw_password[:length]

    # Объявляем метод, который генерирует список тегов.
    def generate_tags(self, count=None, unique=True):
        # Выбираем случайное количество тегов от 1 до 3, если количество не передали.
        tags_count = count if count is not None else self.randomizer.randint(1, 3)
        # Проверяем, что количество тегов не отрицательное.
        if tags_count < 0:
            # Сообщаем понятную ошибку, если количество меньше нуля.
            raise ValueError("count не должен быть меньше 0")
        # Проверяем, нужны ли уникальные теги.
        if unique:
            # Ограничиваем количество размером списка, чтобы sample не упал.
            safe_count = min(tags_count, len(self.data_provider.tags))
            # Возвращаем список случайных тегов без повторов.
            return self.randomizer.sample(self.data_provider.tags, safe_count)
        # Возвращаем список тегов, где повторы разрешены.
        return [self.randomizer.choice(self.data_provider.tags) for _ in range(tags_count)]
