# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.


class Rectangle:
    slots = ('_length', '_width')

    def __init__(self, length, width=None):
        self._length = length
        self._width = width if width is not None else length

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_square(self):
        return self.length * self.width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if length > 0:
            self._length = length
        else:
            raise ValueError('Length must be greater than 0')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError('Width must be greater than 0')

p1 = Rectangle(-5)
print(p1.get_perimeter())
p2 = Rectangle(10)
print(p2.get_square())