# Словари и множества

my_dict = {'Egor': 1981, 'Masha': 2005, 'Petya': 1998}
print(my_dict)
print(my_dict['Masha'], my_dict.get('Vasya'))
my_dict.update({'Sasha': 2000, 'Liza': 1990})
print(my_dict.pop('Egor'))
print(my_dict)

print()
my_set = {15, 56, 543, 15, True, 'string', 'hello', True, 'hello', 543}
print(my_set)
my_set.add((100, 54, 'string'))
my_set.add(False)
my_set.discard(15)
print(my_set)
