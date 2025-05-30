number = input("Введите трехзначное число: ")

# Проверяем, что введено трехзначное число
if len(number) != 3 or not number.isdigit():
    print("Ошибка: введите трехзначное число!")
else:
    first = int(number[0])
    second = int(number[1])
    last = int(number[2])

    # а) первая или последняя цифра
    if first > last:
        print(f"а) Первая цифра ({first}) больше последней ({last})")
    elif first < last:
        print(f"а) Последняя цифра ({last}) больше первой ({first})")
    else:
        print(f"а) Первая и последняя цифры равны ({first})")

    # б) первая или вторая цифра
    if first > second:
        print(f"б) Первая цифра ({first}) больше второй ({second})")
    elif first < second:
        print(f"б) Вторая цифра ({second}) больше первой ({first})")
    else:
        print(f"б) Первая и вторая цифры равны ({first})")

    # в) вторая или последняя цифра
    if second > last:
        print(f"в) Вторая цифра ({second}) больше последней ({last})")
    elif second < last:
        print(f"в) Последняя цифра ({last}) больше второй ({second})")
    else:
        print(f"в) Вторая и последняя цифры равны ({second})")