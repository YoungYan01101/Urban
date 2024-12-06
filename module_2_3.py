# Домашняя работа по уроку "Стиль кода. Цикл While. 1.2"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0
while index < len(my_list):
    if my_list[index] < 0:
        break
    elif my_list[index] == 0:
        index += 1
        continue
    print(my_list[index])
    index += 1


# for x in my_list:
#     if x < 0:
#         break
#     elif x == 0:
#         continue
#     print(x)
