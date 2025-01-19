# Цель: научиться создавать классы наследованные от класса Thread.
# Задача "За честь и отвагу!":

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        count = 100
        day = 0
        while count > 0:
            time.sleep(1)
            day += 1
            count -= self.power
            print(f'{self.name} сражается {day} дней/дня/день...,   осталось {count if count >= 0 else 0} войнов')
        print(f'***  {self.name} одержал победу спустя {day} дней  ***')


# список с объектами - рыцарями
knights = [
    first_knight := Knight('Sir Lancelot', 10),
    second_knight := Knight("Sir Galahad", 20)
           ]

# Запускаем все потоки - битвы
for x in knights:
    x.start()
    time.sleep(0.001)  # задержка в 1ms что бы строки разных потоков не выводились в одну

# Ожидаем выполнение всех потоков
for x in knights:
    x.join()

print('Все битвы окончены')
