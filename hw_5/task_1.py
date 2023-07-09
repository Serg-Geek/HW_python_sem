# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_file_path(file_path):
    part = file_path.split('\\')
    file_name = part[-1]
    name, extension = file_name.rsplit('.')
    path = '/'.join(part[:-1])
    return path, name, extension

print(split_file_path(' C:\\Users\\Second\\PycharmProjects\\HW_python_sem\\hw_5\\task_1.py '))
