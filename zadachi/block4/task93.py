y = float(input('Введите координату "y": '))

if y != 2.5 and y != 5.0:
    if y < 2.5:
        print(f'y с координатами {y} попадает в 3-ью область.')
    elif y > 2.5 and y < 5.0:
        print(f'y с координатами {y} попадает в 2-ую область.')
    elif y > 5.0:
        print(f'y с координатами {y} попадает в 1-ую область.')
else:
    print('Введите другую координату.')
