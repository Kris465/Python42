def all_digits_unique(s):
    s = s.zfill(4)
    return len(set(s)) == 4


n = input("Введите 4-х значное число!: ")

if not n.isdigit() or len(n.zfill(4)) != 4:
    print("Ошибка: введите 4 числа!")
else:
    res = all_digits_unique(n)
    if res:
        print("Все цифра различны.")
    else:
        print("Цифры не все различны.")
