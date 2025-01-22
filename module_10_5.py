# Цель: понять разницу между линейным и многопроцессорным подходом, выполнив операции обоими способами
# Задача "Многопроцессорное считываение"

import multiprocessing
import time


print('             Процесс', __name__, 'начал работу')


def read_info(name):
    all_data = []
    count = 0
    with open(name, 'r', encoding='utf8') as file:
        for line in file:
            all_data.append(line)
            count += 1
    print(f'{multiprocessing.process.current_process().name} - закончил работу с файлом  {name}  '
          f'Считано строк:  {count}')


file_names = [f'file {number}.txt' for number in range(1, 5)]


if __name__ == '__main__':
    print('...Чтение файлов линейным методом...')
    t = time.time()
    for file_name in file_names:
        read_info(file_name)
    print('...Work time:', round(time.time() - t, 3), 'sec...')
    print()

    print('...Чтение файлов многопроцессорным методом...')
    t = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    print('...Work time:', round(time.time() - t, 3), 'sec...')

