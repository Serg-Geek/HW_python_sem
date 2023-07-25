# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.   /home/serg/PycharmProjects/HW_python_sem/seminar_7/res_file.txt
import json


def get_json_file():
    with (
        open('/home/serg/PycharmProjects/HW_python_sem/seminar_7/res_file.txt', 'r', encoding='utf-8') as f1,
        open('new_res.json', 'w', encoding='utf-8') as f2,
    ):
        my_dict = {}
        for line in f1:
            key, value = line.strip().split('|')
            key = key.capitalize()
            my_dict[key] = value
        json.dump(my_dict, f2, ensure_ascii=False,indent=2)
        print(my_dict)


get_json_file()
