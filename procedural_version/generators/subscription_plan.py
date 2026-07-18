# Импортируем список тарифов для генерации тарифа пользователя.
from procedural_version.data.names_data import SUBSCRIPTION_PLANS
# Импортируем функцию создания генератора случайности.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая генерирует тариф пользователя.
def generate_subscription_plan(allowed_plans=None, seed=None):
    # Создаем генератор случайности для выбора тарифа.
    randomizer = create_random(seed)
    # Используем переданный список тарифов или общий учебный список.
    plans = allowed_plans if allowed_plans is not None else SUBSCRIPTION_PLANS
    # Проверяем, что список тарифов не пустой.
    if not plans:
        # Сообщаем понятную ошибку, если выбирать не из чего.
        raise ValueError("Список тарифов не должен быть пустым")
    # Возвращаем случайный тариф из выбранного списка тарифов.
    return randomizer.choice(plans)
