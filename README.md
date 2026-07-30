# gen_test_data

Учебный проект для практики написания функций-генераторов тестовых данных на Python.

## Структура проекта

- `procedural_version/` - процедурная версия генераторов.
- `procedural_version/generators/` - файлы с учебными функциями.
- `procedural_version/tests/` - автоматические тесты.
- `docs/` - документация и инструкции.
- `check.py` - удобный запускатель тестов по короткому имени.

## Запуск проверок

Запускать команды нужно из корня проекта, где лежит файл `check.py`.

Если команда `python` не запускается, попробуйте использовать команду `py`.

Проверить одну функцию:

```bash
python check.py generate_email
py check.py generate_email
```

Проверить все функции процедурной версии:

```bash
python check.py all
py check.py all
```

Проверить готовые примеры:

```bash
python check.py active_example
python check.py score_example
python check.py plan_example
python check.py reg_date_example
py check.py active_example
py check.py score_example
py check.py plan_example
py check.py reg_date_example
```

## Генерация тестовых данных

Для ручной генерации тестовых данных используйте файл `launch.py`.

Запускать команду нужно из корня проекта:

```bash
python launch.py
py launch.py
```

Файл `launch.py` вызывает функции-генераторы, печатает результаты в терминал и сохраняет их в новый текстовый файл внутри папки `test_data`.

По умолчанию в `launch.py` уже есть примеры:

```text
active_example
plan_example
reg_date_example
score_example
```

Чтобы сохранить результаты своих функций, замените вызовы example-функций в учебном блоке `launch.py` на нужные генераторы и добавьте каждый результат через функцию `save`.

Например:

```python
email_result = generate_email(seed=1)
print(email_result)
save("generate_email", email_result)
```

При каждом запуске создается новый файл с очередным номером: `001.txt`, `002.txt`, `003.txt` и так далее. Файл сохраняется в папку `test_data`.

## Где смотреть задания

Подробные требования к функциям находятся в:

```text
docs/function_specifications.md
docs/testing_for_students.md
```
