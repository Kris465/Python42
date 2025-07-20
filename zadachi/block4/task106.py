number = int(input('Введите число от 1 до 12: '))

if number >= 1 and number <= 10:
    match number:
        case 1:
            print('1 - Январь')
        case 2:
            print('2 - Февраль')
        case 3:
            print('3 - Март')
        case 4:
            print('4 - Апрель')
        case 5:
            print('5 - Май')
        case 6:
            print('6 - Июнь')
        case 7:
            print('7 - Июль')
        case 8:
            print('8 - Август')
        case 9:
            print('9 - Сентябрь')
        case 10:
            print('10 - Октябрь')
        case 11:
            print('11 - Ноябрь')
        case 12:
            print('12 - Декабрь')
else:
    print('Ошибка! Попробуйте снова')