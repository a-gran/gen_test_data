# Инструкции для команд

В проекте 7 учеников.

Ученики делятся на 2 команды.

В первой команде 3 человека.

Во второй команде 4 человека.

Базовое распределение: по 2 функции на одного ученика.

Команда 1 получает 6 основных функций и 4 оставшиеся функции.

Команда 2 получает 8 функций.

Каждый генератор должен быть не просто случайным выбором, а маленькой учебной задачей про тестовые данные.

---

# Общий порядок работы

1. Сначала реализуйте все функции своей команды в процедурной версии.
2. Запустите автотесты процедурной версии.
3. Исправьте процедурную версию, если тесты показали ошибки.
4. Только после этого реализуйте такие же возможности в ООП-версии.
5. Запустите автотесты ООП-версии.
6. Исправьте ООП-версию, если тесты показали ошибки.
7. После этого проверьте, что процедурная и ООП-версия работают одинаково.

Команды для проверки:

Сначала процедурная версия:

```bash
python -m unittest discover -s procedural_version/tests
```

Потом ООП-версия:

```bash
python -m unittest discover -s oop_version/tests
```

Тесты ООП-версии дополнительно сравнивают результаты методов с процедурными функциями при одинаковых параметрах и `seed`.

`seed` помогает получать одинаковый случайный результат. Например, два запуска с `seed=1` должны вернуть одно и то же значение. Это удобно для тестов.

---

# Команда 1. Числа, границы и данные человека

## Функции

- `generate_user_id(length=6, only_digits=True, seed=None)`
- `generate_first_name(min_length=None, max_length=None, seed=None)`
- `generate_last_name(min_length=None, max_length=None, seed=None)`
- `generate_full_name(max_total_length=None, seed=None)`
- `generate_age(min_age=18, max_age=80, boundary=None, seed=None)`
- `generate_birth_year(min_year=1950, max_year=2008, boundary=None, seed=None)`

Готовые примеры:

- `generate_score_example(min_score=1, max_score=100, boundary=None, seed=None)`
- `generate_is_active_example(seed=None)`
- `generate_subscription_plan_example(allowed_plans=None, seed=None)`
- `generate_registration_date_example(start_year=2020, end_year=2026, boundary=None, seed=None)`

У этих примеров `example` есть и в названии файла, и в названии функции.

## Чему учится команда

- задавать длину строки;
- проверять минимальную и максимальную длину;
- работать с диапазонами чисел;
- генерировать значения на границах;
- генерировать значения за границами для негативных тестов;
- ограничивать выбор разрешенными значениями;
- генерировать даты на границах диапазона.

## Примеры требований

- `generate_user_id(length=8)` должен вернуть строку ровно из 8 символов.
- `generate_age(boundary="min")` должен вернуть нижнюю границу.
- `generate_age(boundary="above_max")` должен вернуть значение выше верхней границы.
- `generate_full_name(max_total_length=10)` не должен вернуть строку длиннее 10 символов.
- `generate_subscription_plan_example(allowed_plans=["free", "premium"])` должен выбрать только из этих планов подписки.
- `generate_registration_date_example(boundary="min")` должен вернуть дату на нижней границе.

---

# Команда 2. Строки, контакты, списки и профиль

## Функции

- `generate_city(starts_with=None, seed=None)`
- `generate_phone(valid=True, seed=None)`
- `generate_email(valid=True, username_length=8, seed=None)`
- `generate_username(length=10, seed=None)`
- `generate_comment(length=100, seed=None)`
- `generate_password(length=12, use_digits=True, use_symbols=True, seed=None)`
- `generate_tags(count=None, unique=True, seed=None)`
- `generate_user_profile(valid=True, seed=None)`

## Чему учится команда

- генерировать строки точной длины;
- делать валидные и невалидные данные;
- проверять формат email;
- проверять формат телефона;
- гарантировать наличие цифр и специальных символов в пароле;
- генерировать списки нужного размера;
- делать элементы списка уникальными;
- собирать сложный словарь из нескольких генераторов.

## Примеры требований

- `generate_comment(length=255)` должен вернуть строку ровно 255 символов.
- `generate_comment(length=1)` должен вернуть строку ровно 1 символ.
- `generate_comment(length=1000)` должен вернуть строку ровно 1000 символов.
- `generate_email(valid=True)` должен вернуть строку со знаком `@`.
- `generate_email(valid=False)` должен вернуть намеренно неправильный email.
- `generate_password(length=16, use_digits=True, use_symbols=True)` должен вернуть пароль длиной 16 символов с цифрой и спецсимволом.
- `generate_tags(count=5, unique=True)` должен вернуть 5 уникальных тегов.
- `generate_user_profile(valid=False)` должен вернуть профиль с намеренно невалидным email.
