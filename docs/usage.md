# Инструкция по использованию библиотеки

## Общая идея

Проект содержит две версии одной библиотеки генерации тестовых данных:

1. `procedural_version` — процедурная версия.
2. `oop_version` — объектно-ориентированная версия.

Библиотека нужна не только для случайного выбора данных.

Она помогает создавать тестовые данные под конкретные проверки:

- строки точной длины;
- числа на границах диапазона;
- числа за границами диапазона;
- валидные форматы;
- невалидные форматы;
- списки нужного размера;
- сложные профили пользователей.

---

# Процедурная версия

## Числа и границы

```python
from procedural_version.generators.age import generate_age

print(generate_age(min_age=18, max_age=80, boundary="min"))
print(generate_age(min_age=18, max_age=80, boundary="max"))
print(generate_age(min_age=18, max_age=80, boundary="above_max"))
```

```python
from procedural_version.generators.score import generate_score

print(generate_score(min_score=1, max_score=100, boundary="below_min"))
```

## Строки точной длины

```python
from procedural_version.generators.comment import generate_comment

comment = generate_comment(length=255, seed=1)
print(len(comment))
```

```python
from procedural_version.generators.username import generate_username

username = generate_username(length=12, seed=1)
print(username)
print(len(username))
```

## Валидные и невалидные форматы

```python
from procedural_version.generators.email import generate_email

print(generate_email(valid=True, username_length=8, seed=1))
print(generate_email(valid=False, username_length=8, seed=1))
```

```python
from procedural_version.generators.phone import generate_phone

print(generate_phone(valid=True, seed=1))
print(generate_phone(valid=False, seed=1))
```

## Пароль с требованиями

```python
from procedural_version.generators.password import generate_password

password = generate_password(length=16, use_digits=True, use_symbols=True, seed=1)
print(password)
print(len(password))
```

## Списки и профиль

```python
from procedural_version.generators.tags import generate_tags

tags = generate_tags(count=5, unique=True, seed=1)
print(tags)
```

```python
from procedural_version.generators.user_profile import generate_user_profile

print(generate_user_profile(valid=True, seed=1))
print(generate_user_profile(valid=False, seed=1))
```

---

# ООП-версия

## Числа и границы

```python
from oop_version.generators.person_generator import PersonGenerator

person_generator = PersonGenerator(seed=1)
print(person_generator.generate_age(min_age=18, max_age=80, boundary="min"))
```

```python
from oop_version.generators.person_generator import PersonGenerator

person_generator = PersonGenerator(seed=1)
print(person_generator.generate_score(min_score=1, max_score=100, boundary="max"))
```

## Строки точной длины

```python
from oop_version.generators.text_generator import TextGenerator

text_generator = TextGenerator(seed=1)
comment = text_generator.generate_comment(length=255)
print(len(comment))
```

```python
from oop_version.generators.person_generator import PersonGenerator

person_generator = PersonGenerator(seed=1)
username = person_generator.generate_username(length=12)
print(username)
print(len(username))
```

## Валидные и невалидные форматы

```python
from oop_version.generators.contact_generator import ContactGenerator

contact_generator = ContactGenerator(seed=1)
print(contact_generator.generate_email(valid=True, username_length=8))
print(contact_generator.generate_email(valid=False, username_length=8))
```

## Сложный профиль

```python
from oop_version.generators.profile_generator import ProfileGenerator

profile_generator = ProfileGenerator(seed=1)
print(profile_generator.generate_user_profile(valid=True))
print(profile_generator.generate_user_profile(valid=False))
```

---

# Как запустить тесты

```bash
python -m unittest discover -s procedural_version/tests
python -m unittest discover -s oop_version/tests
```

Если тесты завершились со статусом `OK`, значит проверяемая часть работает правильно.
