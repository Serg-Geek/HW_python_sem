# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import math
import random
import json
from functools import wraps

# Нахождение корней квадратного уравнения
def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2

# Генерация csv файла с тремя случайными числами в каждой строке (100-1000 строк)
def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            numbers = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(numbers)

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла
def solve_quadratic_equation_from_csv(func):
    @wraps(func)
    def wrapper(file_name):
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                numbers = list(map(int, row))
                result = func(*numbers)
                print(f"For numbers {numbers}, quadratic equation roots: {result}")
    return wrapper

# Декоратор, сохраняющий переданные параметры из csv файла в функцию нахождения корней квадратного уравнения
# и результаты работы функции в json файл
def save_to_json(func):
    func_name = func.__name__

    def decorator(file_name):
        result_list = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                numbers = list(map(int, row))
                result = func(*numbers)
                result_dict = {
                    'args': numbers,
                    'result': result
                }
                result_list.append(result_dict)

        with open(f'{func_name}.json', 'w') as json_file:
            json.dump(result_list, json_file, indent=4)

    return decorator




# Создаем CSV файл с тремя случайными числами в каждой строке (например, 'data.csv')
generate_csv_file('data.csv', 500)

# Нахождение корней квадратного уравнения
roots = solve_quadratic_equation(1, -3, 2)
print(f"Корни квадратного уравнения: {roots}")

# Декорируем функцию solve_quadratic_equation с декоратором solve_quadratic_equation_from_csv
@solve_quadratic_equation_from_csv
def solve_quadratic_equation_csv(a, b, c):
    return solve_quadratic_equation(a, b, c)

# Вызываем декорированную функцию, которая будет применяться к каждой тройке чисел из CSV файла
solve_quadratic_equation_csv('data.csv')

# Декорируем функцию solve_quadratic_equation с декоратором save_to_json
@save_to_json
def solve_quadratic_equation_with_json(a, b, c):
    return solve_quadratic_equation(a, b, c)

solve_quadratic_equation_with_json('data.csv')

