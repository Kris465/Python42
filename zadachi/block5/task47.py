m = input("Введите 6 чисел через пробел: ").split()
summa = 1

for i in m:
    summa *= int(i)

print(f"Произведение всех чисел: {round(summa, 2)}")
