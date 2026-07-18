# Импортируем sys, чтобы прочитать короткое имя проверки из команды.
import sys
# Импортируем unittest, чтобы запускать уже готовые автотесты.
import unittest

# Создаем словарь: короткая команда ученика -> список настоящих unittest-тестов.
TESTS = {
    # Проверки ID пользователя.
    "id": [
        # Тест ID из цифр и точной длины.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_id_digits",
        # Тест ID из букв и цифр.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_id_alnum",
        # Тест ошибки при неправильной длине ID.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_id_bad_length",
        # Тест повторяемости ID при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_id_seed",
    ],
    # Проверки имени.
    "first_name": [
        # Тест минимальной длины имени.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_first_name_min_len",
        # Тест максимальной длины имени.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_first_name_max_len",
        # Тест ошибки, если подходящих имен нет.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_first_name_no_match",
        # Тест повторяемости имени при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_first_name_seed",
    ],
    # Проверки фамилии.
    "last_name": [
        # Тест максимальной длины фамилии.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_last_name_max_len",
        # Тест минимальной длины фамилии.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_last_name_min_len",
        # Тест ошибки, если подходящих фамилий нет.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_last_name_no_match",
        # Тест повторяемости фамилии при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_last_name_seed",
    ],
    # Проверки полного имени.
    "full_name": [
        # Тест ограничения общей длины полного имени.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_full_name_max_len",
        # Тест имени и фамилии в одной строке.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_full_name_basic",
        # Тест повторяемости полного имени при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_full_name_seed",
    ],
    # Проверки возраста.
    "age": [
        # Тест специальных значений возраста.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_age_bounds",
        # Тест обычного возраста внутри диапазона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_age_range",
        # Тест ошибки при неправильном диапазоне возраста.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_age_bad_range",
        # Тест повторяемости возраста при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_age_seed",
    ],
    # Проверки года рождения.
    "birth_year": [
        # Тест специальных значений года рождения.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_birth_year_bounds",
        # Тест обычного года внутри диапазона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_birth_year_range",
        # Тест ошибки при неправильном диапазоне годов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_birth_year_bad_range",
        # Тест повторяемости года при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_birth_year_seed",
    ],
    # Проверки города.
    "city": [
        # Тест фильтра города по первой букве.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_city_prefix",
        # Тест города из учебного списка.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_city_list",
        # Тест ошибки, если подходящего города нет.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_city_bad_prefix",
        # Тест повторяемости города при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_city_seed",
    ],
    # Проверки email.
    "email": [
        # Тест правильного и неправильного email.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_email_validity",
        # Тест ошибки при неправильной длине username.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_email_bad_len",
        # Тест повторяемости email при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_email_seed",
    ],
    # Проверки username.
    "username": [
        # Тест точной длины username.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_username_len",
        # Тест ошибки при неправильной длине username.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_username_bad_len",
        # Тест повторяемости username при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_username_seed",
    ],
    # Проверки комментария.
    "comment": [
        # Тест комментария любой нужной длины.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_comment_lengths",
        # Тест ошибки при отрицательной длине.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_comment_bad_len",
        # Тест повторяемости комментария при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_comment_seed",
    ],
    # Проверки пароля.
    "password": [
        # Тест обязательных частей пароля.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_password_parts",
        # Тест ошибки при неправильной длине пароля.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_password_bad_len",
        # Тест повторяемости пароля при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_password_seed",
    ],
    # Проверки телефона.
    "phone": [
        # Тест правильного и неправильного телефона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_phone_validity",
        # Тест кода оператора.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_phone_code",
        # Тест повторяемости телефона при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_phone_seed",
    ],
    # Проверки тегов.
    "tags": [
        # Тест количества и уникальности тегов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_tags_unique",
        # Тест ошибки при отрицательном количестве тегов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_tags_bad_count",
        # Тест тегов с повторами.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_tags_dupes",
        # Тест повторяемости тегов при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_tags_seed",
    ],
    # Проверки профиля.
    "profile": [
        # Тест богатого словаря профиля.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_user_profile_fields",
        # Тест профиля с неправильным email.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_user_profile_invalid_email",
        # Тест повторяемости профиля при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_user_profile_seed",
    ],
    # Проверки функции-образца балла.
    "score": [
        # Тест специальных значений балла.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_score_bounds",
        # Тест обычного балла внутри диапазона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_score_range",
        # Тест повторяемости балла при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_score_seed",
        # Тест ошибки при неправильном диапазоне баллов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_score_bad_range",
    ],
    # Проверки функции-образца активности.
    "active": [
        # Тест булевого результата.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_active_bool",
        # Тест повторяемости активности при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_active_seed",
    ],
    # Проверки функции-образца плана подписки.
    "plan": [
        # Тест выбора только из разрешенных планов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_plan_allowed",
        # Тест выбора из общего списка планов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_plan_default",
        # Тест повторяемости плана при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_plan_seed",
        # Тест ошибки при пустом списке планов.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_plan_empty",
    ],
    # Проверки функции-образца даты регистрации.
    "date": [
        # Тест специальных значений даты.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_reg_date_bounds",
        # Тест обычной даты внутри диапазона.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_reg_date_range",
        # Тест повторяемости даты при одинаковом seed.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_reg_date_seed",
        # Тест ошибки при неправильном диапазоне лет.
        "procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_reg_date_bad_range",
    ],
    # Проверки всей ООП-версии.
    "oop": [
        # Запускаем весь файл тестов ООП-версии.
        "oop_version.tests.test_generators",
    ],
    # Проверки всей процедурной версии.
    "all": [
        # Запускаем весь файл тестов процедурной версии.
        "procedural_version.tests.test_generators",
    ],
}

