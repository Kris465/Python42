def leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


month = int(input('Введите месяц от 1 до 12: '))
year = int(input('Введите год пожалуйста :_>: '))

if month >= 1 and month <= 10:
    match month:
        case 1:
            print('в Январе - 31 дней')
        case 2:
            if leap_year(year):
                print("Год високосный, в феврале 29 дней")
            else:
                print('в Феврале - 28 дней')
        case 3:
            print('в Марте - 31 дней')
        case 4:
            print('в Апреле - 30 дней')
        case 5:
            print('в Мае - 31 дней')
        case 6:
            print('в Июне - 30 дней')
        case 7:
            print('в Июле - 31 дней')
        case 8:
            print('в Августе - 31 дней')
        case 9:
            print('в Сентябре - 30 дней')
        case 10:
            print('в Октябре - 31 дней')
        case 11:
            print('в Ноябре - 30 дней')
        case 12:
            print('в Декабре - 31 дней')
else:
    print('Ошибка! Попробуйте снова')
