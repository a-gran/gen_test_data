# Спецификация функций генераторов

Документ подробно описывает, что должна получать на вход и возвращать каждая функция.

Для каждой функции указаны:

- входные параметры;
- выходной результат;
- критерии правильной работы;
- примеры вызова.

---

# Команда 1. Числа, границы и данные человека

## `generate_user_id(length=6, only_digits=True, seed=None)`

Вход:

- `length` - сколько символов должно быть в ID.
- `only_digits` - если `True`, ID состоит только из цифр.
- `seed` - значение для повторяемой генерации.

Выход:

- строка длиной ровно `length`.

Критерии:

- результат должен быть строкой;
- длина результата должна быть ровно `length`;
- если `only_digits=True`, строка должна состоять только из цифр;
- если `only_digits=False`, можно использовать цифры и английские буквы;
- при одинаковом `seed` результат должен повторяться.

Пример:

```python
generate_user_id(length=8, only_digits=True, seed=1)
```

## `generate_first_name(min_length=None, max_length=None, seed=None)`

Вход:

- `min_length` - минимальная длина имени.
- `max_length` - максимальная длина имени.
- `seed` - значение для повторяемой генерации.

Выход:

- имя из списка `FIRST_NAMES`.

Критерии:

- результат должен быть строкой;
- имя должно быть из списка имен;
- если задан `min_length`, имя не должно быть короче;
- если задан `max_length`, имя не должно быть длиннее;
- если подходящих имен нет, должна быть понятная ошибка.

Пример:

```python
generate_first_name(min_length=5, seed=1)
```

## `generate_last_name(min_length=None, max_length=None, seed=None)`

Вход:

- `min_length` - минимальная длина фамилии.
- `max_length` - максимальная длина фамилии.
- `seed` - значение для повторяемой генерации.

Выход:

- фамилия из списка `LAST_NAMES`.

Критерии:

- результат должен быть строкой;
- фамилия должна быть из списка фамилий;
- если задан `min_length`, фамилия не должна быть короче;
- если задан `max_length`, фамилия не должна быть длиннее;
- если подходящих фамилий нет, должна быть понятная ошибка.

Пример:

```python
generate_last_name(max_length=7, seed=1)
```

## `generate_full_name(max_total_length=None, seed=None)`

Вход:

- `max_total_length` - максимальная длина полного имени.
- `seed` - значение для повторяемой генерации.

Выход:

- строка с именем и фамилией.

Критерии:

- результат должен быть строкой;
- без ограничения строка должна содержать имя и фамилию;
- если задан `max_total_length`, строка не должна быть длиннее этого значения.

Пример:

```python
generate_full_name(max_total_length=10, seed=1)
```

## `generate_age(min_age=18, max_age=80, boundary=None, seed=None)`

Вход:

- `min_age` - нижняя граница возраста.
- `max_age` - верхняя граница возраста.
- `boundary` - режим граничного значения.
- `seed` - значение для повторяемой генерации.

Выход:

- целое число.

Критерии:

- обычный режим возвращает число от `min_age` до `max_age`;
- `boundary="min"` возвращает `min_age`;
- `boundary="max"` возвращает `max_age`;
- `boundary="below_min"` возвращает `min_age - 1`;
- `boundary="above_max"` возвращает `max_age + 1`;
- если `min_age > max_age`, должна быть ошибка.

Пример:

```python
generate_age(min_age=18, max_age=80, boundary="above_max")
```

## `generate_birth_year(min_year=1950, max_year=2008, boundary=None, seed=None)`

Вход:

- `min_year` - нижняя граница года рождения.
- `max_year` - верхняя граница года рождения.
- `boundary` - режим граничного значения.
- `seed` - значение для повторяемой генерации.

Выход:

- целое число.

Критерии:

- обычный режим возвращает год от `min_year` до `max_year`;
- `boundary="min"` возвращает `min_year`;
- `boundary="max"` возвращает `max_year`;
- `boundary="below_min"` возвращает `min_year - 1`;
- `boundary="above_max"` возвращает `max_year + 1`;
- если `min_year > max_year`, должна быть ошибка.

Пример:

```python
generate_birth_year(min_year=1950, max_year=2008, boundary="min")
```

<<<<<<< HEAD
---

# Команда 2. Строки, контакты и форматы
=======
## `generate_score(min_score=1, max_score=100, boundary=None, seed=None)`

Вход:

- `min_score` - нижняя граница балла.
- `max_score` - верхняя граница балла.
- `boundary` - режим граничного значения.
- `seed` - значение для повторяемой генерации.

Выход:

- целое число.

Критерии:

