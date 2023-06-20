# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 

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
num = randint(LOWER_LIMIT, UPPER_LIMIT)


while count < QUANTITY:
    num_player = digit_check()
    count += 1
    print("Попытка № ", count)
    if num == num_player:
        print ("Вы выиграли")
        break
    if num > num_player:
        print ("больше")
    if num < num_player:
        print ("меньше")
    if count == 10:
        print (f"Вы проиграли, загаданное число", num)
