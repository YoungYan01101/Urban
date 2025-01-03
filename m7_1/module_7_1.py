# Домашнее задание по теме "Режимы открытия файлов"
# Цель: закрепить знания о работе с файлами (чтение/запись) решив задачу.

f = open('products.txt', 'w')
f.close()


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        result = file.read()
        file.close()
        return result

    def add(self, *products):
        for i in products:
            if not isinstance(i, Product):
                continue

            result_list = []
            result = self.get_products()
            if result:
                result = result.split('\n')
                for j in range(len(result)):
                    result_list.append(result[j].split(', '))
                result_list.pop()

            for row in result_list:
                if i.name == row[0] and i.category == row[2]:
                    row[1] = str(float(row[1]) + i.weight)
                    print(f'Продукт {i.name} уже был в магазине, его общий вес теперь равен {row[1]}')
                    break
            else:
                result_list.append([i.name, str(i.weight), i.category])

            file = open(self.__file_name, 'w')
            for row in result_list:
                file.write(row[0] + ', ' + row[1] + ', ' + row[2] + '\n')
            file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
