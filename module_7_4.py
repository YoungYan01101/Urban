# Освоить различные методы форматирования строк в Python.
# Научиться применять эти методы в контексте описания соревнования.
# История: соперничество двух команд - Мастера кода и Волшебники данных.

# Напишите код, который форматирует строки для следующих сценариев.
# Укажите переменные, которые должны быть вставлены в каждую строку:

team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

tasks_total = score_1 + score_2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = f'Победа команды {team1_name}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = f'Победа команды {team2_name}!'
else:
    challenge_result = 'Ничья!'


# Использование %:
print('В команде Мастера кода участников: %s ! ' % team1_num)
print('В команде Волшебники данных участников: %(comand_2)s ! ' % {'comand_2': team2_num})
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print()

# Использование format():
print('Команда Мастера кода решила задач: {} !'.format(score_1))
print('Команда Волшебники данных решила задач: {0} !'.format(score_2))
print('Мастера кода решили задачи за {comand_1_time} с !'.format(comand_1_time=team1_time))
print('Волшебники данных решили задачи за {comand_2_time} с !'.format(comand_2_time=team2_time))
print()

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по '
      f'{(team1_time + team2_time) // tasks_total} секунды на задачу!.')
