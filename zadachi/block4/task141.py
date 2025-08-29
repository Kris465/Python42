n = int(input('Введите кол-во квартир в доме: '))
a = int(input('Введите номер квартиры: '))

lol = []
sum_ = 0

for i in range((n - a), n + 1):
    lol.append(i)

for number in lol:
    sum_ += number

if sum_ % 2 == 0:
    print(f'Сумма ({sum_}) номеров всех квартир начиная с {a} - чётная')
else:
    print(f'Сумма ({sum_}) номеров всех квартир начиная с {a} - не чётная')
