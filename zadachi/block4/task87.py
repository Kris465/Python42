x = float(input('Введите число "x": '))

if x <= 0:
    print('f = 0')
elif x > 0 and x <= 1:
    print(f'f = {x}')
else:
    print(f'f = {x**2}')
