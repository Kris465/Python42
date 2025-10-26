class_1 = [5, 5, 5, 5, 4, 4, 4, 4, 4, 4,
           4, 4, 4, 4, 3, 3, 3, 3, 3, 2]
class_2 = [5, 5, 5, 4, 4, 4, 4, 4, 3, 3,
           3, 3, 3, 3, 3, 3, 2, 2, 2, 2]
sum_1, sum_2 = 0, 0

for i in class_1:
    sum_1 += i
for i in class_2:
    sum_2 += i
sr1, sr2 = round(sum_1 / len(class_1), 2), round(sum_2 / len(class_2), 2)

print(f'Средняя оценка по физике в классе №1: {sr1}\nСредняя оценка по '
      f'физике в классе №2: {sr2}')
