# Цель задания:
# Освоить механизмы создания декораторов Python
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию
# Декораторы в Python
from math import sqrt


def is_prime(func):
    def wrapper(*args):
        summ = func(*args)
        simple = True
        if summ == 2:
            pass
        elif summ % 2 == 0:
            simple = False
        else:
            for i in range(3, int(sqrt(summ))+1, 2):
                if summ % i == 0:
                    simple = False
        if simple:
            print('Простое')
        else:
            print('Составное')
        return summ
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
