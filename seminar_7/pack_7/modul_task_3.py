# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
from typing import TextIO


def read_by_line(file: TextIO):
    test = file.readline()
    if not test:
        file.seek(0)
        test = file.readline()

    return test[:-1]


def open_unit_file(file_1, file_2, res_file, ):
    with(
        open(res_file, 'w', encoding='utf-8') as rf,
        open(file_1, 'r', encoding='utf-8') as f1,
        open(file_2, 'r', encoding='utf-8') as f2
    ):
        lst_prod = [int(line.split('|')[0]) * float(line.split('|')[1]) for line in f1]

        for res_num, line_2 in zip(lst_prod, f2):
            if res_num < 0:
                rf.write(f'{line_2.lower().strip()}|{abs(res_num)} \n')
            else:
                rf.write(f'{(line_2.upper().strip())}|{int(res_num)} \n')
