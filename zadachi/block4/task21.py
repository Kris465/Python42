def is_divisor(a, b):
    if a == 0:
        return False
    return b % a == 0

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if is_divisor(a, b):
    print(f"{a} является делителем числа {b}")
else:
    print(f"{a} не является делителем числа {b}")