# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import math
from fractions import Fraction

def input_str():
    print()
    s = input( 'Введите строки вида “a/b” - дробь с числителем и знаменателем   ')
    return s
def get_numerator_and_denominator(num: str):
    num_lst = num.split('/')
    numerator = int(num_lst[0])
    denominator = int(num_lst[1])
    return numerator, denominator

def sum_fraction(numerator_1, denominator_1,numerator_2, denominator_2):
    greatest_common_diviser = math.gcd(denominator_1, denominator_2)
    least_common_diviser = (denominator_1 * denominator_2) // greatest_common_diviser
        # Приводим обе дроби к общему знаменателю
    numerator_1 *= least_common_diviser // denominator_1
    numerator_2 *= least_common_diviser // denominator_2

    sum_numerator = numerator_1  + numerator_2 
        # Упрощаем полученную дробь
    greatest_common_diviser = math.gcd(sum_numerator, least_common_diviser)
    sum_numerator //= greatest_common_diviser
    least_common_diviser //= greatest_common_diviser
    return sum_numerator, least_common_diviser
       
def mult_fraction(numerator_1, denominator_1,numerator_2, denominator_2):
    numerator = numerator_1 * numerator_2
    denominator = denominator_1 *denominator_2
    greatest_common_diviser = math.gcd(numerator, denominator)
    numerator //= greatest_common_diviser
    denominator //= greatest_common_diviser
    return numerator, denominator

numerator_1, denominator_1 =  (get_numerator_and_denominator(input_str()))
numerator_2, denominator_2 =  (get_numerator_and_denominator(input_str()))
sum = sum_fraction (numerator_1, denominator_1,numerator_2, denominator_2)
mult = mult_fraction(numerator_1, denominator_1,numerator_2, denominator_2)

print(f'Сумма {numerator_1}/{denominator_1} + {numerator_2}/{denominator_2} = {sum[0]}/{sum[1]}')
print(f'Произведение {numerator_1}/{denominator_1} + {numerator_2}/{denominator_2} = {mult[0]}/{mult[1]}')
print(f'проверкa с помощью модуля fractions: Сумма = {Fraction(numerator_1,denominator_1)\
                                                       + Fraction(numerator_2,denominator_2)}')
print(f'проверкa с помощью модуля fractions: произведение = {Fraction(numerator_1,denominator_1) \
                                                             * Fraction(numerator_2,denominator_2)}')
