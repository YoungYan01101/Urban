# Цель: понять разницу между атрибутами объекта и класса, дополнив уже существующий класс. Применить метод __new__
# Задача "История строительства":

def other_is_house(other):
    if not isinstance(other, (int, House)):
        raise ArithmeticError("Аргумент не является классом int или House")
    return other if isinstance(other, int) else other.number_of_floors


class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

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

    def __del__(self): print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

