from datetime import datetime

birth_month, birth_year = map(int, input("""назови свою дату рождения и номер месяца и через пробел год: """).split())
current_year, current_month = datetime.now().year, datetime.now().month

if birth_month > 0 and birth_month < 13:
    a = 2
else:
    pass

if birth_year > 1900 and birth_year < 2100:
    a = 2
else:
    pass
print(current_year - birth_year - (current_month < birth_month))
