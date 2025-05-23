import math

m = int(input("введите число m: "))
n = int(input("число n: "))

res = m / n
if math.fmod(m, n) == 0:
    print(f' без остатка: {res}')
else:
    print(f'с остатком: {res}')
