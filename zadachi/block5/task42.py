n = input('Введите баллы за каждый из 4 экзаменов через пробел: ').split(' ')
sum = 0
for i in n:
    sum += int(i)
print(f"Сумма ваших баллов: {sum}")
