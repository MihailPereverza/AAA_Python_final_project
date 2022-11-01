import random
from string import Template


def log(pattern: str):
    """:param pattern: str containing "$time" (will be replace on worktime)"""

    def decor(func):
        template = Template(pattern)

        def wrapper(*args, **kwargs):
            time_start = random.randint(0, 15)  # имитация засечения времени
            func(*args, **kwargs)
            total_time = random.randint(16, 25) - time_start  # тип посчитали
            print(template.substitute({'time': total_time}))

        return wrapper

    return decor
