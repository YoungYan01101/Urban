# Цель: применить на практике знания о классах, объектах и их атрибутах.
# Задача "Developer - не только разработчик"


class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{self.name}:    Этажа с номером {new_floor} не существует')
        else:
            print(*range(1, new_floor+1))


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Пушкина 10', 180)
h4 = House('Ленина 12', 30)

h1.go_to(5)
h2.go_to(10)
h3.go_to(150)
h4.go_to(-5)

