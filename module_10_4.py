# Цель: Применить очереди в работе с потоками, используя класс Queue.
# Задача "Потоки гостей в кафе":
import random
import time
import threading
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = args

    def guest_arrival(self, *new_guests):
        for guest in new_guests:
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    print(table.guest.name, 'сел(-а) за стол номер', table.number)
                    table.guest.start()
                    break
            else:
                self.queue.put(guest)
                print(guest.name, 'в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(table.guest.name, 'покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and not table.guest:
                    table.guest = self.queue.get()
                    print(table.guest.name, 'вышел(-ла) из очереди и сел(-а) за стол номер', table.number)
                    table.guest.start()


tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
