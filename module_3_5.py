# Цель: применить знания о рекурсии в решении задачи.

def get_multiplied_digits(number):
    first = int(str(number)[0])
    if len(str(number)) == 1:
        return first if first != 0 else 1
    return first * get_multiplied_digits(int(str(number)[1:]))


result = get_multiplied_digits(40203)
print(result)
result = get_multiplied_digits(402030)
print(result)
result = get_multiplied_digits(3795)
print(result)
result = get_multiplied_digits(300700950)
print(result)
