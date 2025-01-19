# Цель: понять как работают потоки на практике, решив задачу
# Задача "Потоковая запись в файлы":

import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое то слово №{i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


test_1_s = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
test_1_f = time.time()
print(f'Время работы программы c 1 потоком: {test_1_f - test_1_s}')


test_2_s = time.time()
flow_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
flow_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
flow_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
flow_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

flow_1.start()
flow_2.start()
flow_3.start()
flow_4.start()

flow_3.join()
test_2_f = time.time()
print(f'Время работы программы c несколькими потоками: {test_2_f - test_2_s}')
