# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


def create_argument_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            argument_dict[value] = key
        except TypeError:
            argument_dict[str(value)] = key
    return argument_dict


result = create_argument_dict(arg1=1, arg2=["value2",3 ,5 ], arg3="value3")
print(result)
