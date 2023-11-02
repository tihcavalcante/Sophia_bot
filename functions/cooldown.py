# cooldown.py define um tempo de espera para nao responder o tempo todo apenas um usuario.

import time

# Dicionário para armazenar o último horário de resposta para cada usuário
cooldown_dict = {}


def has_cooldown(user_id, cooldown_time):
    current_time = time.time()
    last_response_time = cooldown_dict.get(user_id, 0)

    if current_time - last_response_time >= cooldown_time:
        cooldown_dict[user_id] = current_time
        return False

    return True
