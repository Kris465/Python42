import math

def compare_areas(r, a):
    area_circle = math.pi * r**2
    area_square = a**2

    print(f"Площадь круга: {area_circle:.2f}")
    print(f"Площадь квадрата: {area_square:.2f}")

    if area_circle > area_square:
        print("Площадь круга больше.")
    elif area_circle < area_square:
        print("Площадь квадрата больше.")
    else:
        print("Площади равны.")

r = float(input("Введите радиус круга: "))
a = float(input("Введите сторону квадрата: "))

compare_areas(r, a)