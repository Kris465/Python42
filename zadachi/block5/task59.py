first = input('Введите возраст 20 учеников первого класса: ').split(' ')
second = input('Введите возраст 20 учеников второго класса: ').split(' ')

sum_1 = 0
sum_2 = 0

for i in first:
    sum_1 += float(i)
for i in second:
    sum_2 += float(i)

sr1 = round(sum_1 / len(first), 2)
sr2 = round(sum_2 / len(second), 2)

print(f'Средний возраст учеников в первом классе: {sr1}')
print(f'Средний возраст учеников во втором классе: {sr2}')
