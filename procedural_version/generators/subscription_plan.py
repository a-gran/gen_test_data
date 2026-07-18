# Подсказка ученику: SUBSCRIPTION_PLANS хранит общий список тарифов, если свой список не передали.
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Подсказка ученику: create_random(seed) нужен для повторяемого выбора тарифа в тестах.
from procedural_version.utils.random_utils import create_random

# Задание: реализуй генератор тарифа и проверь, что он выбирает только разрешенные значения.
def generate_subscription_plan(allowed_plans=None, seed=None):
    # Шаг 1. Создай генератор случайности через create_random(seed).
    randomizer = create_random(seed)
    # Шаг 2. Если allowed_plans передан, выбирай тариф только из него.
    # Шаг 3. Если allowed_plans не передан, используй общий список SUBSCRIPTION_PLANS.
    plans = allowed_plans if allowed_plans is not None else SUBSCRIPTION_PLANS
    # Шаг 4. Проверь, что список тарифов не пустой.
    if not plans:
        # Проверка тестом: при пустом списке функция должна выбросить ValueError.
        raise ValueError("Список тарифов не должен быть пустым")
    # Шаг 5. Верни случайный тариф из выбранного списка.
    # Проверка тестом: результат должен входить в allowed_plans или SUBSCRIPTION_PLANS.
    # Проверка после реализации: запусти python -m unittest procedural_version.tests.test_generators.ProceduralGeneratorsTest.test_generate_subscription_plan_respects_allowed_plans
    # Если все хорошо, в конце вывода unittest будет написано OK.
    # Если тест упал, проверь, что функция выбирает тариф только из переданного allowed_plans.
    return randomizer.choice(plans)
