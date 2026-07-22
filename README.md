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

Проверить одну функцию:

```bash
python check.py email
```

Проверить все функции процедурной версии:

```bash
python check.py all
```

Проверить готовые примеры:

```bash
python check.py active_example
python check.py score_example
python check.py plan_example
python check.py reg_date_example
```

## Важно про кэш

Перед каждым запуском `check.py` очищает Python-кэш проекта, чтобы тесты проверяли свежий код из файлов.

## Где смотреть задания

Подробные требования к функциям находятся в:

```text
docs/function_specifications.md
docs/testing_for_students.md
```
