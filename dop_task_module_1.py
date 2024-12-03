# Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()
dict_mid_value = {}
dict_mid_value.update({students[0]: "{:.2f}".format(sum(grades[0]) / len(grades[0])),
                       students[1]: "{:.2f}".format(sum(grades[1]) / len(grades[1])),
                       students[2]: "{:.2f}".format(sum(grades[2]) / len(grades[2])),
                       students[3]: "{:.2f}".format(sum(grades[3]) / len(grades[3])),
                       students[4]: "{:.2f}".format(sum(grades[4]) / len(grades[4]))})
print(dict_mid_value)

# Решение через цикл
if len(students) == len(grades):
    # students = list(students)
    # students.sort()
    dict_mid_value = {}
    i = 0
    while i < len(students):
        dict_mid_value.update({students[i]: "{:.2f}".format(sum(grades[i]) / len(grades[i]))})
        i += 1
    print(dict_mid_value)
else:
    print('Количество учеников не совпадает с количеством списков оценок')

