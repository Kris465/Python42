marks = input('Введите оценки по алгебре '
              'всех учеников через пробел: ').split(' ')
sum = 0

for i in marks:
    sum += int(i)
sr = round(sum / len(marks), 2)

print(f'Средняя оценка по алгебре: {sr}')
