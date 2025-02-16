from math import sin, radians

x = float(input('Введите значение "x": '))

if x > 0:
    y = (sin(radians(x))**2)
    print(f'При "x" = {x}, "y" = {round(y, 2)}')
else:
    y = 1 - 2*(sin(radians(x**2)))
    print(f'При "x" = {x}, "y" = {round(y, 2)}')
