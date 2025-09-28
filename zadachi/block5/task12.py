import math

p0 = 1.29
z = 1.25e-4


print("Таблица зависимости плотности от высоты: ")

for h in range(0, 1001, 100):
    p = p0 * math.exp(-h * z)
    print(f'{h:4d}          |  {p:.4f}')
