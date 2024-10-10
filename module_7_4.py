# Примеры форматирования строк

# 1. Использование %:
team1_num = 5
print("В команде Мастера кода участников: %d" % team1_num)

team2_num = 5
team3_num = 6
print("Итого сегодня в командах участников: %d, %d" % (team2_num, team3_num))

# 2. Использование format():
score_2 = 42
print("Команда Волшебники данных решила задач: {} задач".format(score_2))

team1_time = 18015.2
print("Волшебники данных решили задачи за {} c".format(team1_time))

# 3. Использование f-строк:
score_3 = 40
score_4 = 42
print(f"Команды решили {score_3} и {score_4} задач.")

challenge_result = "победа команды Мастера кода!"
print(f"Результат битвы: {challenge_result}")

tasks_total = 82
time_avg = 350.4
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
