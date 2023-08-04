# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
import os
from functools import wraps


def save_to_json(func):
    func_name = func.__name__
    if os.path.exists(f'./{func_name}.json'):
        with open(f'./{func_name}.json',  'r', encoding='utf-8') as j:
            result_list = json.load(j)
    else:
        result_list = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        result = {
            'args': args,
            'kwargs': kwargs,
            'result' : func_result
        }
        result_list.append(result)
        with open(f'./{func_name}.json', 'w', encoding='utf-8') as j:
            json.dump(result_list, j, ensure_ascii=False, indent=4)
        return func_result
    return wrapper

# @save_to_json
# def add(a, b):
#     return a + b

# if __name__ == '__main__':
#     print(add(1, 2))
#     print(add(2, 3))
#     print(add(3, 4))
#     print(add(4, 5))
