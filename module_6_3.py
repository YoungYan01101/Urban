# Цель: закрепить знания множественного наследования в Python.
# Задача "Ошибка эволюции":
import random

class Animal:
    """
    Animal - класс описывающий животных.
    """
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f'X:{self._cords[0]}  Y:{self._cords[1]}  Z:{self._cords[2]}')

    def attack(self):
        print("Sorry, i'm peaceful :)" if self._DEGREE_OF_DANGER < 5 else "Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    """
    Bird - класс описывающий птиц. Наследуется от Animal.
    """
    beak = True

    def lay_eggs(self):
       print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    """
    AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
    """
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.speed //= 2
        dz = -1 * abs(dz)
        self.move(0, 0, dz)
        self.speed *= 2

class PoisonousAnimal(Animal):
    """
    PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
    """
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    """
    Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
    """
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = 'Click-click-click'


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(-6)
db.get_cords()

db.lay_eggs()
