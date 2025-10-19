n = input('Введите сопротивление отделных участков цепи через пробел: ').split(' ')
soprotivlenie = 0

for i in n:
    soprotivlenie += int(i)

print(f'Общее сопротивление всей цепи: {soprotivlenie}')
