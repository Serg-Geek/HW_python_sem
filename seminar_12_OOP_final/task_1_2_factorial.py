# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.


# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json


class Factorial:
    def __init__(self, k, file_name):
        self.k = k
        self.res = []
        self.file = None
        self.file_name = file_name

    def __call__(self, n):
        factorial = self._factorial(n)
        self.res.append({n: factorial})
        self.res = self.res[-self.k:]
        return factorial

    def _factorial(self,n):
        if n < 0:
            raise ValueError(f'меньше 0 нельзя')
        if n == 0:
            return  1
        else:
            return n * self._factorial(n-1)

    def get_last(self):
        return self.res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file = open(f'{self.file_name}', 'w', encoding='utf-8')
        json.dump(self.res, self.file)
        self.file.close()

with Factorial(5, 'task_2.json') as f:

    f1 = f(5)
    f2 = f(6)
    f3 = f(7)
    f4 = f(8)
    f5 = f(9)
    f6 = f(10)
    f7 = f(11)
    # f8 = f(-1)
    print(f.get_last())