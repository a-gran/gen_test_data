# Импортируем учебные слова, с которых можно начать пароль.
from procedural_version.data.names_data import PASSWORD_WORDS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть пароль.
def password(length=12, use_digits=True, use_symbols=True, seed=None):
    # Что делает функция: возвращает строку-пароль ровно из length символов.
    # length=16 значит пароль должен быть длиной ровно 16 символов.
    # use_digits=True значит в пароле должна быть хотя бы одна цифра, например "5".
    # use_symbols=True значит в пароле должен быть хотя бы один спецсимвол, например "!".
    # seed - число для random: с одним и тем же seed random собирает один и тот же пароль.
    # Можно вызвать password() и получить пароль длиной 12 с цифрой и спецсимволом.
    # Можно вызвать password(length=16) и получить пароль длиной 16 символов.
    # Можно вызвать password(use_digits=False) и не требовать цифру.
    # Можно вызвать password(length=16, use_digits=True, use_symbols=True, seed=1) и сочетать настройки.
    # Пример вызова: password(length=16, use_digits=True, use_symbols=True, seed=1).
    # Документация: docs/function_specifications.md, раздел password.
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py password
    # Если в конце написано OK, этот тест прошел.
    # Что проверить в коде: если length меньше или равен 0, нужно вызвать ValueError.
    # Что вернуть: строку с паролем.
    # Тесты: test_password_parts, test_password_bad_len.
    # Проверяем, что длина пароля больше нуля.
    if length <= 0:
        # Сообщаем ошибку, если длина неправильная.
        raise ValueError("length должен быть больше 0")
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Задаем буквы, которые можно использовать в пароле.
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Задаем цифры, которые можно использовать в пароле.
    digits = "0123456789"
    # Задаем спецсимволы, которые можно использовать в пароле.
    symbols = "!@#$%^&*"
    # Начинаем список обязательных символов пустым.
    required_symbols = []
    # Проверяем, нужно ли добавить обязательную цифру.
    if use_digits:
        # Добавляем одну случайную цифру.
        required_symbols.append(randomizer.choice(digits))
    # Проверяем, нужно ли добавить обязательный спецсимвол.
    if use_symbols:
        # Добавляем один случайный спецсимвол.
        required_symbols.append(randomizer.choice(symbols))
    # Проверяем, хватает ли длины для всех обязательных символов.
    if len(required_symbols) > length:
        # Сообщаем ошибку, если пароль слишком короткий для требований.
        raise ValueError("length слишком маленький для выбранных требований")
    # Начинаем общий набор символов с букв.
    alphabet = letters
    # Проверяем, можно ли добавлять цифры в остальные символы.
    if use_digits:
        # Добавляем цифры в общий набор символов.
        alphabet += digits
    # Проверяем, можно ли добавлять спецсимволы в остальные символы.
    if use_symbols:
        # Добавляем спецсимволы в общий набор символов.
        alphabet += symbols
    # Выбираем слово, чтобы импорт PASSWORD_WORDS использовался по смыслу.
    base_word = randomizer.choice(PASSWORD_WORDS)
    # Собираем случайные символы для оставшейся длины.
    extra_symbols = [randomizer.choice(alphabet) for _ in range(length - len(required_symbols))]
    # Складываем обязательные и дополнительные символы вместе.
    password_symbols = required_symbols + extra_symbols
    # Подмешиваем буквы из учебного слова в начало, если для них есть место.
    password_symbols[:len(base_word[:len(password_symbols)])] = base_word[:len(password_symbols)]
    # Возвращаем случайный порядок символов в пароле.
    randomizer.shuffle(password_symbols)
    # Склеиваем список символов в строку пароля.
    return "".join(password_symbols)
