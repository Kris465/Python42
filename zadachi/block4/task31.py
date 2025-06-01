a = int(input("Введите трехзначное число: "))
if 100 <= abs(a) <= 999:
    d1, d2, d3 = map(int, str(abs(a)))
    if d1 == d2 and d2 == d3 or d1 == d3 and d2 == d1:
        print("все трое цифр совпадают")
    elif d1 == d2 or d2 == d3 or d1 == d3:
        print("двое цифр совпадают")
    else:
        print("в числе нет совпадений")
else:
    print("Это не трехзначное число.")
