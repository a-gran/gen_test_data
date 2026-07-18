# Генераторы для реализации

В проекте 18 генераторов.

Главная идея теперь не в том, чтобы просто выбрать случайное значение из списка.

Главная идея — научиться генерировать тестовые данные по правилам:

- значения внутри допустимого диапазона;
- значения на границах диапазона;
- значения за границами диапазона для негативных тестов;
- строки точной длины;
- валидные и невалидные форматы;
- сложные словари и списки.

---

# Распределение по командам

## Команда 1. Числа, границы и данные человека

Команда отвечает за генераторы, где важно работать с диапазонами, длинами и базовыми данными человека.

Нужно реализовать:

- `generate_user_id(length=6, only_digits=True, seed=None)`
- `generate_first_name(min_length=None, max_length=None, seed=None)`
- `generate_last_name(min_length=None, max_length=None, seed=None)`
- `generate_full_name(max_total_length=None, seed=None)`
- `generate_age(min_age=18, max_age=80, boundary=None, seed=None)`
- `generate_birth_year(min_year=1950, max_year=2008, boundary=None, seed=None)`
<<<<<<< HEAD

## Команда 2. Строки, контакты и форматы

Команда отвечает за строки точной длины и валидные/невалидные форматы.
=======
- `generate_score(min_score=1, max_score=100, boundary=None, seed=None)`
- `generate_is_active(seed=None)`
- `generate_subscription_plan(allowed_plans=None, seed=None)`
- `generate_registration_date(start_year=2020, end_year=2026, boundary=None, seed=None)`

## Команда 2. Строки, контакты, списки и профиль

Команда отвечает за строки точной длины, валидные/невалидные форматы, списки и общий профиль пользователя.
>>>>>>> b9c35ad (ref: change structure)

Нужно реализовать:

- `generate_city(starts_with=None, seed=None)`
- `generate_phone(valid=True, seed=None)`
- `generate_email(valid=True, username_length=8, seed=None)`
- `generate_username(length=10, seed=None)`
- `generate_comment(length=100, seed=None)`
- `generate_password(length=12, use_digits=True, use_symbols=True, seed=None)`
<<<<<<< HEAD

## Команда 3. Списки, даты, тарифы и профиль

Команда отвечает за составные данные и общий профиль пользователя.

Нужно реализовать:

- `generate_score(min_score=1, max_score=100, boundary=None, seed=None)`
- `generate_is_active(seed=None)`
- `generate_tags(count=None, unique=True, seed=None)`
- `generate_subscription_plan(allowed_plans=None, seed=None)`
- `generate_registration_date(start_year=2020, end_year=2026, boundary=None, seed=None)`
=======
- `generate_tags(count=None, unique=True, seed=None)`
>>>>>>> b9c35ad (ref: change structure)
- `generate_user_profile(valid=True, seed=None)`

---

# Что обязательно проверить

Для чисел:

- обычное значение внутри диапазона;
- `boundary="min"`;
- `boundary="max"`;
- `boundary="below_min"`;
- `boundary="above_max"`.

Для строк:

- точную длину строки;
- минимальную длину;
- максимальную длину;
- наличие обязательных символов.

Для форматов:

- валидный email;
- невалидный email;
- валидный телефон;
- невалидный телефон;
- дату в формате `YYYY-MM-DD`.

Для структур:

- количество тегов;
- уникальность тегов;
- наличие обязательных ключей в профиле;
- валидный и невалидный профиль.

---

# Правило

Процедурная и ООП-версия должны работать одинаково.

Разница должна быть только в стиле программирования.
