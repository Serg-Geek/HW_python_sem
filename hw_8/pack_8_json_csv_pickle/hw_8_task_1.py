# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию
# возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря для заголовков столбца
# из переданного файла.
import csv
import pickle


# def convert_pickle_to_csv(pickle_file_path, csv_file_path):
#     """
#     Преобразует pickle файл в табличный csv файл.
#     :param pickle_file_path: путь к pickle файлу
#     :param csv_file_path: путь к csv файлу
#     при тестировании введите путь к Вашим файлам
#     """
#     # Загрузка данных из pickle файла
#     with(
#         open(pickle_file_path, 'rb') as pick,
#         open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file,
#     ):
#         data = pickle.load(pick)
#         # Заголовки столбцов
#         headers = list(data.keys())
#         # Запись заголовков столбцов в csv файл
#         writer = csv.writer(csv_file)
#         writer.writerow(headers)
#         # Запись данными в csv файл
#         for row in data.values():
#             writer.writerow(row)
#
#
# if __name__ == '__main__':
#     pickle_file_path = '/home/serg/PycharmProjects/HW_python_sem/seminar_8_json/new_users_personal_data.json.pickle'
#     csv_file_path = '/home/serg/PycharmProjects/HW_python_sem/hw_8/new_res.csv'
#     convert_pickle_to_csv(pickle_file_path, csv_file_path)

import csv
import pickle


def convert_pickle_to_csv(pickle_file_path, csv_file_path):
    """
    Преобразует pickle файл в табличный csv файл.
    :param pickle_file_path: путь к pickle файлу
    :param csv_file_path: путь к csv файлу
    """
    # Загрузка данных из pickle файла
    with open(pickle_file_path, 'rb') as pickle_file:
        data = pickle.load(pickle_file)

    # Если данные в pickle файле представлены в виде списка словарей
    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        # Заголовки столбцов
        headers = list(data[0].keys())

        # Запись данных в csv файл
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)

            # Запись заголовков столбцов
            writer.writerow(headers)

            # Запись данных
            for row in data:
                writer.writerow(row.values())
    else:
        print("Данные в pickle файле должны быть представлены в виде списка словарей.")


if __name__ == '__main__':
    pickle_file_path = '/seminar_8_json/new_users_personal_data.json.pickle'
    csv_file_path = '/hw_8/new_res.csv'
    convert_pickle_to_csv(pickle_file_path, csv_file_path)