- обычный режим возвращает число от `min_score` до `max_score`;
- `boundary="min"` возвращает `min_score`;
- `boundary="max"` возвращает `max_score`;
- `boundary="below_min"` возвращает `min_score - 1`;
- `boundary="above_max"` возвращает `max_score + 1`;
- если `min_score > max_score`, должна быть ошибка.

Пример:

```python
generate_score(min_score=1, max_score=100, boundary="max")
```

## `generate_is_active(seed=None)`

Вход:

- `seed` - значение для повторяемой генерации.

Выход:

- `True` или `False`.

Критерии:

- результат должен быть булевым значением;
- при одинаковом `seed` результат должен повторяться.

Пример:

```python
generate_is_active(seed=1)
```

## `generate_subscription_plan(allowed_plans=None, seed=None)`

Вход:

- `allowed_plans` - список разрешенных тарифов.
- `seed` - значение для повторяемой генерации.

Выход:

- строка с названием тарифа.

Критерии:

- если `allowed_plans` передан, тариф должен быть только из этого списка;
- если `allowed_plans` не передан, тариф берется из общего списка;
- если список тарифов пустой, должна быть ошибка.

Пример:

```python
generate_subscription_plan(allowed_plans=["free", "premium"], seed=1)
```

## `generate_registration_date(start_year=2020, end_year=2026, boundary=None, seed=None)`

Вход:

- `start_year` - нижняя граница года.
- `end_year` - верхняя граница года.
- `boundary` - режим граничного значения.
- `seed` - значение для повторяемой генерации.

Выход:

- строка даты в формате `YYYY-MM-DD`.

Критерии:

- обычный режим возвращает дату внутри диапазона;
- `boundary="min"` возвращает дату в начале диапазона;
- `boundary="max"` возвращает дату в конце диапазона;
- `boundary="below_min"` возвращает дату раньше диапазона;
- `boundary="above_max"` возвращает дату позже диапазона;
- если `start_year > end_year`, должна быть ошибка.

Пример:

```python
generate_registration_date(start_year=2020, end_year=2026, boundary="max")
```

---

# Команда 2. Строки, контакты, списки и профиль
>>>>>>> b9c35ad (ref: change structure)

## `generate_city(starts_with=None, seed=None)`

Вход:

- `starts_with` - начало названия города.
- `seed` - значение для повторяемой генерации.

Выход:

- город из списка `CITY_NAMES`.

Критерии:

- результат должен быть строкой;
- город должен быть из списка городов;
- если задан `starts_with`, город должен начинаться с этого текста;
- если подходящих городов нет, должна быть понятная ошибка.

Пример:

```python
generate_city(starts_with="М", seed=1)
```

## `generate_phone(valid=True, seed=None)`

Вход:

- `valid` - нужен валидный или невалидный телефон.
- `seed` - значение для повторяемой генерации.

Выход:

- словарь с ключами `country_code`, `operator_code`, `number`.

Критерии:

- при `valid=True`:
  - `country_code` равен `"+7"`;
  - `operator_code` от `900` до `999`;
  - `number` от `1000000` до `9999999`;
- при `valid=False`:
  - данные должны быть намеренно неправильными;
  - например, код страны не `"+7"` или номер слишком короткий.

Пример:

```python
generate_phone(valid=False, seed=1)
```

## `generate_email(valid=True, username_length=8, seed=None)`

Вход:

- `valid` - нужен валидный или невалидный email.
- `username_length` - длина части email до `@`.
- `seed` - значение для повторяемой генерации.

Выход:

- строка email.

Критерии:

- при `valid=True` строка должна содержать `@`;
- часть до `@` должна быть ровно `username_length`;
- после `@` должен быть домен;
- при `valid=False` email должен быть намеренно неправильным;
- если `username_length <= 0`, должна быть ошибка.

Пример:

```python
generate_email(valid=True, username_length=8, seed=1)
```

## `generate_username(length=10, seed=None)`

Вход:

- `length` - нужная длина username.
- `seed` - значение для повторяемой генерации.

Выход:

- строка username.

Критерии:

- результат должен быть строкой;
- длина должна быть ровно `length`;
- можно использовать маленькие английские буквы, цифры и `_`;
- если `length <= 0`, должна быть ошибка.

Пример:

```python
generate_username(length=12, seed=1)
```

## `generate_comment(length=100, seed=None)`

Вход:

- `length` - нужная длина комментария.
- `seed` - значение для повторяемой генерации.

Выход:

- строка ровно заданной длины.

Критерии:

- `length=0` возвращает пустую строку;
- `length=1` возвращает строку из 1 символа;
- `length=255` возвращает строку из 255 символов;
- `length=1000` возвращает строку из 1000 символов;
- если `length < 0`, должна быть ошибка.

Пример:

```python
generate_comment(length=255, seed=1)
```

