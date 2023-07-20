# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.


import csv
import json


def save_to_csv():
    file_path = '/home/serg/PycharmProjects/HW_python_sem/seminar_8_json/users_personal_data.json'
    csv_file_path = '/home/serg/PycharmProjects/HW_python_sem/seminar_8_json/users_personal_data.csv'

    # Чтение данных из JSON-файла сохранение данных в csv file
    with (
        open(file_path, 'r', encoding='utf-8') as json_file,
        open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file
    ):
        data = json.load(json_file)
        fieldnames = ['Level', 'ID', 'Name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()  # Запись заголовков столбцов

        for level, users in data.items():
            for id_, name in users.items():
                writer.writerow({'Level': level, 'ID': id_, 'Name': name})

    print(f"Данные успешно сохранены в файле: {csv_file_path}")

if __name__ == '__main__':
    save_to_csv()

