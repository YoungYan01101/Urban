# Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__.
# Закрепить навык создания и выбрасывания исключений.
# Задача "Range - это просто"


class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0', f'step = {step}')
        elif start > stop and step > 0:
            raise StepValueError('Шаг должен быть отрицательным', f'step = {step}')
        elif start < stop and step < 0:
            raise StepValueError('Шаг должен быть положительным', f'step = {step}')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.start > self.stop > self.pointer or
                self.start < self.stop < self.pointer):
            raise StopIteration()
        result = self.pointer
        self.pointer += self.step
        return result


def check(start, stop, step=1):
    try:
        name = Iterator(start, stop, step)
        for iter0 in name:
            print(iter0, end=' ')
    except StepValueError as ex:
        print('Шаг указан неверно', end=' ')
        print(ex.args)
    else:
        print()


check(100, 200, 0)
check(-5, 1)
check(6, 15, 2)
check(5, 1, -1)
check(10, 1)
