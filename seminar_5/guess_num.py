# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.


from random import randint


def digit_check():
    while True:
        try:
            num_int = int(input('Введите число от 0 до 1000: \n'))
            return num_int
        except ValueError:
            print('Введите число от 0 до 1000:\n')
            continue


LOWER_LIMIT = 0
UPPER_LIMIT = 1001
QUANTITY = 10
count = 0


def guess_num(lower_lim, upper_lim, quantity):
    num = randint(lower_lim, upper_lim)
    count = 0
    while count < quantity:
        num_player = digit_check()
        count += 1
        print("Попытка № ", count)
        if num == num_player:
            return True

        if num > num_player:
            print("больше")
        if num < num_player:
            print("меньше")
        if count == 10:
            return False
