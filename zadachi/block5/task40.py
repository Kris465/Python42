n = int(input('Сколько будет чисел: '))
a = input(f"Введите любые дробные числа ({n}) через пробел: ").split(' ')
summa = 0

for i in a:
    summa += float(i)

print(summa)
