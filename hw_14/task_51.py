import json

from exceptions import LevelError, AccessError
from task_3_4 import User
class Project:
    def __init__(self, users=None):
        self.users = users
        self.admin = None
    #
    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

            users = []
            for level, user_data in json_data.items():
                for user_id, user_name in user_data.items():
                    user = User(user_name, int(user_id), int(level))
                    users.append(user)

            return cls(users)

    def login(self, name, id_):
        for proj_user in self.users:
            if name == proj_user.name and id_ == proj_user.id_:
                user = User(name, id_, proj_user.level)
                self.admin = user
                break
        else:
            raise AccessError(name, id_, 'Access Denied')
    def add_user(self, name, id_, level):
        if level < self.admin.level:
            raise LevelError(name, id_, level, 'Level Error')
        user = User(name, id_, level)
        self.users.append(user)
    def remove_user(self, name, id_):
        user = User(name, id_)
        try:
            self.users.remove(user)
        except ValueError:
            print(f"User {user} not found")
    def save_to_json(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            user_data = [(user.name, user.id, user.level) for user in self.users]
            json.dump(user_data, f, ensure_ascii=False)

    def __repr__(self):
        return f'Project(users={self.users})'



    def enter(self):
        return self



    def exit(self, exc_type, exc_value, exc_traceback):
        self.save_to_json('task_5.json')
def show_menu():
    print("===== Проектная система =====")
    print("1. Вход в систему")
    print("2. Добавить пользователя")
    print("3. Удалить пользователя")
    print("4. Сохранить данные в JSON файл")
    print("5. Выход")
    print("==============================")
def choose_option():
    option = input("Выберите опцию: ")
    if option.isdigit():
        return int(option)
    else:
        return -1
# Пример использования

# Загрузка данных из JSON файла
project = Project.from_json('users_personal_data.json')
print(project.users)  # Печатает список пользователей

while True:
    show_menu()
    option = choose_option()

    if option == 1:
        name = input("Введите имя пользователя: ")
        id_ = int(input("Введите ID пользователя: "))

        try:
            project.login(name, id_)
            print("Вход выполнен.")
            print(f"Администратор проекта: {project.admin}")
        except AccessError as e:
            print(e)

    elif option == 2:
        name = input("Введите имя пользователя: ")
        id_ = int(input("Введите ID пользователя: "))
        level = int(input("Введите уровень пользователя: "))

        try:
            project.add_user(name, id_, level)
            print(f"Пользователь {name} добавлен в проект.")
            print("Обновленный список пользователей:", project.users)
        except LevelError as e:
            print(e)
    elif option == 3:
        name = input("Введите имя пользователя для удаления: ")
        id_ = int(input("Введите ID пользователя для удаления: "))

        project.remove_user(name, id_)
        print("Пользователь удален.")
        print("Обновленный список пользователей:", project.users)
    elif option == 4:
        project.save_to_json('task_5.json')
        print("Данные сохранены в JSON файл.")
    elif option == 5:
        break
    else:
        print("Выберите допустимую опцию.")

print("Выход из программы.")

