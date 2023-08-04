# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# # из диапазонов.
from functools import wraps
from random import randint


def number_range_check_decor(func):
    @wraps(func)
    def wrapper(*args):
        secret_number, tries = args

        if secret_number < 1 or secret_number > 100:
            secret_number = randint(1, 100)
        if not 0 < tries < 11:
            tries = randint(1, 10)

        result = func(secret_number, tries)
        return result

    return wrapper

@number_range_check_decor
def guess(secret_number, tries):

    # global guess
    count = 0
    while count < tries:
        count += 1
        guess = int(input('Введите число: '))
        if guess == secret_number:
            print(f'Вы угадали число {secret_number} за {count} попыток')
            break
        elif guess > secret_number:
            print(f'Число {guess} больше загаданного числа ')
        elif guess < secret_number:
            print(f'Число {guess} меньше загаданного числа ')
        if count == tries:
            print(f'Вы не угадали число {secret_number} за {count} попыток')
    return guess




if __name__ == '__main__':
    number = int(input('Введите число от 1 до 100: '))
    tries = int(input('Введите количество попыток: '))

    guess(number, tries)
