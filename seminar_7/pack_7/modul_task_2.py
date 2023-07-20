# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
# import random
#
#
# def gen_name(file_name, lines_num):
#     sing_a = 'aeyuoi'
#     sing_b = 'qwrtpsdfghjklzxcvbnm'
#     rnd = [sing_a, sing_b]
#     with open(file_name, 'a', encoding='utf-8') as f:
#         for _ in range(lines_num):
#                 name_len= random.randint(4, 7)
#                 name = random.choice(sing_a, k=name_len)
#
#                 f.write(name)
import random

def gen_name(file_name, lines_num):
    sing_a = 'аеёиоуыэюя'
    sing_b = 'аеёиоуыэюябвгджзйклмнпрстфхцчшщъь'
    rnd = [sing_a, sing_b]
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(lines_num):
            has_sing_a = False # флаг для проверки
            while not has_sing_a:
                name_len = random.randint(4, 7)
                name = ''.join(random.choices(random.choice(rnd), k=name_len))
                has_sing_a = any(char in sing_a for char in name)
            f.write(name.capitalize() + '\n')

