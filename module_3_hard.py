# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности

def calculate_structure_sum(*args):
    global count
    for i in args:
        if isinstance(i, str):
            count += len(i)
        elif isinstance(i, int):
            count += i
        elif isinstance(i, dict):
            calculate_structure_sum(list(i.items()))
        else:
            calculate_structure_sum(*i)
    return count


count = 0
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
