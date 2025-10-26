marks = input('Введите свои оценки по 10-ти'
              'предметам через пробел: ').split(' ')
sum = 0

for i in marks:
    sum += int(i)
sr = round(sum / len(marks), 2)

print(f'Ваша средняя оценка: {sr}')
