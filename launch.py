# Импортируем sys, чтобы Python мог искать генераторы в папке procedural_version/generators.
import sys

# Импортируем Path, чтобы работать с папкой test_data и файлами 001.txt, 002.txt.
from pathlib import Path

# Добавляем папку generators в список мест, где Python ищет файлы для import.
sys.path.append("procedural_version/generators")

# Импортируем функцию активности.
from active_example import active_example

# Импортируем функцию возраста.
from age import age

# Импортируем функцию года рождения.
from birth_year import birth_year

# Импортируем функцию города.
from city import city

# Импортируем функцию комментария.
from comment import comment

# Импортируем функцию generate_email.
from generate_email import generate_email

# Импортируем функцию имени.
from first_name import first_name

# Импортируем функцию полного имени.
from full_name import full_name

# Импортируем функцию фамилии.
from last_name import last_name

# Импортируем функцию пароля.
from password import password

# Импортируем функцию телефона.
from phone import phone

# Импортируем функцию плана подписки.
from plan_example import plan_example

# Импортируем функцию даты регистрации.
from reg_date_example import reg_date_example

# Импортируем функцию учебного балла.
from score_example import score_example

# Импортируем функцию тегов.
from tags import tags

# Импортируем функцию ID.
from user_id import user_id

# Импортируем функцию username.
from username import username

# Сюда программа будет складывать строки для текстового файла.
results = []


# Объявляем функцию, которая сохраняет один результат в общий список.
def save(function_name, value):
    # Добавляем имя функции и ее результат, чтобы в файле было понятно, откуда данные.
    results.append(f"{function_name}: {value}")


# Ниже идет ручная проверка функций.
# Ученик меняет только этот блок: вызывает готовые функции, печатает результат и сохраняет его.
# Это примеры уже готовых функций. Этот файл можно запустить и проверить какой файл сохраниться в директорию test_data.
# Для того, чтобы проверить, как генерируются и сохраняются данные реализованных функций, вместо функций примеров надо
# поставить свои и запустить файл.

# Вызываем example-функцию активности.
active_result = active_example(seed=1)
# Печатаем результат в терминал.
print(active_result)
# Сохраняем результат в будущий текстовый файл.
save("active_example", active_result)

# Вызываем example-функцию плана подписки.
plan_result = plan_example(seed=1)
# Печатаем результат в терминал.
print(plan_result)
# Сохраняем результат в будущий текстовый файл.
save("plan_example", plan_result)

# Вызываем example-функцию даты регистрации.
reg_date_result = reg_date_example(seed=1)
# Печатаем результат в терминал.
print(reg_date_result)
# Сохраняем результат в будущий текстовый файл.
save("reg_date_example", reg_date_result)

# Вызываем example-функцию учебного балла.
score_result = score_example(seed=1)
# Печатаем результат в терминал.
print(score_result)
# Сохраняем результат в будущий текстовый файл.
save("score_example", score_result)




# Ниже служебный код сохранения в файл, его обычно не нужно менять.

# Сохраняем путь к уже существующей папке test_data.
test_data_dir = Path("test_data")

# Находим все текстовые файлы внутри папки test_data.
txt_files = test_data_dir.glob("*.txt")

# Создаем список для номеров уже созданных файлов.
numbers = []

# Перебираем найденные текстовые файлы.
for txt_file in txt_files:
    # Берем имя файла без расширения .txt.
    file_name = txt_file.stem
    # Проверяем, что имя файла состоит только из цифр.
    if file_name.isdigit():
        # Добавляем номер файла в список.
        numbers.append(int(file_name))

# Проверяем, есть ли уже созданные файлы с номерами.
if numbers:
    # Берем следующий номер после самого большого найденного.
    next_number = max(numbers) + 1
# Если таких файлов еще нет, начинаем с первого.
else:
    # Первый файл будет называться 001.txt.
    next_number = 1

# Создаем имя файла в формате 001.txt, 002.txt, 003.txt.
new_file_name = f"{next_number:03d}.txt"

# Собираем путь к новому файлу внутри папки test_data.
new_file_path = test_data_dir / new_file_name

# Склеиваем сохраненные результаты в один текст.
file_text = "\n".join(results)

# Записываем текст в новый файл.
new_file_path.write_text(file_text, encoding="utf-8")

# Печатаем путь к созданному файлу.
print(f"Создан файл: {new_file_path}")
