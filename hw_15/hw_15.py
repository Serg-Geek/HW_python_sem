# Урок 15. Обзор стандартной библиотеки Python
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import os
import sys
from collections import namedtuple
import logging

logging.basicConfig(filename='directory_info.log', level=logging.INFO)

DirectoryInfo = namedtuple('DirectoryInfo', ['name', 'extension', 'is_directory', 'parent'])

def collect_directory_info(path):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            info = DirectoryInfo(name=d, extension=None, is_directory=True, parent=root)
            logging.info(info)
        for f in files:
            name, ext = os.path.splitext(f)
            info = DirectoryInfo(name=name, extension=ext, is_directory=False, parent=root)
            logging.info(info)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python collect_directory_info.py <path>')
        sys.exit(1)
    path = sys.argv[1]
    collect_directory_info(path)
