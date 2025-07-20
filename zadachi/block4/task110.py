x = int(input('Введите число масти от 1 до 4: '))

if x >= 1 and x <= 4:
    match x:
        case 1:
            print('1 -  это - пики')
        case 2:
            print('2 -  это - трефы')
        case 3:
            print('3 -  это - бубны')
        case 4:
            print('4 -  это - черви')
else:
    print('Прочтите условие внимательнее!')

y = int(input('Введите число от 6 до 14: '))

if y >= 6 and y <= 14:
    match y:
        case 6:
            print('6 - это "шестёрка"')
        case 7:
            print('7 - это "семёрка"')
        case 8:
            print('8 - это "восьмёрка"')
        case 9:
            print('9 - это "девятка"')
        case 10:
            print('10 - это "десятка"')
        case 11:
            print('11 - это "валет"')
        case 12:
            print('12 - это "дама"')
        case 13:
            print('13 - это "король"')
        case 14:
            print('14 - это "туз"')
else:
    print('Прочтите условие внимательнее!')
