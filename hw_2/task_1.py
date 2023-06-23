# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.



def input_int():
    num = None
    while True:
        num = input(" Введите целое число: ")
        if num.isdigit() == True:
            break
    return int(num)    
   
    
def hex_number(num):
    result = ''
    while num > 0:
        tmp = num % 16 
        if tmp == 10:
            result = 'a' + result
        elif tmp == 11:
            result = 'b' + result
        elif tmp == 12:
            result = 'c' + result
        elif tmp == 13:
            result = 'd' + result
        elif tmp == 14:
            result = 'e' + result
        elif tmp == 15:
            result = 'f' + result
        else:
            result = str(num % 16) + result
        num = num // 16
    return result

dec_number = input_int()
print (f'число "{dec_number}" в шестьнадцатеричной системе счисления -->>  {hex_number(dec_number)}') 
print (f'Проверка с помощью функции Hex({dec_number})  -->> {hex(dec_number)}')  
   
