import math

print('Синус       |      Значение')
for i in range(2, 21):
    sin = math.sin(i)
    print(f'sin{i:2}     |     {sin:.4f}')
