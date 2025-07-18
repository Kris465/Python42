x = float(input('Введите первое дробное число: '))
y = float(input('Введите второе дробное число: '))
z = float(input('Введите третье дробное число: '))

if x > y and x > z:
    if y > z:
        print(f'{x} - большее')
        print(f'{z} - меньшее')
    else:
        print(f'{x} - большее')
        print(f'{y} - меньшее')

if y > x and y > z:
    if x > z:
        print(f'{y} - большее')
        print(f'{z} - меньшее')
    else:
        print(f'{y} - большее')
        print(f'{x} - меньшее')

if z > y and z > x:
    if y > x:
        print(f'{z} - большее')
        print(f'{x} - меньшее')
    else:
        print(f'{z} - большее')
        print(f'{y} - меньшее')
