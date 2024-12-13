# Цель: применить на практике начальные знания о пространстве имён и оператор global.
# Закрепить навыки из предыдущих модулей.

def count_calls():
    global calls
    calls += 1


def string_info(string):
    my_tuple = len(string), string.upper(), string.lower()
    count_calls()
    return my_tuple


def is_contains(string, list_to_search):
    new_list = []
    for x in list_to_search:
        new_list.append(x.lower())
    count_calls()
    return string.lower() in new_list


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
