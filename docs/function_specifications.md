# Спецификация функций генераторов

Этот документ объясняет, что должна получать и возвращать каждая функция.

Входные данные - это значения в скобках функции.

Выходные данные - это то, что функция возвращает через `return`.

`seed` помогает получать одинаковый случайный результат. Например, два вызова с `seed=1` должны дать одинаковый результат. Если `seed=None`, результат может меняться.

Внутренние переменные можно называть по-своему. Тесты проверяют результат функции, а не названия переменных.

---

# Готовые примеры

Эти функции уже реализованы в процедурной версии как примеры:

- `generate_score_example(...)`
- `generate_is_active_example(...)`
- `generate_subscription_plan_example(...)`
- `generate_registration_date_example(...)`

У этих примеров `example` есть и в названии файла, и в названии функции:

- `score_example.py`
- `is_active_example.py`
- `subscription_plan_example.py`
- `registration_date_example.py`

---

# Команда 1. Числа, границы и данные человека

## `generate_user_id(length=6, only_digits=True, seed=None)`

Вход:

- `length` - сколько символов должно быть в ID.
- `only_digits` - если `True`, ID состоит только из цифр; если `False`, можно использовать цифры и английские буквы.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- строка длиной ровно `length`.

Проверить:

- результат является строкой;
- длина результата ровно `length`;
- при `only_digits=True` строка состоит только из цифр;
- при `only_digits=False` можно использовать цифры и английские буквы;
- при одинаковом `seed` результат повторяется.

Пример:

```python
generate_user_id(length=8, only_digits=True, seed=1)
```

## `generate_first_name(min_length=None, max_length=None, seed=None)`

Вход:

- `min_length` - минимальная длина имени или `None`.
- `max_length` - максимальная длина имени или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- имя из списка `FIRST_NAMES`.

Проверить:

- результат является строкой;
- имя есть в списке имен;
- имя не короче `min_length`, если он передан;
- имя не длиннее `max_length`, если он передан;
- если подходящих имен нет, появляется понятная ошибка.

Пример:

```python
generate_first_name(min_length=5, seed=1)
```

## `generate_last_name(min_length=None, max_length=None, seed=None)`

Вход:

- `min_length` - минимальная длина фамилии или `None`.
- `max_length` - максимальная длина фамилии или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- фамилия из списка `LAST_NAMES`.

Проверить:

- результат является строкой;
- фамилия есть в списке фамилий;
- фамилия не короче `min_length`, если он передан;
- фамилия не длиннее `max_length`, если он передан;
- если подходящих фамилий нет, появляется понятная ошибка.

Пример:

```python
generate_last_name(max_length=7, seed=1)
```

## `generate_full_name(max_total_length=None, seed=None)`

Вход:

- `max_total_length` - максимальная длина полного имени или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- строка с именем и фамилией.

Проверить:

- результат является строкой;
- без ограничения строка содержит имя и фамилию;
- если `max_total_length` передан, строка не длиннее этого значения.

Пример:

```python
generate_full_name(max_total_length=10, seed=1)
```

## `generate_age(min_age=18, max_age=80, boundary=None, seed=None)`

Вход:

- `min_age` - самый маленький разрешенный возраст.
- `max_age` - самый большой разрешенный возраст.
- `boundary` - режим границы: `"min"`, `"max"`, `"below_min"`, `"above_max"` или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- целое число.

Проверить:

- обычный режим возвращает число от `min_age` до `max_age`;
- `boundary="min"` возвращает `min_age`;
- `boundary="max"` возвращает `max_age`;
- `boundary="below_min"` возвращает `min_age - 1`;
- `boundary="above_max"` возвращает `max_age + 1`;
- если `min_age > max_age`, появляется понятная ошибка.

Пример:

```python
generate_age(min_age=18, max_age=80, boundary="above_max")
```

## `generate_birth_year(min_year=1950, max_year=2008, boundary=None, seed=None)`

Вход:

- `min_year` - самый маленький разрешенный год рождения.
- `max_year` - самый большой разрешенный год рождения.
- `boundary` - режим границы: `"min"`, `"max"`, `"below_min"`, `"above_max"` или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- целое число.

Проверить:

- обычный режим возвращает год от `min_year` до `max_year`;
- `boundary="min"` возвращает `min_year`;
- `boundary="max"` возвращает `max_year`;
- `boundary="below_min"` возвращает `min_year - 1`;
- `boundary="above_max"` возвращает `max_year + 1`;
- если `min_year > max_year`, появляется понятная ошибка.

Пример:

```python
generate_birth_year(min_year=1950, max_year=2008, boundary="min")
```

---

# Готовые примеры для команды 1

## `generate_score_example(min_score=1, max_score=100, boundary=None, seed=None)`

Это пример готового решения для генератора с числами и границами.

Файл с примером: `procedural_version/generators/score_example.py`.

Вход:

- `min_score` - самый маленький разрешенный балл.
- `max_score` - самый большой разрешенный балл.
- `boundary` - режим границы: `"min"`, `"max"`, `"below_min"`, `"above_max"` или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- целое число с баллом.

## `generate_is_active_example(seed=None)`

Это пример готового решения для генератора `True` или `False`.

Файл с примером: `procedural_version/generators/is_active_example.py`.

Вход:

