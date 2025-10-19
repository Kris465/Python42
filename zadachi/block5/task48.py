m = input("Введите 10 чисел через пробел: ").split()
summa = 0

for i in m:
    summa += int(i)**2

print(f"Сумма квадратов всех чисел: {round(summa, 2)}")
