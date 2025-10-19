n = input('Введите сопротивление отделных участков цепи через пробел: ').split(' ')
umn = 1
sum = 0

for i in n:
    umn *= int(i)
    sum += int(i)

soprotivlenie = umn/sum
print(f'Общее сопротивление всей цепи: {round(soprotivlenie, 2)}')
