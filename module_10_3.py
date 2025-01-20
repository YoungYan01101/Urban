# Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.
# Задача "Банковские операции":

import threading
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            summ = randint(50, 500)
            self.balance += summ
            print(f'Пополнение: {summ}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            summ = randint(50, 500)
            print(f'Запрос на {summ}')
            if summ <= self.balance:
                self.balance -= summ
                print(f'Снятие: {summ}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')