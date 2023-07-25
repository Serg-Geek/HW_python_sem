# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json
from pathlib import Path

import json
from pathlib import Path

def users_personal_data():
    file_path = '/home/serg/PycharmProjects/HW_python_sem/seminar_8_json/users_personal_data.json'
    if Path(file_path).exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            file = json.load(f)
    else:
        file = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}}

    while True:
        id_ = input('Введите id или нажмите Enter для выхода ---> ')
        if not id_:
            break

        name = input('Введите имя ---> ')
        level = input('Введите уровень доступа ---> ')
        if level not in file:
            print('Некорректный уровень доступа!')
            continue

        file[level].update({id_: name})

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    users_personal_data()

