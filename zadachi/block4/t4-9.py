km = float(input("Скорость в км/ч: "))
m = float(input("скорость в м/с: "))

m1 = m * 3600 / 1000
print(m1)

if km == m1:
    print(f'они равны {m} м/с равны {km} км/ч')
elif m1 == km:
    print(f'{m} м/с больше {km} км/ч, Т.К. {m} м/с = {m1}')
else:
    print(f'{km} км/ч больше {m} м/с , Т.К. {m} м/с = {m1}')
