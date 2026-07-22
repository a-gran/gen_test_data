# Как использовать генераторы тестовых данных

## Что это за проект

Этот проект помогает быстро создавать тестовые данные.

Тестовые данные - это ненастоящие данные, которые нужны для проверки программы.

Например, программа просит заполнить анкету пользователя:

- имя;
- фамилию;
- email;
- пароль;
- город;
- возраст.

Чтобы не придумывать эти данные руками каждый раз, можно использовать готовые функции.

## Простой пример

Допустим, нам нужен email для теста.

Создай файл `manual_check.py` в корне проекта.

Корень проекта - это папка, где лежит файл `check.py`.

Напиши в файл:

```python
from procedural_version.generators import email

test_email = email(valid=True, username_length=8, seed=1)

print(test_email)
```

Запусти:

```bash
python manual_check.py
```

Если на Windows команда `python` не работает, попробуй:

```bash
py manual_check.py
```

## Что происходит в примере

```python
from procedural_version.generators import email
```

Эта строка берет функцию `email` из проекта.

```python
test_email = email(valid=True, username_length=8, seed=1)
```

Эта строка создает email.

```python
print(test_email)
```

Эта строка показывает email на экране.

## Где это может пригодиться в реальной работе

Представь, что тестировщик проверяет сайт.

На сайте есть форма регистрации:

```text
Имя:
Email:
Пароль:
Город:
```

Тестировщику нужно много раз вводить разные данные.

Вместо того чтобы каждый раз писать данные руками, можно создать их кодом.

Пример:

```python
from procedural_version.generators import email
from procedural_version.generators import plan_example
from procedural_version.generators import reg_date_example

user = {
    "email": email(valid=True, username_length=8, seed=1),
    "plan": plan_example(seed=1),
    "registration_date": reg_date_example(seed=1),
}

print(user)
```

Так получается словарь с тестовым пользователем.

Его можно использовать для проверки сайта, формы или API.

## Правильные и неправильные данные

Программа должна уметь принимать правильные данные и не принимать неправильные.

Например, правильный email содержит знак `@`.

```python
from procedural_version.generators import email

good_email = email(valid=True, username_length=8, seed=1)

print(good_email)
```

А неправильный email можно создать так:

```python
from procedural_version.generators import email

bad_email = email(valid=False, username_length=8, seed=1)

print(bad_email)
```

Так можно проверить, что сайт показывает ошибку, если email неправильный.

## Что такое seed

`seed` - это число, которое помогает получать одинаковый случайный результат.

Пример:

```python
from procedural_version.generators import email

first_email = email(seed=1)
second_email = email(seed=1)

print(first_email)
print(second_email)
```

Если `seed` одинаковый, email тоже будет одинаковый.

Это удобно в тестах, потому что тест не должен каждый раз получать совсем другие данные.

## Пример: создать несколько пользователей

Иногда нужно проверить не одного пользователя, а сразу несколько.

```python
from procedural_version.generators import email
from procedural_version.generators import plan_example

users = []

for number in range(1, 4):
    user = {
        "email": email(seed=number),
        "plan": plan_example(seed=number),
    }

    users.append(user)

print(users)
```

Этот код создаст список из трех пользователей.

Так можно проверять таблицу пользователей или список клиентов.

## Пример: проверка граничных значений

Граница - это самое маленькое или самое большое разрешенное значение.

Например, балл может быть от 1 до 100.

```python
from procedural_version.generators import score_example

print(score_example(min_score=1, max_score=100, boundary="min"))
print(score_example(min_score=1, max_score=100, boundary="max"))
print(score_example(min_score=1, max_score=100, boundary="below_min"))
print(score_example(min_score=1, max_score=100, boundary="above_max"))
```

Этот код проверяет:

- минимальное значение;
- максимальное значение;
- значение меньше минимума;
- значение больше максимума.

Так тестировщики ищут ошибки в программах.

## Какие функции есть в проекте

Готовые функции-примеры:

- `active_example()` - активен пользователь или нет;
- `score_example()` - учебный балл;
- `plan_example()` - тариф пользователя;
- `reg_date_example()` - дата регистрации.

Функция `email()` тоже уже реализована.

Остальные функции пока оставлены для самостоятельной работы. Внутри них стоит `pass`.

`pass` значит: здесь пока пусто, ученик должен написать код сам.

## Как запускать проверки

Проверить email:

```bash
python check.py email
```

Проверить готовый пример с баллами:

```bash
python check.py score_example
```

Проверить готовый пример с датой:

```bash
python check.py reg_date_example
```

Проверить все функции:

```bash
python check.py all
```

Если функция еще не написана и внутри стоит `pass`, тесты будут падать. Это нормально.

## Важно

Перед каждым запуском `check.py` проект очищает кэш Python.

Это нужно, чтобы тесты проверяли новый код, который ученик только что написал.
