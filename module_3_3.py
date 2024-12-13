# Цель задания: Освоить создание функций с параметрами по умолчанию
# и практику вызова этих функций с различным количеством аргументов.

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [False, 12, 'Error-404']
values_dict = {'a': 23, 'b': [0, 0], 'c': 'night'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [(14, 12, 2024), 'STRING']
values_list_3 = ['Hello', 'apple', 'Im going to eat you']

print_params(-5, *values_list_2)
print_params(*values_list_2[0])
print_params(*values_list_2, 42)
print_params(*values_list_3)
