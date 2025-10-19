m = input("Введите массу 12-ти предметов через пробел (в кг): ").split()
summa = 0

for i in m:
    summa += float(i)

print(f"Общий вес всех предметов: {round(summa, 2)}")
