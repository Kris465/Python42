import math

m = int(input("введите число m: "))
n = int(input("число n: "))

res = m / n
if math.fmod(m, n) == 0:
    print(f'числа m и n делятся без остатка , результат: {res}')
else:
    print(f'числа m и n делятся с остатком , результат: {res}')
