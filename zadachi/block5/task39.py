numbers = input("Введите 10 чисел через пробел: ").split(' ')
summa = 0

for i in numbers:
    summa += int(i)

print(summa)
