# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
# Задание "Они все так похожи":
import math


class Figure:
    sides_count = 0

    def __init__(self, rgb, list_, *args):
        self.__sides = list_
        self.__color = []
        self.filled = False
        self.set_color(*rgb)
        self.set_sides(*args)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (not isinstance(r, int) or not isinstance(g, int) or not isinstance(b, int) or
                not 0 <= r <= 255 or not 0 <= g <= 255 or not 0 <= b <= 255):
            return False
        return True

    def set_color(self, *rgb):
        r, g, b = rgb[0], rgb[1], rgb[2]
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        for x in args:
            if not isinstance(x, int) or x < 0:
                return False
        if len(args) != self.sides_count:
            return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(x for x in self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *args):
        super().__init__(rgb, [1], *args)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *args):
        super().__init__(rgb, [1, 1, 1], *args)

    def get_square(self):
        c = self.get_sides()
        a = c[0]
        b = c[1]
        c = c[2]
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(area, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *args):
        super().__init__(rgb, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], *args)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            super().set_sides(*(new_sides * self.sides_count))

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)   # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)   # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)    # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)     # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)   # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
