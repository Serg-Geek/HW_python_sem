# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def traverse_directory(directory, json_file_path, csv_file_path, pickle_file_path):
    """
     Рекурсивно обходит директорию и все вложенные директории и сохраняет результаты обхода
     в файлы формата JSON, CSV и pickle.
    :param directory: путь к директории
    :param json_file_path: путь к JSON файлу
    :param csv_file_path: путь к CSV файлу
    :param pickle_file_path: путь к pickle файлу
    """

    if not os.path.exists(directory):
        raise ValueError('Директории не существует')
    elif not os.path.isdir(directory):
        raise ValueError('Директория не является директорией')

    result = []

    for root, dirs, files in os.walk(directory):
        total_size = sum(os.stat(os.path.join(root, file)).st_size for file in files)
        relativ_path = os.path.relpath(root, directory)
        result.append({
            'path': relativ_path,
            'types': 'directory',
            'size': total_size,
        })

        for file in files:
            file_path = os.path.join(directory,root , file)
            file_size = os.stat(file_path).st_size

            result.append({
                'path': os.path.join(relativ_path, file),
                'types': 'file',
                'size': file_size,
            })

    with(
        open(json_file_path, 'w', encoding='utf-8') as jf,
        open(csv_file_path, 'w', newline='', encoding='utf-8') as cf,
        open(pickle_file_path, 'wb') as pf,
    ):
        json.dump(result, jf, ensure_ascii=False, indent=4)
        csv_writer = csv.writer(cf)
        csv_writer.writerows(result)
        pickle.dump(result, pf)



if __name__ == '__main__':
    directory = '/home/serg/PycharmProjects/HW_python_sem'
    json_file_path = '/home/serg/PycharmProjects/HW_python_sem/hw_8/files_hw/jf_task_3.json'
    csv_file_path = '/home/serg/PycharmProjects/HW_python_sem/hw_8/files_hw/csv_task_3.csv'
    pickle_file_path = '/home/serg/PycharmProjects/HW_python_sem/hw_8/files_hw/pickle_task_3.pickle'

    traverse_directory(directory, json_file_path, csv_file_path, pickle_file_path)



