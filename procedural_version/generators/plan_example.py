# Файл нужен для функции plan_example.
# Функция plan_example показывает готовый пример выбора плана подписки.
# В тестировании ПО такую функцию можно использовать, чтобы проверять разные тарифы и права пользователей.

# Импортируем общий список планов подписки.
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем готовый пример функции плана подписки.
def plan_example(allowed_plans=None, seed=None):
    # Что делает функция: выбирает один план подписки.
    # План подписки - это вариант аккаунта пользователя.
    # Примеры планов подписки: "free", "basic", "premium".
    # allowed_plans=None значит выбрать из общего списка SUBSCRIPTION_PLANS.
    # allowed_plans=["free", "premium"] значит выбрать только "free" или "premium".
    # allowed_plans=[] значит выбирать не из чего, поэтому нужна ошибка ValueError.
    # seed - число для random: с одним и тем же seed random выбирает один и тот же план.
    # Как вызвать функцию в своем коде:
    # 1. Создай файл для проверки в корне проекта, рядом с check.py.
    # 2. Например, создай файл try_generators.py.
    # 3. В одном таком файле можно проверять сразу много функций.
    # 4. В файле try_generators.py можно написать такой код:
    # """
    # from procedural_version.generators.plan_example import plan_example
    # from procedural_version.generators.age import age
    #
    # plan_result = plan_example(allowed_plans=["free", "premium"], seed=1)
    # print(plan_result)
    #
    # age_result = age(seed=1)
    # print(age_result)
    # """
    # 5. Открой терминал в корне проекта, где лежат check.py и try_generators.py.
    # 6. Запусти файл командой: python try_generators.py
    # Вызов без параметров: result = plan_example()
    # Вызов с разрешенными планами: result = plan_example(allowed_plans=["free", "premium"])
    # Вызов с seed: result = plan_example(allowed_plans=["free"], seed=1)
    # Пример результата: функция должна вернуть один план подписки.
    # Документация: docs/function_specifications.md, раздел plan.
    # Шаги реализации:
    # 1. Создать random через create_random(seed).
    # 2. Если allowed_plans передан, использовать его как список планов.
    # 3. Если allowed_plans не передан, использовать общий список SUBSCRIPTION_PLANS.
    # 4. Проверить, что выбранный список планов не пустой.
    # 5. Вернуть случайный план из выбранного списка.
    # Проверка с помощью автотестов:
    # Открой терминал в папке проекта, где лежит файл check.py.
    # Затем запусти: python check.py plan_example
    # Если в конце написано OK, этот тест прошел.
    # Что вернуть: строку с одним планом подписки.
    # Проверка тестами: python check.py plan_example
    # Создаем random с переданным seed.
    randomizer = create_random(seed)
    # Выбираем список: переданный allowed_plans или общий SUBSCRIPTION_PLANS.
    plans = allowed_plans if allowed_plans is not None else SUBSCRIPTION_PLANS
    # Проверяем, что список планов не пустой.
    if not plans:
        # Сообщаем ошибку, если выбирать не из чего.
        raise ValueError("Список планов подписки не должен быть пустым")
    # Возвращаем случайный план из выбранного списка.
    return randomizer.choice(plans)
