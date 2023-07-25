# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
from functools import wraps



def count(num: int = 1):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(num):
                result.append(func(*args, **kwargs))
            return result
        return wrapper

    return decorator
