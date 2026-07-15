# Как ученикам пользоваться тестами

## Зачем нужны тесты

Тесты помогают проверить, что генераторы создают данные по правилам.

В этом проекте тесты проверяют:

- точную длину строк;
- граничные значения;
- значения за границами;
- валидные и невалидные форматы;
- состав словарей;
- размер списков;
- совпадение процедурной и ООП-версии.

---

# Как запустить все тесты

Тесты нужно запускать по этапам.

Сначала ученики реализуют процедурную версию и проверяют только ее.

## Процедурная версия

```bash
python -m unittest discover -s procedural_version/tests
```

Если процедурные тесты прошли успешно, можно переходить к ООП-версии.

## ООП-версия

```bash
python -m unittest discover -s oop_version/tests
```

Эти тесты проверяют, что методы ООП-версии дают такие же результаты, как процедурные функции.

Поэтому порядок важен:

1. Сначала процедурная версия.
2. Потом тесты процедурной версии.
3. Потом ООП-версия.
4. Потом тесты ООП-версии.
5. Потом сравнение поведения двух версий.

---

# Примеры отдельных тестов

## Проверка ID точной длины

```bash
python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_user_id_returns_digits_with_exact_length
```

## Проверка возраста на границах

```bash
python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_age_returns_boundary_values
```

## Проверка комментария точной длины

```bash
python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_comment_returns_exact_length
```

## Проверка валидного и невалидного email

```bash
python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_email_can_return_valid_and_invalid_values
```

## Проверка пароля

```bash
python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_password_respects_required_parts
```

## Проверка тегов

```bash
python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_tags_respects_count_and_unique
```

## Проверка профиля

```bash
python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_user_profile_returns_rich_dictionary
```

## Проверка совпадения ООП и процедурной версии

```bash
python -m unittest oop_version.tests.test_generators.OopGeneratorsTest.test_generate_user_profile_matches_procedural_version
```

---

# Что делать, если тесты упали

Ошибка теста — это подсказка.

Нужно посмотреть:

- какой тест упал;
- какую функцию или метод он проверял;
- какое значение ожидалось;
- какое значение получилось.

После исправления кода тесты нужно запустить снова.

Главное правило: менять нужно реализацию генератора, а не смысл теста.
