# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.

import csv
import pickle

def read_csv_as_pickle_string(csv_file_path):
    """
       Читает csv файл и возвращает его содержимое в виде строки pickle.
       :param csv_file_path: путь к csv файлу
       :return: строка pickle
       """
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        data = [line for line in reader]
        return pickle.dumps(list(data))





if __name__ == '__main__':
    print(read_csv_as_pickle_string('/hw_8/new_res.csv'))
