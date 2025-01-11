# Цель: понять как работают исключения внутри функций
# и как обрабатываются эти исключения на практике при помощи try-except.
# Задача "План перехват"

def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        summ = personal_sum(numbers)
        return summ[0] / (len(numbers) - summ[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
