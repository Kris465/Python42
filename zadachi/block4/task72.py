a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))

if a > b and a > c:
    print(f"Больше число: {a}")
if b > a and b > c:
    print(f"Больше число: {b}")
if c > a and c > b:
    print(f"Больше число: {c}")

if a < b and a < c:
    print(f"Меньшее число: {a}")
if b < a and b < c:
    print(f"Меньшее число: {b}")
if c < a and c < b:
    print(f"Меньшее число: {c}")
