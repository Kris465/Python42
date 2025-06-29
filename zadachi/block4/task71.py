a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

if a > b:
    print(f"Больше число: {a}")
if b > a:
    print(f"Больше число: {b}")
if (a - b) < 0 and (a - b) != 0:
    print(f"Больше число: {b}")
if (b - a) < 0 and (b - a) != 0:
    print(f"Меньше число: {b}")