## `generate_password(length=12, use_digits=True, use_symbols=True, seed=None)`

Вход:

- `length` - длина пароля.
- `use_digits` - добавлять ли цифры.
- `use_symbols` - добавлять ли спецсимволы.
- `seed` - значение для повторяемой генерации.

Выход:

- строка пароля.

Критерии:

- длина результата ровно `length`;
- если `use_digits=True`, в пароле должна быть хотя бы одна цифра;
- если `use_symbols=True`, в пароле должен быть хотя бы один спецсимвол;
- если `length <= 0`, должна быть ошибка.

Пример:

```python
generate_password(length=16, use_digits=True, use_symbols=True, seed=1)
```

<<<<<<< HEAD
---

# Команда 3. Списки, даты, тарифы и профиль

## `generate_score(min_score=1, max_score=100, boundary=None, seed=None)`

Вход:

- `min_score` - нижняя граница балла.
- `max_score` - верхняя граница балла.
- `boundary` - режим граничного значения.
- `seed` - значение для повторяемой генерации.

Выход:

- целое число.

Критерии:

- обычный режим возвращает число от `min_score` до `max_score`;
- `boundary="min"` возвращает `min_score`;
- `boundary="max"` возвращает `max_score`;
- `boundary="below_min"` возвращает `min_score - 1`;
- `boundary="above_max"` возвращает `max_score + 1`;
- если `min_score > max_score`, должна быть ошибка.

Пример:

```python
generate_score(min_score=1, max_score=100, boundary="max")
```

## `generate_is_active(seed=None)`

Вход:

- `seed` - значение для повторяемой генерации.

Выход:

- `True` или `False`.

Критерии:

- результат должен быть булевым значением;
- при одинаковом `seed` результат должен повторяться.

Пример:

```python
generate_is_active(seed=1)
```

=======
>>>>>>> b9c35ad (ref: change structure)
## `generate_tags(count=None, unique=True, seed=None)`

Вход:

- `count` - сколько тегов нужно вернуть.
- `unique` - должны ли теги быть уникальными.
- `seed` - значение для повторяемой генерации.

Выход:

- список тегов.

Критерии:

- результат должен быть списком;
- если задан `count`, длина списка должна соответствовать `count`;
- если `unique=True`, теги не должны повторяться;
- все теги должны быть из списка `TAGS`;
- если `count < 0`, должна быть ошибка.

Пример:

```python
generate_tags(count=5, unique=True, seed=1)
```

<<<<<<< HEAD
## `generate_subscription_plan(allowed_plans=None, seed=None)`

Вход:

- `allowed_plans` - список разрешенных тарифов.
- `seed` - значение для повторяемой генерации.

Выход:

- строка с названием тарифа.

Критерии:

- если `allowed_plans` передан, тариф должен быть только из этого списка;
- если `allowed_plans` не передан, тариф берется из общего списка;
- если список тарифов пустой, должна быть ошибка.

Пример:

```python
generate_subscription_plan(allowed_plans=["free", "premium"], seed=1)
```

## `generate_registration_date(start_year=2020, end_year=2026, boundary=None, seed=None)`

Вход:

- `start_year` - нижняя граница года.
- `end_year` - верхняя граница года.
- `boundary` - режим граничного значения.
- `seed` - значение для повторяемой генерации.

Выход:

- строка даты в формате `YYYY-MM-DD`.

Критерии:

- обычный режим возвращает дату внутри диапазона;
- `boundary="min"` возвращает дату в начале диапазона;
- `boundary="max"` возвращает дату в конце диапазона;
- `boundary="below_min"` возвращает дату раньше диапазона;
- `boundary="above_max"` возвращает дату позже диапазона;
- если `start_year > end_year`, должна быть ошибка.

Пример:

```python
generate_registration_date(start_year=2020, end_year=2026, boundary="max")
```

=======
>>>>>>> b9c35ad (ref: change structure)
## `generate_user_profile(valid=True, seed=None)`

Вход:

- `valid` - нужен валидный или частично невалидный профиль.
- `seed` - значение для повторяемой генерации.

Выход:

- словарь профиля пользователя.

Критерии:

- профиль должен быть словарем;
- должен содержать `user_id`, `first_name`, `last_name`, `age`, `city`, `is_active`;
- должен содержать `username`, `email`, `password`, `tags`;
- должен содержать `registration_date`, `subscription_plan`;
- `user_id` должен быть строкой длиной 6;
- `username` должен быть строкой длиной 10;
- `password` должен быть строкой длиной 12;
- `tags` должен быть списком из 3 уникальных тегов;
- при `valid=True` email должен быть валидным;
- при `valid=False` email должен быть намеренно невалидным.

Пример:

```python
generate_user_profile(valid=False, seed=1)
```