- `seed` - число для повторения случайного результата или `None`.

Выход:

- `True` или `False`.

## `generate_subscription_plan_example(allowed_plans=None, seed=None)`

Это пример готового решения для выбора плана подписки.

План подписки - это вариант аккаунта пользователя, например `"free"` или `"premium"`.

Файл с примером: `procedural_version/generators/subscription_plan_example.py`.

Вход:

- `allowed_plans` - список разрешенных планов подписки или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- строка с названием плана подписки.

## `generate_registration_date_example(start_year=2020, end_year=2026, boundary=None, seed=None)`

Это пример готового решения для генератора даты с границами.

Файл с примером: `procedural_version/generators/registration_date_example.py`.

Вход:

- `start_year` - первый разрешенный год регистрации.
- `end_year` - последний разрешенный год регистрации.
- `boundary` - режим границы: `"min"`, `"max"`, `"below_min"`, `"above_max"` или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- строка даты в формате `YYYY-MM-DD`.

---

# Команда 2. Строки, контакты, списки и профиль

## `generate_city(starts_with=None, seed=None)`

Вход:

- `starts_with` - начало названия города или `None`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- город из списка `CITY_NAMES`.

Проверить:

- результат является строкой;
- город есть в списке городов;
- если `starts_with` передан, город начинается с этого текста;
- если подходящих городов нет, появляется понятная ошибка.

Пример:

```python
generate_city(starts_with="М", seed=1)
```

## `generate_phone(valid=True, seed=None)`

Вход:

- `valid` - если `True`, нужен правильный телефон; если `False`, телефон с ошибкой.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- словарь с ключами `country_code`, `operator_code`, `number`.

Проверить:

- при `valid=True` код страны равен `"+7"`;
- при `valid=True` `operator_code` от `900` до `999`;
- при `valid=True` `number` от `1000000` до `9999999`;
- при `valid=False` данные намеренно неправильные.

Пример:

```python
generate_phone(valid=False, seed=1)
```

## `generate_email(valid=True, username_length=8, seed=None)`

Вход:

- `valid` - если `True`, нужен правильный email; если `False`, email с ошибкой.
- `username_length` - длина части email до `@`.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- строка email.

Проверить:

- при `valid=True` строка содержит `@`;
- часть до `@` имеет длину `username_length`;
- при `valid=False` email намеренно неправильный;
- если `username_length <= 0`, появляется понятная ошибка.

Пример:

```python
generate_email(valid=True, username_length=8, seed=1)
```

## `generate_username(length=10, seed=None)`

Вход:

- `length` - нужная длина username.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- строка username.

Проверить:

- результат является строкой;
- длина ровно `length`;
- можно использовать маленькие английские буквы, цифры и `_`;
- если `length <= 0`, появляется понятная ошибка.

Пример:

```python
generate_username(length=12, seed=1)
```

## `generate_comment(length=100, seed=None)`

Вход:

- `length` - нужная длина комментария.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- строка ровно заданной длины.

Проверить:

- `length=0` возвращает пустую строку;
- `length=1` возвращает строку из 1 символа;
- `length=255` возвращает строку из 255 символов;
- `length=1000` возвращает строку из 1000 символов;
- если `length < 0`, появляется понятная ошибка.

Пример:

```python
generate_comment(length=255, seed=1)
```

## `generate_password(length=12, use_digits=True, use_symbols=True, seed=None)`

Вход:

- `length` - длина пароля.
- `use_digits` - если `True`, в пароле должна быть цифра.
- `use_symbols` - если `True`, в пароле должен быть специальный символ.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- строка пароля.

Проверить:

- длина результата ровно `length`;
- если `use_digits=True`, в пароле есть хотя бы одна цифра;
- если `use_symbols=True`, в пароле есть хотя бы один специальный символ;
- если `length <= 0`, появляется понятная ошибка.

Пример:

```python
generate_password(length=16, use_digits=True, use_symbols=True, seed=1)
```

## `generate_tags(count=None, unique=True, seed=None)`

Вход:

- `count` - сколько тегов нужно вернуть или `None`.
- `unique` - если `True`, теги не повторяются; если `False`, повторы разрешены.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- список тегов.

Проверить:

- результат является списком;
- если `count` передан, длина списка равна `count`;
- если `unique=True`, теги не повторяются;
- все теги есть в списке `TAGS`;
- если `count < 0`, появляется понятная ошибка.

Пример:

```python
generate_tags(count=5, unique=True, seed=1)
```

## `generate_user_profile(valid=True, seed=None)`

Вход:

- `valid` - если `True`, профиль правильный; если `False`, email в профиле должен быть с ошибкой.
- `seed` - число для повторения случайного результата или `None`.

Выход:

- словарь профиля пользователя.

Проверить:

- профиль является словарем;
- есть ключи `user_id`, `first_name`, `last_name`, `age`, `city`, `is_active`;
- есть ключи `username`, `email`, `password`, `tags`;
- есть ключи `registration_date`, `subscription_plan`;
- `user_id` имеет длину 6;
- `username` имеет длину 10;
- `password` имеет длину 12;
- `tags` содержит 3 уникальных тега;
- при `valid=True` email правильный;
- при `valid=False` email намеренно неправильный.

Пример:

```python
generate_user_profile(valid=False, seed=1)
```
