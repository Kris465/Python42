from math import sin, radians, sqrt


print('Синус         |      Значение')
for i in range(1, 10):
    temp = sqrt(i / 10)
    my_sin = sin(radians(temp))
    print(f'sin{temp:.4f}     |     {my_sin:.4f}')
