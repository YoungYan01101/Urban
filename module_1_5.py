# Неизменяемые и изменяемые объекты. Кортежи и списки

immutable_var = (23, 'string', False)
print(immutable_var)
# immutable_var[0] = 58
# нельзя изменить, потому что кортеж не изменяемый тип данных
# Перевод ошибки полностью отвечает на поставленный вопрос: объект "кортеж" не поддерживает назначение элементов

mutable_list = [23, 'string', False]
mutable_list[0] = True
mutable_list[2] = 455
print(mutable_list)