# Объявляем функцию, которая печатает подсказку по коротким командам.
def show_help():
    # Печатаем заголовок подсказки.
    print("Использование: python check.py <имя>")
    # Печатаем пример самой частой команды.
    print("Пример: python check.py city")
    # Печатаем пустую строку для читаемости.
    print()
    # Печатаем список доступных коротких имен.
    print("Доступные имена:")
    # Проходим по всем коротким именам в алфавитном порядке.
    for name in sorted(TESTS):
        # Печатаем одно короткое имя.
        print(f"- {name}")

# Объявляем главную функцию запуска.
def main():
    # Проверяем, передал ли ученик короткое имя проверки.
    if len(sys.argv) != 2:
        # Показываем подсказку, если имя не передали.
        show_help()
        # Возвращаем код ошибки, потому что команда неполная.
        return 1
    # Забираем короткое имя из команды.
    check_name = sys.argv[1]
    # Проверяем, знает ли программа такое короткое имя.
    if check_name not in TESTS:
        # Печатаем понятную ошибку.
        print(f"Не знаю проверку: {check_name}")
        # Показываем список доступных проверок.
        show_help()
        # Возвращаем код ошибки.
        return 1
    # Создаем загрузчик тестов unittest.
    loader = unittest.defaultTestLoader
    # Создаем пустой набор тестов.
    suite = unittest.TestSuite()
    # Проходим по настоящим именам тестов для выбранной короткой команды.
    for test_name in TESTS[check_name]:
        # Загружаем нужный тест по его полному пути внутри проекта.
        suite.addTests(loader.loadTestsFromName(test_name))
    # Создаем запускатель тестов с обычной подробностью вывода.
    runner = unittest.TextTestRunner(verbosity=1)
    # Запускаем выбранные тесты.
    result = runner.run(suite)
    # Возвращаем 0, если тесты прошли, и 1, если была ошибка.
    return 0 if result.wasSuccessful() else 1

# Проверяем, что файл запустили напрямую из терминала.
if __name__ == "__main__":
    # Запускаем главную функцию и передаем ее код системе.
    raise SystemExit(main())
