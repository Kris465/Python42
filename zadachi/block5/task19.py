from math import sin, radians


print('Синус     |      Значение')
for i in range(1, 11):
    temp = i / 10
    my_sin = sin(radians(temp))
    print(f'sin{i:2}     |     {my_sin:.4f}')
