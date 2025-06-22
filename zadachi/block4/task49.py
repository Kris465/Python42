import math

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if a == 0:
    print("Нельзя так!")
else:
    D = b ** 2 - 4 * a * c

    if D < 0:
        print(f"Ну дискриминант меньше нуля = {D}")
    elif D == 0:
        x = -b // (2 * a)
        print(f"Корнь = {x}")
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-b + sqrt_D) // (2 * a)
        x2 = (-b - sqrt_D) // (2 * a)
        print(f"Корень первый = {x1}, второй корень = {x2}")
