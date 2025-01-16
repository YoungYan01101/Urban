# Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

def all_variants(text):
    for count_symbol in range(len(text)):
        for position in range(len(text)-count_symbol):
            yield text[position:position + count_symbol + 1]


a = all_variants('abc')
for i in a:
    print(i)
