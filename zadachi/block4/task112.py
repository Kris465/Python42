from datetime import datetime
from dateutil.relativedelta import relativedelta

n = int(input('Введите сколько месяцев прошло: '))

start_date = datetime(1900, 1, 1)
final_date = start_date + relativedelta(months=n, days=2)
month_num = final_date

match month_num:
    case 1:
        print('в Январе - 31 дней')
    case 2:
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

print(month_num)