# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
MIN_LIMIT = 0
MAX_LIMIT = 100_000


def digit_check():
    while True:
        try:
            num_int = int(input('Введите число от 1 до 100 000: \n')) 
            if  num_int > MIN_LIMIT and num_int < MAX_LIMIT:
                return num_int
        except ValueError:
            print('Введите число от 1 до 100_000:\n')
            continue

def simple_num(num):
    count = 0
    for i in range(2, num ):
        if num % i == 0:
            count +=1
    if count > 2:
        return False
    else:
        return True


res = (simple_num(digit_check()))
if res == True:
    print ("Число простое")
else:
    print("число составное")