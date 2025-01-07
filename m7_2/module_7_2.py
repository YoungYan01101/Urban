# Цель: Закрепить знания о позиционировании в файле, использовав метод tell() файлового объекта.
# Написать усовершенствованную функцию записи.
# Задача "Записать и запомнить"

def custom_write(file_name, strings):
    strings_positions = dict()
    file = open(file_name, 'w', encoding='utf-8')
    for row in strings:
        strings_positions[(strings.index(row)+1, file.tell())] = row
        file.write(row+'\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
