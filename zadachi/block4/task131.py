x = input('Введите через пробел год и номер месяца рождения человека: ').split()
y = input('Введите через пробел сегодняшний год и номер месяца: ').split()

year_x = int(x[0])
year_y = int(y[0])
month_x = int(x[1])
month_y = int(y[1])

if year_x <= year_y:
    if year_x != year_y:
        if month_y < month_x:
            total_year = year_y - year_x - 1
            total_month = 12 - (year_y - year_x)
            print(f'Полных лет:\n{total_year}\nПолных месяцев\n{total_month}')
        elif month_y == month_x:
            total_year = year_y - year_x
            total_month = 0
            print(f'Полных лет:\n{total_year}\nПолных месяцев\n{total_month}')
        else:
            total_year = year_y - year_x
            total_month = month_y - month_x
            print(f'Полных лет:\n{total_year}\nПолных месяцев\n{total_month}')
    else:
        if month_y < month_x:
            print('Такого не может быть...')
        elif month_y == month_x:
            total_year = 0
            total_month = 0
            print(f'Полных лет:\n{total_year}\nПолных месяцев\n{total_month}')
        else:
            total_year = 0
            total_month = month_y - month_x
            print(f'Полных лет:\n{total_year}\nПолных месяцев\n{total_month}')
