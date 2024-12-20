# Цель: применить знания о перегрузке арифметических операторов и операторов сравнения.
# Задача "Нужно больше этажей"


def other_is_house(other):
    if not isinstance(other, (int, House)):
        raise ArithmeticError("Аргумент не является классом int или House")
    return other if isinstance(other, int) else other.number_of_floors


class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{self.name}:    Этажа с номером {new_floor} не существует')
        else:
            print(*range(1, new_floor+1))

    def __len__(self): return self.number_of_floors
    def __str__(self): return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other): return self.number_of_floors == other_is_house(other)
    def __lt__(self, other): return self.number_of_floors < other_is_house(other)
    def __le__(self, other): return self.number_of_floors <= other_is_house(other)
    def __gt__(self, other): return self.number_of_floors > other_is_house(other)
    def __ge__(self, other): return self.number_of_floors >= other_is_house(other)
    def __ne__(self, other): return self.number_of_floors != other_is_house(other)

    def __add__(self, value):
        self.number_of_floors += other_is_house(value)
        return self

    def __radd__(self, value): return self.__add__(value)
    def __iadd__(self, value): return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)         # __eq__

h1 = h1 + 10            # __add__
print(h1)
print(h1 == h2)

h1 += 10                # __iadd__
print(h1)

h2 = 10 + h2            # __radd__
print(h2)

print(h1 > h2)          # __gt__
print(h1 >= h2)         # __ge__
print(h1 < h2)          # __lt__
print(h1 <= h2)         # __le__
print(h1 != h2)         # __ne__


