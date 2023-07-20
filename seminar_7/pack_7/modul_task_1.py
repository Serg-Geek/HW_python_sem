#  Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


START, END = -1000, 1000


def input_file(file_name, lines_num):
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(lines_num):
            f.write(f'{randint(START,END)}|{uniform(START,END)} \n')
