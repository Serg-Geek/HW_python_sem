variable1s = " 1"
variable2s = "2"
variable3s = 3
variable4 = ["4", 5, 6,]
variable5s = 7.0

def replace_variables():
    variables = list(globals().items())
    for name, value in variables:
        if name.endswith("s") and len(name) > 1:
            # Создание нового имени переменной без "s" на конце
            new_name = name[:-1]
            # Замена содержимого переменной на None
            globals()[name] = None
            # Создание новой переменной с сохраненным значением
            globals()[new_name] = value


replace_variables()

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)
print(variable1s)
print(variable2s)
print(variable3s)
print(variable5s)
