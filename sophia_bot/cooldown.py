# cooldown.py sets a cooldown time to not respond all the time just one user.

import time

cooldown_dict = {}

def has_cooldown(user_id, cooldown_time):
    current_time = time.time()
    last_response_time = cooldown_dict.get(user_id, 0)

    if current_time - last_response_time >= cooldown_time:
        cooldown_dict[user_id] = current_time
        return False

    return True
