import json

from task_3_4 import User, AccessError, LevelError


class Project:
    def __init__(self, users=None):
        self.users = users
        self.admin = None

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
            users = [User(name, id_, level) for name, id_, level in user_data]
            return cls(users)

    def login(self, name, id_):
        user = User(name, id_)
        for proj_user in self.users:
            if user == proj_user:
                self.admin = proj_user
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        with open('task_5.json', 'w', encoding='utf-8') as f:
            user_data = [(user.name, user.id, user.level) for user in self.users]
            json.dump(user_data, f, ensure_ascii=False)

    def __repr__(self):
        return f'Project(users={self.users})'