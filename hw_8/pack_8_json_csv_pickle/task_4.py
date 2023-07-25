# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json
import hashlib

def process_csv_to_json(input_file, output_file):
    record = []
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
       # reader = next(reader)

        for i, (level, id_, name) in enumerate(reader):
            if i:
                record.append({'level': level,
                               'id': id_.zfill(10),
                               'name': name.capitalize(),
                               'hash': hash(id_ + name)})

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(record, json_file, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    process_csv_to_json('/home/serg/PycharmProjects/HW_python_sem/seminar_8_json/users_personal_data.csv',
    '/home/serg/PycharmProjects/HW_python_sem/seminar_8_json/new_users_personal_data.json')

