def card_hide(number):
    stroka = str(number)
    return len(stroka) * '*' + stroka[-4:]


print(card_hide(5456789515658562))


def is_palindrome(stroka):
    stroka2 = stroka[::-1]
    if stroka == stroka2:
        return True
    else:
        return False


print(is_palindrome('summer'))
print(is_palindrome('шалаш'))

from abc import ABC, abstractmethod
import math


class math_figure(ABC):

    @abstractmethod
    def area(self, value):
        pass


class Circle(math_figure):
    def __init__(self, value):
        self.value = value

    def area(self):
        return f'Площадь круга = {round(self.value ** 2 * math.pi, 2)}'


class Square(math_figure):
    def __init__(self, value):
        self.value = value

    def area(self):
        return f'Площадь Квадрата = {self.value * self.value}'


class Rectangle(math_figure):
    def __init__(self, storona_a, storona_b):
        self.storona_a = storona_a
        self.storona_b = storona_b

    def area(self):
        return f'Площадь прямоугольника  = {self.storona_a * self.storona_b}'


square = Square(4)
rectangle = Rectangle(2, 6)
circle = Circle(3)
figures = [square, rectangle, circle]
for i in figures:
    print(i.area())
