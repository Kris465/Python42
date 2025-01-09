number = int(input("Введите число: "))
degree = int(input("Введите степень числа: "))
if degree >= 0 and degree < 8:
    print(number ** degree)
else:
    print("Неправильная степень.")
