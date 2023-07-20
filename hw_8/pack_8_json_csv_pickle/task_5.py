# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import os
import pickle
from pathlib import Path


def find_json_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_file_path = os.path.join(root, file)
                with open(json_file_path, 'r', encoding='utf-8') as json_file:
                    data = json.loads(json_file.read())

                pickle_file_path = os.path.join(directory, f'{file}.pickle')
                with open(pickle_file_path, 'wb') as pickle_file:
                    pickle.dump(data, pickle_file)


if __name__ == '__main__':
    find_json_files(Path().cwd())
