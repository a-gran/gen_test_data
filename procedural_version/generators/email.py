from procedural_version.data.names_data import EMAIL_DOMAINS
# Импортируем слова, из которых можно начать имя почтового ящика.
from procedural_version.data.names_data import USERNAME_WORDS
# Импортируем функцию, которая создает random с нужным seed.
from procedural_version.utils.random_utils import create_random

# Объявляем функцию, которая должна вернуть email.
def email(valid=True, username_length=8, seed=None):

    if username_length <= 0:
        raise ValueError("username_length must be greater than 0")

    rnd = create_random(seed)
    raw_words = "".join(rnd.choices(USERNAME_WORDS, k=int(username_length) + 5))
    username = raw_words[:username_length]
    domain = rnd.choice(EMAIL_DOMAINS)

    if valid:
        return f"{username}@{domain}"
    else:
        return f"{username}{domain}"














    # Версия от Ноама
    '''
    def email(valid=True, username_length=8, seed=None):
    if username_length <= 0:
        return "username_length must be greater than 0"

    if username_length > 8:
        return "username_length must be 8"

    if seed is not None:
        random = create_random(seed)
        return random

    if valid:
        username = "".join(random.choices(USERNAME_WORDS, int(username_length)))
        domain = random.choice(EMAIL_DOMAINS)
        return f"{username}@{domain}"

    if not valid:
        username = "".join(random.choices(USERNAME_WORDS, int(username_length)))
        domain = random.choice(EMAIL_DOMAINS)
        return f"{username}{domain}"
    '''
>>>>>>> 387e21d (ref: change structure)
