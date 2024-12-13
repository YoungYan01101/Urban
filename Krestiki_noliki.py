# Крестики - Нолики
def check_win():
    if place[0][0] == 'X' and place[0][1] == 'X' and place[0][2] == 'X':
        return 'X'
    if place[1][0] == 'X' and place[1][1] == 'X' and place[1][2] == 'X':
        return 'X'
    if place[2][0] == 'X' and place[2][1] == 'X' and place[2][2] == 'X':
        return 'X'
    if place[0][0] == 'X' and place[1][0] == 'X' and place[2][0] == 'X':
        return 'X'
    if place[0][1] == 'X' and place[1][1] == 'X' and place[2][1] == 'X':
        return 'X'
    if place[0][2] == 'X' and place[1][2] == 'X' and place[2][2] == 'X':
        return 'X'
    if place[0][0] == 'X' and place[1][1] == 'X' and place[2][2] == 'X':
        return 'X'
    if place[0][2] == 'X' and place[1][1] == 'X' and place[2][0] == 'X':
        return 'X'
    if place[0][0] == 'O' and place[0][1] == 'O' and place[0][2] == 'O':
        return 'O'
    if place[1][0] == 'O' and place[1][1] == 'O' and place[1][2] == 'O':
        return 'O'
    if place[2][0] == 'O' and place[2][1] == 'O' and place[2][2] == 'O':
        return 'O'
    if place[0][0] == 'O' and place[1][0] == 'O' and place[2][0] == 'O':
        return 'O'
    if place[0][1] == 'O' and place[1][1] == 'O' and place[2][1] == 'O':
        return 'O'
    if place[0][2] == 'O' and place[1][2] == 'O' and place[2][2] == 'O':
        return 'O'
    if place[0][0] == 'O' and place[1][1] == 'O' and place[2][2] == 'O':
        return 'O'
    if place[0][2] == 'O' and place[1][1] == 'O' and place[2][0] == 'O':
        return 'O'
    return '*'


place = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
step = 1
win = '*'
print('Добро пожаловать в консольную игру: крестики-нолики')
while win == '*' and step < 10:
    while True:
        print('-' * 10 + f' Ход №{step} ' + '-' * 10)
        print('Ходят ' + ('нолики' if step % 2 == 0 else 'крестики'))
        row = int(input('Введите номер строки: '))
        col = int(input('Введите номер столбца: '))
        if (1 <= row <= 3) and (1 <= col <= 3):
            if place[row-1][col-1] == '.':
                place[row-1][col-1] = ('O' if step % 2 == 0 else 'X')
                break
            else:
                print('Место уже занято!')
        else:
            print('Не корректный ввод места')
        for i in place:
            print(*i)
    step += 1
    for i in place:
        print(*i)
    win = check_win()
print('-'*20)
print('Победа крестиков!!!' if win == 'X' else 'Победа Ноликов!!!' if win == 'O' else 'Ничья )')
