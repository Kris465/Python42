n = int(input("Введите ваш возраст: "))

if 1 <= n <= 99 and n not in [11, 12, 13, 14]:
    if n % 10 in [2, 3, 4]:
        print(f"Вам {n} года..")
    if n % 10 in [1]:
        print(f"Вам {n} год")
elif 1 <= n <= 99 and n in [11, 12, 13, 14]:
    if n % 10 in [5, 6, 7, 8, 9, 0] or n in [11, 12, 13, 14]:
        print(f"Вам {n} лет..")
else:
    print("Вы слишком стары...")
