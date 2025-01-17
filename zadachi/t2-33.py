n = input("Введите число от 1 до 999: ")

if len(n) == 1:
    print(f"Ваше число x - {n}")
elif len(n) == 2:
    first = n[0]
    second = n[1]
    print(f"Ваше число x - {n[1] + n[0]}")
else:
    first = n[0]
    second = n[1]
    third = n[2]
    print(f"Ваше число x - {n[2] + n[1] + n[0]}")