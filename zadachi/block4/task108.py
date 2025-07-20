m = int(input('Введите число от 1 до 4: '))

if m >= 1 and m <= 4:
    match m:
        case 1:
            print("Пики")
        case 2:
            print("Трефы")
        case 3:
            print("Бубны")
        case 4:
            print("Черви")
else:
    print("Такой масти нет")
