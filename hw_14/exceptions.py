
class MyException(Exception):
    pass

class LevelError(MyException):
    def __init__(self, name, id_, level, message):
        self.name = name
        self.id_ = id_
        self.level = level
        self.message = message

    def __str__(self):
        return f"LevelError: {self.message}. User: {self.name} (ID: {self.id_}), Level: {self.level}"


class AccessError(MyException):
    def __init__(self, name, id_, message):
        self.name = name
        self.id_ = id_
        self.message = message

    def __str__(self):
        return f"AccessError: {self.message}. User: {self.name} (ID: {self.id_})"