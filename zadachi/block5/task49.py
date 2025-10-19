n = int(input('Сколько будет чисел: '))
a = input(f"Введите любые дробные числа ({n}) через пробел: ").split(' ')
summa = 0

for i in a:
    summa += float(i)**2

print(f'Сумма квадратов ваших чисел: {round(summa, 2)}')
