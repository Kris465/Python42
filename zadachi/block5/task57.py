first = input('Введите оценки по 4 предметам'
              ' первого ученика через пробел: ').split(' ')

second = input('Введите оценки по 4 предметам'
               ' второго ученика через пробел: ').split(' ')

sum = 0

for i in first:
    sum += int(i)
for i in second:
    sum += int(i)

print(f'Сумма оценок обоих учеников: {sum}')
