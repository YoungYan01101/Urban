# Цель: освоить на практике замыкание, объекты-функторы и lambda-функции.
# Задача "Функциональное разнообразие"
from random import choice


# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


# Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w+', encoding='utf8') as file:
            for string in data_set:
                file.write(str(string) + '\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = [x for x in words]

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 1, 5, 7, 8)
print(first_ball())
print(first_ball())
print(first_ball())
