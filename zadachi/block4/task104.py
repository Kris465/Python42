number = int(input('Введите число от 1 до 7: '))

if number >= 1 and number <= 7:
    match number:
        case 1:
            print('1 - это понедельник')
        case 2:
            print('2 - это вторник')
        case 3:
            print('3 - это среда')
        case 4:
            print('4 - это четверг')
        case 5:
            print('5 - это пятница')
        case 6:
            print('6 - это суббота')
        case 7:
            print('7 - это воскресенье')
else:
    print('Ошибка! Попробуйте снова')
